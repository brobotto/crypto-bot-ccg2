"""Deterministic historical backtest replay."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from cbot.config import RunConfig
from cbot.engine.events import JsonlEventWriter, RunDirectory, create_run_directory, write_json
from cbot.strategies.protocol import Strategy
from cbot.types import Candle, SignalAction


@dataclass(frozen=True)
class BacktestResult:
    run_id: str
    run_dir: Path
    signals_seen: int


def run_backtest(
    config: RunConfig,
    candles: list[Candle],
    strategy: Strategy,
    runs_root: Path = Path("logs/runs"),
) -> BacktestResult:
    if strategy.metadata.name != config.strategy_name:
        raise ValueError(f"Config strategy {config.strategy_name} does not match {strategy.metadata.name}.")
    if strategy.metadata.version != config.strategy_version:
        raise ValueError(f"Config strategy version {config.strategy_version} does not match {strategy.metadata.version}.")

    strategy.validate_parameters(config.strategy_parameters)
    run_dir = create_run_directory(runs_root, config.label)
    writer = JsonlEventWriter(run_dir.events_path)
    write_json(run_dir.config_path, config.to_event_payload())
    write_json(
        run_dir.strategy_meta_path,
        {
            "name": strategy.metadata.name,
            "version": strategy.metadata.version,
            "hypothesis": strategy.metadata.hypothesis,
            "warmup_candles": strategy.metadata.warmup_candles,
        },
    )

    writer.write("run.started", run_dir.run_id, config.to_event_payload())
    signals_seen = 0
    history: list[Candle] = []
    portfolio_view: dict[str, Any] = {
        "has_position": False,
        "cash": config.initial_cash,
        "base_asset": config.base_asset,
        "quote_asset": config.quote_asset,
    }

    for candle in candles:
        if candle.symbol != config.symbol or candle.timeframe != config.timeframe:
            continue
        if not config.start <= candle.timestamp <= config.end:
            continue

        history.append(candle)
        signal = strategy.on_candle(tuple(history), portfolio_view, config.strategy_parameters)
        if signal.action != SignalAction.HOLD:
            signals_seen += 1
            writer.write(
                "strategy.signal",
                run_dir.run_id,
                {
                    "strategy": strategy.metadata.name,
                    "symbol": candle.symbol,
                    "timeframe": candle.timeframe,
                    "candle_time": candle.timestamp.isoformat().replace("+00:00", "Z"),
                    "signal": signal.action.value,
                    "reason": signal.reason,
                    "features": dict(signal.features),
                },
            )
            if signal.action == SignalAction.BUY:
                portfolio_view["has_position"] = True
            elif signal.action in {SignalAction.SELL, SignalAction.EXIT}:
                portfolio_view["has_position"] = False

    writer.write(
        "run.completed",
        run_dir.run_id,
        {
            "status": "COMPLETED",
            "verdict": "INSUFFICIENT_DATA",
            "metrics": {
                "signals_seen": signals_seen,
            },
            "warnings": ["Slice 5 emits signals only; execution simulation is not implemented yet."],
        },
    )
    write_json(
        run_dir.report_path,
        {
            "run_id": run_dir.run_id,
            "status": "COMPLETED",
            "verdict": "INSUFFICIENT_DATA",
            "metrics": {"signals_seen": signals_seen},
        },
    )
    run_dir.summary_path.write_text(
        f"# Backtest Summary\n\nRun: `{run_dir.run_id}`\n\nSignals seen: {signals_seen}\n",
        encoding="utf-8",
    )
    return BacktestResult(run_id=run_dir.run_id, run_dir=run_dir.path, signals_seen=signals_seen)

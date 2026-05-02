"""Deterministic historical backtest replay."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from cbot.config import RunConfig
from cbot.engine.events import JsonlEventWriter, RunDirectory, create_run_directory, write_json
from cbot.engine.execution import ExecutionSettings, ExecutionSimulator
from cbot.engine.portfolio import Portfolio
from cbot.strategies.protocol import Strategy
from cbot.types import Candle, Fill, SignalAction


@dataclass(frozen=True)
class BacktestResult:
    run_id: str
    run_dir: Path
    signals_seen: int
    fills_seen: int


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
    fills_seen = 0
    history: list[Candle] = []
    portfolio = Portfolio(
        cash=config.initial_cash,
        base_asset=config.base_asset,
        quote_asset=config.quote_asset,
    )
    execution = ExecutionSimulator(
        ExecutionSettings(fee_bps=config.fee_bps, slippage_bps=config.slippage_bps)
    )

    for candle in candles:
        if candle.symbol != config.symbol or candle.timeframe != config.timeframe:
            continue
        if not config.start <= candle.timestamp <= config.end:
            continue

        history.append(candle)
        signal = strategy.on_candle(tuple(history), portfolio.view(), config.strategy_parameters)
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
            intent = execution.intent_from_signal(candle.symbol, signal)
            if intent:
                fill = execution.simulate_fill(intent, candle, portfolio)
                if fill:
                    portfolio.apply_fill(fill)
                    fills_seen += 1
                    writer.write("simulation.fill", run_dir.run_id, fill_payload(fill))
                    writer.write(
                        "portfolio.snapshot",
                        run_dir.run_id,
                        portfolio.snapshot(candle.close),
                    )

    writer.write(
        "run.completed",
        run_dir.run_id,
        {
            "status": "COMPLETED",
            "verdict": "INSUFFICIENT_DATA",
            "metrics": {
                "signals_seen": signals_seen,
                "fills_seen": fills_seen,
                "final_equity": portfolio.equity(history[-1].close) if history else config.initial_cash,
                "max_drawdown_pct": portfolio.max_drawdown_pct,
            },
            "warnings": ["Slice 6 simulation is basic; metrics/verdict rules are implemented in later slices."],
        },
    )
    write_json(
        run_dir.report_path,
        {
            "run_id": run_dir.run_id,
            "status": "COMPLETED",
            "verdict": "INSUFFICIENT_DATA",
            "metrics": {
                "signals_seen": signals_seen,
                "fills_seen": fills_seen,
                "final_equity": portfolio.equity(history[-1].close) if history else config.initial_cash,
                "max_drawdown_pct": portfolio.max_drawdown_pct,
            },
        },
    )
    run_dir.summary_path.write_text(
        (
            "# Backtest Summary\n\n"
            f"Run: `{run_dir.run_id}`\n\n"
            f"Signals seen: {signals_seen}\n\n"
            f"Fills seen: {fills_seen}\n"
        ),
        encoding="utf-8",
    )
    return BacktestResult(
        run_id=run_dir.run_id,
        run_dir=run_dir.path,
        signals_seen=signals_seen,
        fills_seen=fills_seen,
    )


def fill_payload(fill: Fill) -> dict[str, Any]:
    return {
        "symbol": fill.symbol,
        "side": "SELL" if fill.side == SignalAction.EXIT else fill.side.value,
        "quantity": fill.quantity,
        "price": fill.price,
        "fee": fill.fee,
        "fee_asset": fill.fee_asset,
        "slippage_bps": fill.slippage_bps,
        "order_id": fill.order_id,
    }

"""Run configuration helpers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml


def parse_date(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


@dataclass(frozen=True)
class RunConfig:
    label: str
    sample_label: str
    start: datetime
    end: datetime
    symbol: str
    timeframe: str
    strategy_name: str
    strategy_version: str
    strategy_parameters: dict[str, Any]
    initial_cash: float
    base_asset: str
    quote_asset: str
    fee_bps: float
    slippage_bps: float
    max_drawdown_pct: float
    min_trade_count: int
    drawdown_mode: str

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "RunConfig":
        run = raw["run"]
        market = raw["market"]
        strategy = raw["strategy"]
        portfolio = raw["portfolio"]
        simulation = raw["simulation"]

        start_key = "test_start" if run.get("sample_label") == "OUT_OF_SAMPLE" else "train_start"
        end_key = "test_end" if run.get("sample_label") == "OUT_OF_SAMPLE" else "train_end"

        return cls(
            label=str(run["label"]),
            sample_label=str(run["sample_label"]),
            start=parse_date(str(run[start_key])),
            end=parse_date(str(run[end_key])),
            symbol=str(market["symbol"]),
            timeframe=str(market["timeframe"]),
            strategy_name=str(strategy["name"]),
            strategy_version=str(strategy["version"]),
            strategy_parameters=dict(strategy.get("parameters", {})),
            initial_cash=float(portfolio["initial_cash"]),
            base_asset=str(portfolio["base_asset"]),
            quote_asset=str(portfolio["quote_asset"]),
            fee_bps=float(simulation["fee_bps"]),
            slippage_bps=float(simulation["slippage_bps"]),
            max_drawdown_pct=float(simulation["max_drawdown_pct"]),
            min_trade_count=int(simulation["min_trade_count"]),
            drawdown_mode=str(simulation["drawdown_mode"]),
        )

    @classmethod
    def from_yaml(cls, path: Path) -> "RunConfig":
        return cls.from_dict(yaml.safe_load(path.read_text(encoding="utf-8")))

    def to_event_payload(self) -> dict[str, Any]:
        return {
            "label": self.label,
            "sample_label": self.sample_label,
            "market": {
                "symbol": self.symbol,
                "timeframe": self.timeframe,
            },
            "strategy": {
                "name": self.strategy_name,
                "version": self.strategy_version,
                "parameters": self.strategy_parameters,
            },
            "simulation": {
                "fee_bps": self.fee_bps,
                "slippage_bps": self.slippage_bps,
                "max_drawdown_pct": self.max_drawdown_pct,
                "min_trade_count": self.min_trade_count,
                "drawdown_mode": self.drawdown_mode,
            },
        }

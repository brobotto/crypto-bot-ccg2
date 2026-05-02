"""Baseline strategies and benchmarks."""

from __future__ import annotations

from typing import Any, Mapping

from cbot.strategies.protocol import BaseStrategy, StrategyMetadata
from cbot.types import Candle, Signal, SignalAction


class CashNoTradeStrategy(BaseStrategy):
    metadata = StrategyMetadata(
        name="cash_no_trade",
        version="1.0.0",
        hypothesis="Holding cash is the sanity baseline for active strategy evaluation.",
    )

    def on_candle(
        self,
        history: tuple[Candle, ...],
        portfolio_view: Mapping[str, Any],
        parameters: Mapping[str, Any],
    ) -> Signal:
        return Signal.hold("cash baseline never trades")


class BuyAndHoldStrategy(BaseStrategy):
    metadata = StrategyMetadata(
        name="buy_and_hold",
        version="1.0.0",
        hypothesis="Buying once at the start and holding is the market exposure benchmark.",
        warmup_candles=1,
    )

    def on_candle(
        self,
        history: tuple[Candle, ...],
        portfolio_view: Mapping[str, Any],
        parameters: Mapping[str, Any],
    ) -> Signal:
        has_position = bool(portfolio_view.get("has_position", False))
        if not has_position:
            return Signal(
                action=SignalAction.BUY,
                reason="enter buy-and-hold benchmark",
                target_fraction=1.0,
            )
        return Signal.hold("already holding benchmark position")

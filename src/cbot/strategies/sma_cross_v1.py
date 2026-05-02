"""Simple SMA crossover strategy for engine validation only."""

from __future__ import annotations

from typing import Any, Mapping

from cbot.strategies.protocol import BaseStrategy, ParameterSpec, StrategyMetadata
from cbot.types import Candle, Signal, SignalAction


class SmaCrossV1Strategy(BaseStrategy):
    metadata = StrategyMetadata(
        name="sma_cross_v1",
        version="1.0.0",
        hypothesis=(
            "A fast moving average crossing a slow moving average can validate signal "
            "generation mechanics. This is not a profitability claim."
        ),
        parameters={
            "fast_window": ParameterSpec(default=20, minimum=2, description="Fast SMA window."),
            "slow_window": ParameterSpec(default=50, minimum=3, description="Slow SMA window."),
        },
        warmup_candles=50,
    )

    def validate_parameters(self, parameters: Mapping[str, Any]) -> None:
        super().validate_parameters(parameters)
        fast_window = int(parameters.get("fast_window", self.metadata.parameters["fast_window"].default))
        slow_window = int(parameters.get("slow_window", self.metadata.parameters["slow_window"].default))
        if fast_window >= slow_window:
            raise ValueError("fast_window must be less than slow_window.")

    def on_candle(
        self,
        history: tuple[Candle, ...],
        portfolio_view: Mapping[str, Any],
        parameters: Mapping[str, Any],
    ) -> Signal:
        self.validate_parameters(parameters)
        fast_window = int(parameters.get("fast_window", self.metadata.parameters["fast_window"].default))
        slow_window = int(parameters.get("slow_window", self.metadata.parameters["slow_window"].default))
        if len(history) < slow_window + 1:
            return Signal.hold("warming up")

        previous_fast = average_close(history[-fast_window - 1 : -1])
        previous_slow = average_close(history[-slow_window - 1 : -1])
        current_fast = average_close(history[-fast_window:])
        current_slow = average_close(history[-slow_window:])
        has_position = bool(portfolio_view.get("has_position", False))

        if previous_fast <= previous_slow and current_fast > current_slow and not has_position:
            return Signal(
                action=SignalAction.BUY,
                reason="fast SMA crossed above slow SMA",
                target_fraction=1.0,
                features={
                    "fast_sma": current_fast,
                    "slow_sma": current_slow,
                },
            )
        if previous_fast >= previous_slow and current_fast < current_slow and has_position:
            return Signal(
                action=SignalAction.EXIT,
                reason="fast SMA crossed below slow SMA",
                target_fraction=0.0,
                features={
                    "fast_sma": current_fast,
                    "slow_sma": current_slow,
                },
            )
        return Signal.hold("no crossover")


def average_close(candles: tuple[Candle, ...]) -> float:
    if not candles:
        raise ValueError("Cannot average an empty candle set.")
    return sum(candle.close for candle in candles) / len(candles)

"""Strategy protocol and metadata contracts."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol, runtime_checkable

from cbot.types import Candle, Signal


@dataclass(frozen=True)
class ParameterSpec:
    default: Any
    description: str
    minimum: float | None = None
    maximum: float | None = None


@dataclass(frozen=True)
class StrategyMetadata:
    name: str
    version: str
    hypothesis: str
    parameters: Mapping[str, ParameterSpec] = field(default_factory=dict)
    warmup_candles: int = 0

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Strategy name is required.")
        if not self.version:
            raise ValueError("Strategy version is required.")
        if not self.hypothesis:
            raise ValueError("Strategy hypothesis is required.")
        if self.warmup_candles < 0:
            raise ValueError("warmup_candles must not be negative.")


@runtime_checkable
class Strategy(Protocol):
    metadata: StrategyMetadata

    def validate_parameters(self, parameters: Mapping[str, Any]) -> None:
        ...

    def on_candle(
        self,
        history: tuple[Candle, ...],
        portfolio_view: Mapping[str, Any],
        parameters: Mapping[str, Any],
    ) -> Signal:
        ...


class BaseStrategy:
    metadata: StrategyMetadata

    def validate_parameters(self, parameters: Mapping[str, Any]) -> None:
        for name, spec in self.metadata.parameters.items():
            value = parameters.get(name, spec.default)
            if spec.minimum is not None and value < spec.minimum:
                raise ValueError(f"{name} must be >= {spec.minimum}.")
            if spec.maximum is not None and value > spec.maximum:
                raise ValueError(f"{name} must be <= {spec.maximum}.")

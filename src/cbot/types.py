"""Shared domain types for the research workbench."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from types import MappingProxyType
from typing import Any, Mapping


def ensure_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


@dataclass(frozen=True)
class Candle:
    symbol: str
    timeframe: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "timestamp", ensure_utc(self.timestamp))

    def to_record(self) -> dict[str, object]:
        return {
            "symbol": self.symbol,
            "timeframe": self.timeframe,
            "timestamp": self.timestamp.isoformat().replace("+00:00", "Z"),
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
        }

    @classmethod
    def from_record(cls, record: dict[str, object]) -> "Candle":
        timestamp = record["timestamp"]
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        if not isinstance(timestamp, datetime):
            raise TypeError("timestamp must be a datetime or ISO string")
        return cls(
            symbol=str(record["symbol"]),
            timeframe=str(record["timeframe"]),
            timestamp=timestamp,
            open=float(record["open"]),
            high=float(record["high"]),
            low=float(record["low"]),
            close=float(record["close"]),
            volume=float(record["volume"]),
        )


class SignalAction(StrEnum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    EXIT = "EXIT"


@dataclass(frozen=True)
class Signal:
    action: SignalAction
    reason: str
    target_fraction: float | None = None
    features: Mapping[str, Any] = MappingProxyType({})

    def __post_init__(self) -> None:
        if self.target_fraction is not None and not 0 <= self.target_fraction <= 1:
            raise ValueError("target_fraction must be between 0 and 1.")

    @classmethod
    def hold(cls, reason: str = "no signal") -> "Signal":
        return cls(action=SignalAction.HOLD, reason=reason)


@dataclass(frozen=True)
class OrderIntent:
    symbol: str
    side: SignalAction
    target_fraction: float
    reason: str


@dataclass(frozen=True)
class Fill:
    symbol: str
    side: SignalAction
    quantity: float
    price: float
    fee: float
    fee_asset: str
    slippage_bps: float
    order_id: str

    @property
    def notional(self) -> float:
        return self.quantity * self.price

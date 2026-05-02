"""Validation helpers for historical OHLCV candles."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta

from cbot.types import Candle


@dataclass(frozen=True)
class DataValidationWarning:
    code: str
    message: str
    timestamp: str | None = None


def timeframe_delta(timeframe: str) -> timedelta:
    unit = timeframe[-1]
    amount = int(timeframe[:-1])
    if unit == "m":
        return timedelta(minutes=amount)
    if unit == "h":
        return timedelta(hours=amount)
    if unit == "d":
        return timedelta(days=amount)
    raise ValueError(f"Unsupported timeframe: {timeframe}")


def validate_candles(
    candles: list[Candle],
    expected_symbol: str | None = None,
    expected_timeframe: str | None = None,
) -> list[DataValidationWarning]:
    warnings: list[DataValidationWarning] = []
    if not candles:
        return [DataValidationWarning("empty_dataset", "No candles were provided.")]

    expected_step = timeframe_delta(expected_timeframe or candles[0].timeframe)
    seen = set()
    previous: Candle | None = None

    for candle in candles:
        timestamp = candle.timestamp.isoformat().replace("+00:00", "Z")

        if expected_symbol and candle.symbol != expected_symbol:
            warnings.append(
                DataValidationWarning(
                    "symbol_mismatch",
                    f"Expected {expected_symbol}, got {candle.symbol}.",
                    timestamp,
                )
            )

        if expected_timeframe and candle.timeframe != expected_timeframe:
            warnings.append(
                DataValidationWarning(
                    "timeframe_mismatch",
                    f"Expected {expected_timeframe}, got {candle.timeframe}.",
                    timestamp,
                )
            )

        if candle.timestamp in seen:
            warnings.append(DataValidationWarning("duplicate_candle", "Duplicate candle.", timestamp))
        seen.add(candle.timestamp)

        if previous:
            if candle.timestamp < previous.timestamp:
                warnings.append(
                    DataValidationWarning("unordered_candle", "Candles are not chronological.", timestamp)
                )
            elif candle.timestamp - previous.timestamp != expected_step:
                warnings.append(
                    DataValidationWarning(
                        "gap_or_overlap",
                        f"Expected step {expected_step}, got {candle.timestamp - previous.timestamp}.",
                        timestamp,
                    )
                )

        if min(candle.open, candle.high, candle.low, candle.close) <= 0:
            warnings.append(DataValidationWarning("non_positive_price", "OHLC prices must be positive.", timestamp))

        if candle.volume < 0:
            warnings.append(DataValidationWarning("negative_volume", "Volume must not be negative.", timestamp))

        if candle.high < max(candle.open, candle.close, candle.low):
            warnings.append(DataValidationWarning("invalid_high", "High is below another OHLC value.", timestamp))

        if candle.low > min(candle.open, candle.close, candle.high):
            warnings.append(DataValidationWarning("invalid_low", "Low is above another OHLC value.", timestamp))

        previous = candle

    return warnings

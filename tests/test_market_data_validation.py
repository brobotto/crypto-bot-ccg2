from datetime import UTC, datetime, timedelta

from cbot.market_data.validation import timeframe_delta, validate_candles
from cbot.types import Candle


def candle_at(offset_hours=0, **overrides):
    values = {
        "symbol": "BTCUSDT",
        "timeframe": "1h",
        "timestamp": datetime(2024, 1, 1, tzinfo=UTC) + timedelta(hours=offset_hours),
        "open": 100.0,
        "high": 110.0,
        "low": 90.0,
        "close": 105.0,
        "volume": 10.0,
    }
    values.update(overrides)
    return Candle(**values)


def test_timeframe_delta_supports_expected_units():
    assert timeframe_delta("1m") == timedelta(minutes=1)
    assert timeframe_delta("1h") == timedelta(hours=1)
    assert timeframe_delta("1d") == timedelta(days=1)


def test_validate_valid_candles_has_no_warnings():
    warnings = validate_candles([candle_at(0), candle_at(1)], "BTCUSDT", "1h")
    assert warnings == []


def test_validate_candles_finds_duplicate_and_gap():
    warnings = validate_candles([candle_at(0), candle_at(0), candle_at(2)], "BTCUSDT", "1h")
    codes = {warning.code for warning in warnings}
    assert "duplicate_candle" in codes
    assert "gap_or_overlap" in codes


def test_validate_candles_finds_bad_ohlc_and_volume():
    warnings = validate_candles(
        [candle_at(high=80, low=120, volume=-1)],
        "BTCUSDT",
        "1h",
    )
    codes = {warning.code for warning in warnings}
    assert {"invalid_high", "invalid_low", "negative_volume"} <= codes


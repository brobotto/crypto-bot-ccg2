from datetime import UTC, datetime

from cbot.market_data.binance import build_klines_url, parse_kline


def test_build_klines_url_contains_expected_query():
    url = build_klines_url(
        "BTCUSDT",
        "1h",
        datetime(2024, 1, 1, tzinfo=UTC),
        datetime(2024, 1, 2, tzinfo=UTC),
    )

    assert "symbol=BTCUSDT" in url
    assert "interval=1h" in url
    assert "startTime=1704067200000" in url
    assert "endTime=1704153600000" in url


def test_parse_kline_returns_candle():
    raw = [
        1704067200000,
        "100.0",
        "110.0",
        "90.0",
        "105.0",
        "123.45",
        1704070799999,
        "0",
        1,
        "0",
        "0",
        "0",
    ]

    candle = parse_kline(raw, "BTCUSDT", "1h")

    assert candle.symbol == "BTCUSDT"
    assert candle.timeframe == "1h"
    assert candle.timestamp == datetime(2024, 1, 1, tzinfo=UTC)
    assert candle.close == 105.0
    assert candle.volume == 123.45


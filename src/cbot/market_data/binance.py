"""Public Binance historical candle fetching."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from urllib.parse import urlencode
from urllib.request import urlopen

from cbot.types import Candle
from cbot.market_data.validation import timeframe_delta


BINANCE_KLINES_URL = "https://api.binance.com/api/v3/klines"


def timestamp_ms(value: datetime) -> int:
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return int(value.astimezone(UTC).timestamp() * 1000)


def build_klines_url(
    symbol: str,
    interval: str,
    start: datetime,
    end: datetime,
    limit: int = 1000,
) -> str:
    query = urlencode(
        {
            "symbol": symbol,
            "interval": interval,
            "startTime": timestamp_ms(start),
            "endTime": timestamp_ms(end),
            "limit": limit,
        }
    )
    return f"{BINANCE_KLINES_URL}?{query}"


def parse_kline(raw: list[object], symbol: str, timeframe: str) -> Candle:
    return Candle(
        symbol=symbol,
        timeframe=timeframe,
        timestamp=datetime.fromtimestamp(int(raw[0]) / 1000, UTC),
        open=float(raw[1]),
        high=float(raw[2]),
        low=float(raw[3]),
        close=float(raw[4]),
        volume=float(raw[5]),
    )


def _fetch_page(symbol: str, interval: str, start: datetime, end: datetime) -> list[Candle]:
    url = build_klines_url(symbol, interval, start, end)
    with urlopen(url, timeout=30) as response:  # nosec B310 - fixed Binance public API URL.
        payload = json.loads(response.read().decode("utf-8"))
    return [parse_kline(item, symbol=symbol, timeframe=interval) for item in payload]


def fetch_klines(symbol: str, interval: str, start: datetime, end: datetime) -> list[Candle]:
    """Fetch Binance klines from the public REST API with page-sized requests."""

    candles: list[Candle] = []
    cursor = start
    step = timeframe_delta(interval)
    while cursor < end:
        page = _fetch_page(symbol, interval, cursor, end)
        if not page:
            break
        candles.extend(page)
        next_cursor = page[-1].timestamp + step
        if next_cursor <= cursor:
            break
        cursor = next_cursor
        if len(page) < 1000:
            break
    return candles

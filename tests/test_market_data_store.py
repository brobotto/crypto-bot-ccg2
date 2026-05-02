from datetime import UTC, datetime

import pytest

from cbot.market_data.store import MarketDataStore, parquet_available
from cbot.types import Candle


def sample_candles():
    return [
        Candle(
            symbol="BTCUSDT",
            timeframe="1h",
            timestamp=datetime(2024, 1, 1, tzinfo=UTC),
            open=100,
            high=110,
            low=90,
            close=105,
            volume=10,
        )
    ]


def test_store_paths_are_partitioned(tmp_path):
    store = MarketDataStore(tmp_path)
    assert store.dataset_path("BTCUSDT", "1h") == tmp_path / "symbol=BTCUSDT" / "timeframe=1h" / "candles.parquet"


def test_write_empty_candles_fails(tmp_path):
    store = MarketDataStore(tmp_path)
    with pytest.raises(ValueError):
        store.write_candles([])


def test_parquet_roundtrip_or_clear_dependency_error(tmp_path):
    store = MarketDataStore(tmp_path)
    candles = sample_candles()

    if not parquet_available():
        with pytest.raises(RuntimeError, match="pyarrow"):
            store.write_candles(candles)
        return

    path = store.write_candles(candles)
    loaded = store.read_candles("BTCUSDT", "1h")

    assert path.exists()
    assert loaded == candles


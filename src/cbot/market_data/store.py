"""Local market data persistence."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from cbot.types import Candle


def parquet_available() -> bool:
    return importlib.util.find_spec("pyarrow") is not None


class MarketDataStore:
    def __init__(self, root: Path) -> None:
        self.root = root

    def partition_dir(self, symbol: str, timeframe: str) -> Path:
        return self.root / f"symbol={symbol}" / f"timeframe={timeframe}"

    def dataset_path(self, symbol: str, timeframe: str) -> Path:
        return self.partition_dir(symbol, timeframe) / "candles.parquet"

    def write_candles(self, candles: list[Candle]) -> Path:
        if not candles:
            raise ValueError("Cannot write an empty candle set.")
        if not parquet_available():
            raise RuntimeError("pyarrow is required to write Parquet market data.")

        import pandas as pd

        symbol = candles[0].symbol
        timeframe = candles[0].timeframe
        path = self.dataset_path(symbol, timeframe)
        path.parent.mkdir(parents=True, exist_ok=True)
        frame = pd.DataFrame([candle.to_record() for candle in candles])
        frame.to_parquet(path, index=False)
        return path

    def read_candles(self, symbol: str, timeframe: str) -> list[Candle]:
        if not parquet_available():
            raise RuntimeError("pyarrow is required to read Parquet market data.")

        import pandas as pd

        path = self.dataset_path(symbol, timeframe)
        frame = pd.read_parquet(path)
        return [Candle.from_record(record) for record in frame.to_dict(orient="records")]

import json
from datetime import UTC, datetime, timedelta

from cbot.config import RunConfig
from cbot.engine.backtest import run_backtest
from cbot.strategies.sma_cross_v1 import SmaCrossV1Strategy
from cbot.types import Candle

from tests.test_config import raw_config


def candles_from_closes(closes):
    return [
        Candle(
            symbol="BTCUSDT",
            timeframe="1h",
            timestamp=datetime(2021, 1, 1, tzinfo=UTC) + timedelta(hours=index),
            open=close,
            high=close + 1,
            low=close - 1,
            close=close,
            volume=10,
        )
        for index, close in enumerate(closes)
    ]


def normalized_events(run_dir):
    records = [
        json.loads(line)
        for line in (run_dir / "events.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    for record in records:
        record["run_id"] = "<run>"
        record["timestamp"] = "<timestamp>"
    return records


def test_backtest_writes_reproducible_event_stream(tmp_path):
    config = RunConfig.from_dict(raw_config())
    candles = candles_from_closes([10, 10, 10, 10, 20, 20, 20])
    strategy = SmaCrossV1Strategy()

    first = run_backtest(config, candles, strategy, tmp_path)
    second = run_backtest(config, candles, strategy, tmp_path)

    assert first.signals_seen == second.signals_seen == 1
    assert normalized_events(first.run_dir) == normalized_events(second.run_dir)


def test_backtest_writes_run_artifacts(tmp_path):
    config = RunConfig.from_dict(raw_config())
    result = run_backtest(config, candles_from_closes([10, 10, 10, 10, 20]), SmaCrossV1Strategy(), tmp_path)

    assert (result.run_dir / "config.resolved.json").exists()
    assert (result.run_dir / "strategy.meta.json").exists()
    assert (result.run_dir / "events.jsonl").exists()
    assert (result.run_dir / "report.json").exists()
    assert (result.run_dir / "summary.md").exists()


def test_backtest_rejects_strategy_mismatch(tmp_path):
    config = RunConfig.from_dict(raw_config())
    changed = config.__class__(**{**config.__dict__, "strategy_name": "other"})

    try:
        run_backtest(changed, [], SmaCrossV1Strategy(), tmp_path)
    except ValueError as error:
        assert "does not match" in str(error)
    else:
        raise AssertionError("Expected strategy mismatch to fail")

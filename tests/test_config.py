from datetime import UTC, datetime

from cbot.config import RunConfig


def raw_config(sample_label="IN_SAMPLE"):
    return {
        "run": {
            "label": "smoke",
            "sample_label": sample_label,
            "train_start": "2021-01-01",
            "train_end": "2021-12-31",
            "test_start": "2022-01-01",
            "test_end": "2022-12-31",
        },
        "market": {
            "exchange": "binance",
            "symbol": "BTCUSDT",
            "quote": "USDT",
            "timeframe": "1h",
        },
        "strategy": {
            "name": "sma_cross_v1",
            "version": "1.0.0",
            "parameters": {"fast_window": 2, "slow_window": 4},
        },
        "portfolio": {
            "initial_cash": 10000,
            "base_asset": "BTC",
            "quote_asset": "USDT",
        },
        "simulation": {
            "fee_bps": 10,
            "slippage_bps": 20,
            "max_drawdown_pct": 20,
            "min_trade_count": 30,
            "drawdown_mode": "flag_only",
        },
    }


def test_run_config_uses_train_window_for_in_sample():
    config = RunConfig.from_dict(raw_config("IN_SAMPLE"))
    assert config.start == datetime(2021, 1, 1, tzinfo=UTC)
    assert config.end == datetime(2021, 12, 31, tzinfo=UTC)


def test_run_config_uses_test_window_for_out_of_sample():
    config = RunConfig.from_dict(raw_config("OUT_OF_SAMPLE"))
    assert config.start == datetime(2022, 1, 1, tzinfo=UTC)
    assert config.end == datetime(2022, 12, 31, tzinfo=UTC)


def test_run_config_event_payload_contains_required_groups():
    payload = RunConfig.from_dict(raw_config()).to_event_payload()
    assert {"label", "sample_label", "market", "strategy", "simulation"} <= set(payload)


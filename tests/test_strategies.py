from datetime import UTC, datetime, timedelta

import pytest

from cbot.strategies import STRATEGIES
from cbot.strategies.baselines import BuyAndHoldStrategy, CashNoTradeStrategy
from cbot.strategies.sma_cross_v1 import SmaCrossV1Strategy, average_close
from cbot.types import Candle, SignalAction


def candles_from_closes(closes):
    candles = []
    for index, close in enumerate(closes):
        candles.append(
            Candle(
                symbol="BTCUSDT",
                timeframe="1h",
                timestamp=datetime(2024, 1, 1, tzinfo=UTC) + timedelta(hours=index),
                open=close,
                high=close + 1,
                low=close - 1,
                close=close,
                volume=10,
            )
        )
    return tuple(candles)


def test_registry_contains_baseline_strategies():
    assert {"cash_no_trade", "buy_and_hold", "sma_cross_v1"} <= set(STRATEGIES)


def test_cash_no_trade_never_trades():
    strategy = CashNoTradeStrategy()
    signal = strategy.on_candle(candles_from_closes([100]), {}, {})
    assert signal.action == SignalAction.HOLD


def test_buy_and_hold_buys_once_then_holds():
    strategy = BuyAndHoldStrategy()

    first = strategy.on_candle(candles_from_closes([100]), {"has_position": False}, {})
    second = strategy.on_candle(candles_from_closes([100, 101]), {"has_position": True}, {})

    assert first.action == SignalAction.BUY
    assert first.target_fraction == 1.0
    assert second.action == SignalAction.HOLD


def test_sma_cross_validates_windows():
    strategy = SmaCrossV1Strategy()
    with pytest.raises(ValueError, match="fast_window"):
        strategy.validate_parameters({"fast_window": 20, "slow_window": 20})


def test_sma_cross_warms_up_before_signal():
    strategy = SmaCrossV1Strategy()
    signal = strategy.on_candle(candles_from_closes([100, 101]), {}, {"fast_window": 2, "slow_window": 3})
    assert signal.action == SignalAction.HOLD
    assert signal.reason == "warming up"


def test_sma_cross_emits_buy_on_bullish_cross():
    strategy = SmaCrossV1Strategy()
    # Previous fast average <= previous slow average, current fast > current slow.
    history = candles_from_closes([10, 10, 10, 10, 20])

    signal = strategy.on_candle(history, {"has_position": False}, {"fast_window": 2, "slow_window": 4})

    assert signal.action == SignalAction.BUY
    assert signal.target_fraction == 1.0
    assert "fast_sma" in signal.features


def test_sma_cross_emits_exit_on_bearish_cross():
    strategy = SmaCrossV1Strategy()
    history = candles_from_closes([20, 20, 20, 20, 10])

    signal = strategy.on_candle(history, {"has_position": True}, {"fast_window": 2, "slow_window": 4})

    assert signal.action == SignalAction.EXIT
    assert signal.target_fraction == 0.0


def test_average_close_rejects_empty_input():
    with pytest.raises(ValueError):
        average_close(())


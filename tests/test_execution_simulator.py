from datetime import UTC, datetime

from cbot.engine.execution import ExecutionSettings, ExecutionSimulator, apply_slippage
from cbot.engine.portfolio import Portfolio
from cbot.types import Candle, Signal, SignalAction


def candle(close=100):
    return Candle(
        symbol="BTCUSDT",
        timeframe="1h",
        timestamp=datetime(2024, 1, 1, tzinfo=UTC),
        open=close,
        high=close + 1,
        low=close - 1,
        close=close,
        volume=10,
    )


def test_apply_slippage_moves_against_trade():
    assert apply_slippage(100, 20, buy=True) == 100.2
    assert apply_slippage(100, 20, buy=False) == 99.8


def test_buy_signal_simulates_fill_with_fee_and_slippage():
    simulator = ExecutionSimulator(ExecutionSettings(fee_bps=10, slippage_bps=20))
    portfolio = Portfolio(cash=1000, base_asset="BTC", quote_asset="USDT")
    intent = simulator.intent_from_signal(
        "BTCUSDT",
        Signal(SignalAction.BUY, "buy", target_fraction=1.0),
    )

    fill = simulator.simulate_fill(intent, candle(100), portfolio)

    assert fill is not None
    assert fill.price == 100.2
    assert fill.fee > 0
    assert fill.notional + fill.fee <= 1000 + 1e-9


def test_sell_signal_simulates_exit_fill():
    simulator = ExecutionSimulator(ExecutionSettings(fee_bps=10, slippage_bps=20))
    portfolio = Portfolio(cash=0, base_asset="BTC", quote_asset="USDT", position_qty=1)
    intent = simulator.intent_from_signal(
        "BTCUSDT",
        Signal(SignalAction.EXIT, "exit", target_fraction=0.0),
    )

    fill = simulator.simulate_fill(intent, candle(100), portfolio)

    assert fill is not None
    assert fill.side == SignalAction.EXIT
    assert fill.price == 99.8
    assert fill.quantity == 1


def test_small_order_returns_no_fill():
    simulator = ExecutionSimulator(ExecutionSettings(fee_bps=10, slippage_bps=20, min_notional=10))
    portfolio = Portfolio(cash=5, base_asset="BTC", quote_asset="USDT")
    intent = simulator.intent_from_signal(
        "BTCUSDT",
        Signal(SignalAction.BUY, "buy", target_fraction=1.0),
    )

    assert simulator.simulate_fill(intent, candle(100), portfolio) is None

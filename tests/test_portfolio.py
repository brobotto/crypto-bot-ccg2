from cbot.engine.portfolio import Portfolio
from cbot.types import Fill, SignalAction


def test_portfolio_applies_buy_and_sell_fills():
    portfolio = Portfolio(cash=1000, base_asset="BTC", quote_asset="USDT")

    portfolio.apply_fill(
        Fill(
            symbol="BTCUSDT",
            side=SignalAction.BUY,
            quantity=1,
            price=100,
            fee=1,
            fee_asset="USDT",
            slippage_bps=0,
            order_id="sim-1",
        )
    )
    assert portfolio.cash == 899
    assert portfolio.position_qty == 1

    portfolio.apply_fill(
        Fill(
            symbol="BTCUSDT",
            side=SignalAction.EXIT,
            quantity=0.5,
            price=110,
            fee=1,
            fee_asset="USDT",
            slippage_bps=0,
            order_id="sim-2",
        )
    )
    assert portfolio.cash == 953
    assert portfolio.position_qty == 0.5


def test_portfolio_snapshot_tracks_drawdown():
    portfolio = Portfolio(cash=0, base_asset="BTC", quote_asset="USDT", position_qty=1)
    first = portfolio.snapshot(100)
    second = portfolio.snapshot(80)

    assert first["equity"] == 100
    assert second["equity"] == 80
    assert second["drawdown_pct"] == 20
    assert portfolio.max_drawdown_pct == 20


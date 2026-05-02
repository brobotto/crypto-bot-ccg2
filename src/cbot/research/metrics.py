"""Research metric calculation."""

from __future__ import annotations

from dataclasses import dataclass

from cbot.engine.portfolio import Portfolio


@dataclass(frozen=True)
class MetricSummary:
    initial_cash: float
    final_equity: float
    total_return_pct: float
    max_drawdown_pct: float
    trade_count: int
    fee_drag: float
    buy_and_hold_return_pct: float | None = None
    cash_return_pct: float = 0.0

    def to_dict(self) -> dict[str, float | int | None]:
        return {
            "initial_cash": self.initial_cash,
            "final_equity": self.final_equity,
            "total_return_pct": self.total_return_pct,
            "max_drawdown_pct": self.max_drawdown_pct,
            "trade_count": self.trade_count,
            "fee_drag": self.fee_drag,
            "buy_and_hold_return_pct": self.buy_and_hold_return_pct,
            "cash_return_pct": self.cash_return_pct,
        }


def calculate_metrics(
    portfolio: Portfolio,
    initial_cash: float,
    final_price: float,
    first_price: float | None = None,
    total_fees: float = 0.0,
) -> MetricSummary:
    final_equity = portfolio.equity(final_price)
    total_return_pct = percent_return(initial_cash, final_equity)
    buy_and_hold_return_pct = None
    if first_price and first_price > 0:
        buy_and_hold_return_pct = percent_return(first_price, final_price)
    return MetricSummary(
        initial_cash=round(initial_cash, 10),
        final_equity=round(final_equity, 10),
        total_return_pct=round(total_return_pct, 10),
        max_drawdown_pct=round(portfolio.max_drawdown_pct, 10),
        trade_count=portfolio.fills_count,
        fee_drag=round(total_fees, 10),
        buy_and_hold_return_pct=None
        if buy_and_hold_return_pct is None
        else round(buy_and_hold_return_pct, 10),
    )


def percent_return(start: float, end: float) -> float:
    if start == 0:
        return 0.0
    return (end - start) / start * 100

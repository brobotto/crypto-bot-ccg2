"""Strategy contracts and baseline strategies."""

from cbot.strategies.baselines import BuyAndHoldStrategy, CashNoTradeStrategy
from cbot.strategies.sma_cross_v1 import SmaCrossV1Strategy

STRATEGIES = {
    "cash_no_trade": CashNoTradeStrategy,
    "buy_and_hold": BuyAndHoldStrategy,
    "sma_cross_v1": SmaCrossV1Strategy,
}

__all__ = [
    "BuyAndHoldStrategy",
    "CashNoTradeStrategy",
    "SmaCrossV1Strategy",
    "STRATEGIES",
]

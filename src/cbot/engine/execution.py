"""Simple spot execution simulation."""

from __future__ import annotations

from dataclasses import dataclass

from cbot.engine.portfolio import Portfolio
from cbot.types import Candle, Fill, OrderIntent, Signal, SignalAction


@dataclass(frozen=True)
class ExecutionSettings:
    fee_bps: float
    slippage_bps: float
    min_notional: float = 10.0


class ExecutionSimulator:
    def __init__(self, settings: ExecutionSettings) -> None:
        self.settings = settings
        self._order_sequence = 0

    def intent_from_signal(self, symbol: str, signal: Signal) -> OrderIntent | None:
        if signal.action == SignalAction.HOLD:
            return None
        target_fraction = signal.target_fraction
        if target_fraction is None:
            target_fraction = 1.0 if signal.action == SignalAction.BUY else 0.0
        return OrderIntent(
            symbol=symbol,
            side=signal.action,
            target_fraction=target_fraction,
            reason=signal.reason,
        )

    def simulate_fill(self, intent: OrderIntent, candle: Candle, portfolio: Portfolio) -> Fill | None:
        self._order_sequence += 1
        order_id = f"sim-{self._order_sequence:06d}"

        if intent.side == SignalAction.BUY:
            price = apply_slippage(candle.close, self.settings.slippage_bps, buy=True)
            target_notional = portfolio.equity(candle.close) * intent.target_fraction
            spendable = min(portfolio.cash, target_notional)
            if spendable < self.settings.min_notional:
                return None
            fee_rate = self.settings.fee_bps / 10_000
            quantity = spendable / (price * (1 + fee_rate))
            fee = quantity * price * fee_rate
            return Fill(
                symbol=intent.symbol,
                side=SignalAction.BUY,
                quantity=quantity,
                price=price,
                fee=fee,
                fee_asset=portfolio.quote_asset,
                slippage_bps=self.settings.slippage_bps,
                order_id=order_id,
            )

        if intent.side in {SignalAction.SELL, SignalAction.EXIT}:
            quantity = portfolio.position_qty * (1 - intent.target_fraction)
            if quantity <= 0:
                return None
            price = apply_slippage(candle.close, self.settings.slippage_bps, buy=False)
            if quantity * price < self.settings.min_notional:
                return None
            fee = quantity * price * (self.settings.fee_bps / 10_000)
            return Fill(
                symbol=intent.symbol,
                side=intent.side,
                quantity=quantity,
                price=price,
                fee=fee,
                fee_asset=portfolio.quote_asset,
                slippage_bps=self.settings.slippage_bps,
                order_id=order_id,
            )

        return None


def apply_slippage(price: float, slippage_bps: float, buy: bool) -> float:
    adjustment = price * slippage_bps / 10_000
    return price + adjustment if buy else price - adjustment

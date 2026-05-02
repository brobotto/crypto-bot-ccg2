"""Simulated spot portfolio accounting."""

from __future__ import annotations

from dataclasses import dataclass, field

from cbot.types import Fill, SignalAction


@dataclass
class Portfolio:
    cash: float
    base_asset: str
    quote_asset: str
    position_qty: float = 0.0
    realized_pnl: float = 0.0
    peak_equity: float = field(init=False)
    max_drawdown_pct: float = 0.0
    fills_count: int = 0

    def __post_init__(self) -> None:
        self.peak_equity = self.cash

    @property
    def has_position(self) -> bool:
        return self.position_qty > 0

    def view(self) -> dict[str, object]:
        return {
            "has_position": self.has_position,
            "cash": self.cash,
            "position_qty": self.position_qty,
            "base_asset": self.base_asset,
            "quote_asset": self.quote_asset,
        }

    def equity(self, mark_price: float) -> float:
        return self.cash + self.position_qty * mark_price

    def apply_fill(self, fill: Fill) -> None:
        if fill.side == SignalAction.BUY:
            total_cost = fill.notional + fill.fee
            if total_cost > self.cash + 1e-9:
                raise ValueError("Fill cost exceeds available cash.")
            self.cash -= total_cost
            self.position_qty += fill.quantity
        elif fill.side in {SignalAction.SELL, SignalAction.EXIT}:
            if fill.quantity > self.position_qty + 1e-9:
                raise ValueError("Fill quantity exceeds current position.")
            self.cash += fill.notional - fill.fee
            self.position_qty -= fill.quantity
        else:
            raise ValueError(f"Unsupported fill side: {fill.side}")
        self.fills_count += 1

    def snapshot(self, mark_price: float) -> dict[str, object]:
        equity = self.equity(mark_price)
        if equity > self.peak_equity:
            self.peak_equity = equity
        drawdown_pct = 0.0
        if self.peak_equity:
            drawdown_pct = max(0.0, (self.peak_equity - equity) / self.peak_equity * 100)
        self.max_drawdown_pct = max(self.max_drawdown_pct, drawdown_pct)
        return {
            "cash": round(self.cash, 10),
            "equity": round(equity, 10),
            "drawdown_pct": round(drawdown_pct, 10),
            "positions": {
                self.base_asset: round(self.position_qty, 10),
            },
            "realized_pnl": round(self.realized_pnl, 10),
            "unrealized_pnl": round(self.position_qty * mark_price, 10),
        }

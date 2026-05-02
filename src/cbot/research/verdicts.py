"""Research verdict rules."""

from __future__ import annotations

from enum import StrEnum

from cbot.research.metrics import MetricSummary


class Verdict(StrEnum):
    REJECT = "REJECT"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    CONDITIONAL = "CONDITIONAL"
    CANDIDATE = "CANDIDATE"


def choose_verdict(
    metrics: MetricSummary,
    max_drawdown_pct: float,
    min_trade_count: int,
    sample_label: str,
) -> tuple[Verdict, list[str]]:
    warnings: list[str] = []

    if metrics.max_drawdown_pct >= max_drawdown_pct:
        warnings.append("DRAWDOWN_BREACHED")
        return Verdict.REJECT, warnings

    if metrics.trade_count < min_trade_count:
        warnings.append("TRADE_COUNT_BELOW_FLOOR")
        return Verdict.INSUFFICIENT_DATA, warnings

    if sample_label != "OUT_OF_SAMPLE":
        warnings.append("NOT_OUT_OF_SAMPLE")
        return Verdict.CONDITIONAL, warnings

    if metrics.total_return_pct <= metrics.cash_return_pct:
        warnings.append("UNDERPERFORMS_CASH")
        return Verdict.REJECT, warnings

    if (
        metrics.buy_and_hold_return_pct is not None
        and metrics.total_return_pct < metrics.buy_and_hold_return_pct
    ):
        warnings.append("UNDERPERFORMS_BUY_AND_HOLD")
        return Verdict.CONDITIONAL, warnings

    return Verdict.CANDIDATE, warnings

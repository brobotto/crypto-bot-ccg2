"""Report writing for completed research runs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from cbot.engine.events import write_json
from cbot.research.metrics import MetricSummary
from cbot.research.verdicts import Verdict


@dataclass(frozen=True)
class ResearchReport:
    run_id: str
    status: str
    verdict: Verdict
    metrics: MetricSummary
    warnings: list[str]

    def to_dict(self) -> dict[str, object]:
        return {
            "run_id": self.run_id,
            "status": self.status,
            "verdict": self.verdict.value,
            "metrics": self.metrics.to_dict(),
            "warnings": self.warnings,
        }


def write_report(report: ResearchReport, report_path: Path, summary_path: Path) -> None:
    write_json(report_path, report.to_dict())
    summary_path.write_text(render_summary(report), encoding="utf-8")


def render_summary(report: ResearchReport) -> str:
    metrics = report.metrics
    warnings = "\n".join(f"- {warning}" for warning in report.warnings) or "- none"
    return (
        "# Backtest Summary\n\n"
        f"Run: `{report.run_id}`\n\n"
        f"Verdict: `{report.verdict.value}`\n\n"
        "## Metrics\n\n"
        f"- Final equity: {metrics.final_equity:.4f}\n"
        f"- Total return: {metrics.total_return_pct:.4f}%\n"
        f"- Max drawdown: {metrics.max_drawdown_pct:.4f}%\n"
        f"- Trade count: {metrics.trade_count}\n"
        f"- Fee drag: {metrics.fee_drag:.4f}\n"
        f"- Buy and hold return: {metrics.buy_and_hold_return_pct}\n\n"
        "## Warnings\n\n"
        f"{warnings}\n"
    )

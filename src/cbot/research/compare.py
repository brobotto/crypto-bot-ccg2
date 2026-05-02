"""Compare completed run reports without selecting a winner."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_report(run_dir: Path) -> dict[str, Any]:
    return json.loads((run_dir / "report.json").read_text(encoding="utf-8"))


def compare_runs(run_dirs: list[Path]) -> dict[str, Any]:
    rows = []
    warnings: list[str] = []
    for run_dir in run_dirs:
        report = load_report(run_dir)
        metrics = report["metrics"]
        rows.append(
            {
                "run_id": report["run_id"],
                "verdict": report["verdict"],
                "total_return_pct": metrics["total_return_pct"],
                "max_drawdown_pct": metrics["max_drawdown_pct"],
                "trade_count": metrics["trade_count"],
                "fee_drag": metrics["fee_drag"],
                "buy_and_hold_return_pct": metrics.get("buy_and_hold_return_pct"),
                "warnings": report.get("warnings", []),
            }
        )
    if rows:
        returns = [row["total_return_pct"] for row in rows]
        if max(returns) - min(returns) > 0:
            warnings.append("Comparison is descriptive only; it does not select best parameters.")
    return {"runs": rows, "warnings": warnings}


def render_comparison(comparison: dict[str, Any]) -> str:
    lines = [
        "# Run Comparison",
        "",
        "| run_id | verdict | return % | max DD % | trades | fee drag |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in comparison["runs"]:
        lines.append(
            "| {run_id} | {verdict} | {total_return_pct:.4f} | {max_drawdown_pct:.4f} | "
            "{trade_count} | {fee_drag:.4f} |".format(**row)
        )
    lines.extend(["", "## Warnings", ""])
    if comparison["warnings"]:
        lines.extend(f"- {warning}" for warning in comparison["warnings"])
    else:
        lines.append("- none")
    return "\n".join(lines) + "\n"

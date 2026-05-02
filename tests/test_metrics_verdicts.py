import json

from cbot.engine.portfolio import Portfolio
from cbot.research.metrics import MetricSummary, calculate_metrics, percent_return
from cbot.research.reporter import ResearchReport, render_summary, write_report
from cbot.research.verdicts import Verdict, choose_verdict


def test_percent_return():
    assert percent_return(100, 110) == 10
    assert percent_return(0, 110) == 0


def test_calculate_metrics_includes_buy_and_hold():
    portfolio = Portfolio(cash=0, base_asset="BTC", quote_asset="USDT", position_qty=1)
    portfolio.snapshot(100)
    portfolio.snapshot(80)

    metrics = calculate_metrics(portfolio, initial_cash=100, final_price=80, first_price=50, total_fees=2)

    assert metrics.final_equity == 80
    assert metrics.total_return_pct == -20
    assert metrics.max_drawdown_pct == 20
    assert metrics.buy_and_hold_return_pct == 60
    assert metrics.fee_drag == 2


def test_verdict_rejects_drawdown_breach():
    metrics = MetricSummary(
        initial_cash=100,
        final_equity=120,
        total_return_pct=20,
        max_drawdown_pct=25,
        trade_count=100,
        fee_drag=1,
    )

    verdict, warnings = choose_verdict(metrics, max_drawdown_pct=20, min_trade_count=30, sample_label="OUT_OF_SAMPLE")

    assert verdict == Verdict.REJECT
    assert "DRAWDOWN_BREACHED" in warnings


def test_verdict_requires_trade_count_floor():
    metrics = MetricSummary(
        initial_cash=100,
        final_equity=120,
        total_return_pct=20,
        max_drawdown_pct=5,
        trade_count=1,
        fee_drag=1,
    )

    verdict, warnings = choose_verdict(metrics, max_drawdown_pct=20, min_trade_count=30, sample_label="OUT_OF_SAMPLE")

    assert verdict == Verdict.INSUFFICIENT_DATA
    assert "TRADE_COUNT_BELOW_FLOOR" in warnings


def test_verdict_marks_in_sample_as_conditional():
    metrics = MetricSummary(
        initial_cash=100,
        final_equity=120,
        total_return_pct=20,
        max_drawdown_pct=5,
        trade_count=100,
        fee_drag=1,
    )

    verdict, warnings = choose_verdict(metrics, max_drawdown_pct=20, min_trade_count=30, sample_label="IN_SAMPLE")

    assert verdict == Verdict.CONDITIONAL
    assert "NOT_OUT_OF_SAMPLE" in warnings


def test_write_report_outputs_json_and_summary(tmp_path):
    report = ResearchReport(
        run_id="run_20260502_123005_smoke",
        status="COMPLETED",
        verdict=Verdict.CONDITIONAL,
        metrics=MetricSummary(
            initial_cash=100,
            final_equity=120,
            total_return_pct=20,
            max_drawdown_pct=5,
            trade_count=100,
            fee_drag=1,
        ),
        warnings=["NOT_OUT_OF_SAMPLE"],
    )

    report_path = tmp_path / "report.json"
    summary_path = tmp_path / "summary.md"
    write_report(report, report_path, summary_path)

    assert json.loads(report_path.read_text(encoding="utf-8"))["verdict"] == "CONDITIONAL"
    assert "NOT_OUT_OF_SAMPLE" in render_summary(report)
    assert "Verdict" in summary_path.read_text(encoding="utf-8")


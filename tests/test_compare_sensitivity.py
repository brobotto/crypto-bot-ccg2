import json

from cbot.research.compare import compare_runs, render_comparison
from cbot.research.sensitivity import config_with_parameter, parse_values, run_sensitivity

from tests.test_config import raw_config
from cbot.config import RunConfig


def write_report(run_dir, run_id, total_return):
    run_dir.mkdir()
    (run_dir / "report.json").write_text(
        json.dumps(
            {
                "run_id": run_id,
                "verdict": "CONDITIONAL",
                "metrics": {
                    "total_return_pct": total_return,
                    "max_drawdown_pct": 5,
                    "trade_count": 30,
                    "fee_drag": 1,
                    "buy_and_hold_return_pct": 10,
                },
                "warnings": [],
            }
        ),
        encoding="utf-8",
    )


def test_compare_runs_is_descriptive(tmp_path):
    first = tmp_path / "run_a"
    second = tmp_path / "run_b"
    write_report(first, "run_a", 1)
    write_report(second, "run_b", 2)

    comparison = compare_runs([first, second])
    rendered = render_comparison(comparison)

    assert len(comparison["runs"]) == 2
    assert "does not select best parameters" in comparison["warnings"][0]
    assert "| run_a |" in rendered


def test_parse_values_converts_numbers_and_strings():
    assert parse_values("1,2.5,foo") == [1, 2.5, "foo"]


def test_config_with_parameter_updates_label_and_value():
    config = RunConfig.from_dict(raw_config())
    updated = config_with_parameter(config, "fast_window", 10)

    assert updated.strategy_parameters["fast_window"] == 10
    assert updated.label.endswith("fast_window_10")
    assert config.strategy_parameters["fast_window"] == 2


def test_run_sensitivity_calls_backtest_for_each_value(tmp_path):
    config = RunConfig.from_dict(raw_config())
    calls = []

    class Result:
        def __init__(self, label):
            self.run_id = label
            self.run_dir = tmp_path / label
            self.signals_seen = 0
            self.fills_seen = 0

    def fake_backtest(variant, candles, strategy, runs_root):
        calls.append((variant.strategy_parameters["fast_window"], runs_root))
        return Result(variant.label)

    results = run_sensitivity(config, [], "fast_window", [3, 4], tmp_path, backtest_fn=fake_backtest)

    assert [call[0] for call in calls] == [3, 4]
    assert len(results) == 2


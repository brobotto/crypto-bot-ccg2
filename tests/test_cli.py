from cbot.cli import build_parser, main
from cbot.types import Candle
from datetime import UTC, datetime


def test_cli_help_exits_cleanly(capsys):
    assert main([]) == 0
    captured = capsys.readouterr()
    assert "Local-first crypto research workbench" in captured.out


def test_cli_has_expected_commands():
    parser = build_parser()
    command_actions = [
        action for action in parser._actions if action.__class__.__name__ == "_SubParsersAction"
    ]
    assert command_actions
    commands = set(command_actions[0].choices)
    assert {"fetch-data", "backtest", "compare", "sensitivity", "report"} <= commands


def test_fetch_data_command_uses_market_data_layer(monkeypatch, capsys):
    candle = Candle(
        symbol="BTCUSDT",
        timeframe="1h",
        timestamp=datetime(2024, 1, 1, tzinfo=UTC),
        open=100,
        high=110,
        low=90,
        close=105,
        volume=10,
    )

    monkeypatch.setattr("cbot.cli.fetch_klines", lambda *args: [candle])
    monkeypatch.setattr("cbot.cli.MarketDataStore.write_candles", lambda self, candles: "fake.parquet")

    result = main(
        [
            "fetch-data",
            "--symbol",
            "BTCUSDT",
            "--timeframe",
            "1h",
            "--start",
            "2024-01-01",
            "--end",
            "2024-01-02",
        ]
    )

    captured = capsys.readouterr()
    assert result == 0
    assert "Wrote 1 candles to fake.parquet" in captured.out


def test_backtest_command_uses_engine(monkeypatch, tmp_path, capsys):
    config_path = tmp_path / "config.yaml"
    config_path.write_text("{}", encoding="utf-8")

    class FakeStore:
        def __init__(self, root):
            self.root = root

        def read_candles(self, symbol, timeframe):
            return []

    class FakeConfig:
        symbol = "BTCUSDT"
        timeframe = "1h"
        strategy_name = "cash_no_trade"

        @classmethod
        def from_yaml(cls, path):
            assert path == config_path
            return cls()

    class FakeResult:
        run_id = "run_20260502_123005_smoke"
        run_dir = "logs/runs/run_20260502_123005_smoke"

    monkeypatch.setattr("cbot.cli.RunConfig", FakeConfig)
    monkeypatch.setattr("cbot.cli.MarketDataStore", FakeStore)
    monkeypatch.setattr("cbot.cli.run_backtest", lambda config, candles, strategy: FakeResult())

    result = main(["backtest", "--config", str(config_path)])

    captured = capsys.readouterr()
    assert result == 0
    assert "Wrote run run_20260502_123005_smoke" in captured.out

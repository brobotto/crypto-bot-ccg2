"""Command-line entry point for the crypto research workbench."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path

from cbot import __version__
from cbot.config import RunConfig
from cbot.engine.backtest import run_backtest
from cbot.market_data.binance import fetch_klines
from cbot.market_data.store import MarketDataStore
from cbot.market_data.validation import validate_candles
from cbot.research.compare import compare_runs, load_report, render_comparison
from cbot.research.sensitivity import parse_values, run_sensitivity
from cbot.strategies import STRATEGIES


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cbot",
        description="Local-first crypto research workbench.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command")

    fetch_data = subparsers.add_parser("fetch-data", help="Fetch public market data.")
    fetch_data.add_argument("--symbol", required=True)
    fetch_data.add_argument("--timeframe", default="1h")
    fetch_data.add_argument("--start", required=True)
    fetch_data.add_argument("--end", required=True)

    backtest = subparsers.add_parser("backtest", help="Run a historical backtest.")
    backtest.add_argument("--config", required=True)

    compare = subparsers.add_parser("compare", help="Compare completed run directories.")
    compare.add_argument("--runs", nargs="+", required=True)

    sensitivity = subparsers.add_parser("sensitivity", help="Run a bounded sensitivity sweep.")
    sensitivity.add_argument("--config", required=True)
    sensitivity.add_argument("--param", required=True)
    sensitivity.add_argument("--values", required=True)

    report = subparsers.add_parser("report", help="Render a report for one run directory.")
    report.add_argument("--run", required=True)

    return parser


def parse_date(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


def handle_fetch_data(args: argparse.Namespace) -> int:
    candles = fetch_klines(args.symbol, args.timeframe, parse_date(args.start), parse_date(args.end))
    warnings = validate_candles(candles, args.symbol, args.timeframe)
    for warning in warnings:
        print(f"data warning [{warning.code}]: {warning.message}")
    path = MarketDataStore(Path("data/market")).write_candles(candles)
    print(f"Wrote {len(candles)} candles to {path}")
    return 0


def handle_backtest(args: argparse.Namespace) -> int:
    config = RunConfig.from_yaml(Path(args.config))
    candles = MarketDataStore(Path("data/market")).read_candles(config.symbol, config.timeframe)
    strategy_cls = STRATEGIES[config.strategy_name]
    result = run_backtest(config, candles, strategy_cls())
    print(f"Wrote run {result.run_id} to {result.run_dir}")
    return 0


def handle_compare(args: argparse.Namespace) -> int:
    comparison = compare_runs([Path(run) for run in args.runs])
    print(render_comparison(comparison))
    return 0


def handle_sensitivity(args: argparse.Namespace) -> int:
    config = RunConfig.from_yaml(Path(args.config))
    candles = MarketDataStore(Path("data/market")).read_candles(config.symbol, config.timeframe)
    results = run_sensitivity(
        config=config,
        candles=candles,
        parameter=args.param,
        values=parse_values(args.values),
        runs_root=Path("logs/runs"),
    )
    print("Sensitivity runs completed:")
    for result in results:
        print(f"- {result.run_id}: {result.run_dir}")
    print("No winner was selected; compare the generated reports before making decisions.")
    return 0


def handle_report(args: argparse.Namespace) -> int:
    report = load_report(Path(args.run))
    print(f"Run: {report['run_id']}")
    print(f"Verdict: {report['verdict']}")
    print(f"Total return: {report['metrics']['total_return_pct']:.4f}%")
    print(f"Max drawdown: {report['metrics']['max_drawdown_pct']:.4f}%")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "fetch-data":
        return handle_fetch_data(args)
    if args.command == "backtest":
        return handle_backtest(args)
    if args.command == "compare":
        return handle_compare(args)
    if args.command == "sensitivity":
        return handle_sensitivity(args)
    if args.command == "report":
        return handle_report(args)

    print(f"{args.command} is not implemented yet. Slice 1 only created the CLI shell.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

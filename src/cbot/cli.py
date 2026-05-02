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

    print(f"{args.command} is not implemented yet. Slice 1 only created the CLI shell.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

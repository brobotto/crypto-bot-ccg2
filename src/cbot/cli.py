"""Command-line entry point for the crypto research workbench."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from cbot import __version__


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


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    print(f"{args.command} is not implemented yet. Slice 1 only created the CLI shell.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


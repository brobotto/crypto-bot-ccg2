"""Bounded sensitivity sweeps."""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path
from typing import Callable

from cbot.config import RunConfig
from cbot.engine.backtest import BacktestResult, run_backtest
from cbot.strategies import STRATEGIES
from cbot.types import Candle


def parse_values(raw: str) -> list[float | int | str]:
    values: list[float | int | str] = []
    for item in raw.split(","):
        stripped = item.strip()
        if not stripped:
            continue
        try:
            number = float(stripped)
        except ValueError:
            values.append(stripped)
            continue
        values.append(int(number) if number.is_integer() else number)
    return values


def config_with_parameter(config: RunConfig, parameter: str, value: float | int | str) -> RunConfig:
    parameters = dict(config.strategy_parameters)
    parameters[parameter] = value
    label = f"{config.label}_{parameter}_{value}"
    return replace(config, label=label, strategy_parameters=parameters)


def run_sensitivity(
    config: RunConfig,
    candles: list[Candle],
    parameter: str,
    values: list[float | int | str],
    runs_root: Path,
    backtest_fn: Callable[..., BacktestResult] = run_backtest,
) -> list[BacktestResult]:
    results: list[BacktestResult] = []
    strategy_cls = STRATEGIES[config.strategy_name]
    for value in values:
        variant = config_with_parameter(config, parameter, value)
        results.append(backtest_fn(variant, candles, strategy_cls(), runs_root))
    return results

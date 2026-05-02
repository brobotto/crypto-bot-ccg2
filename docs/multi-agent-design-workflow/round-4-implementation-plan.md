# Round 4 - Implementation Plan

Status: `draft`
Date: `2026-05-02`
Source:

- `round-3-final-architecture.md`

## Goal

Convert the final architecture into an implementation plan for milestone 1.

Milestone 1 builds a local-first crypto research workbench with deterministic historical backtesting, simulated portfolio accounting, structured logs, benchmark comparison, sensitivity analysis, and cautious research verdicts.

## Proposed Project Layout

```text
crypto-bot-ccg2/
  pyproject.toml
  README.md
  config/
    example-run.yaml
  data/
    market/
      .gitkeep
  logs/
    schema/
      v1/
        run.started.schema.json
        strategy.signal.schema.json
        simulation.fill.schema.json
        portfolio.snapshot.schema.json
        run.completed.schema.json
    runs/
      .gitkeep
  src/
    cbot/
      __init__.py
      cli.py
      config.py
      types.py
      market_data/
        __init__.py
        binance.py
        store.py
        validation.py
      strategies/
        __init__.py
        protocol.py
        baselines.py
        sma_cross_v1.py
      engine/
        __init__.py
        backtest.py
        execution.py
        portfolio.py
        events.py
      research/
        __init__.py
        metrics.py
        reporter.py
        compare.py
        sensitivity.py
        verdicts.py
  tests/
    test_config.py
    test_market_data_validation.py
    test_strategy_protocol.py
    test_backtest_determinism.py
    test_execution_simulator.py
    test_portfolio.py
    test_events_schema.py
    test_metrics_verdicts.py
```

## Dependency Plan

Keep dependencies small.

Required:

- `pandas` or `polars` for data handling.
- `pyarrow` for Parquet support.
- `requests` or `httpx` for public Binance historical candle fetching.
- `pydantic` or `dataclasses` plus manual validation for config/domain objects.
- `PyYAML` for run configs.
- `pytest` for tests.
- `jsonschema` for validating event logs against v1 schemas.

Recommended initial choice:

- Use `pandas` + `pyarrow` because they are familiar and stable.
- Use `dataclasses` for core domain types unless validation complexity forces `pydantic`.
- Use `argparse` first for CLI unless command complexity grows.

## CLI Commands

Milestone 1 should expose these commands:

```powershell
py -m cbot.cli fetch-data --symbol BTCUSDT --timeframe 1h --start 2021-01-01 --end 2024-12-31
py -m cbot.cli backtest --config config/example-run.yaml
py -m cbot.cli compare --runs logs/runs/run_a logs/runs/run_b
py -m cbot.cli sensitivity --config config/example-run.yaml --param fast_window --values 10,20,30
py -m cbot.cli report --run logs/runs/<run_id>
```

## Configuration Shape

`config/example-run.yaml`:

```yaml
run:
  label: sma_cross_smoke
  sample_label: IN_SAMPLE
  train_start: "2021-01-01"
  train_end: "2023-12-31"
  test_start: "2024-01-01"
  test_end: "2024-12-31"

market:
  exchange: binance
  symbol: BTCUSDT
  quote: USDT
  timeframe: 1h

strategy:
  name: sma_cross_v1
  version: "1.0.0"
  parameters:
    fast_window: 20
    slow_window: 50

portfolio:
  initial_cash: 10000
  base_asset: BTC
  quote_asset: USDT

simulation:
  fee_bps: 10
  slippage_bps: 20
  max_drawdown_pct: 20
  min_trade_count: 30
  drawdown_mode: flag_only
```

## Core Domain Types

Define shared types in `src/cbot/types.py`:

- `Candle`
- `Signal`
- `OrderIntent`
- `Fill`
- `PortfolioSnapshot`
- `RunMetadata`
- `StrategyMetadata`
- `MetricSummary`
- `Verdict`

Keep these small and serializable.

## v1 Event Schema

Define field-level JSON Schema before engine implementation.

Minimum schemas:

- `run.started`
- `strategy.signal`
- `simulation.fill`
- `portfolio.snapshot`
- `run.completed`

All event records should include:

- `schema_version`
- `event_type`
- `run_id`
- `timestamp`
- `sequence`

Recommended common envelope:

```json
{
  "schema_version": "1.0",
  "event_type": "strategy.signal",
  "run_id": "run_20260502_160000_sma_cross",
  "timestamp": "2024-01-01T01:00:00Z",
  "sequence": 42,
  "payload": {}
}
```

## Implementation Slices

### Slice 1 - Project Skeleton

Create:

- `pyproject.toml`
- source package
- tests folder
- config example
- data/log directories

Acceptance:

- `pytest` runs.
- `py -m cbot.cli --help` works.

### Slice 2 - Event Schema and Logger

Create:

- JSON Schema files.
- event envelope type.
- append-only JSONL writer.
- run directory creation.
- frozen config and strategy metadata output.

Acceptance:

- event schema tests pass.
- a fake run can write valid JSONL events.

### Slice 3 - Market Data Layer

Create:

- Binance public OHLCV fetcher.
- candle validator.
- Parquet store partitioned by symbol/timeframe.
- local read path.

Acceptance:

- can fetch and persist sample `BTCUSDT` `1h` candles.
- validation catches duplicate, missing, and unordered candles.
- no credentials are needed.

### Slice 4 - Strategy Protocol and Baselines

Create:

- strategy protocol.
- `cash_no_trade`.
- `buy_and_hold`.
- `sma_cross_v1`.

Acceptance:

- strategies expose required metadata.
- strategy logic is deterministic for fixed inputs.
- invalid parameters fail clearly.

### Slice 5 - Backtest Engine

Create:

- deterministic candle replay.
- warmup handling.
- no-future-data boundary.
- signal event emission.

Acceptance:

- same input run produces same event stream.
- golden dataset test proves no future candle access.

### Slice 6 - Execution and Portfolio Simulation

Create:

- order-intent conversion.
- fee/slippage application.
- insufficient balance rejection.
- simulated fills.
- portfolio accounting.
- drawdown tracking.

Acceptance:

- known trade sequence produces expected balances, equity, PnL, and drawdown.
- drawdown breach is flagged.

### Slice 7 - Metrics, Verdicts, and Reports

Create:

- metrics calculator.
- benchmark comparison.
- verdict rules.
- `report.json`.
- `summary.md`.

Acceptance:

- report includes costs, drawdown, trade count, benchmark comparison, and verdict.
- drawdown breach prevents verdict better than `REJECT`.
- low trade count becomes `INSUFFICIENT_DATA`.

### Slice 8 - Comparison and Sensitivity

Create:

- compare multiple run directories.
- run bounded parameter sweeps.
- sensitivity band warnings.

Acceptance:

- comparison report can compare two runs.
- sensitivity tool does not auto-select a winner.
- output warns when performance exists only in a narrow parameter band.

## Test Strategy

Use focused tests:

- Config parsing.
- Event schema validation.
- Candle validation.
- Strategy metadata contract.
- Backtest determinism.
- Execution simulator math.
- Portfolio accounting.
- Metrics and verdict rules.
- Golden-run smoke test.

Avoid network-dependent tests by default. Binance fetch tests should be marked as integration and skipped unless explicitly enabled.

## Definition of Done

Implementation is ready for milestone 1 when:

- All tests pass.
- Example config runs end-to-end without credentials.
- `BTCUSDT` and `ETHUSDT` `1h` historical data can be fetched and cached.
- A baseline run produces valid JSONL events, `report.json`, and `summary.md`.
- Strategy reports include benchmark comparison and anti-overfitting fields.
- There is no live order path, credential requirement, web server, or dynamic plugin loader.

## Round 4 Open Questions

- Use `pandas` or `polars` first?
- Use `argparse` or a CLI helper like `typer`?
- What exact Binance date range should the example config use?
- Should initial generated artifacts live under `logs/runs` or `runs`?
- What default trade count floor should ship: `30`, `50`, or configurable-only?
- Should drawdown breach verdict be always `REJECT`, or `CONDITIONAL` if out-of-sample is not yet run?


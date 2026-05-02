# Round 3 - Final Architecture Decision

Status: `complete`
Date: `2026-05-02`
Source:

- `00-problem-brief.md`
- `round-1-candidate-designs.md`
- `round-2-cross-review.md`
- `round-3-arbiter-brief.md`

## Decision

Milestone 1 will be a local-first crypto research workbench for Binance spot `BTC/USDT` and `ETH/USDT` on `1h` candles.

The system will support deterministic historical backtesting, simulated portfolio accounting, strategy comparison, sensitivity analysis, benchmark comparison, structured logs, and cautious research verdicts. It will not include live trading, credentials, read-only Binance account monitoring, live market dry-run, a web dashboard, or dynamic plugin loading.

## Accepted Ideas

- Codex-Architect's module boundaries:
  - Research Runner.
  - Market Data Layer.
  - Strategy boundary.
  - Backtest Engine.
  - Execution Simulator.
  - Portfolio Simulator.
  - Risk/Evaluation Layer.
  - Structured Event Logger.
  - Research Reporter.
- Claude's file-per-run discipline, immutable run artifacts, versioned log schema, mandatory strategy hypothesis/version, and verdict caution.
- Gemini's hybrid storage insight, function-like strategy discipline, and warning that `1h` OHLCV has fill-fidelity limits.
- Round 2's anti-overfitting requirements:
  - declared train/test split
  - in-sample/out-of-sample labels
  - trade count floor
  - sensitivity band warnings
  - benchmark comparison
  - no automatic parameter optimizer

## Rejected or Deferred Ideas

- Live market dry-run in milestone 1: deferred.
- Binance read-only account monitoring in milestone 1: deferred.
- Dynamic strategy plugin loading: rejected for milestone 1.
- Web dashboard: rejected for milestone 1.
- SQLite/database-first design: rejected for milestone 1.
- `1m` dual-resolution fill validation as an MVP requirement: deferred.
- Automated strategy optimization: rejected for milestone 1.
- Full exchange microstructure simulation: deferred.

## Rationale

The project currently has no confirmed profitable strategy. Therefore, milestone 1 should maximize research integrity, reproducibility, and honest rejection rather than runtime automation.

The strongest combined architecture is conservative: local files, CLI commands, deterministic replay, explicit assumptions, and structured evidence. This keeps the system small enough to build while still enforcing the habits needed before any paper/live milestone is considered.

Gemini is correct that `1h` OHLCV can hide intrabar execution ordering problems. However, requiring `1m` data now would expand ingestion, storage, validation, simulation, and testing before any strategy has earned that fidelity. The final design preserves an extension path for `1m` data and forces reports to warn when a strategy depends on intrabar assumptions.

## Final Architecture

### 1. Research Runner

Owns run orchestration:

- CLI command handling.
- Run IDs.
- Config loading.
- Strategy selection.
- Date range selection.
- Symbol/timeframe selection.
- Train/test split declaration.
- Sensitivity batches.
- Output directory creation.

The runner must freeze the effective config and strategy metadata into each run directory.

### 2. Market Data Layer

Owns public Binance historical data:

- Fetching public OHLCV candles.
- Validating timestamps, gaps, duplicates, OHLC integrity, and symbol/timeframe.
- Normalizing all timestamps to UTC.
- Persisting normalized candles.

Storage decision:

- Use Parquet or an equivalent columnar file format for normalized market data.
- Partition by symbol and timeframe.
- `1h` is required for milestone 1.
- The storage shape should allow `1m` later, but `1m` is not required for MVP completion.

### 3. Strategy Boundary

Use a provisional internal protocol, not a full dynamic plugin system.

Each strategy must provide:

- `name`
- `version`
- `hypothesis`
- parameter schema/defaults
- warmup requirements
- deterministic signal function

The signal function should be function-like:

```text
available_market_history + read_only_portfolio_view + parameters -> signal_or_none
```

Strategies may not mutate portfolio state, place orders, fetch network data, or write logs directly. Strategy output is intent. The engine owns simulation, fills, accounting, logs, and evaluation.

Security note:

Milestone 1 strategies are local Python code and therefore have normal interpreter access. This is acceptable for a private single-operator tool. Any multi-user or remote deployment must revisit sandboxing.

### 4. Backtest Engine

Owns deterministic event-driven replay:

- Replays candles chronologically.
- Enforces no future data access.
- Applies warmup periods.
- Calls the strategy boundary.
- Passes signals to execution simulation.
- Emits structured events.

Milestone 1 uses `1h` candles as the execution clock. Any strategy whose claim depends on intrabar stop-loss/take-profit ordering or precise fill timing must be capped at `CONDITIONAL` until higher-fidelity validation exists.

### 5. Execution Simulator

Owns simulated order/fill behavior:

- Converts strategy signals to simulated order intents.
- Applies required fee assumptions.
- Applies required pessimistic slippage assumptions.
- Applies basic Binance spot constraints where practical:
  - minimum notional
  - quantity precision
  - symbol validity
  - insufficient balance rejection
- Emits order intent, rejection, and fill events.

Partial fills and latency models are deferred unless a strategy reaches later candidate status.

### 6. Portfolio Simulator

Owns simulated portfolio state:

- Cash balance.
- Asset balances.
- Position/exposure.
- Realized and unrealized PnL.
- Mark-to-market equity.
- Equity curve.
- Max drawdown.
- Trade ledger.

Portfolio monitoring in milestone 1 means simulated portfolio state only.

### 7. Risk and Evaluation Layer

Owns metrics, warnings, and verdicts:

- Total return after costs.
- Buy-and-hold comparison.
- Cash/no-trade comparison.
- Max drawdown.
- Drawdown duration.
- Profit factor.
- Trade count.
- Win/loss distribution.
- Average trade return.
- Fee drag.
- Exposure time.
- Turnover.
- Parameter sensitivity.
- In-sample/out-of-sample labels.
- Data quality warnings.

Verdicts:

- `REJECT`
- `INSUFFICIENT_DATA`
- `CONDITIONAL`
- `CANDIDATE`

The system must never emit `APPROVE`.

Drawdown decision:

- Default research mode runs to completion.
- If configured max drawdown is breached, report `DRAWDOWN_BREACHED: true`.
- A drawdown breach prevents any verdict better than `REJECT`.
- Optional `halt_on_breach` can be added later as a risk-control simulation mode, but it is not the default.

### 8. Structured Event Logger

Owns append-only JSONL run logs with versioned schemas.

Run directory:

```text
logs/runs/<run_id>/
  config.resolved.json
  strategy.meta.json
  events.jsonl
  report.json
  summary.md
```

Completed run directories are immutable by convention. Later tools may read them but should not mutate them.

Required v1 event families:

- `run.started`
- `data.loaded`
- `data.validation_warning`
- `strategy.signal`
- `simulation.order_intent`
- `simulation.order_rejected`
- `simulation.fill`
- `portfolio.snapshot`
- `risk.limit_warning`
- `alert.generated`
- `metrics.summary`
- `run.completed`
- `run.failed`

Event volume policy:

- Always log run metadata, data validation warnings, strategy signals, order intents, fills/rejections, risk warnings, alerts, metrics, and completion/failure.
- Portfolio snapshots should be logged on meaningful changes and periodic checkpoints by default.
- Full candle-by-candle snapshots belong behind a debug flag.

Before implementation begins, define the v1 field-level schema for at least:

- `run.started`
- `strategy.signal`
- `simulation.fill`
- `portfolio.snapshot`
- `run.completed`

### 9. Research Reporter

Owns human and machine-readable outputs:

- `report.json` for tooling.
- `summary.md` for operator review.
- Strategy comparison reports.
- Sensitivity reports.
- Benchmark comparison.
- Rejection warnings.

The reporter should explain why a strategy was rejected or marked conditional.

## Anti-Overfitting Workflow

Milestone 1 must include anti-overfitting safeguards.

Required:

- Strategy hypothesis must be written before running.
- Train/test split must be declared before runs.
- Runs must be labeled `IN_SAMPLE`, `OUT_OF_SAMPLE`, or `FULL_PERIOD`.
- Reports must show whether the result is in-sample or out-of-sample.
- Minimum trade count floor must be configurable.
- Results below the trade count floor are `INSUFFICIENT_DATA`.
- Sensitivity analysis must report whether performance exists across a broad parameter band or only a narrow region.
- The system must not auto-select "best" parameters.
- Reports must compare against buy-and-hold and cash/no-trade baselines.

## Benchmarks and Baselines

Milestone 1 includes:

- `cash_no_trade`: sanity baseline.
- `buy_and_hold`: primary active-strategy benchmark.
- `sma_cross_v1`: engine-validation strategy only.

Reports must label these clearly so no baseline is mistaken for a profitability recommendation.

## Milestone 1 Definition of Done

Milestone 1 is done when:

1. Public Binance `1h` OHLCV for `BTC/USDT` and `ETH/USDT` can be fetched, validated, and persisted locally.
2. A deterministic event-driven backtest can run without credentials.
3. Strategies must declare `name`, `version`, `hypothesis`, parameters, and warmup requirements.
4. The engine can run at least `cash_no_trade`, `buy_and_hold`, and `sma_cross_v1`.
5. Simulated portfolio accounting tracks balances, equity, PnL, exposure, trades, and drawdown.
6. Fee and slippage assumptions are required in run config.
7. Versioned JSONL event logs are produced for every run.
8. Each run writes frozen config, strategy metadata, events, report, and summary.
9. Reports include costs, drawdown, benchmarks, sensitivity, and verdict.
10. Anti-overfitting fields are present: train/test split, sample label, trade count floor, and sensitivity warnings.
11. A weak strategy can be rejected with explicit evidence.
12. No live order path, credentials, read-only account integration, live dry-run, web server, or dynamic plugin loader exists.

## Open Questions for Round 4

- Which Python package layout should be used?
- Which CLI library should be used, if any?
- Which Parquet library should be used: `pyarrow`, `polars`, or another option?
- What exact v1 JSON Schema fields should each core event contain?
- What default fee and slippage assumptions should ship in the initial config?
- What default historical windows should be used for in-sample and out-of-sample examples?
- What minimum trade count should default to `INSUFFICIENT_DATA`?

## Next Actions

1. Create Round 4 implementation plan.
2. Define v1 event schemas before engine implementation.
3. Choose Python dependencies and project layout.
4. Implement in narrow vertical slices:
   - config and run directory
   - market data persistence
   - strategy protocol
   - backtest loop
   - portfolio simulator
   - logs and reports
   - anti-overfitting workflow


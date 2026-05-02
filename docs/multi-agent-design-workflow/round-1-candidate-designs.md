# Round 1 - Candidate Designs

Status: `complete`
Date: `2026-05-02`
Source:

- `00-problem-brief.md`
- Codex-Architect Round 1 answer
- Claude Round 1 answer
- Gemini Round 1 answer

## Purpose

Round 1 asks each architect to propose a candidate architecture from the same canonical problem brief.

The purpose is not to pick a winner yet. The purpose is to expose design options, trade-offs, and unresolved architecture decisions before Round 2 cross-review.

## Shared Direction Across Proposals

All three proposals converge on these points:

- Milestone 1 should be non-live.
- No Binance API credentials are needed in milestone 1.
- No live order placement, no read-only account monitoring, and no live WebSocket runtime are needed in milestone 1.
- The first product should be local-first and operator-triggered, not a daemon or server.
- The first interface should be CLI plus structured logs/reports.
- Strategy extension should be provisional/internal, not a full dynamic plugin system.
- The research workflow should prioritize honest rejection, sensitivity analysis, and comparison over automated optimization.
- A baseline strategy is useful only to validate framework behavior, not as a profitability claim.
- Structured logs should be a primary artifact and should be stable enough to audit runs.

## Proposal A - Codex-Architect

### Core Design

Codex-Architect proposes a historical research workbench with a strict internal strategy contract.

Major components:

- Research Runner.
- Market Data Layer.
- Provisional Strategy Interface.
- Backtest Engine.
- Execution Simulator.
- Portfolio Simulator.
- Risk/Evaluation Layer.
- Structured Event Logger.
- Research Reporter.

### Strongest Ideas

- Clear separation between strategy, simulation, portfolio accounting, risk/evaluation, logging, and reporting.
- Strategy extensibility is important, but research discipline is more important.
- Strategy emits intent-level signals; core modules own orders, fills, accounting, logging, and evaluation.
- Milestone 1 definition of done is concrete and testable.
- Structured event families are named early:
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

### Main Trade-offs

- Uses `1h` OHLCV first, which keeps the system focused but limits execution realism.
- Chooses a provisional internal strategy interface, accepting future migration cost.
- Defers live dry-run and read-only monitoring, keeping milestone 1 safer but validating runtime concerns later.

## Proposal B - Claude

### Core Design

Claude proposes `strabot-research`: a single-process, file-in/file-out research system with no server, no database daemon, no API surface, and CLI as the only operator interface.

Major directories:

- `data/raw`
- `data/cache`
- `strategies`
- `engine`
- `research`
- `logs/schema/v1`
- `logs/runs`
- `config`

### Strongest Ideas

- Event-driven backtesting instead of vectorized backtesting to reduce look-ahead bias.
- File-per-run output directories for reproducibility and auditability.
- Required `hypothesis` and `version` fields on every strategy.
- Versioned JSON Schema for log events from day one.
- Completed run directories should be immutable.
- No network imports outside data loading.
- Drawdown threshold can mark or halt simulation runs.
- The system should never output `APPROVE`; possible verdicts are `REJECT`, `INSUFFICIENT_DATA`, `CONDITIONAL`, or `CANDIDATE`.

### Main Trade-offs

- Chooses JSONL/local files over SQLite for auditability and simplicity.
- Avoids dynamic plugin loading.
- Treats alerts as log events only.
- Prefers research workflow before formal plugin design.

## Proposal C - Gemini

### Core Design

Gemini proposes a Stateless Functional Research Pipeline.

Major components:

- Ingestion Layer / Harvester.
- Simulation Engine / Time-Machine.
- Strategy boundary as a pure function:
  - `(MarketState, AccountState) -> Signal`
- Observer / Black Box JSON logger.
- Evaluator / Inquisitor post-processing tool.

### Strongest Ideas

- Parquet for time-series storage and data science workflows.
- Dual-resolution execution: `1h` signals with `1m` candles for fill validation.
- Pure-function strategy boundary for reproducibility.
- Post-process evaluator can run sensitivity and Monte Carlo slippage simulations without rerunning the main backtest where possible.
- Deterministic seeds for any randomized stress tests.
- Stress tests should include higher slippage and randomized order failures.

### Main Trade-offs

- More data fidelity and future analytical power, but more storage and implementation complexity.
- Dual-resolution execution may be valuable for honest fills, but may be too expensive for milestone 1 if the first strategies do not require intrabar assumptions.
- Parquet is strong for analytics but less directly inspectable than JSONL.

## Key Architecture Decisions for Round 2 Review

Round 2 should challenge these questions:

1. Storage format:
   - JSONL only.
   - JSONL run logs plus raw data files.
   - Parquet for market data plus JSONL for event logs.
   - SQLite or another store.

2. Backtest fidelity:
   - `1h` OHLCV only for milestone 1.
   - Optional `1m` data for fill validation.
   - Fee/slippage assumptions only.
   - Partial fills and latency assumptions.

3. Strategy boundary:
   - Abstract base class.
   - Pure function.
   - Provisional internal interface.
   - Full plugin system, likely rejected for milestone 1.

4. Log contract:
   - JSONL event logs.
   - Versioned JSON Schema.
   - File-per-run directories.
   - Whether every candle should emit portfolio snapshots or only meaningful changes plus periodic snapshots.

5. Research workflow:
   - Comparison across fixed windows.
   - Sensitivity analysis.
   - Monte Carlo/stress testing.
   - No automated optimization.

6. Drawdown handling:
   - Halt the simulation on threshold breach.
   - Continue and flag threshold breach.
   - Support both modes depending on run config.

7. Baseline strategy:
   - SMA crossover.
   - Buy-and-hold benchmark.
   - Cash/no-trade baseline.
   - One baseline only for engine validation versus multiple benchmarks for reporting.

8. Milestone 1 output:
   - CLI commands.
   - Structured logs.
   - JSON reports.
   - Human-readable summaries.

## Round 1 Interim Synthesis

The strongest combined direction is:

- Local-first CLI research workbench.
- Public Binance historical data only.
- Market data persisted separately from run logs.
- JSONL event logs with versioned schemas.
- File-per-run output directories.
- Provisional strategy interface with required hypothesis/version metadata.
- Deterministic event-driven backtesting.
- Simulated portfolio accounting.
- Fee and slippage assumptions required by config.
- Sensitivity and comparison workflow.
- No live dry-run, no credentials, no read-only account monitoring, no dynamic plugin system in milestone 1.

Round 2 should not reopen live trading. It should focus on selecting the best storage/fidelity/strategy-boundary/log-schema choices from the three proposals.

## Next Actions

1. Send this file plus `00-problem-brief.md` to Codex-Architect, Claude, and Gemini with the Round 2 cross-review prompt.
2. Ask each agent to challenge the other proposals and rank the unresolved architecture decisions.
3. After Round 2, Codex-Arbiter should produce `round-3-final-architecture.md`.


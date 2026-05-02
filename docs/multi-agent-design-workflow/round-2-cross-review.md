# Round 2 - Cross Review

Status: `complete`
Date: `2026-05-02`
Source:

- `00-problem-brief.md`
- `round-1-candidate-designs.md`
- Codex-Architect Round 2 answer
- Claude Round 2 answer
- Gemini Round 2 answer

## Purpose

Round 2 challenges the Round 1 candidate architectures and identifies which design choices should be combined, rejected, deferred, or escalated to Codex-Arbiter for Round 3.

## Strong Consensus

All reviewers support:

- Local-first CLI research workbench.
- No live trading in milestone 1.
- No credentials in milestone 1.
- No read-only Binance account monitoring in milestone 1.
- No dynamic plugin system in milestone 1.
- Event-driven backtesting.
- Strategy metadata, especially required `hypothesis` and `version`.
- Structured JSONL event logs for run auditability.
- Immutable run directories.
- Public Binance historical data only.
- Research workflow focused on rejection, comparison, and sensitivity analysis.
- No automated optimizer that searches for the best-looking backtest.

## Major Agreements

### Hybrid Storage

Codex-Architect and Claude agree that the best storage model is hybrid:

- Parquet or similar columnar format for normalized historical candle data.
- JSONL for run/event logs.
- JSON reports and frozen config/metadata snapshots inside each run directory.

Gemini also supports Parquet for market data and JSONL for logs.

Decision pressure:

- High confidence. Round 3 should adopt hybrid storage unless implementation constraints make Parquet impractical.

### Strategy Boundary

The combined recommendation is not a heavy abstract base class and not a metadata-free pure function.

Preferred shape:

- A small protocol-style internal strategy interface.
- Required metadata:
  - `name`
  - `version`
  - `hypothesis`
  - parameter schema/defaults
  - warmup requirements
- Signal behavior should remain function-like and deterministic.
- Engine owns state, simulation, portfolio, logging, and evaluation.

Decision pressure:

- High confidence. Round 3 should adopt a metadata-bearing protocol with pure-function-like strategy logic.

### Drawdown Behavior

Codex-Architect recommends supporting both `flag_only` and `halt_on_breach`.

Claude recommends always running to completion and using drawdown breach as a verdict gate.

Gemini ranks drawdown behavior as lower priority and supports flagging unless portfolio hits zero.

Decision pressure:

- Medium-high confidence. Round 3 should likely choose run-to-completion as default research mode, record `DRAWDOWN_BREACHED`, and block any verdict better than `REJECT` or `CONDITIONAL`. Optional `halt_on_breach` may be added as a separate risk-control simulation mode later.

### Baselines and Benchmarks

Codex-Architect recommends:

- cash/no-trade
- buy-and-hold
- simple rule strategy such as SMA crossover

Claude strongly argues that buy-and-hold is the primary active-strategy benchmark and SMA crossover should be engine validation only.

Decision pressure:

- High confidence. Round 3 should include buy-and-hold benchmark, cash/no-trade baseline, and one simple engine-validation strategy.

## Major Disagreement

### 1m Dual-Resolution Fill Validation

Gemini argues strongly that `1h` OHLCV creates a fidelity gap, especially for stop-loss/take-profit ordering inside a candle. Gemini recommends `1h` signals with `1m` candles for fill validation.

Codex-Architect and Claude recommend deferring `1m` from milestone 1:

- Milestone 1 is about historical research and hypothesis rejection.
- `1m` ingestion/validation/storage/test complexity is large.
- No chosen strategy currently requires stop-loss/take-profit ordering.
- Required pessimistic slippage and explicit report warnings may be enough for first milestone.

Synthesis:

- Gemini is right about the fidelity risk.
- Codex-Architect and Claude are likely right about milestone scope.
- The final architecture should not depend on `1m` data for MVP completion.
- The market data layer should be designed so `1m` data can be added later.
- Reports must explicitly flag when a strategy's claim depends on intrabar price ordering or fill precision.
- Round 3 should decide whether `1m` is:
  - deferred entirely to milestone 2, or
  - represented as an optional future-compatible data resolution but not required for MVP.

## Critical Issues Raised

### Log Schema Is the Primary Interface

Claude argues that all proposals underspecify the log schema, even though structured logs are the first operator interface.

Round 3 should require v1 field-level schema before implementation for at least:

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

Round 3 should also define event volume policy:

- Always log run metadata, validation warnings, signals, order intents, fills/rejections, risk warnings, alerts, and final metrics.
- Portfolio snapshots should be periodic and on meaningful changes by default.
- Full candle-by-candle logging should be debug mode, not default.

### Anti-Overfitting Is Under-Specified

Claude identifies anti-overfitting as a core product requirement, not a nice-to-have.

Round 3 should include:

- Declared train/test split before runs.
- In-sample and out-of-sample labels on every run.
- Trade count floor for result validity.
- Sensitivity band reporting.
- Benchmark comparison.
- Warnings for narrow parameter bands.
- No auto-selection of best parameters.

### Post-Processing Limits

Codex-Architect warns that post-processing sensitivity or Monte Carlo slippage is only valid when it does not alter simulated state.

Round 3 should distinguish:

- Safe post-processing:
  - metrics recalculation
  - report formatting
  - simple sensitivity on assumptions that do not change fills/signals
- Must rerun simulation:
  - slippage changes that affect fills
  - rejected order scenarios
  - balance/exposure changes
  - anything that could alter future signals

## Ranked Decisions for Round 3

1. Log schema and event volume policy.
2. Anti-overfitting workflow.
3. Hybrid storage format.
4. Strategy boundary.
5. Backtest fidelity and whether `1m` is deferred or optional.
6. Drawdown handling and verdict gating.
7. Baselines and benchmarks.
8. Definition of done.

## Recommended Combined Architecture for Arbiter

Round 3 should combine:

- Codex-Architect's module boundaries.
- Claude's file-per-run, schema-versioning, immutability, verdict discipline, and anti-overfitting workflow.
- Gemini's Parquet market-data storage insight, functional strategy discipline, and fidelity warning around `1h` OHLCV.

Recommended defaults:

- Market data: Parquet, partitioned by symbol/timeframe.
- Event logs: JSONL, versioned schema, one immutable directory per run.
- Backtester: deterministic event-driven replay.
- Strategy boundary: protocol with required metadata and function-like signal generation.
- Timeframe: `1h` required for MVP.
- `1m` data: deferred from MVP, but supported later by storage shape.
- Fill model: required fee and pessimistic slippage assumptions.
- Drawdown: run to completion by default; breach gates verdict.
- Benchmarks: cash/no-trade, buy-and-hold, and simple SMA crossover for engine validation.
- Verdicts: `REJECT`, `INSUFFICIENT_DATA`, `CONDITIONAL`, `CANDIDATE`; never `APPROVE`.

## Next Actions

1. Codex-Arbiter produces `round-3-final-architecture.md`.
2. Round 3 should explicitly decide the `1m` fidelity question.
3. Round 3 should define milestone 1 done criteria.
4. Round 3 should produce an implementation plan outline for Round 4.


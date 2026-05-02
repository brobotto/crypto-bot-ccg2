# Round 3 - Arbiter Brief

Status: `ready`
Date: `2026-05-02`

## Inputs

Use these files:

- `00-problem-brief.md`
- `round-1-candidate-designs.md`
- `round-2-cross-review.md`

## Arbiter Task

Produce the final architecture decision for milestone 1.

You must decide:

- Storage model.
- Strategy boundary.
- Backtest fidelity.
- Log schema/event policy.
- Anti-overfitting workflow.
- Drawdown behavior.
- Benchmarks and baselines.
- Milestone 1 definition of done.

## Constraints

Do not reopen:

- Live trading in milestone 1.
- Binance credentials in milestone 1.
- Read-only account monitoring in milestone 1.
- Dynamic plugin loading in milestone 1.
- Web dashboard in milestone 1.

## Decisions the Arbiter Should Likely Adopt

- Hybrid storage: Parquet for market data, JSONL for run events.
- Deterministic event-driven backtesting.
- Metadata-bearing strategy protocol with function-like signal generation.
- `1h` data required for MVP.
- `1m` data deferred but made possible by storage partitioning.
- Required fee and pessimistic slippage assumptions.
- Run-to-completion default with `DRAWDOWN_BREACHED` verdict gating.
- Buy-and-hold and cash/no-trade benchmarks.
- SMA crossover as engine-validation strategy only.
- Versioned v1 event schema before implementation.
- Declared train/test split and in-sample/out-of-sample labels.

## Open Decision Needing Care

The only major unresolved disagreement is `1m` dual-resolution fill validation.

Recommended stance:

- Do not make `1m` data a milestone 1 requirement.
- Do design market data storage and simulation interfaces so additional timeframes can be added later.
- Reports must warn when a strategy relies on intrabar fill assumptions.
- Any strategy requiring stop-loss/take-profit ordering inside a candle cannot be promoted beyond `CONDITIONAL` until higher-fidelity validation exists.


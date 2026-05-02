# Round 0 - Brief Synthesis

Status: `complete`
Date: `2026-05-02`
Source:

- `round-minus-1-trading-bot-principles.md`
- `round-0-problem-framing.md`
- Codex-Architect Round 0 answer
- Claude Round 0 answer
- Gemini Round 0 answer
- User clarifications

## Purpose

This file records the Codex-Arbiter synthesis step between Round 0 agent answers and the canonical problem brief.

The output of this synthesis is:

- `00-problem-brief.md`

## Inputs

### User Clarifications

- Milestone interests: backtesting, paper trading readiness, alert bot, portfolio monitor.
- No real funds in milestone 1.
- Market scope: Binance spot.
- Asset scope: `BTC/USDT`, `ETH/USDT`.
- First timeframe: `1h`.
- Strategy hypothesis: none confirmed.
- First interface: log files.
- Risk boundary: maximum drawdown of `10-20%`.
- Live market dry-run is desirable, but sequencing is uncertain.
- Binance read-only account monitoring is uncertain and should be debated.
- The user is interested in both a strategy plugin interface and a strategy research workflow.

### Codex-Architect Contribution

Codex-Architect framed the project as a non-live research and simulation system. The strongest point was sequencing: milestone 1 should prove trustworthy evaluation, reproducible results, structured audit logs, and rejection criteria before live market dry-run or read-only Binance account integration are assumed.

Key concerns:

- Scope creep across backtesting, plugins, alerts, monitoring, dry-run, and account integration.
- False confidence from weak simulation realism.
- Ambiguous meaning of portfolio monitoring, paper trading, alerts, and max drawdown.
- Need to define strategy boundary and evaluation workflow.

### Claude Contribution

Claude challenged the scope and argued that the project contains two different goals:

- Research tooling.
- Runtime infrastructure.

The strongest point was that milestone 1 needs explicit exit criteria, a defined structured log schema, and a decision about whether the strategy interface is a real plugin contract or a provisional internal abstraction.

Claude recommended research workflow before plugin formalization, because real strategy experiments should teach what the plugin contract needs to be.

### Gemini Contribution

Gemini framed the project as a hypothesis-first research platform.

The strongest point was that high-fidelity backtesting and strategy comparison are more valuable in milestone 1 than live dry-run, because live dry-run on a `1h` timeframe takes weeks to produce meaningful evidence.

Gemini recommended sensitivity analysis over automated optimization to reduce curve fitting.

## Synthesis

### Canonical Problem Statement

This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`.

The first milestone should support historical backtesting, structured log-based observability, simulated portfolio monitoring, strategy comparison, and strategy hypothesis rejection without placing live orders or using real funds.

Because no strategy hypothesis is confirmed yet, the architecture must help define, test, compare, monitor, and reject strategies honestly rather than assuming a profitable strategy already exists.

### Settled Decisions

- Milestone 1 is non-live.
- Historical backtesting comes before live market dry-run.
- Binance read-only account monitoring is deferred from milestone 1 unless Round 1 justifies a minimal future-compatible boundary.
- Portfolio monitoring starts as simulated portfolio state.
- Research workflow is central to milestone 1.
- Automated optimization is not a milestone 1 priority.
- Sensitivity analysis and comparison are preferred over parameter chasing.
- Structured logs are the first operator interface.

### Remaining Round 1 Design Questions

- What is the formal definition of done for milestone 1?
- What structured log format and event schema should be the first operator interface?
- Should the strategy extension boundary be a real plugin contract or a provisional internal abstraction?
- How should the research workflow prevent overfitting and false confidence?
- What baseline strategy, if any, should be included only to validate framework behavior?
- How much Binance order-rule simulation is necessary in historical backtesting?
- What metrics are required in milestone 1 versus later?
- Should backtesting use only `1h` OHLCV candles first, or should data storage leave room for higher-resolution candles later?
- Where should historical data be persisted: local files, SQLite, another database, or on-demand fetching with cache?

## Decision

Proceed to Round 1 candidate architecture proposals using `00-problem-brief.md` as the canonical problem brief.

Round 1 architects should not reopen live trading as milestone 1 scope. They may propose minimal interface boundaries that keep future live dry-run possible without adding credentials, live runtime loops, or account integration now.

## Next Actions

1. Send `00-problem-brief.md` to Codex-Architect, Claude, and Gemini with Round 1 prompts.
2. Require each architect to answer the remaining design questions.
3. After receiving Round 1 proposals, run Round 2 cross-review.


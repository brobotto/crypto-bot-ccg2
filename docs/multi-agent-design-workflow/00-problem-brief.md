# Problem Brief

Status: `round-0-synthesized`
Date: `2026-05-02`
Source: Round -1 and Round 0 synthesis

## Goal

Build a safety-first crypto research and paper-readiness system for Binance spot markets. The system should help define, test, compare, monitor, and reject trading strategy hypotheses before any real-money trading is considered.

The project should not begin as "build a profitable bot." It should begin as "build a narrow, auditable research and simulation system that can test whether any proposed strategy deserves further attention."

## Target Users

- Primary operator: the repo owner.
- Secondary future user: a technical operator who can read logs, review backtests, inspect assumptions, and decide whether a strategy is worth paper or live testing.

ASSUMPTION: This is a private or small-team tool, not a public SaaS product.

## Confirmed Scope

- Exchange/data source: Binance.
- Market type: spot only.
- Assets: `BTC/USDT`, `ETH/USDT`.
- First timeframe: `1h`.
- First interface: structured log files.
- Real funds: out of scope for milestone 1.
- Withdrawal permissions: out of scope.
- Margin, futures, perpetuals, and leverage: out of scope.
- Risk boundary: maximum drawdown target/limit of `10-20%` for evaluation and future controls.

## Milestone 1

Milestone 1 should include:

- Historical backtesting for Binance spot `BTC/USDT` and `ETH/USDT` on `1h` candles.
- A carefully scoped strategy extension boundary. Round 1 should decide whether this is a real plugin contract or a provisional internal strategy interface.
- A strategy research workflow that helps compare candidate strategies, run sensitivity analysis, and reject weak ones.
- Alert generation from strategy signals or monitoring rules.
- Simulated portfolio-state monitoring.
- Structured logs for auditability and debugging.
- Clear milestone exit criteria and reports for deciding whether a strategy deserves later paper/live dry-run.

## Non-Goals

- Live order placement.
- Using real funds.
- Multiple exchanges.
- High-frequency trading.
- Cross-exchange arbitrage.
- Leverage, margin, futures, or perpetual trading.
- Complex machine learning models.
- Automatic strategy discovery that optimizes against recent backtests.
- Full web dashboard.
- Live market dry-run in milestone 1, unless Round 1 justifies a minimal future-compatible interface without adding runtime complexity.
- Binance read-only account monitoring in milestone 1, unless Round 1 justifies a strong use case.
- Tax reporting.
- Copy trading or social/news sentiment trading.

## Core Workflows

1. The operator defines or installs a strategy candidate.
2. The system loads historical Binance spot candle data.
3. The system runs a backtest with explicit fees and realistic assumptions.
4. The system records signals, simulated orders, portfolio state, drawdown, and metrics.
5. The system compares strategy results without assuming that the best backtest is a real edge.
6. The system emits structured logs and alerts.
7. The operator reviews whether a strategy should be rejected, revised, or considered for later paper/live dry-run.

## Safety and Evaluation Principles

- Every strategy must have an explicit hypothesis.
- Backtest results must be treated as evidence, not proof.
- Results should include fees, spread/slippage assumptions, drawdown, trade distribution, and sensitivity where practical.
- The system should make weak strategies easy to reject.
- The system should avoid overfitting incentives.
- Paper/live dry-run should be treated as a later milestone, not proof of live profitability.
- Any future live mode must require separate design, approval, and risk controls.
- Research tooling should favor sensitivity analysis and comparison over automated optimization.

## Open Design Questions for Round 1

- QUESTION: What is the formal definition of done for milestone 1?
- QUESTION: What structured log format and event schema should be the first operator interface?
- QUESTION: Should the strategy extension boundary be a real plugin contract or a provisional internal abstraction?
- QUESTION: How should the research workflow prevent overfitting and false confidence?
- QUESTION: What baseline strategy, if any, should be included only to validate framework behavior?
- QUESTION: How much Binance order-rule simulation is necessary in historical backtesting?
- QUESTION: What metrics are required in milestone 1 versus later?
- QUESTION: Should backtesting use only `1h` OHLCV candles first, or should data storage leave room for higher-resolution candles to improve execution assumptions later?
- QUESTION: Where should historical data be persisted: local files, SQLite, another database, or on-demand fetching with cache?

## Architecture Constraints

- The first architecture should keep live trading out of the system boundary.
- The strategy interface should be testable without Binance credentials.
- Binance credentials, if added later for read-only monitoring, must be optional and restricted.
- Logs must be structured enough to reconstruct decisions.
- Strategy code must be separated from core data loading, simulation, portfolio accounting, and reporting.
- The system should support future paper/live dry-run conceptually without forcing that runtime complexity into the first backtester.
- Live integrations requiring credentials should remain outside milestone 1 unless explicitly justified.

## Decision

Proceed to Round 1 candidate architecture proposals.

Round 1 architects should explicitly debate the open design questions rather than assuming a single answer. Candidate designs should prioritize historical research quality, reproducibility, log-based auditability, strategy comparison, and anti-overfitting safeguards.

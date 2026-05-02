# Round -1 - Trading Bot Principles

Status: `draft`
Date: `2026-05-02`
Repo: `C:\Users\User\Documents\crypto-bot-ccg2`

## Goal of This Round

Build a shared baseline for the question:

> What should a good and potentially profitable crypto trading bot have?

This round happens before project-specific problem framing. The goal is to clarify principles, risks, evaluation standards, and false assumptions before deciding what this repo should build.

Round -1 does not design this project, choose exchanges, select frameworks, or define a specific trading strategy.

## Ground Rules

- Do not claim guaranteed profit.
- Separate "good bot qualities" from "profitability requirements".
- Treat risk controls, auditability, and validation as first-class concerns.
- Assume backtest results can be misleading until proven otherwise.
- Do not recommend live trading before paper trading and risk boundaries are defined.
- Mark assumptions as `ASSUMPTION`.
- Mark questions as `QUESTION`.

## Shared Question

What should a good and potentially profitable crypto trading bot have?

## Agent Focus

### Codex-Architect

Focus on:

- System qualities.
- Architecture implications.
- Testing and verification.
- Observability and audit logs.
- Maintainability and safe iteration.

### Claude

Focus on:

- Flawed assumptions.
- Human risk and overconfidence.
- Decision boundaries.
- Edge cases and failure modes.
- What should remain human-approved.

### Gemini

Focus on:

- Alternative bot types.
- Market and data constraints.
- Exchange and integration risks.
- Evaluation methods.
- External constraints that could dominate design.

## Questions for Agents

Each agent should answer:

1. What makes a crypto trading bot good?
2. What conditions are required before it can plausibly be profitable?
3. What risk controls are non-negotiable?
4. What data, testing, and validation are required?
5. What common false assumptions should we avoid?
6. What should be excluded from MVP?
7. What are the 10 most important questions before designing our bot?

## Initial Shared Baseline

Good bot qualities:

- Clear operating mode: alerts, research, backtesting, paper trading, or live execution.
- Separation between market data, strategy logic, risk controls, execution, state, and reporting.
- Full audit trail for inputs, decisions, orders, errors, overrides, and configuration changes.
- Deterministic replay/debug mode for understanding past decisions.
- Operator controls for pause, kill switch, configuration review, and emergency shutdown.
- Safe secret handling if exchange API keys or wallet credentials ever become involved.
- Tests for strategy logic, risk logic, execution adapters, and failure handling.

Profitability requirements:

- A testable hypothesis for why the strategy should have edge.
- Historical validation without look-ahead bias, survivorship bias, or data leakage.
- Evaluation after fees, spread, slippage, funding rates, latency, and failed orders.
- Out-of-sample testing or walk-forward validation.
- Paper trading before live trading.
- Position sizing and drawdown controls.
- Monitoring for market regime changes.

Non-negotiable risk controls:

- Max position size.
- Max daily loss.
- Max drawdown.
- Per-trade risk limit.
- Exchange/API failure handling.
- Duplicate order protection.
- Kill switch.
- Dry-run or paper mode.
- Read-only mode for analysis features.
- Human approval mode before live automation.

Common false assumptions:

- Backtest profit means future profit.
- High win rate means good strategy.
- AI can reliably predict sudden market moves.
- More indicators mean better signals.
- Live trading is just backtesting with real orders.
- Exchange APIs behave reliably during volatility.
- Fees and slippage are small enough to ignore.
- A bot should trade often to be useful.

## Codex-Arbiter Synthesis Template

After the three agents answer, produce:

1. Shared principles accepted by all agents.
2. Disagreements or tensions worth preserving.
3. Non-negotiable safety requirements.
4. Evaluation standards for profitability claims.
5. MVP exclusions.
6. Questions that should flow into Round 0.

## Agent Answer Summary

### Codex-Architect

Codex-Architect framed a good bot as a controlled, observable, testable decision and execution system. The strongest points were separation of strategy, execution, risk, data, configuration, and monitoring; deterministic testing; fail-safe behavior; idempotent execution; strong state reconciliation; and explicit modes for backtest, paper, shadow, and live trading.

Codex-Architect emphasized that profitability requires a real market edge after fees, spread, slippage, latency, funding, failed orders, and regime changes. It also stressed that the bot should support strategy retirement when live performance diverges from expectations.

### Claude

Claude focused on adversarial clarity and warned that the most common failure is starting implementation before the strategy hypothesis is honest. The strongest points were that profitability belongs to the strategy, market, cost structure, execution quality, and timing together, not to the bot by itself.

Claude emphasized falsifiable strategy hypotheses, out-of-sample validation, hard drawdown circuit breakers, UTC/time discipline, human restart after major risk events, and predefined failure conditions for stopping the project or strategy.

### Gemini

Gemini emphasized alternative bot types, market/data constraints, and execution realities. The strongest points were operational resilience, telemetry, exchange integration risk, low-latency path where relevant, high-fidelity data handling, inventory management for market making or arbitrage, and the need to define the intended market regime.

Gemini also highlighted tick-to-trade latency, partial fills, orphan orders, WebSocket/REST divergence, maker/taker fee assumptions, fat-tail events, and kill-switch authority.

## Codex-Arbiter Synthesis

### Shared Principles Accepted by All Agents

- A good crypto trading bot is first a safety-critical automation system, not a profit machine.
- Strategy logic, risk controls, exchange execution, data ingestion, state management, configuration, monitoring, and reporting should be separated.
- Every trade decision must be auditable after the fact from logs and stored state.
- The bot must fail safely when data, connectivity, exchange APIs, or internal state become unreliable.
- Backtest profitability is not sufficient evidence of live profitability.
- Profitability claims must include fees, spread, slippage, latency, partial fills, failed orders, funding or borrow costs where relevant, and market regime effects.
- Paper trading is necessary before live trading, but paper trading is still not proof of live profitability.
- Risk controls belong in the MVP, not after the MVP.
- The first version should be narrow, explainable, and easy to shut down.

### Disagreements or Tensions Worth Preserving

- Claude recommends excluding dashboard and alerting from MVP, while Codex-Architect treats observability from day one as essential. The synthesis is: avoid a complex UI dashboard, but keep operational logs, basic metrics, and alerts for dangerous states.
- Gemini mentions a low-latency path, while Claude warns latency must match the strategy horizon. The synthesis is: do not optimize for low latency generally; define latency requirements only after the strategy type and timeframe are chosen.
- Claude prefers no auto-restart on crash, while production systems often need recovery behavior. The synthesis is: allow process restart only into a safe paused/reconcile mode, not automatic trading resumption.
- Codex-Architect assumes the bot may eventually trade real capital. Round 0 must confirm whether real funds are in scope for milestone 1.

### Non-Negotiable Safety Requirements

- Read-only, paper, and live modes must be explicit and hard to confuse.
- No withdrawal permissions for any exchange API key used by the bot.
- Kill switch must cancel open orders where possible and disable new trading.
- The bot must reconcile exchange/account state before trading on startup, reconnect, or restart.
- Duplicate order protection is required.
- Hard maximums are required for order size, position size, portfolio exposure, daily loss, drawdown, open orders, and order rate.
- The bot must halt or enter safe mode on stale data, repeated exchange errors, abnormal slippage, rejected orders, reconciliation mismatch, or connectivity loss.
- Human approval should be required before live automation and before scaling capital.
- All timestamps should be consistent and timezone-aware, preferably UTC internally.
- Every signal, order intent, order response, fill, cancellation, error, override, and configuration change must be logged.

### Evaluation Standards for Profitability Claims

- The strategy must have a falsifiable hypothesis explaining why an edge should exist.
- Backtests must avoid look-ahead bias, data leakage, and excessive parameter fitting.
- Validation must include out-of-sample data or walk-forward testing.
- Evaluation must include multiple market regimes where possible.
- Results must be measured after fees, spread, slippage, latency, partial fills, failed orders, and funding or borrow costs where relevant.
- Metrics should include total return, profit factor, Sharpe or Sortino, max drawdown, drawdown duration, win/loss distribution, tail losses, turnover, exposure, and sensitivity to parameters.
- Paper trading must compare expected fills against simulated or actual paper fills.
- Live trading, if ever allowed, should start with minimal capital and require evidence that live behavior matches expected behavior.
- A strategy must have predefined retirement or pause criteria when live performance diverges from expectations.

### MVP Exclusions

- Leverage, margin, perpetuals, and futures unless explicitly chosen later with separate risk design.
- Multiple exchanges.
- Multiple unrelated strategies.
- Cross-exchange arbitrage.
- High-frequency trading.
- Complex machine learning or automatic strategy discovery.
- Auto-optimization against recent backtests.
- Social/news sentiment trading.
- Copy trading.
- Withdrawal automation.
- Fully autonomous capital scaling.
- Complex UI dashboards beyond minimal operational visibility.
- Any feature that makes trades harder to explain.

### Questions That Flow Into Round 0

- QUESTION: What specific bot type is milestone 1: alerting, research, backtesting, paper trading, live spot trading, market making, arbitrage, portfolio tracking, or something else?
- QUESTION: What falsifiable market hypothesis do we want to test first?
- QUESTION: What market regime is the first strategy intended for?
- QUESTION: What trading horizon is targeted: seconds, minutes, hours, days, or longer?
- QUESTION: Which asset universe is allowed for milestone 1?
- QUESTION: Which exchange or data source is targeted first?
- QUESTION: Will milestone 1 involve real funds, or only read-only/paper mode?
- QUESTION: What maximum loss or drawdown is acceptable before the bot must halt?
- QUESTION: What evidence is required before moving from backtest to paper, and from paper to live?
- QUESTION: Who can trigger the kill switch, and what should the recovery protocol be?
- QUESTION: What interface should the operator use first: CLI, logs, simple dashboard, API, or chat?
- QUESTION: What monitoring is mandatory from day one?
- QUESTION: What is the minimum acceptable audit trail for every decision?

## Decision

Round -1 establishes the baseline: this project should not frame the first milestone as "build a profitable bot." It should frame the first milestone as "build a narrow, safe, auditable system for testing one falsifiable trading hypothesis under realistic costs and failure conditions."

Proceed to Round 0 only after the user chooses the first milestone and answers the blocking questions about bot type, automation level, target market, target data source/exchange, allowed risk, and operator controls.

## Next Actions

1. Use this synthesis as input to Round 0 problem framing.
2. User answers the Round 0 blocking questions, especially bot type and whether real funds are in scope.
3. Codex-Arbiter updates `round-0-problem-framing.md` with the chosen first milestone.
4. Round 1 begins only after the problem brief is narrow enough for candidate architectures.

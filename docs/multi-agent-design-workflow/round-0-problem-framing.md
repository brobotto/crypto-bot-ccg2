# Round 0 - Problem Framing

Status: `draft`
Date: `2026-05-02`
Repo: `C:\Users\User\Documents\crypto-bot-ccg2`

## Goal of This Round

Frame the problem before selecting a solution. Round 0 should end with a shared understanding of what the crypto bot is supposed to do, who it serves, what constraints matter, and which unknowns must be resolved before architecture begins.

Round 0 does not choose libraries, exchanges, strategies, infrastructure, or implementation details unless they are already fixed constraints.

## Known Facts

- The repository is newly initialized and currently has no committed project files.
- The requested workflow uses four roles:
  - `Codex-Architect`
  - `Claude`
  - `Gemini`
  - `Codex-Arbiter`
- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
- The first market scope is Binance spot.
- The first assets are `BTC/USDT` and `ETH/USDT`.
- There is no confirmed strategy hypothesis yet.
- The first operator interface should be log files, not a web dashboard.
- The initial risk tolerance is maximum drawdown of `10-20%`.
- The initial backtest timeframe should be `1h`.
- The user is interested in both historical backtesting and live market dry-run, but is open to sequencing historical data first and live dry-run later.
- If live market dry-run is included, Binance read-only account support may be useful, but this is not confirmed.
- The user is interested in both a strategy plugin interface and a strategy research workflow.

## Working Problem Statement

This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.

Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.

## Round 0 Prompts

### Codex-Architect

Answer:

1. What system boundaries are implied by a crypto bot?
2. What architectural decisions are blocked until requirements are clearer?
3. What repo structure would remain flexible while the product scope is still unknown?
4. What facts must be gathered before Round 1 candidate designs?

### Claude

Answer:

1. Who is the likely user or operator of this bot?
2. What could go wrong if the bot is underspecified?
3. Which human decisions should not be automated yet?
4. What language in the goal is ambiguous and needs clarification?

### Gemini

Answer:

1. What are the plausible interpretations of "crypto bot"?
2. Which alternative framings should be considered before architecture?
3. What external constraints could dominate the design?
4. What is the fastest way to reduce uncertainty?

### Codex-Arbiter

After the three design agents answer, produce:

1. Canonical problem statement.
2. In-scope and out-of-scope boundaries.
3. Blocking questions.
4. Non-blocking assumptions.
5. Decision on whether to proceed to Round 1.

## Initial Agent Notes

### Codex-Architect

Read of the problem:

The repo needs a design workflow before implementation. Because the repo is empty, the first architecture decision is process-level: create a repeatable decision protocol that prevents premature framework or exchange choices.

Key observations:

- There are no existing app, config, tests, or deployment conventions to preserve.
- Crypto bots often need boundaries around market data ingestion, strategy evaluation, execution, risk controls, state, logging, and observability.
- Trading execution, if in scope, raises reliability, security, and financial-risk requirements immediately.

Assumptions:

- ASSUMPTION: The user wants this workflow to guide future implementation, not just produce a one-time discussion.
- ASSUMPTION: The project may evolve from design docs into code after the problem is framed.

Questions:

- QUESTION: Should milestone 1 include both historical backtesting and live market dry-run, or should live dry-run wait until historical simulation is trustworthy?
- QUESTION: Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state only?
- QUESTION: Should the first architecture prioritize a strategy plugin interface, a strategy research workflow, or a parallel strategy-monitoring system?
- QUESTION: How should the system help discover or compare strategies when no hypothesis is confirmed yet?
- QUESTION: What first class of strategy should be used only as a baseline to test the framework, without implying it is profitable?

Recommendation:

Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.

Risks:

- A generic "crypto bot" architecture could accidentally optimize for live execution when the real need is research, alerts, or backtesting.
- Security design changes dramatically if private keys or exchange API keys are stored in this repo or runtime environment.

### Claude

Read of the problem:

The most important ambiguity is human intent. A crypto bot can be a helper, a signal generator, a trading system, or a fully autonomous financial actor. Those are different products with different safety expectations.

Key observations:

- The user has requested a multi-agent design process, which suggests they want stronger deliberation before coding.
- The repo name alone does not define the operator, risk tolerance, capital exposure, or legal environment.

Assumptions:

- ASSUMPTION: The operator is likely the repo owner or a small private team.
- ASSUMPTION: The first useful output is a disciplined set of questions, not a complete design.

Questions:

- QUESTION: What decisions should remain human-approved?
- QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
- QUESTION: How should the operator review, override, pause, or audit bot behavior?
- QUESTION: What is the acceptable balance between speed, safety, and explainability?
- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, a plugin interface for manually supplied strategies, or both?
- QUESTION: If multiple strategies are evaluated in parallel, how should the operator avoid overfitting and false confidence?

Recommendation:

Define the operator journey first: configure, observe, approve or reject actions, pause, recover, and audit. That journey should shape the architecture.

Risks:

- Underdefining human controls can turn a useful assistant into an unsafe automation system.
- A technically correct bot can still fail the project if its behavior is not explainable to the operator.

### Gemini

Read of the problem:

"Crypto bot" has several plausible meanings. The design should not collapse into a single interpretation until the project chooses one.

Possible framings:

- Trading executor: consumes strategy signals and places orders.
- Alerting bot: monitors markets and notifies the user.
- Research bot: gathers data and performs analysis.
- Backtesting engine: tests strategies over historical data.
- Portfolio assistant: tracks balances, PnL, and exposure.
- On-chain automation bot: watches contracts or wallets and submits transactions.

External constraints:

- Exchange API limitations, rate limits, and regional access.
- Custody model and secret management.
- Market data quality and latency requirements.
- Tax, audit, and record retention needs.
- Hosting environment and uptime expectations.

Questions:

- QUESTION: Which framing best matches the first milestone?
- QUESTION: Is real money involved in milestone 1?
- QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
- QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
- QUESTION: Should the first design sequence be historical candles first, then live WebSocket dry-run, then read-only portfolio monitoring?
- QUESTION: Does Binance read-only monitoring materially improve milestone 1, or does it add unnecessary security and setup complexity?

Recommendation:

Pick a narrow first milestone and design around that. The fastest uncertainty reducer is a one-page product brief answering: mode, user, assets, exchange/data source, automation level, and success metric.

Risks:

- Trying to support all crypto-bot framings at once will produce a large but weak architecture.
- On-chain bots and exchange-trading bots have different failure modes and should not be casually merged.

## Codex-Arbiter Synthesis

### Round 0 Agent Answer Summary

Codex-Architect framed the project as a non-live research and simulation system. The strongest point was sequencing: milestone 1 should prove trustworthy evaluation, reproducible results, structured audit logs, and rejection criteria before live market dry-run or read-only Binance account integration are assumed.

Claude challenged the scope and argued that the project contains two different goals: research tooling and runtime infrastructure. The strongest point was that milestone 1 needs explicit exit criteria, a defined structured log schema, and a decision about whether the strategy interface is a real plugin contract or a provisional internal abstraction.

Gemini framed the project as a hypothesis-first research platform. The strongest point was that high-fidelity backtesting and strategy comparison are more valuable in milestone 1 than live dry-run, because live dry-run on a `1h` timeframe takes weeks to produce meaningful evidence. Gemini also recommended sensitivity analysis over automated optimization to reduce curve fitting.

Canonical problem statement:

This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`. The first milestone should support historical backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Live market dry-run and Binance read-only account monitoring are desirable but should be debated for sequencing and complexity. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, monitor, and reject rather than assuming a profitable strategy already exists.

In scope for Round 0:

- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
- Identifying risk, safety, and human-control requirements for non-live operation.
- Clarifying data source and simulation fidelity requirements for Binance spot.
- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
- Recording blocking questions and assumptions.
- Preparing for candidate architecture designs in Round 1.

Out of scope for Round 0:

- Selecting a final tech stack.
- Choosing exchange SDKs or trading libraries.
- Writing trading strategy code.
- Designing live order execution flows.
- Enabling real-money trading.
- Supporting leverage, futures, margin, or withdrawals.

Blocking questions:

- What is the formal milestone 1 exit condition?
- What exact structured log format and event schema should be treated as the first operator interface?
- Should the strategy interface in milestone 1 be a real plugin contract or a provisional internal abstraction?
- What minimum simulation realism is required for milestone 1: fees only, fees plus spread/slippage, or partial fill/latency assumptions?
- What benchmark should strategy candidates be compared against, such as buy-and-hold, cash, or simple baseline strategies?

Non-blocking assumptions:

- The repo is early enough that workflow docs can define the decision process.
- The first implementation should be narrow and reversible.
- Safety and auditability should be treated as first-class design concerns.
- Binance is the initial exchange/data source.
- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
- Spot-only scope excludes leverage, margin, futures, and perpetuals.
- Log files are sufficient for the first operator interface if they are structured and easy to audit.
- Maximum drawdown of `10-20%` is a project-level risk boundary for evaluation and future paper/live controls.
- The first timeframe is `1h`.
- Live market dry-run should be sequenced after historical backtesting is reliable.
- Binance read-only account monitoring should be deferred unless Round 1 identifies a strong reason to include it.
- Milestone 1 portfolio monitoring can start with simulated portfolio state.
- The research workflow should prioritize comparison and sensitivity analysis over automated parameter optimization.

Decision:

Proceed to Round 1 candidate designs with a narrower milestone: historical backtesting, simulated portfolio monitoring, structured logs, strategy comparison/research workflow, and a carefully scoped strategy extension boundary. Live market dry-run and Binance read-only account monitoring are deferred to milestone 2 unless an architect can justify a minimal interface stub that does not add credential or runtime complexity.

Next actions:

1. Codex-Arbiter updates the neutral problem brief with this narrower milestone.
2. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
3. Round 1 proposals must explicitly answer the remaining architecture questions: log schema, strategy boundary, data persistence, backtest realism, metrics, and anti-overfitting workflow.

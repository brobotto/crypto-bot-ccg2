# Context Pack

Generated: 2026-05-02T18:16:38
Repo: `C:\Users\User\Documents\crypto-bot-ccg2`

## Current Task

Slice 1 complete: project skeleton verified

## Git Status

```text
M docs/multi-agent-design-workflow/README.md
 M reviews/latest/context-pack.md
?? .gitignore
?? config/
?? data/
?? docs/multi-agent-design-workflow/round-4-implementation-plan.md
?? logs/
?? pyproject.toml
?? src/
?? tests/
```

## Git Diff

```diff
diff --git a/docs/multi-agent-design-workflow/README.md b/docs/multi-agent-design-workflow/README.md
index b1a8497..c31a6e4 100644
--- a/docs/multi-agent-design-workflow/README.md
+++ b/docs/multi-agent-design-workflow/README.md
@@ -30,6 +30,7 @@ The workflow is round-based. Each round produces a short decision record that ca
    - Final decision: [Round 3 Final Architecture](./round-3-final-architecture.md).
 7. `Round 4 - Implementation Plan`
    - Convert the selected design into files, tasks, tests, and rollout steps.
+   - Start from [Round 4 Implementation Plan](./round-4-implementation-plan.md).
 
 ## Operating Rules
 
diff --git a/reviews/latest/context-pack.md b/reviews/latest/context-pack.md
index ab8c2ab..57561cc 100644
--- a/reviews/latest/context-pack.md
+++ b/reviews/latest/context-pack.md
@@ -1,5626 +1,33 @@
 # Context Pack
 
-Generated: 2026-05-02T18:11:13
+Generated: 2026-05-02T18:13:41
 Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
 
 ## Current Task
 
-Round 4: implementation plan from final architecture
+Implementation: start Slice 1 project skeleton
 
 ## Git Status
 
 ```text
 M docs/multi-agent-design-workflow/README.md
- M reviews/latest/context-pack.md
-?? docs/multi-agent-design-workflow/round-2-cross-review.md
-?? docs/multi-agent-design-workflow/round-3-arbiter-brief.md
-?? docs/multi-agent-design-workflow/round-3-final-architecture.md
+?? docs/multi-agent-design-workflow/round-4-implementation-plan.md
 ```
 
 ## Git Diff
 
 ```diff
 diff --git a/docs/multi-agent-design-workflow/README.md b/docs/multi-agent-design-workflow/README.md
-index f3a9be4..b1a8497 100644
+index b1a8497..c31a6e4 100644
 --- a/docs/multi-agent-design-workflow/README.md
 +++ b/docs/multi-agent-design-workflow/README.md
-@@ -26,6 +26,8 @@ The workflow is round-based. Each round produces a short decision record that ca
-    - Start from [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).
- 6. `Round 3 - Synthesis`
-    - Codex-Arbiter selects or combines a direction and records tradeoffs.
-+   - Start from [Round 3 Arbiter Brief](./round-3-arbiter-brief.md).
-+   - Final decision: [Round 3 Final Architecture](./round-3-final-architecture.md).
+@@ -30,6 +30,7 @@ The workflow is round-based. Each round produces a short decision record that ca
+    - Final decision: [Round 3 Final Architecture](./round-3-final-architecture.md).
  7. `Round 4 - Implementation Plan`
     - Convert the selected design into files, tasks, tests, and rollout steps.
++   - Start from [Round 4 Implementation Plan](./round-4-implementation-plan.md).
  
-@@ -44,4 +46,4 @@ The workflow is round-based. Each round produces a short decision record that ca
- 
- ## Current Starting Point
- 
--Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), the canonical [Problem Brief](./00-problem-brief.md), [Round 1 Candidate Designs](./round-1-candidate-designs.md), and [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).
-+Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), the canonical [Problem Brief](./00-problem-brief.md), [Round 1 Candidate Designs](./round-1-candidate-designs.md), [Round 2 Cross Review](./round-2-cross-review.md), and [Round 3 Arbiter Brief](./round-3-arbiter-brief.md).
-diff --git a/reviews/latest/context-pack.md b/reviews/latest/context-pack.md
-index f6db9f7..25cc1d9 100644
---- a/reviews/latest/context-pack.md
-+++ b/reviews/latest/context-pack.md
-@@ -1,5230 +1,44 @@
- # Context Pack
- 
--Generated: 2026-05-02T18:00:53
-+Generated: 2026-05-02T18:08:51
- Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
- 
- ## Current Task
- 
--Round 2: cross-review candidate architectures
-+Round 3: arbitrate final architecture after cross-review
- 
- ## Git Status
- 
- ```text
--M README.md
-- M docs/multi-agent-design-workflow/README.md
-- M docs/multi-agent-design-workflow/round-0-problem-framing.md
-- M prompts/README.md
-- M reviews/latest/context-pack.md
--?? docs/multi-agent-design-workflow/00-problem-brief.md
--?? docs/multi-agent-design-workflow/round-0-brief-synthesis.md
--?? docs/multi-agent-design-workflow/round-1-candidate-designs.md
--?? docs/multi-agent-design-workflow/round-2-cross-review-brief.md
--?? docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md
--?? prompts/round-minus-1-trading-bot-principles.md
-+M docs/multi-agent-design-workflow/README.md
-+?? docs/multi-agent-design-workflow/round-2-cross-review.md
-+?? docs/multi-agent-design-workflow/round-3-arbiter-brief.md
- ```
- 
- ## Git Diff
- 
- ```diff
--diff --git a/README.md b/README.md
--index a2ea905..8236365 100644
----- a/README.md
--+++ b/README.md
--@@ -4,16 +4,18 @@ This repo starts with a multi-agent design workflow before implementation.
-- 
-- The intended loop is:
-- 
---1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
---2. Codex-Arbiter turns the answers into a neutral problem brief.
---3. Round 1: each architect proposes a design from the same brief.
---4. Round 2: agents critique the candidate designs.
---5. Round 3: Codex-Arbiter records the final architecture.
---6. Round 4: Codex implements the accepted plan and runs verification.
--+1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--+2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--+3. Codex-Arbiter turns the answers into a neutral problem brief.
--+4. Round 1: each architect proposes a design from the same brief.
--+5. Round 2: agents critique the candidate designs.
--+6. Round 3: Codex-Arbiter records the final architecture.
--+7. Round 4: Codex implements the accepted plan and runs verification.
-- 
-- Start here:
-- 
-- - [Workflow README](docs/multi-agent-design-workflow/README.md)
--+- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
-- - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
-- - [Prompt Library](prompts/README.md)
-- 
- diff --git a/docs/multi-agent-design-workflow/README.md b/docs/multi-agent-design-workflow/README.md
--index a532bf4..f3a9be4 100644
-+index f3a9be4..adc13e0 100644
- --- a/docs/multi-agent-design-workflow/README.md
- +++ b/docs/multi-agent-design-workflow/README.md
--@@ -11,16 +11,22 @@ The workflow is round-based. Each round produces a short decision record that ca
-- 
-- ## Round Sequence
-- 
---1. `Round 0 - Problem Framing`
--+1. `Round -1 - Trading Bot Principles`
--+   - Define what a good and potentially profitable crypto trading bot requires.
--+   - Establish safety, validation, and profitability standards before project-specific design.
--+2. `Round 0 - Problem Framing`
--    - Define the actual problem, users, success criteria, constraints, and unknowns.
--    - No solution is selected in this round.
---2. `Round 1 - Candidate Designs`
--+3. `Round 0B - Brief Synthesis`
--+   - Codex-Arbiter turns Round 0 agent answers into the canonical problem brief.
--+4. `Round 1 - Candidate Designs`
--    - Each design agent proposes one or more viable approaches.
---3. `Round 2 - Critique and Risk`
--+5. `Round 2 - Critique and Risk`
--    - Agents critique designs from their role perspective.
---4. `Round 3 - Synthesis`
--+   - Start from [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).
--+6. `Round 3 - Synthesis`
-+@@ -26,6 +26,7 @@ The workflow is round-based. Each round produces a short decision record that ca
-+    - Start from [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).
-+ 6. `Round 3 - Synthesis`
-     - Codex-Arbiter selects or combines a direction and records tradeoffs.
---5. `Round 4 - Implementation Plan`
--+7. `Round 4 - Implementation Plan`
-++   - Start from [Round 3 Arbiter Brief](./round-3-arbiter-brief.md).
-+ 7. `Round 4 - Implementation Plan`
-     - Convert the selected design into files, tasks, tests, and rollout steps.
-  
-- ## Operating Rules
--@@ -38,4 +44,4 @@ The workflow is round-based. Each round produces a short decision record that ca
-+@@ -44,4 +45,4 @@ The workflow is round-based. Each round produces a short decision record that ca
-  
-  ## Current Starting Point
-  
---Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--+Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), the canonical [Problem Brief](./00-problem-brief.md), [Round 1 Candidate Designs](./round-1-candidate-designs.md), and [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).
--diff --git a/docs/multi-agent-design-workflow/round-0-problem-framing.md b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--index e5c5a3d..cef3ead 100644
----- a/docs/multi-agent-design-workflow/round-0-problem-framing.md
--+++ b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--@@ -18,13 +18,23 @@ Round 0 does not choose libraries, exchanges, strategies, infrastructure, or imp
--   - `Claude`
--   - `Gemini`
--   - `Codex-Arbiter`
---- The project name suggests a crypto bot, but the exact product scope is not yet defined.
--+- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
--+- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
--+- The first market scope is Binance spot.
--+- The first assets are `BTC/USDT` and `ETH/USDT`.
--+- There is no confirmed strategy hypothesis yet.
--+- The first operator interface should be log files, not a web dashboard.
--+- The initial risk tolerance is maximum drawdown of `10-20%`.
--+- The initial backtest timeframe should be `1h`.
--+- The user is interested in both historical backtesting and live market dry-run, but is open to sequencing historical data first and live dry-run later.
--+- If live market dry-run is included, Binance read-only account support may be useful, but this is not confirmed.
--+- The user is interested in both a strategy plugin interface and a strategy research workflow.
-- 
-- ## Working Problem Statement
-- 
---ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.
--+This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.
-- 
---The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.
--+Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.
-- 
-- ## Round 0 Prompts
-- 
--@@ -86,15 +96,15 @@ Assumptions:
-- 
-- Questions:
-- 
---- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
---- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
---- QUESTION: Is the bot allowed to place orders automatically?
---- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
---- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?
--+- QUESTION: Should milestone 1 include both historical backtesting and live market dry-run, or should live dry-run wait until historical simulation is trustworthy?
--+- QUESTION: Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state only?
--+- QUESTION: Should the first architecture prioritize a strategy plugin interface, a strategy research workflow, or a parallel strategy-monitoring system?
--+- QUESTION: How should the system help discover or compare strategies when no hypothesis is confirmed yet?
--+- QUESTION: What first class of strategy should be used only as a baseline to test the framework, without implying it is profitable?
-- 
-- Recommendation:
-- 
---Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.
--+Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.
-- 
-- Risks:
-- 
--@@ -123,6 +133,8 @@ Questions:
-- - QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
-- - QUESTION: How should the operator review, override, pause, or audit bot behavior?
-- - QUESTION: What is the acceptable balance between speed, safety, and explainability?
--+- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, a plugin interface for manually supplied strategies, or both?
--+- QUESTION: If multiple strategies are evaluated in parallel, how should the operator avoid overfitting and false confidence?
-- 
-- Recommendation:
-- 
--@@ -162,6 +174,8 @@ Questions:
-- - QUESTION: Is real money involved in milestone 1?
-- - QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
-- - QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
--+- QUESTION: Should the first design sequence be historical candles first, then live WebSocket dry-run, then read-only portfolio monitoring?
--+- QUESTION: Does Binance read-only monitoring materially improve milestone 1, or does it add unnecessary security and setup complexity?
-- 
-- Recommendation:
-- 
--@@ -174,14 +188,24 @@ Risks:
-- 
-- ## Codex-Arbiter Synthesis
-- 
--+### Round 0 Agent Answer Summary
--+
--+Codex-Architect framed the project as a non-live research and simulation system. The strongest point was sequencing: milestone 1 should prove trustworthy evaluation, reproducible results, structured audit logs, and rejection criteria before live market dry-run or read-only Binance account integration are assumed.
--+
--+Claude challenged the scope and argued that the project contains two different goals: research tooling and runtime infrastructure. The strongest point was that milestone 1 needs explicit exit criteria, a defined structured log schema, and a decision about whether the strategy interface is a real plugin contract or a provisional internal abstraction.
--+
--+Gemini framed the project as a hypothesis-first research platform. The strongest point was that high-fidelity backtesting and strategy comparison are more valuable in milestone 1 than live dry-run, because live dry-run on a `1h` timeframe takes weeks to produce meaningful evidence. Gemini also recommended sensitivity analysis over automated optimization to reduce curve fitting.
--+
-- Canonical problem statement:
-- 
---This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.
--+This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`. The first milestone should support historical backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Live market dry-run and Binance read-only account monitoring are desirable but should be debated for sequencing and complexity. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, monitor, and reject rather than assuming a profitable strategy already exists.
-- 
-- In scope for Round 0:
-- 
---- Clarifying bot type and first milestone.
---- Identifying risk, safety, and human-control requirements.
--+- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
--+- Identifying risk, safety, and human-control requirements for non-live operation.
--+- Clarifying data source and simulation fidelity requirements for Binance spot.
--+- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
-- - Recording blocking questions and assumptions.
-- - Preparing for candidate architecture designs in Round 1.
-- 
--@@ -191,27 +215,39 @@ Out of scope for Round 0:
-- - Choosing exchange SDKs or trading libraries.
-- - Writing trading strategy code.
-- - Designing live order execution flows.
--+- Enabling real-money trading.
--+- Supporting leverage, futures, margin, or withdrawals.
-- 
-- Blocking questions:
-- 
---- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
---- Will the bot handle real funds or private keys in milestone 1?
---- What user approval or kill-switch controls are required?
---- What exchange, chain, wallet, or market-data source is targeted first?
---- What interface should the operator use first: CLI, web UI, chat, API, or background service only?
--+- What is the formal milestone 1 exit condition?
--+- What exact structured log format and event schema should be treated as the first operator interface?
--+- Should the strategy interface in milestone 1 be a real plugin contract or a provisional internal abstraction?
--+- What minimum simulation realism is required for milestone 1: fees only, fees plus spread/slippage, or partial fill/latency assumptions?
--+- What benchmark should strategy candidates be compared against, such as buy-and-hold, cash, or simple baseline strategies?
-- 
-- Non-blocking assumptions:
-- 
-- - The repo is early enough that workflow docs can define the decision process.
-- - The first implementation should be narrow and reversible.
-- - Safety and auditability should be treated as first-class design concerns.
--+- Binance is the initial exchange/data source.
--+- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
--+- Spot-only scope excludes leverage, margin, futures, and perpetuals.
--+- Log files are sufficient for the first operator interface if they are structured and easy to audit.
--+- Maximum drawdown of `10-20%` is a project-level risk boundary for evaluation and future paper/live controls.
--+- The first timeframe is `1h`.
--+- Live market dry-run should be sequenced after historical backtesting is reliable.
--+- Binance read-only account monitoring should be deferred unless Round 1 identifies a strong reason to include it.
--+- Milestone 1 portfolio monitoring can start with simulated portfolio state.
--+- The research workflow should prioritize comparison and sensitivity analysis over automated parameter optimization.
-- 
-- Decision:
-- 
---Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.
--+Proceed to Round 1 candidate designs with a narrower milestone: historical backtesting, simulated portfolio monitoring, structured logs, strategy comparison/research workflow, and a carefully scoped strategy extension boundary. Live market dry-run and Binance read-only account monitoring are deferred to milestone 2 unless an architect can justify a minimal interface stub that does not add credential or runtime complexity.
-- 
-- Next actions:
-- 
---1. User answers the blocking questions.
---2. Codex-Arbiter updates this document with the chosen first milestone.
---3. Round 1 begins with candidate designs constrained to that milestone.
--+1. Codex-Arbiter updates the neutral problem brief with this narrower milestone.
--+2. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
--+3. Round 1 proposals must explicitly answer the remaining architecture questions: log schema, strategy boundary, data persistence, backtest realism, metrics, and anti-overfitting workflow.
--diff --git a/prompts/README.md b/prompts/README.md
--index d8a2217..ef2814f 100644
----- a/prompts/README.md
--+++ b/prompts/README.md
--@@ -4,12 +4,12 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
-- 
-- Recommended order:
-- 
---1. `round0-problem-framing.md`
---2. `round0-brief-synthesis.md`
---3. `round1-codex-architect.md`
---4. `round1-external-architect.md`
---5. `round2-cross-review.md`
---6. `round3-arbiter.md`
---
---Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
---
--+1. `round-minus-1-trading-bot-principles.md`
--+2. `round0-problem-framing.md`
--+3. `round0-brief-synthesis.md`
--+4. `round1-codex-architect.md`
--+5. `round1-external-architect.md`
--+6. `round2-cross-review.md`
--+7. `round3-arbiter.md`
--+
--+Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--diff --git a/reviews/latest/context-pack.md b/reviews/latest/context-pack.md
--index 3caebdb..14c080e 100644
----- a/reviews/latest/context-pack.md
--+++ b/reviews/latest/context-pack.md
--@@ -1,37 +1,4125 @@
-- # Context Pack
-- 
---Generated: 2026-05-02T16:04:56
--+Generated: 2026-05-02T17:52:33
-- Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
-- 
-- ## Current Task
-- 
---Verify multi-agent design workflow setup
--+Round 1 preparation after adding Round 0 brief synthesis artifact
-- 
-- ## Git Status
-- 
-- ```text
---?? .env.example
---?? README.md
---?? docs/
---?? prompts/
---?? reviews/
---?? tools/
--+M README.md
--+ M docs/multi-agent-design-workflow/README.md
--+ M docs/multi-agent-design-workflow/round-0-problem-framing.md
--+ M prompts/README.md
--+ M reviews/latest/context-pack.md
--+?? docs/multi-agent-design-workflow/00-problem-brief.md
--+?? docs/multi-agent-design-workflow/round-0-brief-synthesis.md
--+?? docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md
--+?? prompts/round-minus-1-trading-bot-principles.md
-- ```
-- 
-- ## Git Diff
-- 
-- ```diff
---[no diff]
--+diff --git a/README.md b/README.md
--+index a2ea905..8236365 100644
--+--- a/README.md
--++++ b/README.md
--+@@ -4,16 +4,18 @@ This repo starts with a multi-agent design workflow before implementation.
--+ 
--+ The intended loop is:
--+ 
--+-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--+-2. Codex-Arbiter turns the answers into a neutral problem brief.
--+-3. Round 1: each architect proposes a design from the same brief.
--+-4. Round 2: agents critique the candidate designs.
--+-5. Round 3: Codex-Arbiter records the final architecture.
--+-6. Round 4: Codex implements the accepted plan and runs verification.
--++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--++3. Codex-Arbiter turns the answers into a neutral problem brief.
--++4. Round 1: each architect proposes a design from the same brief.
--++5. Round 2: agents critique the candidate designs.
--++6. Round 3: Codex-Arbiter records the final architecture.
--++7. Round 4: Codex implements the accepted plan and runs verification.
--+ 
--+ Start here:
--+ 
--+ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--+ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--+ - [Prompt Library](prompts/README.md)
--+ 
--+diff --git a/docs/multi-agent-design-workflow/README.md b/docs/multi-agent-design-workflow/README.md
--+index a532bf4..1c1c7ce 100644
--+--- a/docs/multi-agent-design-workflow/README.md
--++++ b/docs/multi-agent-design-workflow/README.md
--+@@ -11,16 +11,21 @@ The workflow is round-based. Each round produces a short decision record that ca
--+ 
--+ ## Round Sequence
--+ 
--+-1. `Round 0 - Problem Framing`
--++1. `Round -1 - Trading Bot Principles`
--++   - Define what a good and potentially profitable crypto trading bot requires.
--++   - Establish safety, validation, and profitability standards before project-specific design.
--++2. `Round 0 - Problem Framing`
--+    - Define the actual problem, users, success criteria, constraints, and unknowns.
--+    - No solution is selected in this round.
--+-2. `Round 1 - Candidate Designs`
--++3. `Round 0B - Brief Synthesis`
--++   - Codex-Arbiter turns Round 0 agent answers into the canonical problem brief.
--++4. `Round 1 - Candidate Designs`
--+    - Each design agent proposes one or more viable approaches.
--+-3. `Round 2 - Critique and Risk`
--++5. `Round 2 - Critique and Risk`
--+    - Agents critique designs from their role perspective.
--+-4. `Round 3 - Synthesis`
--++6. `Round 3 - Synthesis`
--+    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--+-5. `Round 4 - Implementation Plan`
--++7. `Round 4 - Implementation Plan`
--+    - Convert the selected design into files, tasks, tests, and rollout steps.
--+ 
--+ ## Operating Rules
--+@@ -38,4 +43,4 @@ The workflow is round-based. Each round produces a short decision record that ca
--+ 
--+ ## Current Starting Point
--+ 
--+-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), and the canonical [Problem Brief](./00-problem-brief.md).
--+diff --git a/docs/multi-agent-design-workflow/round-0-problem-framing.md b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--+index e5c5a3d..cef3ead 100644
--+--- a/docs/multi-agent-design-workflow/round-0-problem-framing.md
--++++ b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--+@@ -18,13 +18,23 @@ Round 0 does not choose libraries, exchanges, strategies, infrastructure, or imp
--+   - `Claude`
--+   - `Gemini`
--+   - `Codex-Arbiter`
--+-- The project name suggests a crypto bot, but the exact product scope is not yet defined.
--++- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
--++- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
--++- The first market scope is Binance spot.
--++- The first assets are `BTC/USDT` and `ETH/USDT`.
--++- There is no confirmed strategy hypothesis yet.
--++- The first operator interface should be log files, not a web dashboard.
--++- The initial risk tolerance is maximum drawdown of `10-20%`.
--++- The initial backtest timeframe should be `1h`.
--++- The user is interested in both historical backtesting and live market dry-run, but is open to sequencing historical data first and live dry-run later.
--++- If live market dry-run is included, Binance read-only account support may be useful, but this is not confirmed.
--++- The user is interested in both a strategy plugin interface and a strategy research workflow.
--+ 
--+ ## Working Problem Statement
--+ 
--+-ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.
--++This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.
--+ 
--+-The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.
--++Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.
--+ 
--+ ## Round 0 Prompts
--+ 
--+@@ -86,15 +96,15 @@ Assumptions:
--+ 
--+ Questions:
--+ 
--+-- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
--+-- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
--+-- QUESTION: Is the bot allowed to place orders automatically?
--+-- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
--+-- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?
--++- QUESTION: Should milestone 1 include both historical backtesting and live market dry-run, or should live dry-run wait until historical simulation is trustworthy?
--++- QUESTION: Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state only?
--++- QUESTION: Should the first architecture prioritize a strategy plugin interface, a strategy research workflow, or a parallel strategy-monitoring system?
--++- QUESTION: How should the system help discover or compare strategies when no hypothesis is confirmed yet?
--++- QUESTION: What first class of strategy should be used only as a baseline to test the framework, without implying it is profitable?
--+ 
--+ Recommendation:
--+ 
--+-Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.
--++Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.
--+ 
--+ Risks:
--+ 
--+@@ -123,6 +133,8 @@ Questions:
--+ - QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
--+ - QUESTION: How should the operator review, override, pause, or audit bot behavior?
--+ - QUESTION: What is the acceptable balance between speed, safety, and explainability?
--++- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, a plugin interface for manually supplied strategies, or both?
--++- QUESTION: If multiple strategies are evaluated in parallel, how should the operator avoid overfitting and false confidence?
--+ 
--+ Recommendation:
--+ 
--+@@ -162,6 +174,8 @@ Questions:
--+ - QUESTION: Is real money involved in milestone 1?
--+ - QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
--+ - QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
--++- QUESTION: Should the first design sequence be historical candles first, then live WebSocket dry-run, then read-only portfolio monitoring?
--++- QUESTION: Does Binance read-only monitoring materially improve milestone 1, or does it add unnecessary security and setup complexity?
--+ 
--+ Recommendation:
--+ 
--+@@ -174,14 +188,24 @@ Risks:
--+ 
--+ ## Codex-Arbiter Synthesis
--+ 
--++### Round 0 Agent Answer Summary
--++
--++Codex-Architect framed the project as a non-live research and simulation system. The strongest point was sequencing: milestone 1 should prove trustworthy evaluation, reproducible results, structured audit logs, and rejection criteria before live market dry-run or read-only Binance account integration are assumed.
--++
--++Claude challenged the scope and argued that the project contains two different goals: research tooling and runtime infrastructure. The strongest point was that milestone 1 needs explicit exit criteria, a defined structured log schema, and a decision about whether the strategy interface is a real plugin contract or a provisional internal abstraction.
--++
--++Gemini framed the project as a hypothesis-first research platform. The strongest point was that high-fidelity backtesting and strategy comparison are more valuable in milestone 1 than live dry-run, because live dry-run on a `1h` timeframe takes weeks to produce meaningful evidence. Gemini also recommended sensitivity analysis over automated optimization to reduce curve fitting.
--++
--+ Canonical problem statement:
--+ 
--+-This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.
--++This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`. The first milestone should support historical backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Live market dry-run and Binance read-only account monitoring are desirable but should be debated for sequencing and complexity. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, monitor, and reject rather than assuming a profitable strategy already exists.
--+ 
--+ In scope for Round 0:
--+ 
--+-- Clarifying bot type and first milestone.
--+-- Identifying risk, safety, and human-control requirements.
--++- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
--++- Identifying risk, safety, and human-control requirements for non-live operation.
--++- Clarifying data source and simulation fidelity requirements for Binance spot.
--++- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
--+ - Recording blocking questions and assumptions.
--+ - Preparing for candidate architecture designs in Round 1.
--+ 
--+@@ -191,27 +215,39 @@ Out of scope for Round 0:
--+ - Choosing exchange SDKs or trading libraries.
--+ - Writing trading strategy code.
--+ - Designing live order execution flows.
--++- Enabling real-money trading.
--++- Supporting leverage, futures, margin, or withdrawals.
--+ 
--+ Blocking questions:
--+ 
--+-- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
--+-- Will the bot handle real funds or private keys in milestone 1?
--+-- What user approval or kill-switch controls are required?
--+-- What exchange, chain, wallet, or market-data source is targeted first?
--+-- What interface should the operator use first: CLI, web UI, chat, API, or background service only?
--++- What is the formal milestone 1 exit condition?
--++- What exact structured log format and event schema should be treated as the first operator interface?
--++- Should the strategy interface in milestone 1 be a real plugin contract or a provisional internal abstraction?
--++- What minimum simulation realism is required for milestone 1: fees only, fees plus spread/slippage, or partial fill/latency assumptions?
--++- What benchmark should strategy candidates be compared against, such as buy-and-hold, cash, or simple baseline strategies?
--+ 
--+ Non-blocking assumptions:
--+ 
--+ - The repo is early enough that workflow docs can define the decision process.
--+ - The first implementation should be narrow and reversible.
--+ - Safety and auditability should be treated as first-class design concerns.
--++- Binance is the initial exchange/data source.
--++- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
--++- Spot-only scope excludes leverage, margin, futures, and perpetuals.
--++- Log files are sufficient for the first operator interface if they are structured and easy to audit.
--++- Maximum drawdown of `10-20%` is a project-level risk boundary for evaluation and future paper/live controls.
--++- The first timeframe is `1h`.
--++- Live market dry-run should be sequenced after historical backtesting is reliable.
--++- Binance read-only account monitoring should be deferred unless Round 1 identifies a strong reason to include it.
--++- Milestone 1 portfolio monitoring can start with simulated portfolio state.
--++- The research workflow should prioritize comparison and sensitivity analysis over automated parameter optimization.
--+ 
--+ Decision:
--+ 
--+-Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.
--++Proceed to Round 1 candidate designs with a narrower milestone: historical backtesting, simulated portfolio monitoring, structured logs, strategy comparison/research workflow, and a carefully scoped strategy extension boundary. Live market dry-run and Binance read-only account monitoring are deferred to milestone 2 unless an architect can justify a minimal interface stub that does not add credential or runtime complexity.
--+ 
--+ Next actions:
--+ 
--+-1. User answers the blocking questions.
--+-2. Codex-Arbiter updates this document with the chosen first milestone.
--+-3. Round 1 begins with candidate designs constrained to that milestone.
--++1. Codex-Arbiter updates the neutral problem brief with this narrower milestone.
--++2. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
--++3. Round 1 proposals must explicitly answer the remaining architecture questions: log schema, strategy boundary, data persistence, backtest realism, metrics, and anti-overfitting workflow.
--+diff --git a/prompts/README.md b/prompts/README.md
--+index d8a2217..ef2814f 100644
--+--- a/prompts/README.md
--++++ b/prompts/README.md
--+@@ -4,12 +4,12 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--+ 
--+ Recommended order:
--+ 
--+-1. `round0-problem-framing.md`
--+-2. `round0-brief-synthesis.md`
--+-3. `round1-codex-architect.md`
--+-4. `round1-external-architect.md`
--+-5. `round2-cross-review.md`
--+-6. `round3-arbiter.md`
--+-
--+-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--+-
--++1. `round-minus-1-trading-bot-principles.md`
--++2. `round0-problem-framing.md`
--++3. `round0-brief-synthesis.md`
--++4. `round1-codex-architect.md`
--++5. `round1-external-architect.md`
--++6. `round2-cross-review.md`
--++7. `round3-arbiter.md`
--++
--++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--+diff --git a/reviews/latest/context-pack.md b/reviews/latest/context-pack.md
--+index 3caebdb..0643786 100644
--+--- a/reviews/latest/context-pack.md
--++++ b/reviews/latest/context-pack.md
--+@@ -1,37 +1,3129 @@
--+ # Context Pack
--+ 
--+-Generated: 2026-05-02T16:04:56
--++Generated: 2026-05-02T17:50:50
--+ Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--+ 
--+ ## Current Task
--+ 
--+-Verify multi-agent design workflow setup
--++Round 1: architecture proposals after Round 0 synthesis
--+ 
--+ ## Git Status
--+ 
--+ ```text
--+-?? .env.example
--+-?? README.md
--+-?? docs/
--+-?? prompts/
--+-?? reviews/
--+-?? tools/
--++M README.md
--++ M docs/multi-agent-design-workflow/README.md
--++ M docs/multi-agent-design-workflow/round-0-problem-framing.md
--++ M prompts/README.md
--++ M reviews/latest/context-pack.md
--++?? docs/multi-agent-design-workflow/00-problem-brief.md
--++?? docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md
--++?? prompts/round-minus-1-trading-bot-principles.md
--+ ```
--+ 
--+ ## Git Diff
--+ 
--+ ```diff
--+-[no diff]
--++diff --git a/README.md b/README.md
--++index a2ea905..8236365 100644
--++--- a/README.md
--+++++ b/README.md
--++@@ -4,16 +4,18 @@ This repo starts with a multi-agent design workflow before implementation.
--++ 
--++ The intended loop is:
--++ 
--++-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--++-2. Codex-Arbiter turns the answers into a neutral problem brief.
--++-3. Round 1: each architect proposes a design from the same brief.
--++-4. Round 2: agents critique the candidate designs.
--++-5. Round 3: Codex-Arbiter records the final architecture.
--++-6. Round 4: Codex implements the accepted plan and runs verification.
--+++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--+++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--+++3. Codex-Arbiter turns the answers into a neutral problem brief.
--+++4. Round 1: each architect proposes a design from the same brief.
--+++5. Round 2: agents critique the candidate designs.
--+++6. Round 3: Codex-Arbiter records the final architecture.
--+++7. Round 4: Codex implements the accepted plan and runs verification.
--++ 
--++ Start here:
--++ 
--++ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--+++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--++ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--++ - [Prompt Library](prompts/README.md)
--++ 
--++diff --git a/docs/multi-agent-design-workflow/README.md b/docs/multi-agent-design-workflow/README.md
--++index a532bf4..b701d3e 100644
--++--- a/docs/multi-agent-design-workflow/README.md
--+++++ b/docs/multi-agent-design-workflow/README.md
--++@@ -11,16 +11,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--++ 
--++ ## Round Sequence
--++ 
--++-1. `Round 0 - Problem Framing`
--+++1. `Round -1 - Trading Bot Principles`
--+++   - Define what a good and potentially profitable crypto trading bot requires.
--+++   - Establish safety, validation, and profitability standards before project-specific design.
--+++2. `Round 0 - Problem Framing`
--++    - Define the actual problem, users, success criteria, constraints, and unknowns.
--++    - No solution is selected in this round.
--++-2. `Round 1 - Candidate Designs`
--+++3. `Round 1 - Candidate Designs`
--++    - Each design agent proposes one or more viable approaches.
--++-3. `Round 2 - Critique and Risk`
--+++4. `Round 2 - Critique and Risk`
--++    - Agents critique designs from their role perspective.
--++-4. `Round 3 - Synthesis`
--+++5. `Round 3 - Synthesis`
--++    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--++-5. `Round 4 - Implementation Plan`
--+++6. `Round 4 - Implementation Plan`
--++    - Convert the selected design into files, tasks, tests, and rollout steps.
--++ 
--++ ## Operating Rules
--++@@ -38,4 +41,4 @@ The workflow is round-based. Each round produces a short decision record that ca
--++ 
--++ ## Current Starting Point
--++ 
--++-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--+++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--++diff --git a/docs/multi-agent-design-workflow/round-0-problem-framing.md b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--++index e5c5a3d..cef3ead 100644
--++--- a/docs/multi-agent-design-workflow/round-0-problem-framing.md
--+++++ b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--++@@ -18,13 +18,23 @@ Round 0 does not choose libraries, exchanges, strategies, infrastructure, or imp
--++   - `Claude`
--++   - `Gemini`
--++   - `Codex-Arbiter`
--++-- The project name suggests a crypto bot, but the exact product scope is not yet defined.
--+++- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
--+++- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
--+++- The first market scope is Binance spot.
--+++- The first assets are `BTC/USDT` and `ETH/USDT`.
--+++- There is no confirmed strategy hypothesis yet.
--+++- The first operator interface should be log files, not a web dashboard.
--+++- The initial risk tolerance is maximum drawdown of `10-20%`.
--+++- The initial backtest timeframe should be `1h`.
--+++- The user is interested in both historical backtesting and live market dry-run, but is open to sequencing historical data first and live dry-run later.
--+++- If live market dry-run is included, Binance read-only account support may be useful, but this is not confirmed.
--+++- The user is interested in both a strategy plugin interface and a strategy research workflow.
--++ 
--++ ## Working Problem Statement
--++ 
--++-ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.
--+++This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.
--++ 
--++-The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.
--+++Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.
--++ 
--++ ## Round 0 Prompts
--++ 
--++@@ -86,15 +96,15 @@ Assumptions:
--++ 
--++ Questions:
--++ 
--++-- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
--++-- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
--++-- QUESTION: Is the bot allowed to place orders automatically?
--++-- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
--++-- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?
--+++- QUESTION: Should milestone 1 include both historical backtesting and live market dry-run, or should live dry-run wait until historical simulation is trustworthy?
--+++- QUESTION: Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state only?
--+++- QUESTION: Should the first architecture prioritize a strategy plugin interface, a strategy research workflow, or a parallel strategy-monitoring system?
--+++- QUESTION: How should the system help discover or compare strategies when no hypothesis is confirmed yet?
--+++- QUESTION: What first class of strategy should be used only as a baseline to test the framework, without implying it is profitable?
--++ 
--++ Recommendation:
--++ 
--++-Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.
--+++Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.
--++ 
--++ Risks:
--++ 
--++@@ -123,6 +133,8 @@ Questions:
--++ - QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
--++ - QUESTION: How should the operator review, override, pause, or audit bot behavior?
--++ - QUESTION: What is the acceptable balance between speed, safety, and explainability?
--+++- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, a plugin interface for manually supplied strategies, or both?
--+++- QUESTION: If multiple strategies are evaluated in parallel, how should the operator avoid overfitting and false confidence?
--++ 
--++ Recommendation:
--++ 
--++@@ -162,6 +174,8 @@ Questions:
--++ - QUESTION: Is real money involved in milestone 1?
--++ - QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
--++ - QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
--+++- QUESTION: Should the first design sequence be historical candles first, then live WebSocket dry-run, then read-only portfolio monitoring?
--+++- QUESTION: Does Binance read-only monitoring materially improve milestone 1, or does it add unnecessary security and setup complexity?
--++ 
--++ Recommendation:
--++ 
--++@@ -174,14 +188,24 @@ Risks:
--++ 
--++ ## Codex-Arbiter Synthesis
--++ 
--+++### Round 0 Agent Answer Summary
--+++
--+++Codex-Architect framed the project as a non-live research and simulation system. The strongest point was sequencing: milestone 1 should prove trustworthy evaluation, reproducible results, structured audit logs, and rejection criteria before live market dry-run or read-only Binance account integration are assumed.
--+++
--+++Claude challenged the scope and argued that the project contains two different goals: research tooling and runtime infrastructure. The strongest point was that milestone 1 needs explicit exit criteria, a defined structured log schema, and a decision about whether the strategy interface is a real plugin contract or a provisional internal abstraction.
--+++
--+++Gemini framed the project as a hypothesis-first research platform. The strongest point was that high-fidelity backtesting and strategy comparison are more valuable in milestone 1 than live dry-run, because live dry-run on a `1h` timeframe takes weeks to produce meaningful evidence. Gemini also recommended sensitivity analysis over automated optimization to reduce curve fitting.
--+++
--++ Canonical problem statement:
--++ 
--++-This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.
--+++This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`. The first milestone should support historical backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Live market dry-run and Binance read-only account monitoring are desirable but should be debated for sequencing and complexity. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, monitor, and reject rather than assuming a profitable strategy already exists.
--++ 
--++ In scope for Round 0:
--++ 
--++-- Clarifying bot type and first milestone.
--++-- Identifying risk, safety, and human-control requirements.
--+++- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
--+++- Identifying risk, safety, and human-control requirements for non-live operation.
--+++- Clarifying data source and simulation fidelity requirements for Binance spot.
--+++- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
--++ - Recording blocking questions and assumptions.
--++ - Preparing for candidate architecture designs in Round 1.
--++ 
--++@@ -191,27 +215,39 @@ Out of scope for Round 0:
--++ - Choosing exchange SDKs or trading libraries.
--++ - Writing trading strategy code.
--++ - Designing live order execution flows.
--+++- Enabling real-money trading.
--+++- Supporting leverage, futures, margin, or withdrawals.
--++ 
--++ Blocking questions:
--++ 
--++-- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
--++-- Will the bot handle real funds or private keys in milestone 1?
--++-- What user approval or kill-switch controls are required?
--++-- What exchange, chain, wallet, or market-data source is targeted first?
--++-- What interface should the operator use first: CLI, web UI, chat, API, or background service only?
--+++- What is the formal milestone 1 exit condition?
--+++- What exact structured log format and event schema should be treated as the first operator interface?
--+++- Should the strategy interface in milestone 1 be a real plugin contract or a provisional internal abstraction?
--+++- What minimum simulation realism is required for milestone 1: fees only, fees plus spread/slippage, or partial fill/latency assumptions?
--+++- What benchmark should strategy candidates be compared against, such as buy-and-hold, cash, or simple baseline strategies?
--++ 
--++ Non-blocking assumptions:
--++ 
--++ - The repo is early enough that workflow docs can define the decision process.
--++ - The first implementation should be narrow and reversible.
--++ - Safety and auditability should be treated as first-class design concerns.
--+++- Binance is the initial exchange/data source.
--+++- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
--+++- Spot-only scope excludes leverage, margin, futures, and perpetuals.
--+++- Log files are sufficient for the first operator interface if they are structured and easy to audit.
--+++- Maximum drawdown of `10-20%` is a project-level risk boundary for evaluation and future paper/live controls.
--+++- The first timeframe is `1h`.
--+++- Live market dry-run should be sequenced after historical backtesting is reliable.
--+++- Binance read-only account monitoring should be deferred unless Round 1 identifies a strong reason to include it.
--+++- Milestone 1 portfolio monitoring can start with simulated portfolio state.
--+++- The research workflow should prioritize comparison and sensitivity analysis over automated parameter optimization.
--++ 
--++ Decision:
--++ 
--++-Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.
--+++Proceed to Round 1 candidate designs with a narrower milestone: historical backtesting, simulated portfolio monitoring, structured logs, strategy comparison/research workflow, and a carefully scoped strategy extension boundary. Live market dry-run and Binance read-only account monitoring are deferred to milestone 2 unless an architect can justify a minimal interface stub that does not add credential or runtime complexity.
--++ 
--++ Next actions:
--++ 
--++-1. User answers the blocking questions.
--++-2. Codex-Arbiter updates this document with the chosen first milestone.
--++-3. Round 1 begins with candidate designs constrained to that milestone.
--+++1. Codex-Arbiter updates the neutral problem brief with this narrower milestone.
--+++2. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
--+++3. Round 1 proposals must explicitly answer the remaining architecture questions: log schema, strategy boundary, data persistence, backtest realism, metrics, and anti-overfitting workflow.
--++diff --git a/prompts/README.md b/prompts/README.md
--++index d8a2217..ef2814f 100644
--++--- a/prompts/README.md
--+++++ b/prompts/README.md
--++@@ -4,12 +4,12 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--++ 
--++ Recommended order:
--++ 
--++-1. `round0-problem-framing.md`
--++-2. `round0-brief-synthesis.md`
--++-3. `round1-codex-architect.md`
--++-4. `round1-external-architect.md`
--++-5. `round2-cross-review.md`
--++-6. `round3-arbiter.md`
--++-
--++-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--++-
--+++1. `round-minus-1-trading-bot-principles.md`
--+++2. `round0-problem-framing.md`
--+++3. `round0-brief-synthesis.md`
--+++4. `round1-codex-architect.md`
--+++5. `round1-external-architect.md`
--+++6. `round2-cross-review.md`
--+++7. `round3-arbiter.md`
--+++
--+++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--++diff --git a/reviews/latest/context-pack.md b/reviews/latest/context-pack.md
--++index 3caebdb..a93e621 100644
--++--- a/reviews/latest/context-pack.md
--+++++ b/reviews/latest/context-pack.md
--++@@ -1,37 +1,2156 @@
--++ # Context Pack
--++ 
--++-Generated: 2026-05-02T16:04:56
--+++Generated: 2026-05-02T17:21:31
--++ Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--++ 
--++ ## Current Task
--++ 
--++-Verify multi-agent design workflow setup
--+++Round 1: propose architecture for non-live Binance spot research and paper-readiness system
--++ 
--++ ## Git Status
--++ 
--++ ```text
--++-?? .env.example
--++-?? README.md
--++-?? docs/
--++-?? prompts/
--++-?? reviews/
--++-?? tools/
--+++M README.md
--+++ M docs/multi-agent-design-workflow/README.md
--+++ M docs/multi-agent-design-workflow/round-0-problem-framing.md
--+++ M prompts/README.md
--+++ M reviews/latest/context-pack.md
--+++?? docs/multi-agent-design-workflow/00-problem-brief.md
--+++?? docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md
--+++?? prompts/round-minus-1-trading-bot-principles.md
--++ ```
--++ 
--++ ## Git Diff
--++ 
--++ ```diff
--++-[no diff]
--+++diff --git a/README.md b/README.md
--+++index a2ea905..8236365 100644
--+++--- a/README.md
--++++++ b/README.md
--+++@@ -4,16 +4,18 @@ This repo starts with a multi-agent design workflow before implementation.
--+++ 
--+++ The intended loop is:
--+++ 
--+++-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--+++-2. Codex-Arbiter turns the answers into a neutral problem brief.
--+++-3. Round 1: each architect proposes a design from the same brief.
--+++-4. Round 2: agents critique the candidate designs.
--+++-5. Round 3: Codex-Arbiter records the final architecture.
--+++-6. Round 4: Codex implements the accepted plan and runs verification.
--++++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--++++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--++++3. Codex-Arbiter turns the answers into a neutral problem brief.
--++++4. Round 1: each architect proposes a design from the same brief.
--++++5. Round 2: agents critique the candidate designs.
--++++6. Round 3: Codex-Arbiter records the final architecture.
--++++7. Round 4: Codex implements the accepted plan and runs verification.
--+++ 
--+++ Start here:
--+++ 
--+++ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--++++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--+++ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--+++ - [Prompt Library](prompts/README.md)
--+++ 
--+++diff --git a/docs/multi-agent-design-workflow/README.md b/docs/multi-agent-design-workflow/README.md
--+++index a532bf4..b701d3e 100644
--+++--- a/docs/multi-agent-design-workflow/README.md
--++++++ b/docs/multi-agent-design-workflow/README.md
--+++@@ -11,16 +11,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--+++ 
--+++ ## Round Sequence
--+++ 
--+++-1. `Round 0 - Problem Framing`
--++++1. `Round -1 - Trading Bot Principles`
--++++   - Define what a good and potentially profitable crypto trading bot requires.
--++++   - Establish safety, validation, and profitability standards before project-specific design.
--++++2. `Round 0 - Problem Framing`
--+++    - Define the actual problem, users, success criteria, constraints, and unknowns.
--+++    - No solution is selected in this round.
--+++-2. `Round 1 - Candidate Designs`
--++++3. `Round 1 - Candidate Designs`
--+++    - Each design agent proposes one or more viable approaches.
--+++-3. `Round 2 - Critique and Risk`
--++++4. `Round 2 - Critique and Risk`
--+++    - Agents critique designs from their role perspective.
--+++-4. `Round 3 - Synthesis`
--++++5. `Round 3 - Synthesis`
--+++    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--+++-5. `Round 4 - Implementation Plan`
--++++6. `Round 4 - Implementation Plan`
--+++    - Convert the selected design into files, tasks, tests, and rollout steps.
--+++ 
--+++ ## Operating Rules
--+++@@ -38,4 +41,4 @@ The workflow is round-based. Each round produces a short decision record that ca
--+++ 
--+++ ## Current Starting Point
--+++ 
--+++-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--++++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--+++diff --git a/docs/multi-agent-design-workflow/round-0-problem-framing.md b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--+++index e5c5a3d..6b67249 100644
--+++--- a/docs/multi-agent-design-workflow/round-0-problem-framing.md
--++++++ b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--+++@@ -18,13 +18,23 @@ Round 0 does not choose libraries, exchanges, strategies, infrastructure, or imp
--+++   - `Claude`
--+++   - `Gemini`
--+++   - `Codex-Arbiter`
--+++-- The project name suggests a crypto bot, but the exact product scope is not yet defined.
--++++- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
--++++- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
--++++- The first market scope is Binance spot.
--++++- The first assets are `BTC/USDT` and `ETH/USDT`.
--++++- There is no confirmed strategy hypothesis yet.
--++++- The first operator interface should be log files, not a web dashboard.
--++++- The initial risk tolerance is maximum drawdown of `10-20%`.
--++++- The initial backtest timeframe should be `1h`.
--++++- The user is interested in both historical backtesting and live market dry-run, but is open to sequencing historical data first and live dry-run later.
--++++- If live market dry-run is included, Binance read-only account support may be useful, but this is not confirmed.
--++++- The user is interested in both a strategy plugin interface and a strategy research workflow.
--+++ 
--+++ ## Working Problem Statement
--+++ 
--+++-ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.
--++++This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.
--+++ 
--+++-The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.
--++++Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.
--+++ 
--+++ ## Round 0 Prompts
--+++ 
--+++@@ -86,15 +96,15 @@ Assumptions:
--+++ 
--+++ Questions:
--+++ 
--+++-- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
--+++-- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
--+++-- QUESTION: Is the bot allowed to place orders automatically?
--+++-- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
--+++-- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?
--++++- QUESTION: Should milestone 1 include both historical backtesting and live market dry-run, or should live dry-run wait until historical simulation is trustworthy?
--++++- QUESTION: Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state only?
--++++- QUESTION: Should the first architecture prioritize a strategy plugin interface, a strategy research workflow, or a parallel strategy-monitoring system?
--++++- QUESTION: How should the system help discover or compare strategies when no hypothesis is confirmed yet?
--++++- QUESTION: What first class of strategy should be used only as a baseline to test the framework, without implying it is profitable?
--+++ 
--+++ Recommendation:
--+++ 
--+++-Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.
--++++Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.
--+++ 
--+++ Risks:
--+++ 
--+++@@ -123,6 +133,8 @@ Questions:
--+++ - QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
--+++ - QUESTION: How should the operator review, override, pause, or audit bot behavior?
--+++ - QUESTION: What is the acceptable balance between speed, safety, and explainability?
--++++- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, a plugin interface for manually supplied strategies, or both?
--++++- QUESTION: If multiple strategies are evaluated in parallel, how should the operator avoid overfitting and false confidence?
--+++ 
--+++ Recommendation:
--+++ 
--+++@@ -162,6 +174,8 @@ Questions:
--+++ - QUESTION: Is real money involved in milestone 1?
--+++ - QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
--+++ - QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
--++++- QUESTION: Should the first design sequence be historical candles first, then live WebSocket dry-run, then read-only portfolio monitoring?
--++++- QUESTION: Does Binance read-only monitoring materially improve milestone 1, or does it add unnecessary security and setup complexity?
--+++ 
--+++ Recommendation:
--+++ 
--+++@@ -176,12 +190,14 @@ Risks:
--+++ 
--+++ Canonical problem statement:
--+++ 
--+++-This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.
--++++This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`. The first milestone should support historical backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Live market dry-run and Binance read-only account monitoring are desirable but should be debated for sequencing and complexity. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, monitor, and reject rather than assuming a profitable strategy already exists.
--+++ 
--+++ In scope for Round 0:
--+++ 
--+++-- Clarifying bot type and first milestone.
--+++-- Identifying risk, safety, and human-control requirements.
--++++- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
--++++- Identifying risk, safety, and human-control requirements for non-live operation.
--++++- Clarifying data source and simulation fidelity requirements for Binance spot.
--++++- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
--+++ - Recording blocking questions and assumptions.
--+++ - Preparing for candidate architecture designs in Round 1.
--+++ 
--+++@@ -191,27 +207,35 @@ Out of scope for Round 0:
--+++ - Choosing exchange SDKs or trading libraries.
--+++ - Writing trading strategy code.
--+++ - Designing live order execution flows.
--++++- Enabling real-money trading.
--++++- Supporting leverage, futures, margin, or withdrawals.
--+++ 
--+++ Blocking questions:
--+++ 
--+++-- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
--+++-- Will the bot handle real funds or private keys in milestone 1?
--+++-- What user approval or kill-switch controls are required?
--+++-- What exchange, chain, wallet, or market-data source is targeted first?
--+++-- What interface should the operator use first: CLI, web UI, chat, API, or background service only?
--++++- Should live market dry-run be included in milestone 1, or sequenced after historical backtesting is reliable?
--++++- Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state?
--++++- Should Round 1 design prioritize a strategy plugin interface, a strategy research workflow, or both?
--++++- If both plugin interface and research workflow are included, how should the system prevent strategy overfitting and false confidence?
--++++- What baseline strategy, if any, should be included only to validate framework behavior?
--+++ 
--+++ Non-blocking assumptions:
--+++ 
--+++ - The repo is early enough that workflow docs can define the decision process.
--+++ - The first implementation should be narrow and reversible.
--+++ - Safety and auditability should be treated as first-class design concerns.
--++++- Binance is the initial exchange/data source.
--++++- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
--++++- Spot-only scope excludes leverage, margin, futures, and perpetuals.
--++++- Log files are sufficient for the first operator interface if they are structured and easy to audit.
--++++- Maximum drawdown of `10-20%` is a project-level risk boundary for evaluation and future paper/live controls.
--++++- The first timeframe is `1h`.
--+++ 
--+++ Decision:
--+++ 
--+++-Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.
--++++Proceed toward Round 1 with the unresolved points treated as explicit design questions for the architects to debate. The Round 1 design space is a non-live Binance spot research system with `1h` backtesting, paper/dry-run simulation planning, alert generation, portfolio-state monitoring, structured logs, strategy plugin support, and strategy research workflow support.
--+++ 
--+++ Next actions:
--+++ 
--+++-1. User answers the blocking questions.
--+++-2. Codex-Arbiter updates this document with the chosen first milestone.
--+++-3. Round 1 begins with candidate designs constrained to that milestone.
--++++1. User clarifies the remaining blocking questions.
--++++2. Codex-Arbiter converts this Round 0 framing into a neutral problem brief.
--++++3. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
--+++diff --git a/prompts/README.md b/prompts/README.md
--+++index d8a2217..ef2814f 100644
--+++--- a/prompts/README.md
--++++++ b/prompts/README.md
--+++@@ -4,12 +4,12 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--+++ 
--+++ Recommended order:
--+++ 
--+++-1. `round0-problem-framing.md`
--+++-2. `round0-brief-synthesis.md`
--+++-3. `round1-codex-architect.md`
--+++-4. `round1-external-architect.md`
--+++-5. `round2-cross-review.md`
--+++-6. `round3-arbiter.md`
--+++-
--+++-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--+++-
--++++1. `round-minus-1-trading-bot-principles.md`
--++++2. `round0-problem-framing.md`
--++++3. `round0-brief-synthesis.md`
--++++4. `round1-codex-architect.md`
--++++5. `round1-external-architect.md`
--++++6. `round2-cross-review.md`
--++++7. `round3-arbiter.md`
--++++
--++++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--+++diff --git a/reviews/latest/context-pack.md b/reviews/latest/context-pack.md
--+++index 3caebdb..87aecb0 100644
--+++--- a/reviews/latest/context-pack.md
--++++++ b/reviews/latest/context-pack.md
--+++@@ -1,27 +1,1308 @@
--+++ # Context Pack
--+++ 
--+++-Generated: 2026-05-02T16:04:56
--++++Generated: 2026-05-02T16:53:36
--+++ Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--+++ 
--+++ ## Current Task
--+++ 
--+++-Verify multi-agent design workflow setup
--++++Round 0: clarify remaining blocking questions for non-live Binance spot research bot
--+++ 
--+++ ## Git Status
--+++ 
--+++ ```text
--+++-?? .env.example
--+++-?? README.md
--+++-?? docs/
--+++-?? prompts/
--+++-?? reviews/
--+++-?? tools/
--++++M README.md
--++++ M docs/multi-agent-design-workflow/README.md
--++++ M docs/multi-agent-design-workflow/round-0-problem-framing.md
--++++ M prompts/README.md
--++++ M reviews/latest/context-pack.md
--++++?? docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md
--++++?? prompts/round-minus-1-trading-bot-principles.md
--+++ ```
--+++ 
--+++ ## Git Diff
--+++ 
--+++ ```diff
--+++-[no diff]
--++++diff --git a/README.md b/README.md
--++++index a2ea905..8236365 100644
--++++--- a/README.md
--+++++++ b/README.md
--++++@@ -4,16 +4,18 @@ This repo starts with a multi-agent design workflow before implementation.
--++++ 
--++++ The intended loop is:
--++++ 
--++++-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--++++-2. Codex-Arbiter turns the answers into a neutral problem brief.
--++++-3. Round 1: each architect proposes a design from the same brief.
--++++-4. Round 2: agents critique the candidate designs.
--++++-5. Round 3: Codex-Arbiter records the final architecture.
--++++-6. Round 4: Codex implements the accepted plan and runs verification.
--+++++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--+++++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--+++++3. Codex-Arbiter turns the answers into a neutral problem brief.
--+++++4. Round 1: each architect proposes a design from the same brief.
--+++++5. Round 2: agents critique the candidate designs.
--+++++6. Round 3: Codex-Arbiter records the final architecture.
--+++++7. Round 4: Codex implements the accepted plan and runs verification.
--++++ 
--++++ Start here:
--++++ 
--++++ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--+++++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--++++ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--++++ - [Prompt Library](prompts/README.md)
--++++ 
--++++diff --git a/docs/multi-agent-design-workflow/README.md b/docs/multi-agent-design-workflow/README.md
--++++index a532bf4..b701d3e 100644
--++++--- a/docs/multi-agent-design-workflow/README.md
--+++++++ b/docs/multi-agent-design-workflow/README.md
--++++@@ -11,16 +11,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--++++ 
--++++ ## Round Sequence
--++++ 
--++++-1. `Round 0 - Problem Framing`
--+++++1. `Round -1 - Trading Bot Principles`
--+++++   - Define what a good and potentially profitable crypto trading bot requires.
--+++++   - Establish safety, validation, and profitability standards before project-specific design.
--+++++2. `Round 0 - Problem Framing`
--++++    - Define the actual problem, users, success criteria, constraints, and unknowns.
--++++    - No solution is selected in this round.
--++++-2. `Round 1 - Candidate Designs`
--+++++3. `Round 1 - Candidate Designs`
--++++    - Each design agent proposes one or more viable approaches.
--++++-3. `Round 2 - Critique and Risk`
--+++++4. `Round 2 - Critique and Risk`
--++++    - Agents critique designs from their role perspective.
--++++-4. `Round 3 - Synthesis`
--+++++5. `Round 3 - Synthesis`
--++++    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--++++-5. `Round 4 - Implementation Plan`
--+++++6. `Round 4 - Implementation Plan`
--++++    - Convert the selected design into files, tasks, tests, and rollout steps.
--++++ 
--++++ ## Operating Rules
--++++@@ -38,4 +41,4 @@ The workflow is round-based. Each round produces a short decision record that ca
--++++ 
--++++ ## Current Starting Point
--++++ 
--++++-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--+++++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--++++diff --git a/docs/multi-agent-design-workflow/round-0-problem-framing.md b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--++++index e5c5a3d..a8bf9fe 100644
--++++--- a/docs/multi-agent-design-workflow/round-0-problem-framing.md
--+++++++ b/docs/multi-agent-design-workflow/round-0-problem-framing.md
--++++@@ -18,13 +18,19 @@ Round 0 does not choose libraries, exchanges, strategies, infrastructure, or imp
--++++   - `Claude`
--++++   - `Gemini`
--++++   - `Codex-Arbiter`
--++++-- The project name suggests a crypto bot, but the exact product scope is not yet defined.
--+++++- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
--+++++- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
--+++++- The first market scope is Binance spot.
--+++++- The first assets are `BTC/USDT` and `ETH/USDT`.
--+++++- There is no confirmed strategy hypothesis yet.
--+++++- The first operator interface should be log files, not a web dashboard.
--+++++- The initial risk tolerance was stated as `10-15%`, but the exact meaning still needs clarification.
--++++ 
--++++ ## Working Problem Statement
--++++ 
--++++-ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.
--+++++This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.
--++++ 
--++++-The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.
--+++++Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.
--++++ 
--++++ ## Round 0 Prompts
--++++ 
--++++@@ -86,15 +92,15 @@ Assumptions:
--++++ 
--++++ Questions:
--++++ 
--++++-- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
--++++-- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
--++++-- QUESTION: Is the bot allowed to place orders automatically?
--++++-- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
--++++-- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?
--+++++- QUESTION: What does the stated `10-15%` risk limit mean: max drawdown, max daily loss, max per-trade loss, max position size, or total capital allocation?
--+++++- QUESTION: Should Binance be used only as a historical/live market data source in milestone 1, or should paper trading simulate Binance order rules as closely as possible?
--+++++- QUESTION: What timeframe should the first backtests support: 1m, 5m, 15m, 1h, 4h, 1d, or multiple?
--+++++- QUESTION: What first class of strategy should the system be able to evaluate: trend-following, mean reversion, breakout, volatility filter, or a plugin-style strategy interface with no built-in claim?
--+++++- QUESTION: Should portfolio monitoring read from a real Binance account in read-only mode, or should it start with simulated portfolio state only?
--++++ 
--++++ Recommendation:
--++++ 
--++++-Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.
--+++++Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.
--++++ 
--++++ Risks:
--++++ 
--++++@@ -123,6 +129,7 @@ Questions:
--++++ - QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
--++++ - QUESTION: How should the operator review, override, pause, or audit bot behavior?
--++++ - QUESTION: What is the acceptable balance between speed, safety, and explainability?
--+++++- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, or only the framework needed to test manually supplied strategies?
--++++ 
--++++ Recommendation:
--++++ 
--++++@@ -162,6 +169,8 @@ Questions:
--++++ - QUESTION: Is real money involved in milestone 1?
--++++ - QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
--++++ - QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
--+++++- QUESTION: Which Binance data path is acceptable for milestone 1: downloaded historical candles, live WebSocket streams, REST polling, or a combination?
--+++++- QUESTION: Does portfolio monitoring require real account balances in read-only mode, or simulated balances from paper trades?
--++++ 
--++++ Recommendation:
--++++ 
--++++@@ -176,12 +185,14 @@ Risks:
--++++ 
--++++ Canonical problem statement:
--++++ 
--++++-This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.
--+++++This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT`. The first milestone should support backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, and reject rather than assuming a profitable strategy already exists.
--++++ 
--++++ In scope for Round 0:
--++++ 
--++++-- Clarifying bot type and first milestone.
--++++-- Identifying risk, safety, and human-control requirements.
--+++++- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
--+++++- Identifying risk, safety, and human-control requirements for non-live operation.
--+++++- Clarifying data source and simulation fidelity requirements for Binance spot.
--+++++- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
--++++ - Recording blocking questions and assumptions.
--++++ - Preparing for candidate architecture designs in Round 1.
--++++ 
--++++@@ -191,27 +202,33 @@ Out of scope for Round 0:
--++++ - Choosing exchange SDKs or trading libraries.
--++++ - Writing trading strategy code.
--++++ - Designing live order execution flows.
--+++++- Enabling real-money trading.
--+++++- Supporting leverage, futures, margin, or withdrawals.
--++++ 
--++++ Blocking questions:
--++++ 
--++++-- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
--++++-- Will the bot handle real funds or private keys in milestone 1?
--++++-- What user approval or kill-switch controls are required?
--++++-- What exchange, chain, wallet, or market-data source is targeted first?
--++++-- What interface should the operator use first: CLI, web UI, chat, API, or background service only?
--+++++- What does `10-15%` mean exactly: max drawdown, max daily loss, max per-trade loss, max position size, or total capital allocation?
--+++++- What timeframe(s) should the first backtester support?
--+++++- Should paper trading simulate orders from historical candles only, or should it also support live market data dry-run mode?
--+++++- Should portfolio monitoring use real Binance read-only account data or simulated paper portfolio state in milestone 1?
--+++++- Since there is no strategy hypothesis yet, should Round 1 design include a strategy research workflow, a plugin strategy interface, or one simple baseline strategy purely for testing the framework?
--++++ 
--++++ Non-blocking assumptions:
--++++ 
--++++ - The repo is early enough that workflow docs can define the decision process.
--++++ - The first implementation should be narrow and reversible.
--++++ - Safety and auditability should be treated as first-class design concerns.
--+++++- Binance is the initial exchange/data source.
--+++++- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
--+++++- Spot-only scope excludes leverage, margin, futures, and perpetuals.
--+++++- Log files are sufficient for the first operator interface if they are structured and easy to audit.
--++++ 
--++++ Decision:
--++++ 
--++++-Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.
--+++++Proceed toward Round 1 only after the remaining blocking questions are answered or explicitly accepted as design assumptions. The likely Round 1 design space is a non-live Binance spot research system with backtesting, paper/dry-run simulation, alert generation, portfolio-state monitoring, structured logs, and strategy hypothesis support.
--++++ 
--++++ Next actions:
--++++ 
--++++-1. User answers the blocking questions.
--++++-2. Codex-Arbiter updates this document with the chosen first milestone.
--++++-3. Round 1 begins with candidate designs constrained to that milestone.
--+++++1. User clarifies the remaining blocking questions.
--+++++2. Codex-Arbiter converts this Round 0 framing into a neutral problem brief.
--+++++3. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
--++++diff --git a/prompts/README.md b/prompts/README.md
--++++index d8a2217..ef2814f 100644
--++++--- a/prompts/README.md
--+++++++ b/prompts/README.md
--++++@@ -4,12 +4,12 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--++++ 
--++++ Recommended order:
--++++ 
--++++-1. `round0-problem-framing.md`
--++++-2. `round0-brief-synthesis.md`
--++++-3. `round1-codex-architect.md`
--++++-4. `round1-external-architect.md`
--++++-5. `round2-cross-review.md`
--++++-6. `round3-arbiter.md`
--++++-
--++++-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--++++-
--+++++1. `round-minus-1-trading-bot-principles.md`
--+++++2. `round0-problem-framing.md`
--+++++3. `round0-brief-synthesis.md`
--+++++4. `round1-codex-architect.md`
--+++++5. `round1-external-architect.md`
--+++++6. `round2-cross-review.md`
--+++++7. `round3-arbiter.md`
--+++++
--+++++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--++++diff --git a/reviews/latest/context-pack.md b/reviews/latest/context-pack.md
--++++index 3caebdb..b0867fc 100644
--++++--- a/reviews/latest/context-pack.md
--+++++++ b/reviews/latest/context-pack.md
--++++@@ -1,27 +1,600 @@
--++++ # Context Pack
--++++ 
--++++-Generated: 2026-05-02T16:04:56
--+++++Generated: 2026-05-02T16:46:31
--++++ Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--++++ 
--++++ ## Current Task
--++++ 
--++++-Verify multi-agent design workflow setup
--+++++Round 0: use Round -1 synthesis to frame the crypto bot MVP
--++++ 
--++++ ## Git Status
--++++ 
--++++ ```text
--++++-?? .env.example
--++++-?? README.md
--++++-?? docs/
--++++-?? prompts/
--++++-?? reviews/
--++++-?? tools/
--+++++M README.md
--+++++ M docs/multi-agent-design-workflow/README.md
--+++++ M prompts/README.md
--+++++ M reviews/latest/context-pack.md
--+++++?? docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md
--+++++?? prompts/round-minus-1-trading-bot-principles.md
--++++ ```
--++++ 
--++++ ## Git Diff
--++++ 
--++++ ```diff
--++++-[no diff]
--+++++diff --git a/README.md b/README.md
--+++++index a2ea905..8236365 100644
--+++++--- a/README.md
--++++++++ b/README.md
--+++++@@ -4,16 +4,18 @@ This repo starts with a multi-agent design workflow before implementation.
--+++++ 
--+++++ The intended loop is:
--+++++ 
--+++++-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--+++++-2. Codex-Arbiter turns the answers into a neutral problem brief.
--+++++-3. Round 1: each architect proposes a design from the same brief.
--+++++-4. Round 2: agents critique the candidate designs.
--+++++-5. Round 3: Codex-Arbiter records the final architecture.
--+++++-6. Round 4: Codex implements the accepted plan and runs verification.
--++++++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--++++++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--++++++3. Codex-Arbiter turns the answers into a neutral problem brief.
--++++++4. Round 1: each architect proposes a design from the same brief.
--++++++5. Round 2: agents critique the candidate designs.
--++++++6. Round 3: Codex-Arbiter records the final architecture.
--++++++7. Round 4: Codex implements the accepted plan and runs verification.
--+++++ 
--+++++ Start here:
--+++++ 
--+++++ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--++++++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--+++++ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--+++++ - [Prompt Library](prompts/README.md)
--+++++ 
--+++++diff --git a/docs/multi-agent-design-workflow/README.md b/docs/multi-agent-design-workflow/README.md
--+++++index a532bf4..b701d3e 100644
--+++++--- a/docs/multi-agent-design-workflow/README.md
--++++++++ b/docs/multi-agent-design-workflow/README.md
--+++++@@ -11,16 +11,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--+++++ 
--+++++ ## Round Sequence
--+++++ 
--+++++-1. `Round 0 - Problem Framing`
--++++++1. `Round -1 - Trading Bot Principles`
--++++++   - Define what a good and potentially profitable crypto trading bot requires.
--++++++   - Establish safety, validation, and profitability standards before project-specific design.
--++++++2. `Round 0 - Problem Framing`
--+++++    - Define the actual problem, users, success criteria, constraints, and unknowns.
--+++++    - No solution is selected in this round.
--+++++-2. `Round 1 - Candidate Designs`
--++++++3. `Round 1 - Candidate Designs`
--+++++    - Each design agent proposes one or more viable approaches.
--+++++-3. `Round 2 - Critique and Risk`
--++++++4. `Round 2 - Critique and Risk`
--+++++    - Agents critique designs from their role perspective.
--+++++-4. `Round 3 - Synthesis`
--++++++5. `Round 3 - Synthesis`
--+++++    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--+++++-5. `Round 4 - Implementation Plan`
--++++++6. `Round 4 - Implementation Plan`
--+++++    - Convert the selected design into files, tasks, tests, and rollout steps.
--+++++ 
--+++++ ## Operating Rules
--+++++@@ -38,4 +41,4 @@ The workflow is round-based. Each round produces a short decision record that ca
--+++++ 
--+++++ ## Current Starting Point
--+++++ 
--+++++-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--++++++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--+++++diff --git a/prompts/README.md b/prompts/README.md
--+++++index d8a2217..ef2814f 100644
--+++++--- a/prompts/README.md
--++++++++ b/prompts/README.md
--+++++@@ -4,12 +4,12 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--+++++ 
--+++++ Recommended order:
--+++++ 
--+++++-1. `round0-problem-framing.md`
--+++++-2. `round0-brief-synthesis.md`
--+++++-3. `round1-codex-architect.md`
--+++++-4. `round1-external-architect.md`
--+++++-5. `round2-cross-review.md`
--+++++-6. `round3-arbiter.md`
--+++++-
--+++++-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--+++++-
--++++++1. `round-minus-1-trading-bot-principles.md`
--++++++2. `round0-problem-framing.md`
--++++++3. `round0-brief-synthesis.md`
--++++++4. `round1-codex-architect.md`
--++++++5. `round1-external-architect.md`
--++++++6. `round2-cross-review.md`
--++++++7. `round3-arbiter.md`
--++++++
--++++++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--+++++diff --git a/reviews/latest/context-pack.md b/reviews/latest/context-pack.md
--+++++index 3caebdb..4b252d3 100644
--+++++--- a/reviews/latest/context-pack.md
--++++++++ b/reviews/latest/context-pack.md
--+++++@@ -1,27 +1,120 @@
--+++++ # Context Pack
--+++++ 
--+++++-Generated: 2026-05-02T16:04:56
--++++++Generated: 2026-05-02T16:36:43
--+++++ Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--+++++ 
--+++++ ## Current Task
--+++++ 
--+++++-Verify multi-agent design workflow setup
--++++++Round -1: define good and potentially profitable crypto trading bot principles
--+++++ 
--+++++ ## Git Status
--+++++ 
--+++++ ```text
--+++++-?? .env.example
--+++++-?? README.md
--+++++-?? docs/
--+++++-?? prompts/
--+++++-?? reviews/
--+++++-?? tools/
--++++++M README.md
--++++++ M docs/multi-agent-design-workflow/README.md
--++++++ M prompts/README.md
--++++++?? docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md
--++++++?? prompts/round-minus-1-trading-bot-principles.md
--+++++ ```
--+++++ 
--+++++ ## Git Diff
--+++++ 
--+++++ ```diff
--+++++-[no diff]
--++++++diff --git a/README.md b/README.md
--++++++index a2ea905..8236365 100644
--++++++--- a/README.md
--+++++++++ b/README.md
--++++++@@ -4,16 +4,18 @@ This repo starts with a multi-agent design workflow before implementation.
--++++++ 
--++++++ The intended loop is:
--++++++ 
--++++++-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--++++++-2. Codex-Arbiter turns the answers into a neutral problem brief.
--++++++-3. Round 1: each architect proposes a design from the same brief.
--++++++-4. Round 2: agents critique the candidate designs.
--++++++-5. Round 3: Codex-Arbiter records the final architecture.
--++++++-6. Round 4: Codex implements the accepted plan and runs verification.
--+++++++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--+++++++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--+++++++3. Codex-Arbiter turns the answers into a neutral problem brief.
--+++++++4. Round 1: each architect proposes a design from the same brief.
--+++++++5. Round 2: agents critique the candidate designs.
--+++++++6. Round 3: Codex-Arbiter records the final architecture.
--+++++++7. Round 4: Codex implements the accepted plan and runs verification.
--++++++ 
--++++++ Start here:
--++++++ 
--++++++ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--+++++++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--++++++ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--++++++ - [Prompt Library](prompts/README.md)
--++++++ 
--++++++diff --git a/docs/multi-agent-design-workflow/README.md b/docs/multi-agent-design-workflow/README.md
--++++++index a532bf4..b701d3e 100644
--++++++--- a/docs/multi-agent-design-workflow/README.md
--+++++++++ b/docs/multi-agent-design-workflow/README.md
--++++++@@ -11,16 +11,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--++++++ 
--++++++ ## Round Sequence
--++++++ 
--++++++-1. `Round 0 - Problem Framing`
--+++++++1. `Round -1 - Trading Bot Principles`
--+++++++   - Define what a good and potentially profitable crypto trading bot requires.
--+++++++   - Establish safety, validation, and profitability standards before project-specific design.
--+++++++2. `Round 0 - Problem Framing`
--++++++    - Define the actual problem, users, success criteria, constraints, and unknowns.
--++++++    - No solution is selected in this round.
--++++++-2. `Round 1 - Candidate Designs`
--+++++++3. `Round 1 - Candidate Designs`
--++++++    - Each design agent proposes one or more viable approaches.
--++++++-3. `Round 2 - Critique and Risk`
--+++++++4. `Round 2 - Critique and Risk`
--++++++    - Agents critique designs from their role perspective.
--++++++-4. `Round 3 - Synthesis`
--+++++++5. `Round 3 - Synthesis`
--++++++    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--++++++-5. `Round 4 - Implementation Plan`
--+++++++6. `Round 4 - Implementation Plan`
--++++++    - Convert the selected design into files, tasks, tests, and rollout steps.
--++++++ 
--++++++ ## Operating Rules
--++++++@@ -38,4 +41,4 @@ The workflow is round-based. Each round produces a short decision record that ca
--++++++ 
--++++++ ## Current Starting Point
--++++++ 
--++++++-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--+++++++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--++++++diff --git a/prompts/README.md b/prompts/README.md
--++++++index d8a2217..ef2814f 100644
--++++++--- a/prompts/README.md
--+++++++++ b/prompts/README.md
--++++++@@ -4,12 +4,12 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--++++++ 
--++++++ Recommended order:
--++++++ 
--++++++-1. `round0-problem-framing.md`
--++++++-2. `round0-brief-synthesis.md`
--++++++-3. `round1-codex-architect.md`
--++++++-4. `round1-external-architect.md`
--++++++-5. `round2-cross-review.md`
--++++++-6. `round3-arbiter.md`
--++++++-
--++++++-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--++++++-
--+++++++1. `round-minus-1-trading-bot-principles.md`
--+++++++2. `round0-problem-framing.md`
--+++++++3. `round0-brief-synthesis.md`
--+++++++4. `round1-codex-architect.md`
--+++++++5. `round1-external-architect.md`
--+++++++6. `round2-cross-review.md`
--+++++++7. `round3-arbiter.md`
--+++++++
--+++++++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--++++++
--++++++[stderr]
--++++++warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
--++++++warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF will be replaced by CRLF the next time Git touches it
--++++++warning: in the working copy of 'prompts/README.md', LF will be replaced by CRLF the next time Git touches it
--+++++ ```
--+++++ 
--+++++ ## File Tree
--+++++@@ -30,8 +123,10 @@ Verify multi-agent design workflow setup
--+++++ - docs\multi-agent-design-workflow\agent-protocol.md
--+++++ - docs\multi-agent-design-workflow\README.md
--+++++ - docs\multi-agent-design-workflow\round-0-problem-framing.md
--++++++- docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--+++++ - docs\multi-agent-design-workflow\round-template.md
--+++++ - prompts\README.md
--++++++- prompts\round-minus-1-trading-bot-principles.md
--+++++ - prompts\round0-brief-synthesis.md
--+++++ - prompts\round0-problem-framing.md
--+++++ - prompts\round1-codex-architect.md
--+++++@@ -41,6 +136,7 @@ Verify multi-agent design workflow setup
--+++++ - README.md
--+++++ - reviews\.gitkeep
--+++++ - reviews\latest\.gitkeep
--++++++- reviews\latest\context-pack.md
--+++++ - tools\make_context.py
--+++++ 
--+++++ ## Included Files
--+++++@@ -178,16 +274,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--+++++ 
--+++++ ## Round Sequence
--+++++ 
--+++++-1. `Round 0 - Problem Framing`
--++++++1. `Round -1 - Trading Bot Principles`
--++++++   - Define what a good and potentially profitable crypto trading bot requires.
--++++++   - Establish safety, validation, and profitability standards before project-specific design.
--++++++2. `Round 0 - Problem Framing`
--+++++    - Define the actual problem, users, success criteria, constraints, and unknowns.
--+++++    - No solution is selected in this round.
--+++++-2. `Round 1 - Candidate Designs`
--++++++3. `Round 1 - Candidate Designs`
--+++++    - Each design agent proposes one or more viable approaches.
--+++++-3. `Round 2 - Critique and Risk`
--++++++4. `Round 2 - Critique and Risk`
--+++++    - Agents critique designs from their role perspective.
--+++++-4. `Round 3 - Synthesis`
--++++++5. `Round 3 - Synthesis`
--+++++    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--+++++-5. `Round 4 - Implementation Plan`
--++++++6. `Round 4 - Implementation Plan`
--+++++    - Convert the selected design into files, tasks, tests, and rollout steps.
--+++++ 
--+++++ ## Operating Rules
--+++++@@ -205,7 +304,7 @@ The workflow is round-based. Each round produces a short decision record that ca
--+++++ 
--+++++ ## Current Starting Point
--+++++ 
--+++++-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--++++++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--+++++ 
--+++++ ```
--+++++ 
--+++++@@ -430,6 +529,154 @@ Next actions:
--+++++ 2. Codex-Arbiter updates this document with the chosen first milestone.
--+++++ 3. Round 1 begins with candidate designs constrained to that milestone.
--+++++ 
--++++++```
--++++++
--++++++### docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--++++++
--++++++```text
--++++++# Round -1 - Trading Bot Principles
--++++++
--++++++Status: `draft`
--++++++Date: `2026-05-02`
--++++++Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--++++++
--++++++## Goal of This Round
--++++++
--++++++Build a shared baseline for the question:
--++++++
--++++++> What should a good and potentially profitable crypto trading bot have?
--++++++
--++++++This round happens before project-specific problem framing. The goal is to clarify principles, risks, evaluation standards, and false assumptions before deciding what this repo should build.
--++++++
--++++++Round -1 does not design this project, choose exchanges, select frameworks, or define a specific trading strategy.
--++++++
--++++++## Ground Rules
--++++++
--++++++- Do not claim guaranteed profit.
--++++++- Separate "good bot qualities" from "profitability requirements".
--++++++- Treat risk controls, auditability, and validation as first-class concerns.
--++++++- Assume backtest results can be misleading until proven otherwise.
--++++++- Do not recommend live trading before paper trading and risk boundaries are defined.
--++++++- Mark assumptions as `ASSUMPTION`.
--++++++- Mark questions as `QUESTION`.
--++++++
--++++++## Shared Question
--++++++
--++++++What should a good and potentially profitable crypto trading bot have?
--++++++
--++++++## Agent Focus
--++++++
--++++++### Codex-Architect
--++++++
--++++++Focus on:
--++++++
--++++++- System qualities.
--++++++- Architecture implications.
--++++++- Testing and verification.
--++++++- Observability and audit logs.
--++++++- Maintainability and safe iteration.
--++++++
--++++++### Claude
--++++++
--++++++Focus on:
--++++++
--++++++- Flawed assumptions.
--++++++- Human risk and overconfidence.
--++++++- Decision boundaries.
--++++++- Edge cases and failure modes.
--++++++- What should remain human-approved.
--++++++
--++++++### Gemini
--++++++
--++++++Focus on:
--++++++
--++++++- Alternative bot types.
--++++++- Market and data constraints.
--++++++- Exchange and integration risks.
--++++++- Evaluation methods.
--++++++- External constraints that could dominate design.
--++++++
--++++++## Questions for Agents
--++++++
--++++++Each agent should answer:
--++++++
--++++++1. What makes a crypto trading bot good?
--++++++2. What conditions are required before it can plausibly be profitable?
--++++++3. What risk controls are non-negotiable?
--++++++4. What data, testing, and validation are required?
--++++++5. What common false assumptions should we avoid?
--++++++6. What should be excluded from MVP?
--++++++7. What are the 10 most important questions before designing our bot?
--++++++
--++++++## Initial Shared Baseline
--++++++
--++++++Good bot qualities:
--++++++
--++++++- Clear operating mode: alerts, research, backtesting, paper trading, or live execution.
--++++++- Separation between market data, strategy logic, risk controls, execution, state, and reporting.
--++++++- Full audit trail for inputs, decisions, orders, errors, overrides, and configuration changes.
--++++++- Deterministic replay/debug mode for understanding past decisions.
--++++++- Operator controls for pause, kill switch, configuration review, and emergency shutdown.
--++++++- Safe secret handling if exchange API keys or wallet credentials ever become involved.
--++++++- Tests for strategy logic, risk logic, execution adapters, and failure handling.
--++++++
--++++++Profitability requirements:
--++++++
--++++++- A testable hypothesis for why the strategy should have edge.
--++++++- Historical validation without look-ahead bias, survivorship bias, or data leakage.
--++++++- Evaluation after fees, spread, slippage, funding rates, latency, and failed orders.
--++++++- Out-of-sample testing or walk-forward validation.
--++++++- Paper trading before live trading.
--++++++- Position sizing and drawdown controls.
--++++++- Monitoring for market regime changes.
--++++++
--++++++Non-negotiable risk controls:
--++++++
--++++++- Max position size.
--++++++- Max daily loss.
--++++++- Max drawdown.
--++++++- Per-trade risk limit.
--++++++- Exchange/API failure handling.
--++++++- Duplicate order protection.
--++++++- Kill switch.
--++++++- Dry-run or paper mode.
--++++++- Read-only mode for analysis features.
--++++++- Human approval mode before live automation.
--++++++
--++++++Common false assumptions:
--++++++
--++++++- Backtest profit means future profit.
--++++++- High win rate means good strategy.
--++++++- AI can reliably predict sudden market moves.
--++++++- More indicators mean better signals.
--++++++- Live trading is just backtesting with real orders.
--++++++- Exchange APIs behave reliably during volatility.
--++++++- Fees and slippage are small enough to ignore.
--++++++- A bot should trade often to be useful.
--++++++
--++++++## Codex-Arbiter Synthesis Template
--++++++
--++++++After the three agents answer, produce:
--++++++
--++++++1. Shared principles accepted by all agents.
--++++++2. Disagreements or tensions worth preserving.
--++++++3. Non-negotiable safety requirements.
--++++++4. Evaluation standards for profitability claims.
--++++++5. MVP exclusions.
--++++++6. Questions that should flow into Round 0.
--++++++
--++++++## Decision
--++++++
--++++++Pending agent answers.
--++++++
--++++++## Next Actions
--++++++
--++++++1. Run Codex-Architect, Claude, and Gemini through the Round -1 prompt.
--++++++2. Paste or save their answers into this document or separate notes.
--++++++3. Ask Codex-Arbiter to synthesize the baseline.
--++++++4. Use the synthesized baseline as input to Round 0 problem framing.
--++++++
--++++++
--+++++ ```
--+++++ 
--+++++ ### docs\multi-agent-design-workflow\round-template.md
--+++++@@ -490,14 +737,85 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--+++++ 
--+++++ Recommended order:
--+++++ 
--+++++-1. `round0-problem-framing.md`
--+++++-2. `round0-brief-synthesis.md`
--+++++-3. `round1-codex-architect.md`
--+++++-4. `round1-external-architect.md`
--+++++-5. `round2-cross-review.md`
--+++++-6. `round3-arbiter.md`
--++++++1. `round-minus-1-trading-bot-principles.md`
--++++++2. `round0-problem-framing.md`
--++++++3. `round0-brief-synthesis.md`
--++++++4. `round1-codex-architect.md`
--++++++5. `round1-external-architect.md`
--++++++6. `round2-cross-review.md`
--++++++7. `round3-arbiter.md`
--+++++ 
--+++++-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--++++++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--++++++
--++++++```
--++++++
--++++++### prompts\round-minus-1-trading-bot-principles.md
--++++++
--++++++```text
--++++++# Round -1 - Trading Bot Principles
--++++++
--++++++You are participating in a multi-agent software design workflow.
--++++++
--++++++Round:
--++++++Round -1 - Trading Bot Principles
--++++++
--++++++Question:
--++++++"What should a good and potentially profitable crypto trading bot have?"
--++++++
--++++++Rules:
--++++++- Do not design this specific project yet.
--++++++- Do not choose frameworks, exchanges, or libraries.
--++++++- Do not claim guaranteed profits.
--++++++- Separate "good bot qualities" from "profitability requirements".
--++++++- Focus on principles, risks, and evaluation criteria.
--++++++- Mark assumptions as `ASSUMPTION`.
--++++++- Mark questions as `QUESTION`.
--++++++
--++++++Your role:
--++++++
--++++++```text
--++++++[Codex-Architect / Claude / Gemini]
--++++++```
--++++++
--++++++Role focus:
--++++++
--++++++```text
--++++++[Codex-Architect: system qualities, architecture implications, testing, observability, maintainability]
--++++++[Claude: flawed assumptions, human risk, decision boundaries, overconfidence, edge cases]
--++++++[Gemini: alternative bot types, market/data constraints, exchange/integration risks, evaluation methods]
--++++++```
--++++++
--++++++Task:
--++++++1. What makes a crypto trading bot good?
--++++++2. What conditions are required before it can plausibly be profitable?
--++++++3. What risk controls are non-negotiable?
--++++++4. What data, testing, and validation are required?
--++++++5. What common false assumptions should we avoid?
--++++++6. What should be excluded from MVP?
--++++++7. What are the 10 most important questions before designing our bot?
--++++++
--++++++Return format:
--++++++
--++++++```md
--++++++## Role
--++++++
--++++++## Good Bot Qualities
--++++++
--++++++## Profitability Requirements
--++++++
--++++++## Non-Negotiable Risk Controls
--++++++
--++++++## Data, Testing, and Validation
--++++++
--++++++## False Assumptions to Avoid
--++++++
--++++++## Exclude from MVP
--++++++
--++++++## Questions Before Design
--++++++- QUESTION:
--++++++
--++++++## Recommendation
--++++++```
--+++++ 
--+++++ 
--+++++ ```
--+++++@@ -872,16 +1190,18 @@ This repo starts with a multi-agent design workflow before implementation.
--+++++ 
--+++++ The intended loop is:
--+++++ 
--+++++-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--+++++-2. Codex-Arbiter turns the answers into a neutral problem brief.
--+++++-3. Round 1: each architect proposes a design from the same brief.
--+++++-4. Round 2: agents critique the candidate designs.
--+++++-5. Round 3: Codex-Arbiter records the final architecture.
--+++++-6. Round 4: Codex implements the accepted plan and runs verification.
--++++++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--++++++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--++++++3. Codex-Arbiter turns the answers into a neutral problem brief.
--++++++4. Round 1: each architect proposes a design from the same brief.
--++++++5. Round 2: agents critique the candidate designs.
--++++++6. Round 3: Codex-Arbiter records the final architecture.
--++++++7. Round 4: Codex implements the accepted plan and runs verification.
--+++++ 
--+++++ Start here:
--+++++ 
--+++++ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--++++++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--+++++ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--+++++ - [Prompt Library](prompts/README.md)
--+++++ 
--+++++@@ -890,12 +1210,17 @@ Start here:
--+++++ Create a context pack for review:
--+++++ 
--+++++ ```powershell
--+++++-python tools/make_context.py --task "Describe the current design question"
--++++++py tools/make_context.py --task "Describe the current design question"
--+++++ ```
--+++++ 
--+++++ The generated file goes to `reviews/latest/context-pack.md`.
--+++++ 
--++++++```
--+++++ 
--++++++### reviews\latest\context-pack.md
--++++++
--++++++```text
--++++++[Skipped: file is 26206 bytes, above 24000 byte limit]
--+++++ ```
--+++++ 
--+++++ ### tools\make_context.py
--+++++
--+++++[stderr]
--+++++warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
--+++++warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF will be replaced by CRLF the next time Git touches it
--+++++warning: in the working copy of 'prompts/README.md', LF will be replaced by CRLF the next time Git touches it
--++++ ```
--++++ 
--++++ ## File Tree
--++++@@ -30,8 +603,10 @@ Verify multi-agent design workflow setup
--++++ - docs\multi-agent-design-workflow\agent-protocol.md
--++++ - docs\multi-agent-design-workflow\README.md
--++++ - docs\multi-agent-design-workflow\round-0-problem-framing.md
--+++++- docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--++++ - docs\multi-agent-design-workflow\round-template.md
--++++ - prompts\README.md
--+++++- prompts\round-minus-1-trading-bot-principles.md
--++++ - prompts\round0-brief-synthesis.md
--++++ - prompts\round0-problem-framing.md
--++++ - prompts\round1-codex-architect.md
--++++@@ -41,6 +616,7 @@ Verify multi-agent design workflow setup
--++++ - README.md
--++++ - reviews\.gitkeep
--++++ - reviews\latest\.gitkeep
--+++++- reviews\latest\context-pack.md
--++++ - tools\make_context.py
--++++ 
--++++ ## Included Files
--++++@@ -178,16 +754,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--++++ 
--++++ ## Round Sequence
--++++ 
--++++-1. `Round 0 - Problem Framing`
--+++++1. `Round -1 - Trading Bot Principles`
--+++++   - Define what a good and potentially profitable crypto trading bot requires.
--+++++   - Establish safety, validation, and profitability standards before project-specific design.
--+++++2. `Round 0 - Problem Framing`
--++++    - Define the actual problem, users, success criteria, constraints, and unknowns.
--++++    - No solution is selected in this round.
--++++-2. `Round 1 - Candidate Designs`
--+++++3. `Round 1 - Candidate Designs`
--++++    - Each design agent proposes one or more viable approaches.
--++++-3. `Round 2 - Critique and Risk`
--+++++4. `Round 2 - Critique and Risk`
--++++    - Agents critique designs from their role perspective.
--++++-4. `Round 3 - Synthesis`
--+++++5. `Round 3 - Synthesis`
--++++    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--++++-5. `Round 4 - Implementation Plan`
--+++++6. `Round 4 - Implementation Plan`
--++++    - Convert the selected design into files, tasks, tests, and rollout steps.
--++++ 
--++++ ## Operating Rules
--++++@@ -205,7 +784,7 @@ The workflow is round-based. Each round produces a short decision record that ca
--++++ 
--++++ ## Current Starting Point
--++++ 
--++++-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--+++++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--++++ 
--++++ ```
--++++ 
--++++@@ -432,6 +1011,253 @@ Next actions:
--++++ 
--++++ ```
--++++ 
--+++++### docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--+++++
--+++++```text
--+++++# Round -1 - Trading Bot Principles
--+++++
--+++++Status: `draft`
--+++++Date: `2026-05-02`
--+++++Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--+++++
--+++++## Goal of This Round
--+++++
--+++++Build a shared baseline for the question:
--+++++
--+++++> What should a good and potentially profitable crypto trading bot have?
--+++++
--+++++This round happens before project-specific problem framing. The goal is to clarify principles, risks, evaluation standards, and false assumptions before deciding what this repo should build.
--+++++
--+++++Round -1 does not design this project, choose exchanges, select frameworks, or define a specific trading strategy.
--+++++
--+++++## Ground Rules
--+++++
--+++++- Do not claim guaranteed profit.
--+++++- Separate "good bot qualities" from "profitability requirements".
--+++++- Treat risk controls, auditability, and validation as first-class concerns.
--+++++- Assume backtest results can be misleading until proven otherwise.
--+++++- Do not recommend live trading before paper trading and risk boundaries are defined.
--+++++- Mark assumptions as `ASSUMPTION`.
--+++++- Mark questions as `QUESTION`.
--+++++
--+++++## Shared Question
--+++++
--+++++What should a good and potentially profitable crypto trading bot have?
--+++++
--+++++## Agent Focus
--+++++
--+++++### Codex-Architect
--+++++
--+++++Focus on:
--+++++
--+++++- System qualities.
--+++++- Architecture implications.
--+++++- Testing and verification.
--+++++- Observability and audit logs.
--+++++- Maintainability and safe iteration.
--+++++
--+++++### Claude
--+++++
--+++++Focus on:
--+++++
--+++++- Flawed assumptions.
--+++++- Human risk and overconfidence.
--+++++- Decision boundaries.
--+++++- Edge cases and failure modes.
--+++++- What should remain human-approved.
--+++++
--+++++### Gemini
--+++++
--+++++Focus on:
--+++++
--+++++- Alternative bot types.
--+++++- Market and data constraints.
--+++++- Exchange and integration risks.
--+++++- Evaluation methods.
--+++++- External constraints that could dominate design.
--+++++
--+++++## Questions for Agents
--+++++
--+++++Each agent should answer:
--+++++
--+++++1. What makes a crypto trading bot good?
--+++++2. What conditions are required before it can plausibly be profitable?
--+++++3. What risk controls are non-negotiable?
--+++++4. What data, testing, and validation are required?
--+++++5. What common false assumptions should we avoid?
--+++++6. What should be excluded from MVP?
--+++++7. What are the 10 most important questions before designing our bot?
--+++++
--+++++## Initial Shared Baseline
--+++++
--+++++Good bot qualities:
--+++++
--+++++- Clear operating mode: alerts, research, backtesting, paper trading, or live execution.
--+++++- Separation between market data, strategy logic, risk controls, execution, state, and reporting.
--+++++- Full audit trail for inputs, decisions, orders, errors, overrides, and configuration changes.
--+++++- Deterministic replay/debug mode for understanding past decisions.
--+++++- Operator controls for pause, kill switch, configuration review, and emergency shutdown.
--+++++- Safe secret handling if exchange API keys or wallet credentials ever become involved.
--+++++- Tests for strategy logic, risk logic, execution adapters, and failure handling.
--+++++
--+++++Profitability requirements:
--+++++
--+++++- A testable hypothesis for why the strategy should have edge.
--+++++- Historical validation without look-ahead bias, survivorship bias, or data leakage.
--+++++- Evaluation after fees, spread, slippage, funding rates, latency, and failed orders.
--+++++- Out-of-sample testing or walk-forward validation.
--+++++- Paper trading before live trading.
--+++++- Position sizing and drawdown controls.
--+++++- Monitoring for market regime changes.
--+++++
--+++++Non-negotiable risk controls:
--+++++
--+++++- Max position size.
--+++++- Max daily loss.
--+++++- Max drawdown.
--+++++- Per-trade risk limit.
--+++++- Exchange/API failure handling.
--+++++- Duplicate order protection.
--+++++- Kill switch.
--+++++- Dry-run or paper mode.
--+++++- Read-only mode for analysis features.
--+++++- Human approval mode before live automation.
--+++++
--+++++Common false assumptions:
--+++++
--+++++- Backtest profit means future profit.
--+++++- High win rate means good strategy.
--+++++- AI can reliably predict sudden market moves.
--+++++- More indicators mean better signals.
--+++++- Live trading is just backtesting with real orders.
--+++++- Exchange APIs behave reliably during volatility.
--+++++- Fees and slippage are small enough to ignore.
--+++++- A bot should trade often to be useful.
--+++++
--+++++## Codex-Arbiter Synthesis Template
--+++++
--+++++After the three agents answer, produce:
--+++++
--+++++1. Shared principles accepted by all agents.
--+++++2. Disagreements or tensions worth preserving.
--+++++3. Non-negotiable safety requirements.
--+++++4. Evaluation standards for profitability claims.
--+++++5. MVP exclusions.
--+++++6. Questions that should flow into Round 0.
--+++++
--+++++## Agent Answer Summary
--+++++
--+++++### Codex-Architect
--+++++
--+++++Codex-Architect framed a good bot as a controlled, observable, testable decision and execution system. The strongest points were separation of strategy, execution, risk, data, configuration, and monitoring; deterministic testing; fail-safe behavior; idempotent execution; strong state reconciliation; and explicit modes for backtest, paper, shadow, and live trading.
--+++++
--+++++Codex-Architect emphasized that profitability requires a real market edge after fees, spread, slippage, latency, funding, failed orders, and regime changes. It also stressed that the bot should support strategy retirement when live performance diverges from expectations.
--+++++
--+++++### Claude
--+++++
--+++++Claude focused on adversarial clarity and warned that the most common failure is starting implementation before the strategy hypothesis is honest. The strongest points were that profitability belongs to the strategy, market, cost structure, execution quality, and timing together, not to the bot by itself.
--+++++
--+++++Claude emphasized falsifiable strategy hypotheses, out-of-sample validation, hard drawdown circuit breakers, UTC/time discipline, human restart after major risk events, and predefined failure conditions for stopping the project or strategy.
--+++++
--+++++### Gemini
--+++++
--+++++Gemini emphasized alternative bot types, market/data constraints, and execution realities. The strongest points were operational resilience, telemetry, exchange integration risk, low-latency path where relevant, high-fidelity data handling, inventory management for market making or arbitrage, and the need to define the intended market regime.
--+++++
--+++++Gemini also highlighted tick-to-trade latency, partial fills, orphan orders, WebSocket/REST divergence, maker/taker fee assumptions, fat-tail events, and kill-switch authority.
--+++++
--+++++## Codex-Arbiter Synthesis
--+++++
--+++++### Shared Principles Accepted by All Agents
--+++++
--+++++- A good crypto trading bot is first a safety-critical automation system, not a profit machine.
--+++++- Strategy logic, risk controls, exchange execution, data ingestion, state management, configuration, monitoring, and reporting should be separated.
--+++++- Every trade decision must be auditable after the fact from logs and stored state.
--+++++- The bot must fail safely when data, connectivity, exchange APIs, or internal state become unreliable.
--+++++- Backtest profitability is not sufficient evidence of live profitability.
--+++++- Profitability claims must include fees, spread, slippage, latency, partial fills, failed orders, funding or borrow costs where relevant, and market regime effects.
--+++++- Paper trading is necessary before live trading, but paper trading is still not proof of live profitability.
--+++++- Risk controls belong in the MVP, not after the MVP.
--+++++- The first version should be narrow, explainable, and easy to shut down.
--+++++
--+++++### Disagreements or Tensions Worth Preserving
--+++++
--+++++- Claude recommends excluding dashboard and alerting from MVP, while Codex-Architect treats observability from day one as essential. The synthesis is: avoid a complex UI dashboard, but keep operational logs, basic metrics, and alerts for dangerous states.
--+++++- Gemini mentions a low-latency path, while Claude warns latency must match the strategy horizon. The synthesis is: do not optimize for low latency generally; define latency requirements only after the strategy type and timeframe are chosen.
--+++++- Claude prefers no auto-restart on crash, while production systems often need recovery behavior. The synthesis is: allow process restart only into a safe paused/reconcile mode, not automatic trading resumption.
--+++++- Codex-Architect assumes the bot may eventually trade real capital. Round 0 must confirm whether real funds are in scope for milestone 1.
--+++++
--+++++### Non-Negotiable Safety Requirements
--+++++
--+++++- Read-only, paper, and live modes must be explicit and hard to confuse.
--+++++- No withdrawal permissions for any exchange API key used by the bot.
--+++++- Kill switch must cancel open orders where possible and disable new trading.
--+++++- The bot must reconcile exchange/account state before trading on startup, reconnect, or restart.
--+++++- Duplicate order protection is required.
--+++++- Hard maximums are required for order size, position size, portfolio exposure, daily loss, drawdown, open orders, and order rate.
--+++++- The bot must halt or enter safe mode on stale data, repeated exchange errors, abnormal slippage, rejected orders, reconciliation mismatch, or connectivity loss.
--+++++- Human approval should be required before live automation and before scaling capital.
--+++++- All timestamps should be consistent and timezone-aware, preferably UTC internally.
--+++++- Every signal, order intent, order response, fill, cancellation, error, override, and configuration change must be logged.
--+++++
--+++++### Evaluation Standards for Profitability Claims
--+++++
--+++++- The strategy must have a falsifiable hypothesis explaining why an edge should exist.
--+++++- Backtests must avoid look-ahead bias, data leakage, and excessive parameter fitting.
--+++++- Validation must include out-of-sample data or walk-forward testing.
--+++++- Evaluation must include multiple market regimes where possible.
--+++++- Results must be measured after fees, spread, slippage, latency, partial fills, failed orders, and funding or borrow costs where relevant.
--+++++- Metrics should include total return, profit factor, Sharpe or Sortino, max drawdown, drawdown duration, win/loss distribution, tail losses, turnover, exposure, and sensitivity to parameters.
--+++++- Paper trading must compare expected fills against simulated or actual paper fills.
--+++++- Live trading, if ever allowed, should start with minimal capital and require evidence that live behavior matches expected behavior.
--+++++- A strategy must have predefined retirement or pause criteria when live performance diverges from expectations.
--+++++
--+++++### MVP Exclusions
--+++++
--+++++- Leverage, margin, perpetuals, and futures unless explicitly chosen later with separate risk design.
--+++++- Multiple exchanges.
--+++++- Multiple unrelated strategies.
--+++++- Cross-exchange arbitrage.
--+++++- High-frequency trading.
--+++++- Complex machine learning or automatic strategy discovery.
--+++++- Auto-optimization against recent backtests.
--+++++- Social/news sentiment trading.
--+++++- Copy trading.
--+++++- Withdrawal automation.
--+++++- Fully autonomous capital scaling.
--+++++- Complex UI dashboards beyond minimal operational visibility.
--+++++- Any feature that makes trades harder to explain.
--+++++
--+++++### Questions That Flow Into Round 0
--+++++
--+++++- QUESTION: What specific bot type is milestone 1: alerting, research, backtesting, paper trading, live spot trading, market making, arbitrage, portfolio tracking, or something else?
--+++++- QUESTION: What falsifiable market hypothesis do we want to test first?
--+++++- QUESTION: What market regime is the first strategy intended for?
--+++++- QUESTION: What trading horizon is targeted: seconds, minutes, hours, days, or longer?
--+++++- QUESTION: Which asset universe is allowed for milestone 1?
--+++++- QUESTION: Which exchange or data source is targeted first?
--+++++- QUESTION: Will milestone 1 involve real funds, or only read-only/paper mode?
--+++++- QUESTION: What maximum loss or drawdown is acceptable before the bot must halt?
--+++++- QUESTION: What evidence is required before moving from backtest to paper, and from paper to live?
--+++++- QUESTION: Who can trigger the kill switch, and what should the recovery protocol be?
--+++++- QUESTION: What interface should the operator use first: CLI, logs, simple dashboard, API, or chat?
--+++++- QUESTION: What monitoring is mandatory from day one?
--+++++- QUESTION: What is the minimum acceptable audit trail for every decision?
--+++++
--+++++## Decision
--+++++
--+++++Round -1 establishes the baseline: this project should not frame the first milestone as "build a profitable bot." It should frame the first milestone as "build a narrow, safe, auditable system for testing one falsifiable trading hypothesis under realistic costs and failure conditions."
--+++++
--+++++Proceed to Round 0 only after the user chooses the first milestone and answers the blocking questions about bot type, automation level, target market, target data source/exchange, allowed risk, and operator controls.
--+++++
--+++++## Next Actions
--+++++
--+++++1. Use this synthesis as input to Round 0 problem framing.
--+++++2. User answers the Round 0 blocking questions, especially bot type and whether real funds are in scope.
--+++++3. Codex-Arbiter updates `round-0-problem-framing.md` with the chosen first milestone.
--+++++4. Round 1 begins only after the problem brief is narrow enough for candidate architectures.
--+++++
--+++++```
--+++++
--++++ ### docs\multi-agent-design-workflow\round-template.md
--++++ 
--++++ ```text
--++++@@ -490,14 +1316,85 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--++++ 
--++++ Recommended order:
--++++ 
--++++-1. `round0-problem-framing.md`
--++++-2. `round0-brief-synthesis.md`
--++++-3. `round1-codex-architect.md`
--++++-4. `round1-external-architect.md`
--++++-5. `round2-cross-review.md`
--++++-6. `round3-arbiter.md`
--+++++1. `round-minus-1-trading-bot-principles.md`
--+++++2. `round0-problem-framing.md`
--+++++3. `round0-brief-synthesis.md`
--+++++4. `round1-codex-architect.md`
--+++++5. `round1-external-architect.md`
--+++++6. `round2-cross-review.md`
--+++++7. `round3-arbiter.md`
--+++++
--+++++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--+++++
--+++++```
--+++++
--+++++### prompts\round-minus-1-trading-bot-principles.md
--+++++
--+++++```text
--+++++# Round -1 - Trading Bot Principles
--+++++
--+++++You are participating in a multi-agent software design workflow.
--+++++
--+++++Round:
--+++++Round -1 - Trading Bot Principles
--+++++
--+++++Question:
--+++++"What should a good and potentially profitable crypto trading bot have?"
--+++++
--+++++Rules:
--+++++- Do not design this specific project yet.
--+++++- Do not choose frameworks, exchanges, or libraries.
--+++++- Do not claim guaranteed profits.
--+++++- Separate "good bot qualities" from "profitability requirements".
--+++++- Focus on principles, risks, and evaluation criteria.
--+++++- Mark assumptions as `ASSUMPTION`.
--+++++- Mark questions as `QUESTION`.
--+++++
--+++++Your role:
--+++++
--+++++```text
--+++++[Codex-Architect / Claude / Gemini]
--+++++```
--+++++
--+++++Role focus:
--+++++
--+++++```text
--+++++[Codex-Architect: system qualities, architecture implications, testing, observability, maintainability]
--+++++[Claude: flawed assumptions, human risk, decision boundaries, overconfidence, edge cases]
--+++++[Gemini: alternative bot types, market/data constraints, exchange/integration risks, evaluation methods]
--+++++```
--+++++
--+++++Task:
--+++++1. What makes a crypto trading bot good?
--+++++2. What conditions are required before it can plausibly be profitable?
--+++++3. What risk controls are non-negotiable?
--+++++4. What data, testing, and validation are required?
--+++++5. What common false assumptions should we avoid?
--+++++6. What should be excluded from MVP?
--+++++7. What are the 10 most important questions before designing our bot?
--+++++
--+++++Return format:
--+++++
--+++++```md
--+++++## Role
--+++++
--+++++## Good Bot Qualities
--++++ 
--++++-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--+++++## Profitability Requirements
--+++++
--+++++## Non-Negotiable Risk Controls
--+++++
--+++++## Data, Testing, and Validation
--+++++
--+++++## False Assumptions to Avoid
--+++++
--+++++## Exclude from MVP
--+++++
--+++++## Questions Before Design
--+++++- QUESTION:
--+++++
--+++++## Recommendation
--+++++```
--++++ 
--++++ 
--++++ ```
--++++@@ -872,16 +1769,18 @@ This repo starts with a multi-agent design workflow before implementation.
--++++ 
--++++ The intended loop is:
--++++ 
--++++-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--++++-2. Codex-Arbiter turns the answers into a neutral problem brief.
--++++-3. Round 1: each architect proposes a design from the same brief.
--++++-4. Round 2: agents critique the candidate designs.
--++++-5. Round 3: Codex-Arbiter records the final architecture.
--++++-6. Round 4: Codex implements the accepted plan and runs verification.
--+++++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--+++++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--+++++3. Codex-Arbiter turns the answers into a neutral problem brief.
--+++++4. Round 1: each architect proposes a design from the same brief.
--+++++5. Round 2: agents critique the candidate designs.
--+++++6. Round 3: Codex-Arbiter records the final architecture.
--+++++7. Round 4: Codex implements the accepted plan and runs verification.
--++++ 
--++++ Start here:
--++++ 
--++++ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--+++++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--++++ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--++++ - [Prompt Library](prompts/README.md)
--++++ 
--++++@@ -890,12 +1789,17 @@ Start here:
--++++ Create a context pack for review:
--++++ 
--++++ ```powershell
--++++-python tools/make_context.py --task "Describe the current design question"
--+++++py tools/make_context.py --task "Describe the current design question"
--++++ ```
--++++ 
--++++ The generated file goes to `reviews/latest/context-pack.md`.
--++++ 
--+++++```
--+++++
--+++++### reviews\latest\context-pack.md
--++++ 
--+++++```text
--+++++[Skipped: file is 38144 bytes, above 24000 byte limit]
--++++ ```
--++++ 
--++++ ### tools\make_context.py
--++++
--++++[stderr]
--++++warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
--++++warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF will be replaced by CRLF the next time Git touches it
--++++warning: in the working copy of 'docs/multi-agent-design-workflow/round-0-problem-framing.md', LF will be replaced by CRLF the next time Git touches it
--++++warning: in the working copy of 'prompts/README.md', LF will be replaced by CRLF the next time Git touches it
--+++ ```
--+++ 
--+++ ## File Tree
--+++@@ -30,8 +1311,10 @@ Verify multi-agent design workflow setup
--+++ - docs\multi-agent-design-workflow\agent-protocol.md
--+++ - docs\multi-agent-design-workflow\README.md
--+++ - docs\multi-agent-design-workflow\round-0-problem-framing.md
--++++- docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--+++ - docs\multi-agent-design-workflow\round-template.md
--+++ - prompts\README.md
--++++- prompts\round-minus-1-trading-bot-principles.md
--+++ - prompts\round0-brief-synthesis.md
--+++ - prompts\round0-problem-framing.md
--+++ - prompts\round1-codex-architect.md
--+++@@ -41,6 +1324,7 @@ Verify multi-agent design workflow setup
--+++ - README.md
--+++ - reviews\.gitkeep
--+++ - reviews\latest\.gitkeep
--++++- reviews\latest\context-pack.md
--+++ - tools\make_context.py
--+++ 
--+++ ## Included Files
--+++@@ -178,16 +1462,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--+++ 
--+++ ## Round Sequence
--+++ 
--+++-1. `Round 0 - Problem Framing`
--++++1. `Round -1 - Trading Bot Principles`
--++++   - Define what a good and potentially profitable crypto trading bot requires.
--++++   - Establish safety, validation, and profitability standards before project-specific design.
--++++2. `Round 0 - Problem Framing`
--+++    - Define the actual problem, users, success criteria, constraints, and unknowns.
--+++    - No solution is selected in this round.
--+++-2. `Round 1 - Candidate Designs`
--++++3. `Round 1 - Candidate Designs`
--+++    - Each design agent proposes one or more viable approaches.
--+++-3. `Round 2 - Critique and Risk`
--++++4. `Round 2 - Critique and Risk`
--+++    - Agents critique designs from their role perspective.
--+++-4. `Round 3 - Synthesis`
--++++5. `Round 3 - Synthesis`
--+++    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--+++-5. `Round 4 - Implementation Plan`
--++++6. `Round 4 - Implementation Plan`
--+++    - Convert the selected design into files, tasks, tests, and rollout steps.
--+++ 
--+++ ## Operating Rules
--+++@@ -205,7 +1492,7 @@ The workflow is round-based. Each round produces a short decision record that ca
--+++ 
--+++ ## Current Starting Point
--+++ 
--+++-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--++++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--+++ 
--+++ ```
--+++ 
--+++@@ -232,13 +1519,19 @@ Round 0 does not choose libraries, exchanges, strategies, infrastructure, or imp
--+++   - `Claude`
--+++   - `Gemini`
--+++   - `Codex-Arbiter`
--+++-- The project name suggests a crypto bot, but the exact product scope is not yet defined.
--++++- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
--++++- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
--++++- The first market scope is Binance spot.
--++++- The first assets are `BTC/USDT` and `ETH/USDT`.
--++++- There is no confirmed strategy hypothesis yet.
--++++- The first operator interface should be log files, not a web dashboard.
--++++- The initial risk tolerance was stated as `10-15%`, but the exact meaning still needs clarification.
--+++ 
--+++ ## Working Problem Statement
--+++ 
--+++-ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.
--++++This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.
--+++ 
--+++-The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.
--++++Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.
--+++ 
--+++ ## Round 0 Prompts
--+++ 
--+++@@ -300,15 +1593,15 @@ Assumptions:
--+++ 
--+++ Questions:
--+++ 
--+++-- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
--+++-- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
--+++-- QUESTION: Is the bot allowed to place orders automatically?
--+++-- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
--+++-- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?
--++++- QUESTION: What does the stated `10-15%` risk limit mean: max drawdown, max daily loss, max per-trade loss, max position size, or total capital allocation?
--++++- QUESTION: Should Binance be used only as a historical/live market data source in milestone 1, or should paper trading simulate Binance order rules as closely as possible?
--++++- QUESTION: What timeframe should the first backtests support: 1m, 5m, 15m, 1h, 4h, 1d, or multiple?
--++++- QUESTION: What first class of strategy should the system be able to evaluate: trend-following, mean reversion, breakout, volatility filter, or a plugin-style strategy interface with no built-in claim?
--++++- QUESTION: Should portfolio monitoring read from a real Binance account in read-only mode, or should it start with simulated portfolio state only?
--+++ 
--+++ Recommendation:
--+++ 
--+++-Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.
--++++Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.
--+++ 
--+++ Risks:
--+++ 
--+++@@ -337,6 +1630,7 @@ Questions:
--+++ - QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
--+++ - QUESTION: How should the operator review, override, pause, or audit bot behavior?
--+++ - QUESTION: What is the acceptable balance between speed, safety, and explainability?
--++++- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, or only the framework needed to test manually supplied strategies?
--+++ 
--+++ Recommendation:
--+++ 
--+++@@ -376,6 +1670,8 @@ Questions:
--+++ - QUESTION: Is real money involved in milestone 1?
--+++ - QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
--+++ - QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
--++++- QUESTION: Which Binance data path is acceptable for milestone 1: downloaded historical candles, live WebSocket streams, REST polling, or a combination?
--++++- QUESTION: Does portfolio monitoring require real account balances in read-only mode, or simulated balances from paper trades?
--+++ 
--+++ Recommendation:
--+++ 
--+++@@ -390,12 +1686,14 @@ Risks:
--+++ 
--+++ Canonical problem statement:
--+++ 
--+++-This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.
--++++This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT`. The first milestone should support backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, and reject rather than assuming a profitable strategy already exists.
--+++ 
--+++ In scope for Round 0:
--+++ 
--+++-- Clarifying bot type and first milestone.
--+++-- Identifying risk, safety, and human-control requirements.
--++++- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
--++++- Identifying risk, safety, and human-control requirements for non-live operation.
--++++- Clarifying data source and simulation fidelity requirements for Binance spot.
--++++- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
--+++ - Recording blocking questions and assumptions.
--+++ - Preparing for candidate architecture designs in Round 1.
--+++ 
--+++@@ -405,30 +1703,283 @@ Out of scope for Round 0:
--+++ - Choosing exchange SDKs or trading libraries.
--+++ - Writing trading strategy code.
--+++ - Designing live order execution flows.
--++++- Enabling real-money trading.
--++++- Supporting leverage, futures, margin, or withdrawals.
--+++ 
--+++ Blocking questions:
--+++ 
--+++-- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
--+++-- Will the bot handle real funds or private keys in milestone 1?
--+++-- What user approval or kill-switch controls are required?
--+++-- What exchange, chain, wallet, or market-data source is targeted first?
--+++-- What interface should the operator use first: CLI, web UI, chat, API, or background service only?
--++++- What does `10-15%` mean exactly: max drawdown, max daily loss, max per-trade loss, max position size, or total capital allocation?
--++++- What timeframe(s) should the first backtester support?
--++++- Should paper trading simulate orders from historical candles only, or should it also support live market data dry-run mode?
--++++- Should portfolio monitoring use real Binance read-only account data or simulated paper portfolio state in milestone 1?
--++++- Since there is no strategy hypothesis yet, should Round 1 design include a strategy research workflow, a plugin strategy interface, or one simple baseline strategy purely for testing the framework?
--+++ 
--+++ Non-blocking assumptions:
--+++ 
--+++ - The repo is early enough that workflow docs can define the decision process.
--+++ - The first implementation should be narrow and reversible.
--+++ - Safety and auditability should be treated as first-class design concerns.
--++++- Binance is the initial exchange/data source.
--++++- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
--++++- Spot-only scope excludes leverage, margin, futures, and perpetuals.
--++++- Log files are sufficient for the first operator interface if they are structured and easy to audit.
--+++ 
--+++ Decision:
--+++ 
--+++-Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.
--++++Proceed toward Round 1 only after the remaining blocking questions are answered or explicitly accepted as design assumptions. The likely Round 1 design space is a non-live Binance spot research system with backtesting, paper/dry-run simulation, alert generation, portfolio-state monitoring, structured logs, and strategy hypothesis support.
--+++ 
--+++ Next actions:
--+++ 
--+++-1. User answers the blocking questions.
--+++-2. Codex-Arbiter updates this document with the chosen first milestone.
--+++-3. Round 1 begins with candidate designs constrained to that milestone.
--++++1. User clarifies the remaining blocking questions.
--++++2. Codex-Arbiter converts this Round 0 framing into a neutral problem brief.
--++++3. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
--++++
--++++```
--++++
--++++### docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--++++
--++++```text
--++++# Round -1 - Trading Bot Principles
--++++
--++++Status: `draft`
--++++Date: `2026-05-02`
--++++Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--++++
--++++## Goal of This Round
--++++
--++++Build a shared baseline for the question:
--++++
--++++> What should a good and potentially profitable crypto trading bot have?
--++++
--++++This round happens before project-specific problem framing. The goal is to clarify principles, risks, evaluation standards, and false assumptions before deciding what this repo should build.
--++++
--++++Round -1 does not design this project, choose exchanges, select frameworks, or define a specific trading strategy.
--++++
--++++## Ground Rules
--++++
--++++- Do not claim guaranteed profit.
--++++- Separate "good bot qualities" from "profitability requirements".
--++++- Treat risk controls, auditability, and validation as first-class concerns.
--++++- Assume backtest results can be misleading until proven otherwise.
--++++- Do not recommend live trading before paper trading and risk boundaries are defined.
--++++- Mark assumptions as `ASSUMPTION`.
--++++- Mark questions as `QUESTION`.
--++++
--++++## Shared Question
--++++
--++++What should a good and potentially profitable crypto trading bot have?
--++++
--++++## Agent Focus
--++++
--++++### Codex-Architect
--++++
--++++Focus on:
--++++
--++++- System qualities.
--++++- Architecture implications.
--++++- Testing and verification.
--++++- Observability and audit logs.
--++++- Maintainability and safe iteration.
--++++
--++++### Claude
--++++
--++++Focus on:
--++++
--++++- Flawed assumptions.
--++++- Human risk and overconfidence.
--++++- Decision boundaries.
--++++- Edge cases and failure modes.
--++++- What should remain human-approved.
--++++
--++++### Gemini
--++++
--++++Focus on:
--++++
--++++- Alternative bot types.
--++++- Market and data constraints.
--++++- Exchange and integration risks.
--++++- Evaluation methods.
--++++- External constraints that could dominate design.
--++++
--++++## Questions for Agents
--++++
--++++Each agent should answer:
--++++
--++++1. What makes a crypto trading bot good?
--++++2. What conditions are required before it can plausibly be profitable?
--++++3. What risk controls are non-negotiable?
--++++4. What data, testing, and validation are required?
--++++5. What common false assumptions should we avoid?
--++++6. What should be excluded from MVP?
--++++7. What are the 10 most important questions before designing our bot?
--++++
--++++## Initial Shared Baseline
--++++
--++++Good bot qualities:
--++++
--++++- Clear operating mode: alerts, research, backtesting, paper trading, or live execution.
--++++- Separation between market data, strategy logic, risk controls, execution, state, and reporting.
--++++- Full audit trail for inputs, decisions, orders, errors, overrides, and configuration changes.
--++++- Deterministic replay/debug mode for understanding past decisions.
--++++- Operator controls for pause, kill switch, configuration review, and emergency shutdown.
--++++- Safe secret handling if exchange API keys or wallet credentials ever become involved.
--++++- Tests for strategy logic, risk logic, execution adapters, and failure handling.
--++++
--++++Profitability requirements:
--++++
--++++- A testable hypothesis for why the strategy should have edge.
--++++- Historical validation without look-ahead bias, survivorship bias, or data leakage.
--++++- Evaluation after fees, spread, slippage, funding rates, latency, and failed orders.
--++++- Out-of-sample testing or walk-forward validation.
--++++- Paper trading before live trading.
--++++- Position sizing and drawdown controls.
--++++- Monitoring for market regime changes.
--++++
--++++Non-negotiable risk controls:
--++++
--++++- Max position size.
--++++- Max daily loss.
--++++- Max drawdown.
--++++- Per-trade risk limit.
--++++- Exchange/API failure handling.
--++++- Duplicate order protection.
--++++- Kill switch.
--++++- Dry-run or paper mode.
--++++- Read-only mode for analysis features.
--++++- Human approval mode before live automation.
--++++
--++++Common false assumptions:
--++++
--++++- Backtest profit means future profit.
--++++- High win rate means good strategy.
--++++- AI can reliably predict sudden market moves.
--++++- More indicators mean better signals.
--++++- Live trading is just backtesting with real orders.
--++++- Exchange APIs behave reliably during volatility.
--++++- Fees and slippage are small enough to ignore.
--++++- A bot should trade often to be useful.
--++++
--++++## Codex-Arbiter Synthesis Template
--++++
--++++After the three agents answer, produce:
--++++
--++++1. Shared principles accepted by all agents.
--++++2. Disagreements or tensions worth preserving.
--++++3. Non-negotiable safety requirements.
--++++4. Evaluation standards for profitability claims.
--++++5. MVP exclusions.
--++++6. Questions that should flow into Round 0.
--++++
--++++## Agent Answer Summary
--++++
--++++### Codex-Architect
--++++
--++++Codex-Architect framed a good bot as a controlled, observable, testable decision and execution system. The strongest points were separation of strategy, execution, risk, data, configuration, and monitoring; deterministic testing; fail-safe behavior; idempotent execution; strong state reconciliation; and explicit modes for backtest, paper, shadow, and live trading.
--++++
--++++Codex-Architect emphasized that profitability requires a real market edge after fees, spread, slippage, latency, funding, failed orders, and regime changes. It also stressed that the bot should support strategy retirement when live performance diverges from expectations.
--++++
--++++### Claude
--++++
--++++Claude focused on adversarial clarity and warned that the most common failure is starting implementation before the strategy hypothesis is honest. The strongest points were that profitability belongs to the strategy, market, cost structure, execution quality, and timing together, not to the bot by itself.
--++++
--++++Claude emphasized falsifiable strategy hypotheses, out-of-sample validation, hard drawdown circuit breakers, UTC/time discipline, human restart after major risk events, and predefined failure conditions for stopping the project or strategy.
--++++
--++++### Gemini
--++++
--++++Gemini emphasized alternative bot types, market/data constraints, and execution realities. The strongest points were operational resilience, telemetry, exchange integration risk, low-latency path where relevant, high-fidelity data handling, inventory management for market making or arbitrage, and the need to define the intended market regime.
--++++
--++++Gemini also highlighted tick-to-trade latency, partial fills, orphan orders, WebSocket/REST divergence, maker/taker fee assumptions, fat-tail events, and kill-switch authority.
--++++
--++++## Codex-Arbiter Synthesis
--++++
--++++### Shared Principles Accepted by All Agents
--++++
--++++- A good crypto trading bot is first a safety-critical automation system, not a profit machine.
--++++- Strategy logic, risk controls, exchange execution, data ingestion, state management, configuration, monitoring, and reporting should be separated.
--++++- Every trade decision must be auditable after the fact from logs and stored state.
--++++- The bot must fail safely when data, connectivity, exchange APIs, or internal state become unreliable.
--++++- Backtest profitability is not sufficient evidence of live profitability.
--++++- Profitability claims must include fees, spread, slippage, latency, partial fills, failed orders, funding or borrow costs where relevant, and market regime effects.
--++++- Paper trading is necessary before live trading, but paper trading is still not proof of live profitability.
--++++- Risk controls belong in the MVP, not after the MVP.
--++++- The first version should be narrow, explainable, and easy to shut down.
--++++
--++++### Disagreements or Tensions Worth Preserving
--++++
--++++- Claude recommends excluding dashboard and alerting from MVP, while Codex-Architect treats observability from day one as essential. The synthesis is: avoid a complex UI dashboard, but keep operational logs, basic metrics, and alerts for dangerous states.
--++++- Gemini mentions a low-latency path, while Claude warns latency must match the strategy horizon. The synthesis is: do not optimize for low latency generally; define latency requirements only after the strategy type and timeframe are chosen.
--++++- Claude prefers no auto-restart on crash, while production systems often need recovery behavior. The synthesis is: allow process restart only into a safe paused/reconcile mode, not automatic trading resumption.
--++++- Codex-Architect assumes the bot may eventually trade real capital. Round 0 must confirm whether real funds are in scope for milestone 1.
--++++
--++++### Non-Negotiable Safety Requirements
--++++
--++++- Read-only, paper, and live modes must be explicit and hard to confuse.
--++++- No withdrawal permissions for any exchange API key used by the bot.
--++++- Kill switch must cancel open orders where possible and disable new trading.
--++++- The bot must reconcile exchange/account state before trading on startup, reconnect, or restart.
--++++- Duplicate order protection is required.
--++++- Hard maximums are required for order size, position size, portfolio exposure, daily loss, drawdown, open orders, and order rate.
--++++- The bot must halt or enter safe mode on stale data, repeated exchange errors, abnormal slippage, rejected orders, reconciliation mismatch, or connectivity loss.
--++++- Human approval should be required before live automation and before scaling capital.
--++++- All timestamps should be consistent and timezone-aware, preferably UTC internally.
--++++- Every signal, order intent, order response, fill, cancellation, error, override, and configuration change must be logged.
--++++
--++++### Evaluation Standards for Profitability Claims
--++++
--++++- The strategy must have a falsifiable hypothesis explaining why an edge should exist.
--++++- Backtests must avoid look-ahead bias, data leakage, and excessive parameter fitting.
--++++- Validation must include out-of-sample data or walk-forward testing.
--++++- Evaluation must include multiple market regimes where possible.
--++++- Results must be measured after fees, spread, slippage, latency, partial fills, failed orders, and funding or borrow costs where relevant.
--++++- Metrics should include total return, profit factor, Sharpe or Sortino, max drawdown, drawdown duration, win/loss distribution, tail losses, turnover, exposure, and sensitivity to parameters.
--++++- Paper trading must compare expected fills against simulated or actual paper fills.
--++++- Live trading, if ever allowed, should start with minimal capital and require evidence that live behavior matches expected behavior.
--++++- A strategy must have predefined retirement or pause criteria when live performance diverges from expectations.
--++++
--++++### MVP Exclusions
--++++
--++++- Leverage, margin, perpetuals, and futures unless explicitly chosen later with separate risk design.
--++++- Multiple exchanges.
--++++- Multiple unrelated strategies.
--++++- Cross-exchange arbitrage.
--++++- High-frequency trading.
--++++- Complex machine learning or automatic strategy discovery.
--++++- Auto-optimization against recent backtests.
--++++- Social/news sentiment trading.
--++++- Copy trading.
--++++- Withdrawal automation.
--++++- Fully autonomous capital scaling.
--++++- Complex UI dashboards beyond minimal operational visibility.
--++++- Any feature that makes trades harder to explain.
--++++
--++++### Questions That Flow Into Round 0
--++++
--++++- QUESTION: What specific bot type is milestone 1: alerting, research, backtesting, paper trading, live spot trading, market making, arbitrage, portfolio tracking, or something else?
--++++- QUESTION: What falsifiable market hypothesis do we want to test first?
--++++- QUESTION: What market regime is the first strategy intended for?
--++++- QUESTION: What trading horizon is targeted: seconds, minutes, hours, days, or longer?
--++++- QUESTION: Which asset universe is allowed for milestone 1?
--++++- QUESTION: Which exchange or data source is targeted first?
--++++- QUESTION: Will milestone 1 involve real funds, or only read-only/paper mode?
--++++- QUESTION: What maximum loss or drawdown is acceptable before the bot must halt?
--++++- QUESTION: What evidence is required before moving from backtest to paper, and from paper to live?
--++++- QUESTION: Who can trigger the kill switch, and what should the recovery protocol be?
--++++- QUESTION: What interface should the operator use first: CLI, logs, simple dashboard, API, or chat?
--++++- QUESTION: What monitoring is mandatory from day one?
--++++- QUESTION: What is the minimum acceptable audit trail for every decision?
--++++
--++++## Decision
--++++
--++++Round -1 establishes the baseline: this project should not frame the first milestone as "build a profitable bot." It should frame the first milestone as "build a narrow, safe, auditable system for testing one falsifiable trading hypothesis under realistic costs and failure conditions."
--++++
--++++Proceed to Round 0 only after the user chooses the first milestone and answers the blocking questions about bot type, automation level, target market, target data source/exchange, allowed risk, and operator controls.
--++++
--++++## Next Actions
--++++
--++++1. Use this synthesis as input to Round 0 problem framing.
--++++2. User answers the Round 0 blocking questions, especially bot type and whether real funds are in scope.
--++++3. Codex-Arbiter updates `round-0-problem-framing.md` with the chosen first milestone.
--++++4. Round 1 begins only after the problem brief is narrow enough for candidate architectures.
--+++ 
--+++ ```
--+++ 
--+++@@ -490,14 +2041,85 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--+++ 
--+++ Recommended order:
--+++ 
--+++-1. `round0-problem-framing.md`
--+++-2. `round0-brief-synthesis.md`
--+++-3. `round1-codex-architect.md`
--+++-4. `round1-external-architect.md`
--+++-5. `round2-cross-review.md`
--+++-6. `round3-arbiter.md`
--++++1. `round-minus-1-trading-bot-principles.md`
--++++2. `round0-problem-framing.md`
--++++3. `round0-brief-synthesis.md`
--++++4. `round1-codex-architect.md`
--++++5. `round1-external-architect.md`
--++++6. `round2-cross-review.md`
--++++7. `round3-arbiter.md`
--++++
--++++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--++++
--++++```
--++++
--++++### prompts\round-minus-1-trading-bot-principles.md
--++++
--++++```text
--++++# Round -1 - Trading Bot Principles
--++++
--++++You are participating in a multi-agent software design workflow.
--++++
--++++Round:
--++++Round -1 - Trading Bot Principles
--++++
--++++Question:
--++++"What should a good and potentially profitable crypto trading bot have?"
--++++
--++++Rules:
--++++- Do not design this specific project yet.
--++++- Do not choose frameworks, exchanges, or libraries.
--++++- Do not claim guaranteed profits.
--++++- Separate "good bot qualities" from "profitability requirements".
--++++- Focus on principles, risks, and evaluation criteria.
--++++- Mark assumptions as `ASSUMPTION`.
--++++- Mark questions as `QUESTION`.
--++++
--++++Your role:
--++++
--++++```text
--++++[Codex-Architect / Claude / Gemini]
--++++```
--++++
--++++Role focus:
--++++
--++++```text
--++++[Codex-Architect: system qualities, architecture implications, testing, observability, maintainability]
--++++[Claude: flawed assumptions, human risk, decision boundaries, overconfidence, edge cases]
--++++[Gemini: alternative bot types, market/data constraints, exchange/integration risks, evaluation methods]
--++++```
--++++
--++++Task:
--++++1. What makes a crypto trading bot good?
--++++2. What conditions are required before it can plausibly be profitable?
--++++3. What risk controls are non-negotiable?
--++++4. What data, testing, and validation are required?
--++++5. What common false assumptions should we avoid?
--++++6. What should be excluded from MVP?
--++++7. What are the 10 most important questions before designing our bot?
--++++
--++++Return format:
--++++
--++++```md
--++++## Role
--++++
--++++## Good Bot Qualities
--+++ 
--+++-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--++++## Profitability Requirements
--++++
--++++## Non-Negotiable Risk Controls
--++++
--++++## Data, Testing, and Validation
--++++
--++++## False Assumptions to Avoid
--++++
--++++## Exclude from MVP
--++++
--++++## Questions Before Design
--++++- QUESTION:
--++++
--++++## Recommendation
--++++```
--+++ 
--+++ 
--+++ ```
--+++@@ -872,16 +2494,18 @@ This repo starts with a multi-agent design workflow before implementation.
--+++ 
--+++ The intended loop is:
--+++ 
--+++-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--+++-2. Codex-Arbiter turns the answers into a neutral problem brief.
--+++-3. Round 1: each architect proposes a design from the same brief.
--+++-4. Round 2: agents critique the candidate designs.
--+++-5. Round 3: Codex-Arbiter records the final architecture.
--+++-6. Round 4: Codex implements the accepted plan and runs verification.
--++++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--++++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--++++3. Codex-Arbiter turns the answers into a neutral problem brief.
--++++4. Round 1: each architect proposes a design from the same brief.
--++++5. Round 2: agents critique the candidate designs.
--++++6. Round 3: Codex-Arbiter records the final architecture.
--++++7. Round 4: Codex implements the accepted plan and runs verification.
--+++ 
--+++ Start here:
--+++ 
--+++ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--++++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--+++ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--+++ - [Prompt Library](prompts/README.md)
--+++ 
--+++@@ -890,12 +2514,17 @@ Start here:
--+++ Create a context pack for review:
--+++ 
--+++ ```powershell
--+++-python tools/make_context.py --task "Describe the current design question"
--++++py tools/make_context.py --task "Describe the current design question"
--+++ ```
--+++ 
--+++ The generated file goes to `reviews/latest/context-pack.md`.
--+++ 
--++++```
--++++
--++++### reviews\latest\context-pack.md
--+++ 
--++++```text
--++++[Skipped: file is 63523 bytes, above 24000 byte limit]
--+++ ```
--+++ 
--+++ ### tools\make_context.py
--+++
--+++[stderr]
--+++warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
--+++warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF will be replaced by CRLF the next time Git touches it
--+++warning: in the working copy of 'docs/multi-agent-design-workflow/round-0-problem-framing.md', LF will be replaced by CRLF the next time Git touches it
--+++warning: in the working copy of 'prompts/README.md', LF will be replaced by CRLF the next time Git touches it
--++ ```
--++ 
--++ ## File Tree
--++ 
--++ - .env.example
--+++- docs\multi-agent-design-workflow\00-problem-brief.md
--++ - docs\multi-agent-design-workflow\agent-protocol.md
--++ - docs\multi-agent-design-workflow\README.md
--++ - docs\multi-agent-design-workflow\round-0-problem-framing.md
--+++- docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--++ - docs\multi-agent-design-workflow\round-template.md
--++ - prompts\README.md
--+++- prompts\round-minus-1-trading-bot-principles.md
--++ - prompts\round0-brief-synthesis.md
--++ - prompts\round0-problem-framing.md
--++ - prompts\round1-codex-architect.md
--++@@ -41,6 +2160,7 @@ Verify multi-agent design workflow setup
--++ - README.md
--++ - reviews\.gitkeep
--++ - reviews\latest\.gitkeep
--+++- reviews\latest\context-pack.md
--++ - tools\make_context.py
--++ 
--++ ## Included Files
--++@@ -56,6 +2176,114 @@ GEMINI_API_KEY=
--++ OPENAI_API_KEY=
--++ 
--++ 
--+++```
--+++
--+++### docs\multi-agent-design-workflow\00-problem-brief.md
--+++
--+++```text
--+++# Problem Brief
--+++
--+++Status: `draft`
--+++Date: `2026-05-02`
--+++Source: Round -1 and Round 0 synthesis
--+++
--+++## Goal
--+++
--+++Build a safety-first crypto research and paper-readiness system for Binance spot markets. The system should help define, test, compare, monitor, and reject trading strategy hypotheses before any real-money trading is considered.
--+++
--+++The project should not begin as "build a profitable bot." It should begin as "build a narrow, auditable research and simulation system that can test whether any proposed strategy deserves further attention."
--+++
--+++## Target Users
--+++
--+++- Primary operator: the repo owner.
--+++- Secondary future user: a technical operator who can read logs, review backtests, inspect assumptions, and decide whether a strategy is worth paper or live testing.
--+++
--+++ASSUMPTION: This is a private or small-team tool, not a public SaaS product.
--+++
--+++## Confirmed Scope
--+++
--+++- Exchange/data source: Binance.
--+++- Market type: spot only.
--+++- Assets: `BTC/USDT`, `ETH/USDT`.
--+++- First timeframe: `1h`.
--+++- First interface: structured log files.
--+++- Real funds: out of scope for milestone 1.
--+++- Withdrawal permissions: out of scope.
--+++- Margin, futures, perpetuals, and leverage: out of scope.
--+++- Risk boundary: maximum drawdown target/limit of `10-20%` for evaluation and future controls.
--+++
--+++## Milestone 1
--+++
--+++Milestone 1 should include:
--+++
--+++- Historical backtesting for Binance spot `BTC/USDT` and `ETH/USDT` on `1h` candles.
--+++- A strategy plugin interface so candidate strategies can be added without changing the core engine.
--+++- A strategy research workflow that helps compare candidate strategies and reject weak ones.
--+++- Alert generation from strategy signals or monitoring rules.
--+++- Portfolio-state monitoring, initially without live trading.
--+++- Structured logs for auditability and debugging.
--+++- Paper trading or live market dry-run planning, with sequencing debated by the architects.
--+++
--+++## Non-Goals
--+++
--+++- Live order placement.
--+++- Using real funds.
--+++- Multiple exchanges.
--+++- High-frequency trading.
--+++- Cross-exchange arbitrage.
--+++- Leverage, margin, futures, or perpetual trading.
--+++- Complex machine learning models.
--+++- Automatic strategy discovery that optimizes against recent backtests.
--+++- Full web dashboard.
--+++- Tax reporting.
--+++- Copy trading or social/news sentiment trading.
--+++
--+++## Core Workflows
--+++
--+++1. The operator defines or installs a strategy candidate.
--+++2. The system loads historical Binance spot candle data.
--+++3. The system runs a backtest with explicit fees and realistic assumptions.
--+++4. The system records signals, simulated orders, portfolio state, drawdown, and metrics.
--+++5. The system compares strategy results without assuming that the best backtest is a real edge.
--+++6. The system emits structured logs and alerts.
--+++7. The operator reviews whether a strategy should be rejected, revised, paper-tested, or monitored further.
--+++
--+++## Safety and Evaluation Principles
--+++
--+++- Every strategy must have an explicit hypothesis.
--+++- Backtest results must be treated as evidence, not proof.
--+++- Results should include fees, spread/slippage assumptions, drawdown, trade distribution, and sensitivity where practical.
--+++- The system should make weak strategies easy to reject.
--+++- The system should avoid overfitting incentives.
--+++- Paper/live dry-run should not be treated as equivalent to live profitability.
--+++- Any future live mode must require separate design, approval, and risk controls.
--+++
--+++## Open Design Questions for Round 1
--+++
--+++- QUESTION: Should live market dry-run be included in milestone 1, or sequenced after historical backtesting is reliable?
--+++- QUESTION: Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state?
--+++- QUESTION: Should the first architecture prioritize a strategy plugin interface, a strategy research workflow, or both?
--+++- QUESTION: If both plugin interface and research workflow are included, how should the system prevent strategy overfitting and false confidence?
--+++- QUESTION: What baseline strategy, if any, should be included only to validate framework behavior?
--+++- QUESTION: How much Binance order-rule simulation is necessary before live market dry-run?
--+++- QUESTION: What metrics are required in milestone 1 versus later?
--+++
--+++## Architecture Constraints
--+++
--+++- The first architecture should keep live trading out of the system boundary.
--+++- The strategy interface should be testable without Binance credentials.
--+++- Binance credentials, if added later for read-only monitoring, must be optional and restricted.
--+++- Logs must be structured enough to reconstruct decisions.
--+++- Strategy code must be separated from core data loading, simulation, portfolio accounting, and reporting.
--+++- The system should support future paper/live dry-run without forcing that complexity into the first backtester.
--+++
--+++## Decision
--+++
--+++Proceed to Round 1 candidate architecture proposals.
--+++
--+++Round 1 architects should explicitly debate the open design questions rather than assuming a single answer.
--+++
--+++
--++ ```
--++ 
--++ ### docs\multi-agent-design-workflow\agent-protocol.md
--++@@ -178,16 +2406,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--++ 
--++ ## Round Sequence
--++ 
--++-1. `Round 0 - Problem Framing`
--+++1. `Round -1 - Trading Bot Principles`
--+++   - Define what a good and potentially profitable crypto trading bot requires.
--+++   - Establish safety, validation, and profitability standards before project-specific design.
--+++2. `Round 0 - Problem Framing`
--++    - Define the actual problem, users, success criteria, constraints, and unknowns.
--++    - No solution is selected in this round.
--++-2. `Round 1 - Candidate Designs`
--+++3. `Round 1 - Candidate Designs`
--++    - Each design agent proposes one or more viable approaches.
--++-3. `Round 2 - Critique and Risk`
--+++4. `Round 2 - Critique and Risk`
--++    - Agents critique designs from their role perspective.
--++-4. `Round 3 - Synthesis`
--+++5. `Round 3 - Synthesis`
--++    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--++-5. `Round 4 - Implementation Plan`
--+++6. `Round 4 - Implementation Plan`
--++    - Convert the selected design into files, tasks, tests, and rollout steps.
--++ 
--++ ## Operating Rules
--++@@ -205,7 +2436,7 @@ The workflow is round-based. Each round produces a short decision record that ca
--++ 
--++ ## Current Starting Point
--++ 
--++-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--+++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--++ 
--++ ```
--++ 
--++@@ -232,13 +2463,23 @@ Round 0 does not choose libraries, exchanges, strategies, infrastructure, or imp
--++   - `Claude`
--++   - `Gemini`
--++   - `Codex-Arbiter`
--++-- The project name suggests a crypto bot, but the exact product scope is not yet defined.
--+++- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
--+++- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
--+++- The first market scope is Binance spot.
--+++- The first assets are `BTC/USDT` and `ETH/USDT`.
--+++- There is no confirmed strategy hypothesis yet.
--+++- The first operator interface should be log files, not a web dashboard.
--+++- The initial risk tolerance is maximum drawdown of `10-20%`.
--+++- The initial backtest timeframe should be `1h`.
--+++- The user is interested in both historical backtesting and live market dry-run, but is open to sequencing historical data first and live dry-run later.
--+++- If live market dry-run is included, Binance read-only account support may be useful, but this is not confirmed.
--+++- The user is interested in both a strategy plugin interface and a strategy research workflow.
--++ 
--++ ## Working Problem Statement
--++ 
--++-ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.
--+++This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.
--++ 
--++-The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.
--+++Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.
--++ 
--++ ## Round 0 Prompts
--++ 
--++@@ -300,15 +2541,15 @@ Assumptions:
--++ 
--++ Questions:
--++ 
--++-- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
--++-- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
--++-- QUESTION: Is the bot allowed to place orders automatically?
--++-- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
--++-- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?
--+++- QUESTION: Should milestone 1 include both historical backtesting and live market dry-run, or should live dry-run wait until historical simulation is trustworthy?
--+++- QUESTION: Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state only?
--+++- QUESTION: Should the first architecture prioritize a strategy plugin interface, a strategy research workflow, or a parallel strategy-monitoring system?
--+++- QUESTION: How should the system help discover or compare strategies when no hypothesis is confirmed yet?
--+++- QUESTION: What first class of strategy should be used only as a baseline to test the framework, without implying it is profitable?
--++ 
--++ Recommendation:
--++ 
--++-Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.
--+++Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.
--++ 
--++ Risks:
--++ 
--++@@ -337,6 +2578,8 @@ Questions:
--++ - QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
--++ - QUESTION: How should the operator review, override, pause, or audit bot behavior?
--++ - QUESTION: What is the acceptable balance between speed, safety, and explainability?
--+++- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, a plugin interface for manually supplied strategies, or both?
--+++- QUESTION: If multiple strategies are evaluated in parallel, how should the operator avoid overfitting and false confidence?
--++ 
--++ Recommendation:
--++ 
--++@@ -376,6 +2619,8 @@ Questions:
--++ - QUESTION: Is real money involved in milestone 1?
--++ - QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
--++ - QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
--+++- QUESTION: Should the first design sequence be historical candles first, then live WebSocket dry-run, then read-only portfolio monitoring?
--+++- QUESTION: Does Binance read-only monitoring materially improve milestone 1, or does it add unnecessary security and setup complexity?
--++ 
--++ Recommendation:
--++ 
--++@@ -390,12 +2635,14 @@ Risks:
--++ 
--++ Canonical problem statement:
--++ 
--++-This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.
--+++This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`. The first milestone should support historical backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Live market dry-run and Binance read-only account monitoring are desirable but should be debated for sequencing and complexity. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, monitor, and reject rather than assuming a profitable strategy already exists.
--++ 
--++ In scope for Round 0:
--++ 
--++-- Clarifying bot type and first milestone.
--++-- Identifying risk, safety, and human-control requirements.
--+++- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
--+++- Identifying risk, safety, and human-control requirements for non-live operation.
--+++- Clarifying data source and simulation fidelity requirements for Binance spot.
--+++- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
--++ - Recording blocking questions and assumptions.
--++ - Preparing for candidate architecture designs in Round 1.
--++ 
--++@@ -405,30 +2652,285 @@ Out of scope for Round 0:
--++ - Choosing exchange SDKs or trading libraries.
--++ - Writing trading strategy code.
--++ - Designing live order execution flows.
--+++- Enabling real-money trading.
--+++- Supporting leverage, futures, margin, or withdrawals.
--++ 
--++ Blocking questions:
--++ 
--++-- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
--++-- Will the bot handle real funds or private keys in milestone 1?
--++-- What user approval or kill-switch controls are required?
--++-- What exchange, chain, wallet, or market-data source is targeted first?
--++-- What interface should the operator use first: CLI, web UI, chat, API, or background service only?
--+++- Should live market dry-run be included in milestone 1, or sequenced after historical backtesting is reliable?
--+++- Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state?
--+++- Should Round 1 design prioritize a strategy plugin interface, a strategy research workflow, or both?
--+++- If both plugin interface and research workflow are included, how should the system prevent strategy overfitting and false confidence?
--+++- What baseline strategy, if any, should be included only to validate framework behavior?
--++ 
--++ Non-blocking assumptions:
--++ 
--++ - The repo is early enough that workflow docs can define the decision process.
--++ - The first implementation should be narrow and reversible.
--++ - Safety and auditability should be treated as first-class design concerns.
--+++- Binance is the initial exchange/data source.
--+++- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
--+++- Spot-only scope excludes leverage, margin, futures, and perpetuals.
--+++- Log files are sufficient for the first operator interface if they are structured and easy to audit.
--+++- Maximum drawdown of `10-20%` is a project-level risk boundary for evaluation and future paper/live controls.
--+++- The first timeframe is `1h`.
--++ 
--++ Decision:
--++ 
--++-Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.
--+++Proceed toward Round 1 with the unresolved points treated as explicit design questions for the architects to debate. The Round 1 design space is a non-live Binance spot research system with `1h` backtesting, paper/dry-run simulation planning, alert generation, portfolio-state monitoring, structured logs, strategy plugin support, and strategy research workflow support.
--++ 
--++ Next actions:
--++ 
--++-1. User answers the blocking questions.
--++-2. Codex-Arbiter updates this document with the chosen first milestone.
--++-3. Round 1 begins with candidate designs constrained to that milestone.
--+++1. User clarifies the remaining blocking questions.
--+++2. Codex-Arbiter converts this Round 0 framing into a neutral problem brief.
--+++3. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
--+++
--+++```
--+++
--+++### docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--+++
--+++```text
--+++# Round -1 - Trading Bot Principles
--+++
--+++Status: `draft`
--+++Date: `2026-05-02`
--+++Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--+++
--+++## Goal of This Round
--+++
--+++Build a shared baseline for the question:
--+++
--+++> What should a good and potentially profitable crypto trading bot have?
--+++
--+++This round happens before project-specific problem framing. The goal is to clarify principles, risks, evaluation standards, and false assumptions before deciding what this repo should build.
--+++
--+++Round -1 does not design this project, choose exchanges, select frameworks, or define a specific trading strategy.
--+++
--+++## Ground Rules
--+++
--+++- Do not claim guaranteed profit.
--+++- Separate "good bot qualities" from "profitability requirements".
--+++- Treat risk controls, auditability, and validation as first-class concerns.
--+++- Assume backtest results can be misleading until proven otherwise.
--+++- Do not recommend live trading before paper trading and risk boundaries are defined.
--+++- Mark assumptions as `ASSUMPTION`.
--+++- Mark questions as `QUESTION`.
--+++
--+++## Shared Question
--+++
--+++What should a good and potentially profitable crypto trading bot have?
--+++
--+++## Agent Focus
--+++
--+++### Codex-Architect
--+++
--+++Focus on:
--+++
--+++- System qualities.
--+++- Architecture implications.
--+++- Testing and verification.
--+++- Observability and audit logs.
--+++- Maintainability and safe iteration.
--+++
--+++### Claude
--+++
--+++Focus on:
--+++
--+++- Flawed assumptions.
--+++- Human risk and overconfidence.
--+++- Decision boundaries.
--+++- Edge cases and failure modes.
--+++- What should remain human-approved.
--+++
--+++### Gemini
--+++
--+++Focus on:
--+++
--+++- Alternative bot types.
--+++- Market and data constraints.
--+++- Exchange and integration risks.
--+++- Evaluation methods.
--+++- External constraints that could dominate design.
--+++
--+++## Questions for Agents
--+++
--+++Each agent should answer:
--+++
--+++1. What makes a crypto trading bot good?
--+++2. What conditions are required before it can plausibly be profitable?
--+++3. What risk controls are non-negotiable?
--+++4. What data, testing, and validation are required?
--+++5. What common false assumptions should we avoid?
--+++6. What should be excluded from MVP?
--+++7. What are the 10 most important questions before designing our bot?
--+++
--+++## Initial Shared Baseline
--+++
--+++Good bot qualities:
--+++
--+++- Clear operating mode: alerts, research, backtesting, paper trading, or live execution.
--+++- Separation between market data, strategy logic, risk controls, execution, state, and reporting.
--+++- Full audit trail for inputs, decisions, orders, errors, overrides, and configuration changes.
--+++- Deterministic replay/debug mode for understanding past decisions.
--+++- Operator controls for pause, kill switch, configuration review, and emergency shutdown.
--+++- Safe secret handling if exchange API keys or wallet credentials ever become involved.
--+++- Tests for strategy logic, risk logic, execution adapters, and failure handling.
--+++
--+++Profitability requirements:
--+++
--+++- A testable hypothesis for why the strategy should have edge.
--+++- Historical validation without look-ahead bias, survivorship bias, or data leakage.
--+++- Evaluation after fees, spread, slippage, funding rates, latency, and failed orders.
--+++- Out-of-sample testing or walk-forward validation.
--+++- Paper trading before live trading.
--+++- Position sizing and drawdown controls.
--+++- Monitoring for market regime changes.
--+++
--+++Non-negotiable risk controls:
--+++
--+++- Max position size.
--+++- Max daily loss.
--+++- Max drawdown.
--+++- Per-trade risk limit.
--+++- Exchange/API failure handling.
--+++- Duplicate order protection.
--+++- Kill switch.
--+++- Dry-run or paper mode.
--+++- Read-only mode for analysis features.
--+++- Human approval mode before live automation.
--+++
--+++Common false assumptions:
--+++
--+++- Backtest profit means future profit.
--+++- High win rate means good strategy.
--+++- AI can reliably predict sudden market moves.
--+++- More indicators mean better signals.
--+++- Live trading is just backtesting with real orders.
--+++- Exchange APIs behave reliably during volatility.
--+++- Fees and slippage are small enough to ignore.
--+++- A bot should trade often to be useful.
--+++
--+++## Codex-Arbiter Synthesis Template
--+++
--+++After the three agents answer, produce:
--+++
--+++1. Shared principles accepted by all agents.
--+++2. Disagreements or tensions worth preserving.
--+++3. Non-negotiable safety requirements.
--+++4. Evaluation standards for profitability claims.
--+++5. MVP exclusions.
--+++6. Questions that should flow into Round 0.
--+++
--+++## Agent Answer Summary
--+++
--+++### Codex-Architect
--+++
--+++Codex-Architect framed a good bot as a controlled, observable, testable decision and execution system. The strongest points were separation of strategy, execution, risk, data, configuration, and monitoring; deterministic testing; fail-safe behavior; idempotent execution; strong state reconciliation; and explicit modes for backtest, paper, shadow, and live trading.
--+++
--+++Codex-Architect emphasized that profitability requires a real market edge after fees, spread, slippage, latency, funding, failed orders, and regime changes. It also stressed that the bot should support strategy retirement when live performance diverges from expectations.
--+++
--+++### Claude
--+++
--+++Claude focused on adversarial clarity and warned that the most common failure is starting implementation before the strategy hypothesis is honest. The strongest points were that profitability belongs to the strategy, market, cost structure, execution quality, and timing together, not to the bot by itself.
--+++
--+++Claude emphasized falsifiable strategy hypotheses, out-of-sample validation, hard drawdown circuit breakers, UTC/time discipline, human restart after major risk events, and predefined failure conditions for stopping the project or strategy.
--+++
--+++### Gemini
--+++
--+++Gemini emphasized alternative bot types, market/data constraints, and execution realities. The strongest points were operational resilience, telemetry, exchange integration risk, low-latency path where relevant, high-fidelity data handling, inventory management for market making or arbitrage, and the need to define the intended market regime.
--+++
--+++Gemini also highlighted tick-to-trade latency, partial fills, orphan orders, WebSocket/REST divergence, maker/taker fee assumptions, fat-tail events, and kill-switch authority.
--+++
--+++## Codex-Arbiter Synthesis
--+++
--+++### Shared Principles Accepted by All Agents
--+++
--+++- A good crypto trading bot is first a safety-critical automation system, not a profit machine.
--+++- Strategy logic, risk controls, exchange execution, data ingestion, state management, configuration, monitoring, and reporting should be separated.
--+++- Every trade decision must be auditable after the fact from logs and stored state.
--+++- The bot must fail safely when data, connectivity, exchange APIs, or internal state become unreliable.
--+++- Backtest profitability is not sufficient evidence of live profitability.
--+++- Profitability claims must include fees, spread, slippage, latency, partial fills, failed orders, funding or borrow costs where relevant, and market regime effects.
--+++- Paper trading is necessary before live trading, but paper trading is still not proof of live profitability.
--+++- Risk controls belong in the MVP, not after the MVP.
--+++- The first version should be narrow, explainable, and easy to shut down.
--+++
--+++### Disagreements or Tensions Worth Preserving
--+++
--+++- Claude recommends excluding dashboard and alerting from MVP, while Codex-Architect treats observability from day one as essential. The synthesis is: avoid a complex UI dashboard, but keep operational logs, basic metrics, and alerts for dangerous states.
--+++- Gemini mentions a low-latency path, while Claude warns latency must match the strategy horizon. The synthesis is: do not optimize for low latency generally; define latency requirements only after the strategy type and timeframe are chosen.
--+++- Claude prefers no auto-restart on crash, while production systems often need recovery behavior. The synthesis is: allow process restart only into a safe paused/reconcile mode, not automatic trading resumption.
--+++- Codex-Architect assumes the bot may eventually trade real capital. Round 0 must confirm whether real funds are in scope for milestone 1.
--+++
--+++### Non-Negotiable Safety Requirements
--+++
--+++- Read-only, paper, and live modes must be explicit and hard to confuse.
--+++- No withdrawal permissions for any exchange API key used by the bot.
--+++- Kill switch must cancel open orders where possible and disable new trading.
--+++- The bot must reconcile exchange/account state before trading on startup, reconnect, or restart.
--+++- Duplicate order protection is required.
--+++- Hard maximums are required for order size, position size, portfolio exposure, daily loss, drawdown, open orders, and order rate.
--+++- The bot must halt or enter safe mode on stale data, repeated exchange errors, abnormal slippage, rejected orders, reconciliation mismatch, or connectivity loss.
--+++- Human approval should be required before live automation and before scaling capital.
--+++- All timestamps should be consistent and timezone-aware, preferably UTC internally.
--+++- Every signal, order intent, order response, fill, cancellation, error, override, and configuration change must be logged.
--+++
--+++### Evaluation Standards for Profitability Claims
--+++
--+++- The strategy must have a falsifiable hypothesis explaining why an edge should exist.
--+++- Backtests must avoid look-ahead bias, data leakage, and excessive parameter fitting.
--+++- Validation must include out-of-sample data or walk-forward testing.
--+++- Evaluation must include multiple market regimes where possible.
--+++- Results must be measured after fees, spread, slippage, latency, partial fills, failed orders, and funding or borrow costs where relevant.
--+++- Metrics should include total return, profit factor, Sharpe or Sortino, max drawdown, drawdown duration, win/loss distribution, tail losses, turnover, exposure, and sensitivity to parameters.
--+++- Paper trading must compare expected fills against simulated or actual paper fills.
--+++- Live trading, if ever allowed, should start with minimal capital and require evidence that live behavior matches expected behavior.
--+++- A strategy must have predefined retirement or pause criteria when live performance diverges from expectations.
--+++
--+++### MVP Exclusions
--+++
--+++- Leverage, margin, perpetuals, and futures unless explicitly chosen later with separate risk design.
--+++- Multiple exchanges.
--+++- Multiple unrelated strategies.
--+++- Cross-exchange arbitrage.
--+++- High-frequency trading.
--+++- Complex machine learning or automatic strategy discovery.
--+++- Auto-optimization against recent backtests.
--+++- Social/news sentiment trading.
--+++- Copy trading.
--+++- Withdrawal automation.
--+++- Fully autonomous capital scaling.
--+++- Complex UI dashboards beyond minimal operational visibility.
--+++- Any feature that makes trades harder to explain.
--+++
--+++### Questions That Flow Into Round 0
--+++
--+++- QUESTION: What specific bot type is milestone 1: alerting, research, backtesting, paper trading, live spot trading, market making, arbitrage, portfolio tracking, or something else?
--+++- QUESTION: What falsifiable market hypothesis do we want to test first?
--+++- QUESTION: What market regime is the first strategy intended for?
--+++- QUESTION: What trading horizon is targeted: seconds, minutes, hours, days, or longer?
--+++- QUESTION: Which asset universe is allowed for milestone 1?
--+++- QUESTION: Which exchange or data source is targeted first?
--+++- QUESTION: Will milestone 1 involve real funds, or only read-only/paper mode?
--+++- QUESTION: What maximum loss or drawdown is acceptable before the bot must halt?
--+++- QUESTION: What evidence is required before moving from backtest to paper, and from paper to live?
--+++- QUESTION: Who can trigger the kill switch, and what should the recovery protocol be?
--+++- QUESTION: What interface should the operator use first: CLI, logs, simple dashboard, API, or chat?
--+++- QUESTION: What monitoring is mandatory from day one?
--+++- QUESTION: What is the minimum acceptable audit trail for every decision?
--+++
--+++## Decision
--+++
--+++Round -1 establishes the baseline: this project should not frame the first milestone as "build a profitable bot." It should frame the first milestone as "build a narrow, safe, auditable system for testing one falsifiable trading hypothesis under realistic costs and failure conditions."
--+++
--+++Proceed to Round 0 only after the user chooses the first milestone and answers the blocking questions about bot type, automation level, target market, target data source/exchange, allowed risk, and operator controls.
--+++
--+++## Next Actions
--+++
--+++1. Use this synthesis as input to Round 0 problem framing.
--+++2. User answers the Round 0 blocking questions, especially bot type and whether real funds are in scope.
--+++3. Codex-Arbiter updates `round-0-problem-framing.md` with the chosen first milestone.
--+++4. Round 1 begins only after the problem brief is narrow enough for candidate architectures.
--++ 
--++ ```
--++ 
--++@@ -490,14 +2992,85 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--++ 
--++ Recommended order:
--++ 
--++-1. `round0-problem-framing.md`
--++-2. `round0-brief-synthesis.md`
--++-3. `round1-codex-architect.md`
--++-4. `round1-external-architect.md`
--++-5. `round2-cross-review.md`
--++-6. `round3-arbiter.md`
--+++1. `round-minus-1-trading-bot-principles.md`
--+++2. `round0-problem-framing.md`
--+++3. `round0-brief-synthesis.md`
--+++4. `round1-codex-architect.md`
--+++5. `round1-external-architect.md`
--+++6. `round2-cross-review.md`
--+++7. `round3-arbiter.md`
--+++
--+++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--+++
--+++```
--+++
--+++### prompts\round-minus-1-trading-bot-principles.md
--+++
--+++```text
--+++# Round -1 - Trading Bot Principles
--+++
--+++You are participating in a multi-agent software design workflow.
--+++
--+++Round:
--+++Round -1 - Trading Bot Principles
--+++
--+++Question:
--+++"What should a good and potentially profitable crypto trading bot have?"
--+++
--+++Rules:
--+++- Do not design this specific project yet.
--+++- Do not choose frameworks, exchanges, or libraries.
--+++- Do not claim guaranteed profits.
--+++- Separate "good bot qualities" from "profitability requirements".
--+++- Focus on principles, risks, and evaluation criteria.
--+++- Mark assumptions as `ASSUMPTION`.
--+++- Mark questions as `QUESTION`.
--++ 
--++-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--+++Your role:
--+++
--+++```text
--+++[Codex-Architect / Claude / Gemini]
--+++```
--+++
--+++Role focus:
--+++
--+++```text
--+++[Codex-Architect: system qualities, architecture implications, testing, observability, maintainability]
--+++[Claude: flawed assumptions, human risk, decision boundaries, overconfidence, edge cases]
--+++[Gemini: alternative bot types, market/data constraints, exchange/integration risks, evaluation methods]
--+++```
--+++
--+++Task:
--+++1. What makes a crypto trading bot good?
--+++2. What conditions are required before it can plausibly be profitable?
--+++3. What risk controls are non-negotiable?
--+++4. What data, testing, and validation are required?
--+++5. What common false assumptions should we avoid?
--+++6. What should be excluded from MVP?
--+++7. What are the 10 most important questions before designing our bot?
--+++
--+++Return format:
--+++
--+++```md
--+++## Role
--+++
--+++## Good Bot Qualities
--+++
--+++## Profitability Requirements
--+++
--+++## Non-Negotiable Risk Controls
--+++
--+++## Data, Testing, and Validation
--+++
--+++## False Assumptions to Avoid
--+++
--+++## Exclude from MVP
--+++
--+++## Questions Before Design
--+++- QUESTION:
--+++
--+++## Recommendation
--+++```
--++ 
--++ 
--++ ```
--++@@ -872,16 +3445,18 @@ This repo starts with a multi-agent design workflow before implementation.
--++ 
--++ The intended loop is:
--++ 
--++-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--++-2. Codex-Arbiter turns the answers into a neutral problem brief.
--++-3. Round 1: each architect proposes a design from the same brief.
--++-4. Round 2: agents critique the candidate designs.
--++-5. Round 3: Codex-Arbiter records the final architecture.
--++-6. Round 4: Codex implements the accepted plan and runs verification.
--+++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--+++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--+++3. Codex-Arbiter turns the answers into a neutral problem brief.
--+++4. Round 1: each architect proposes a design from the same brief.
--+++5. Round 2: agents critique the candidate designs.
--+++6. Round 3: Codex-Arbiter records the final architecture.
--+++7. Round 4: Codex implements the accepted plan and runs verification.
--++ 
--++ Start here:
--++ 
--++ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--+++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--++ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--++ - [Prompt Library](prompts/README.md)
--++ 
--++@@ -890,12 +3465,17 @@ Start here:
--++ Create a context pack for review:
--++ 
--++ ```powershell
--++-python tools/make_context.py --task "Describe the current design question"
--+++py tools/make_context.py --task "Describe the current design question"
--++ ```
--++ 
--++ The generated file goes to `reviews/latest/context-pack.md`.
--++ 
--+++```
--+++
--+++### reviews\latest\context-pack.md
--++ 
--+++```text
--+++[Skipped: file is 101739 bytes, above 24000 byte limit]
--++ ```
--++ 
--++ ### tools\make_context.py
--++
--++[stderr]
--++warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
--++warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF will be replaced by CRLF the next time Git touches it
--++warning: in the working copy of 'docs/multi-agent-design-workflow/round-0-problem-framing.md', LF will be replaced by CRLF the next time Git touches it
--++warning: in the working copy of 'prompts/README.md', LF will be replaced by CRLF the next time Git touches it
--+ ```
--+ 
--+ ## File Tree
--+ 
--+ - .env.example
--++- docs\multi-agent-design-workflow\00-problem-brief.md
--+ - docs\multi-agent-design-workflow\agent-protocol.md
--+ - docs\multi-agent-design-workflow\README.md
--+ - docs\multi-agent-design-workflow\round-0-problem-framing.md
--++- docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--+ - docs\multi-agent-design-workflow\round-template.md
--+ - prompts\README.md
--++- prompts\round-minus-1-trading-bot-principles.md
--+ - prompts\round0-brief-synthesis.md
--+ - prompts\round0-problem-framing.md
--+ - prompts\round1-codex-architect.md
--+@@ -41,6 +3133,7 @@ Verify multi-agent design workflow setup
--+ - README.md
--+ - reviews\.gitkeep
--+ - reviews\latest\.gitkeep
--++- reviews\latest\context-pack.md
--+ - tools\make_context.py
--+ 
--+ ## Included Files
--+@@ -56,6 +3149,119 @@ GEMINI_API_KEY=
--+ OPENAI_API_KEY=
--+ 
--+ 
--++```
--++
--++### docs\multi-agent-design-workflow\00-problem-brief.md
--++
--++```text
--++# Problem Brief
--++
--++Status: `round-0-synthesized`
--++Date: `2026-05-02`
--++Source: Round -1 and Round 0 synthesis
--++
--++## Goal
--++
--++Build a safety-first crypto research and paper-readiness system for Binance spot markets. The system should help define, test, compare, monitor, and reject trading strategy hypotheses before any real-money trading is considered.
--++
--++The project should not begin as "build a profitable bot." It should begin as "build a narrow, auditable research and simulation system that can test whether any proposed strategy deserves further attention."
--++
--++## Target Users
--++
--++- Primary operator: the repo owner.
--++- Secondary future user: a technical operator who can read logs, review backtests, inspect assumptions, and decide whether a strategy is worth paper or live testing.
--++
--++ASSUMPTION: This is a private or small-team tool, not a public SaaS product.
--++
--++## Confirmed Scope
--++
--++- Exchange/data source: Binance.
--++- Market type: spot only.
--++- Assets: `BTC/USDT`, `ETH/USDT`.
--++- First timeframe: `1h`.
--++- First interface: structured log files.
--++- Real funds: out of scope for milestone 1.
--++- Withdrawal permissions: out of scope.
--++- Margin, futures, perpetuals, and leverage: out of scope.
--++- Risk boundary: maximum drawdown target/limit of `10-20%` for evaluation and future controls.
--++
--++## Milestone 1
--++
--++Milestone 1 should include:
--++
--++- Historical backtesting for Binance spot `BTC/USDT` and `ETH/USDT` on `1h` candles.
--++- A carefully scoped strategy extension boundary. Round 1 should decide whether this is a real plugin contract or a provisional internal strategy interface.
--++- A strategy research workflow that helps compare candidate strategies, run sensitivity analysis, and reject weak ones.
--++- Alert generation from strategy signals or monitoring rules.
--++- Simulated portfolio-state monitoring.
--++- Structured logs for auditability and debugging.
--++- Clear milestone exit criteria and reports for deciding whether a strategy deserves later paper/live dry-run.
--++
--++## Non-Goals
--++
--++- Live order placement.
--++- Using real funds.
--++- Multiple exchanges.
--++- High-frequency trading.
--++- Cross-exchange arbitrage.
--++- Leverage, margin, futures, or perpetual trading.
--++- Complex machine learning models.
--++- Automatic strategy discovery that optimizes against recent backtests.
--++- Full web dashboard.
--++- Live market dry-run in milestone 1, unless Round 1 justifies a minimal future-compatible interface without adding runtime complexity.
--++- Binance read-only account monitoring in milestone 1, unless Round 1 justifies a strong use case.
--++- Tax reporting.
--++- Copy trading or social/news sentiment trading.
--++
--++## Core Workflows
--++
--++1. The operator defines or installs a strategy candidate.
--++2. The system loads historical Binance spot candle data.
--++3. The system runs a backtest with explicit fees and realistic assumptions.
--++4. The system records signals, simulated orders, portfolio state, drawdown, and metrics.
--++5. The system compares strategy results without assuming that the best backtest is a real edge.
--++6. The system emits structured logs and alerts.
--++7. The operator reviews whether a strategy should be rejected, revised, or considered for later paper/live dry-run.
--++
--++## Safety and Evaluation Principles
--++
--++- Every strategy must have an explicit hypothesis.
--++- Backtest results must be treated as evidence, not proof.
--++- Results should include fees, spread/slippage assumptions, drawdown, trade distribution, and sensitivity where practical.
--++- The system should make weak strategies easy to reject.
--++- The system should avoid overfitting incentives.
--++- Paper/live dry-run should be treated as a later milestone, not proof of live profitability.
--++- Any future live mode must require separate design, approval, and risk controls.
--++- Research tooling should favor sensitivity analysis and comparison over automated optimization.
--++
--++## Open Design Questions for Round 1
--++
--++- QUESTION: What is the formal definition of done for milestone 1?
--++- QUESTION: What structured log format and event schema should be the first operator interface?
--++- QUESTION: Should the strategy extension boundary be a real plugin contract or a provisional internal abstraction?
--++- QUESTION: How should the research workflow prevent overfitting and false confidence?
--++- QUESTION: What baseline strategy, if any, should be included only to validate framework behavior?
--++- QUESTION: How much Binance order-rule simulation is necessary in historical backtesting?
--++- QUESTION: What metrics are required in milestone 1 versus later?
--++- QUESTION: Should backtesting use only `1h` OHLCV candles first, or should data storage leave room for higher-resolution candles to improve execution assumptions later?
--++- QUESTION: Where should historical data be persisted: local files, SQLite, another database, or on-demand fetching with cache?
--++
--++## Architecture Constraints
--++
--++- The first architecture should keep live trading out of the system boundary.
--++- The strategy interface should be testable without Binance credentials.
--++- Binance credentials, if added later for read-only monitoring, must be optional and restricted.
--++- Logs must be structured enough to reconstruct decisions.
--++- Strategy code must be separated from core data loading, simulation, portfolio accounting, and reporting.
--++- The system should support future paper/live dry-run conceptually without forcing that runtime complexity into the first backtester.
--++- Live integrations requiring credentials should remain outside milestone 1 unless explicitly justified.
--++
--++## Decision
--++
--++Proceed to Round 1 candidate architecture proposals.
--++
--++Round 1 architects should explicitly debate the open design questions rather than assuming a single answer. Candidate designs should prioritize historical research quality, reproducibility, log-based auditability, strategy comparison, and anti-overfitting safeguards.
--++
--+ ```
--+ 
--+ ### docs\multi-agent-design-workflow\agent-protocol.md
--+@@ -178,16 +3384,19 @@ The workflow is round-based. Each round produces a short decision record that ca
--+ 
--+ ## Round Sequence
--+ 
--+-1. `Round 0 - Problem Framing`
--++1. `Round -1 - Trading Bot Principles`
--++   - Define what a good and potentially profitable crypto trading bot requires.
--++   - Establish safety, validation, and profitability standards before project-specific design.
--++2. `Round 0 - Problem Framing`
--+    - Define the actual problem, users, success criteria, constraints, and unknowns.
--+    - No solution is selected in this round.
--+-2. `Round 1 - Candidate Designs`
--++3. `Round 1 - Candidate Designs`
--+    - Each design agent proposes one or more viable approaches.
--+-3. `Round 2 - Critique and Risk`
--++4. `Round 2 - Critique and Risk`
--+    - Agents critique designs from their role perspective.
--+-4. `Round 3 - Synthesis`
--++5. `Round 3 - Synthesis`
--+    - Codex-Arbiter selects or combines a direction and records tradeoffs.
--+-5. `Round 4 - Implementation Plan`
--++6. `Round 4 - Implementation Plan`
--+    - Convert the selected design into files, tasks, tests, and rollout steps.
--+ 
--+ ## Operating Rules
--+@@ -205,7 +3414,7 @@ The workflow is round-based. Each round produces a short decision record that ca
--+ 
--+ ## Current Starting Point
--+ 
--+-Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md).
--+ 
--+ ```
--+ 
--+@@ -232,13 +3441,23 @@ Round 0 does not choose libraries, exchanges, strategies, infrastructure, or imp
--+   - `Claude`
--+   - `Gemini`
--+   - `Codex-Arbiter`
--+-- The project name suggests a crypto bot, but the exact product scope is not yet defined.
--++- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
--++- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
--++- The first market scope is Binance spot.
--++- The first assets are `BTC/USDT` and `ETH/USDT`.
--++- There is no confirmed strategy hypothesis yet.
--++- The first operator interface should be log files, not a web dashboard.
--++- The initial risk tolerance is maximum drawdown of `10-20%`.
--++- The initial backtest timeframe should be `1h`.
--++- The user is interested in both historical backtesting and live market dry-run, but is open to sequencing historical data first and live dry-run later.
--++- If live market dry-run is included, Binance read-only account support may be useful, but this is not confirmed.
--++- The user is interested in both a strategy plugin interface and a strategy research workflow.
--+ 
--+ ## Working Problem Statement
--+ 
--+-ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.
--++This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.
--+ 
--+-The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.
--++Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.
--+ 
--+ ## Round 0 Prompts
--+ 
--+@@ -300,15 +3519,15 @@ Assumptions:
--+ 
--+ Questions:
--+ 
--+-- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
--+-- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
--+-- QUESTION: Is the bot allowed to place orders automatically?
--+-- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
--+-- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?
--++- QUESTION: Should milestone 1 include both historical backtesting and live market dry-run, or should live dry-run wait until historical simulation is trustworthy?
--++- QUESTION: Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state only?
--++- QUESTION: Should the first architecture prioritize a strategy plugin interface, a strategy research workflow, or a parallel strategy-monitoring system?
--++- QUESTION: How should the system help discover or compare strategies when no hypothesis is confirmed yet?
--++- QUESTION: What first class of strategy should be used only as a baseline to test the framework, without implying it is profitable?
--+ 
--+ Recommendation:
--+ 
--+-Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.
--++Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.
--+ 
--+ Risks:
--+ 
--+@@ -337,6 +3556,8 @@ Questions:
--+ - QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
--+ - QUESTION: How should the operator review, override, pause, or audit bot behavior?
--+ - QUESTION: What is the acceptable balance between speed, safety, and explainability?
--++- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, a plugin interface for manually supplied strategies, or both?
--++- QUESTION: If multiple strategies are evaluated in parallel, how should the operator avoid overfitting and false confidence?
--+ 
--+ Recommendation:
--+ 
--+@@ -376,6 +3597,8 @@ Questions:
--+ - QUESTION: Is real money involved in milestone 1?
--+ - QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
--+ - QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
--++- QUESTION: Should the first design sequence be historical candles first, then live WebSocket dry-run, then read-only portfolio monitoring?
--++- QUESTION: Does Binance read-only monitoring materially improve milestone 1, or does it add unnecessary security and setup complexity?
--+ 
--+ Recommendation:
--+ 
--+@@ -388,14 +3611,24 @@ Risks:
--+ 
--+ ## Codex-Arbiter Synthesis
--+ 
--++### Round 0 Agent Answer Summary
--++
--++Codex-Architect framed the project as a non-live research and simulation system. The strongest point was sequencing: milestone 1 should prove trustworthy evaluation, reproducible results, structured audit logs, and rejection criteria before live market dry-run or read-only Binance account integration are assumed.
--++
--++Claude challenged the scope and argued that the project contains two different goals: research tooling and runtime infrastructure. The strongest point was that milestone 1 needs explicit exit criteria, a defined structured log schema, and a decision about whether the strategy interface is a real plugin contract or a provisional internal abstraction.
--++
--++Gemini framed the project as a hypothesis-first research platform. The strongest point was that high-fidelity backtesting and strategy comparison are more valuable in milestone 1 than live dry-run, because live dry-run on a `1h` timeframe takes weeks to produce meaningful evidence. Gemini also recommended sensitivity analysis over automated optimization to reduce curve fitting.
--++
--+ Canonical problem statement:
--+ 
--+-This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.
--++This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`. The first milestone should support historical backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Live market dry-run and Binance read-only account monitoring are desirable but should be debated for sequencing and complexity. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, monitor, and reject rather than assuming a profitable strategy already exists.
--+ 
--+ In scope for Round 0:
--+ 
--+-- Clarifying bot type and first milestone.
--+-- Identifying risk, safety, and human-control requirements.
--++- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
--++- Identifying risk, safety, and human-control requirements for non-live operation.
--++- Clarifying data source and simulation fidelity requirements for Binance spot.
--++- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
--+ - Recording blocking questions and assumptions.
--+ - Preparing for candidate architecture designs in Round 1.
--+ 
--+@@ -405,30 +3638,289 @@ Out of scope for Round 0:
--+ - Choosing exchange SDKs or trading libraries.
--+ - Writing trading strategy code.
--+ - Designing live order execution flows.
--++- Enabling real-money trading.
--++- Supporting leverage, futures, margin, or withdrawals.
--+ 
--+ Blocking questions:
--+ 
--+-- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
--+-- Will the bot handle real funds or private keys in milestone 1?
--+-- What user approval or kill-switch controls are required?
--+-- What exchange, chain, wallet, or market-data source is targeted first?
--+-- What interface should the operator use first: CLI, web UI, chat, API, or background service only?
--++- What is the formal milestone 1 exit condition?
--++- What exact structured log format and event schema should be treated as the first operator interface?
--++- Should the strategy interface in milestone 1 be a real plugin contract or a provisional internal abstraction?
--++- What minimum simulation realism is required for milestone 1: fees only, fees plus spread/slippage, or partial fill/latency assumptions?
--++- What benchmark should strategy candidates be compared against, such as buy-and-hold, cash, or simple baseline strategies?
--+ 
--+ Non-blocking assumptions:
--+ 
--+ - The repo is early enough that workflow docs can define the decision process.
--+ - The first implementation should be narrow and reversible.
--+ - Safety and auditability should be treated as first-class design concerns.
--++- Binance is the initial exchange/data source.
--++- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
--++- Spot-only scope excludes leverage, margin, futures, and perpetuals.
--++- Log files are sufficient for the first operator interface if they are structured and easy to audit.
--++- Maximum drawdown of `10-20%` is a project-level risk boundary for evaluation and future paper/live controls.
--++- The first timeframe is `1h`.
--++- Live market dry-run should be sequenced after historical backtesting is reliable.
--++- Binance read-only account monitoring should be deferred unless Round 1 identifies a strong reason to include it.
--++- Milestone 1 portfolio monitoring can start with simulated portfolio state.
--++- The research workflow should prioritize comparison and sensitivity analysis over automated parameter optimization.
--+ 
--+ Decision:
--+ 
--+-Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.
--++Proceed to Round 1 candidate designs with a narrower milestone: historical backtesting, simulated portfolio monitoring, structured logs, strategy comparison/research workflow, and a carefully scoped strategy extension boundary. Live market dry-run and Binance read-only account monitoring are deferred to milestone 2 unless an architect can justify a minimal interface stub that does not add credential or runtime complexity.
--+ 
--+ Next actions:
--+ 
--+-1. User answers the blocking questions.
--+-2. Codex-Arbiter updates this document with the chosen first milestone.
--+-3. Round 1 begins with candidate designs constrained to that milestone.
--++1. Codex-Arbiter updates the neutral problem brief with this narrower milestone.
--++2. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
--++3. Round 1 proposals must explicitly answer the remaining architecture questions: log schema, strategy boundary, data persistence, backtest realism, metrics, and anti-overfitting workflow.
--++
--++```
--++
--++### docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--++
--++```text
--++# Round -1 - Trading Bot Principles
--++
--++Status: `draft`
--++Date: `2026-05-02`
--++Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--++
--++## Goal of This Round
--++
--++Build a shared baseline for the question:
--++
--++> What should a good and potentially profitable crypto trading bot have?
--++
--++This round happens before project-specific problem framing. The goal is to clarify principles, risks, evaluation standards, and false assumptions before deciding what this repo should build.
--++
--++Round -1 does not design this project, choose exchanges, select frameworks, or define a specific trading strategy.
--++
--++## Ground Rules
--++
--++- Do not claim guaranteed profit.
--++- Separate "good bot qualities" from "profitability requirements".
--++- Treat risk controls, auditability, and validation as first-class concerns.
--++- Assume backtest results can be misleading until proven otherwise.
--++- Do not recommend live trading before paper trading and risk boundaries are defined.
--++- Mark assumptions as `ASSUMPTION`.
--++- Mark questions as `QUESTION`.
--++
--++## Shared Question
--++
--++What should a good and potentially profitable crypto trading bot have?
--++
--++## Agent Focus
--++
--++### Codex-Architect
--++
--++Focus on:
--++
--++- System qualities.
--++- Architecture implications.
--++- Testing and verification.
--++- Observability and audit logs.
--++- Maintainability and safe iteration.
--++
--++### Claude
--++
--++Focus on:
--++
--++- Flawed assumptions.
--++- Human risk and overconfidence.
--++- Decision boundaries.
--++- Edge cases and failure modes.
--++- What should remain human-approved.
--++
--++### Gemini
--++
--++Focus on:
--++
--++- Alternative bot types.
--++- Market and data constraints.
--++- Exchange and integration risks.
--++- Evaluation methods.
--++- External constraints that could dominate design.
--++
--++## Questions for Agents
--++
--++Each agent should answer:
--++
--++1. What makes a crypto trading bot good?
--++2. What conditions are required before it can plausibly be profitable?
--++3. What risk controls are non-negotiable?
--++4. What data, testing, and validation are required?
--++5. What common false assumptions should we avoid?
--++6. What should be excluded from MVP?
--++7. What are the 10 most important questions before designing our bot?
--++
--++## Initial Shared Baseline
--++
--++Good bot qualities:
--++
--++- Clear operating mode: alerts, research, backtesting, paper trading, or live execution.
--++- Separation between market data, strategy logic, risk controls, execution, state, and reporting.
--++- Full audit trail for inputs, decisions, orders, errors, overrides, and configuration changes.
--++- Deterministic replay/debug mode for understanding past decisions.
--++- Operator controls for pause, kill switch, configuration review, and emergency shutdown.
--++- Safe secret handling if exchange API keys or wallet credentials ever become involved.
--++- Tests for strategy logic, risk logic, execution adapters, and failure handling.
--++
--++Profitability requirements:
--++
--++- A testable hypothesis for why the strategy should have edge.
--++- Historical validation without look-ahead bias, survivorship bias, or data leakage.
--++- Evaluation after fees, spread, slippage, funding rates, latency, and failed orders.
--++- Out-of-sample testing or walk-forward validation.
--++- Paper trading before live trading.
--++- Position sizing and drawdown controls.
--++- Monitoring for market regime changes.
--++
--++Non-negotiable risk controls:
--++
--++- Max position size.
--++- Max daily loss.
--++- Max drawdown.
--++- Per-trade risk limit.
--++- Exchange/API failure handling.
--++- Duplicate order protection.
--++- Kill switch.
--++- Dry-run or paper mode.
--++- Read-only mode for analysis features.
--++- Human approval mode before live automation.
--++
--++Common false assumptions:
--++
--++- Backtest profit means future profit.
--++- High win rate means good strategy.
--++- AI can reliably predict sudden market moves.
--++- More indicators mean better signals.
--++- Live trading is just backtesting with real orders.
--++- Exchange APIs behave reliably during volatility.
--++- Fees and slippage are small enough to ignore.
--++- A bot should trade often to be useful.
--++
--++## Codex-Arbiter Synthesis Template
--++
--++After the three agents answer, produce:
--++
--++1. Shared principles accepted by all agents.
--++2. Disagreements or tensions worth preserving.
--++3. Non-negotiable safety requirements.
--++4. Evaluation standards for profitability claims.
--++5. MVP exclusions.
--++6. Questions that should flow into Round 0.
--++
--++## Agent Answer Summary
--++
--++### Codex-Architect
--++
--++Codex-Architect framed a good bot as a controlled, observable, testable decision and execution system. The strongest points were separation of strategy, execution, risk, data, configuration, and monitoring; deterministic testing; fail-safe behavior; idempotent execution; strong state reconciliation; and explicit modes for backtest, paper, shadow, and live trading.
--++
--++Codex-Architect emphasized that profitability requires a real market edge after fees, spread, slippage, latency, funding, failed orders, and regime changes. It also stressed that the bot should support strategy retirement when live performance diverges from expectations.
--++
--++### Claude
--++
--++Claude focused on adversarial clarity and warned that the most common failure is starting implementation before the strategy hypothesis is honest. The strongest points were that profitability belongs to the strategy, market, cost structure, execution quality, and timing together, not to the bot by itself.
--++
--++Claude emphasized falsifiable strategy hypotheses, out-of-sample validation, hard drawdown circuit breakers, UTC/time discipline, human restart after major risk events, and predefined failure conditions for stopping the project or strategy.
--++
--++### Gemini
--++
--++Gemini emphasized alternative bot types, market/data constraints, and execution realities. The strongest points were operational resilience, telemetry, exchange integration risk, low-latency path where relevant, high-fidelity data handling, inventory management for market making or arbitrage, and the need to define the intended market regime.
--++
--++Gemini also highlighted tick-to-trade latency, partial fills, orphan orders, WebSocket/REST divergence, maker/taker fee assumptions, fat-tail events, and kill-switch authority.
--++
--++## Codex-Arbiter Synthesis
--++
--++### Shared Principles Accepted by All Agents
--++
--++- A good crypto trading bot is first a safety-critical automation system, not a profit machine.
--++- Strategy logic, risk controls, exchange execution, data ingestion, state management, configuration, monitoring, and reporting should be separated.
--++- Every trade decision must be auditable after the fact from logs and stored state.
--++- The bot must fail safely when data, connectivity, exchange APIs, or internal state become unreliable.
--++- Backtest profitability is not sufficient evidence of live profitability.
--++- Profitability claims must include fees, spread, slippage, latency, partial fills, failed orders, funding or borrow costs where relevant, and market regime effects.
--++- Paper trading is necessary before live trading, but paper trading is still not proof of live profitability.
--++- Risk controls belong in the MVP, not after the MVP.
--++- The first version should be narrow, explainable, and easy to shut down.
--++
--++### Disagreements or Tensions Worth Preserving
--++
--++- Claude recommends excluding dashboard and alerting from MVP, while Codex-Architect treats observability from day one as essential. The synthesis is: avoid a complex UI dashboard, but keep operational logs, basic metrics, and alerts for dangerous states.
--++- Gemini mentions a low-latency path, while Claude warns latency must match the strategy horizon. The synthesis is: do not optimize for low latency generally; define latency requirements only after the strategy type and timeframe are chosen.
--++- Claude prefers no auto-restart on crash, while production systems often need recovery behavior. The synthesis is: allow process restart only into a safe paused/reconcile mode, not automatic trading resumption.
--++- Codex-Architect assumes the bot may eventually trade real capital. Round 0 must confirm whether real funds are in scope for milestone 1.
--++
--++### Non-Negotiable Safety Requirements
--++
--++- Read-only, paper, and live modes must be explicit and hard to confuse.
--++- No withdrawal permissions for any exchange API key used by the bot.
--++- Kill switch must cancel open orders where possible and disable new trading.
--++- The bot must reconcile exchange/account state before trading on startup, reconnect, or restart.
--++- Duplicate order protection is required.
--++- Hard maximums are required for order size, position size, portfolio exposure, daily loss, drawdown, open orders, and order rate.
--++- The bot must halt or enter safe mode on stale data, repeated exchange errors, abnormal slippage, rejected orders, reconciliation mismatch, or connectivity loss.
--++- Human approval should be required before live automation and before scaling capital.
--++- All timestamps should be consistent and timezone-aware, preferably UTC internally.
--++- Every signal, order intent, order response, fill, cancellation, error, override, and configuration change must be logged.
--++
--++### Evaluation Standards for Profitability Claims
--++
--++- The strategy must have a falsifiable hypothesis explaining why an edge should exist.
--++- Backtests must avoid look-ahead bias, data leakage, and excessive parameter fitting.
--++- Validation must include out-of-sample data or walk-forward testing.
--++- Evaluation must include multiple market regimes where possible.
--++- Results must be measured after fees, spread, slippage, latency, partial fills, failed orders, and funding or borrow costs where relevant.
--++- Metrics should include total return, profit factor, Sharpe or Sortino, max drawdown, drawdown duration, win/loss distribution, tail losses, turnover, exposure, and sensitivity to parameters.
--++- Paper trading must compare expected fills against simulated or actual paper fills.
--++- Live trading, if ever allowed, should start with minimal capital and require evidence that live behavior matches expected behavior.
--++- A strategy must have predefined retirement or pause criteria when live performance diverges from expectations.
--++
--++### MVP Exclusions
--++
--++- Leverage, margin, perpetuals, and futures unless explicitly chosen later with separate risk design.
--++- Multiple exchanges.
--++- Multiple unrelated strategies.
--++- Cross-exchange arbitrage.
--++- High-frequency trading.
--++- Complex machine learning or automatic strategy discovery.
--++- Auto-optimization against recent backtests.
--++- Social/news sentiment trading.
--++- Copy trading.
--++- Withdrawal automation.
--++- Fully autonomous capital scaling.
--++- Complex UI dashboards beyond minimal operational visibility.
--++- Any feature that makes trades harder to explain.
--++
--++### Questions That Flow Into Round 0
--++
--++- QUESTION: What specific bot type is milestone 1: alerting, research, backtesting, paper trading, live spot trading, market making, arbitrage, portfolio tracking, or something else?
--++- QUESTION: What falsifiable market hypothesis do we want to test first?
--++- QUESTION: What market regime is the first strategy intended for?
--++- QUESTION: What trading horizon is targeted: seconds, minutes, hours, days, or longer?
--++- QUESTION: Which asset universe is allowed for milestone 1?
--++- QUESTION: Which exchange or data source is targeted first?
--++- QUESTION: Will milestone 1 involve real funds, or only read-only/paper mode?
--++- QUESTION: What maximum loss or drawdown is acceptable before the bot must halt?
--++- QUESTION: What evidence is required before moving from backtest to paper, and from paper to live?
--++- QUESTION: Who can trigger the kill switch, and what should the recovery protocol be?
--++- QUESTION: What interface should the operator use first: CLI, logs, simple dashboard, API, or chat?
--++- QUESTION: What monitoring is mandatory from day one?
--++- QUESTION: What is the minimum acceptable audit trail for every decision?
--++
--++## Decision
--++
--++Round -1 establishes the baseline: this project should not frame the first milestone as "build a profitable bot." It should frame the first milestone as "build a narrow, safe, auditable system for testing one falsifiable trading hypothesis under realistic costs and failure conditions."
--++
--++Proceed to Round 0 only after the user chooses the first milestone and answers the blocking questions about bot type, automation level, target market, target data source/exchange, allowed risk, and operator controls.
--++
--++## Next Actions
--++
--++1. Use this synthesis as input to Round 0 problem framing.
--++2. User answers the Round 0 blocking questions, especially bot type and whether real funds are in scope.
--++3. Codex-Arbiter updates `round-0-problem-framing.md` with the chosen first milestone.
--++4. Round 1 begins only after the problem brief is narrow enough for candidate architectures.
--+ 
--+ ```
--+ 
--+@@ -490,14 +3982,85 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
--+ 
--+ Recommended order:
--+ 
--+-1. `round0-problem-framing.md`
--+-2. `round0-brief-synthesis.md`
--+-3. `round1-codex-architect.md`
--+-4. `round1-external-architect.md`
--+-5. `round2-cross-review.md`
--+-6. `round3-arbiter.md`
--++1. `round-minus-1-trading-bot-principles.md`
--++2. `round0-problem-framing.md`
--++3. `round0-brief-synthesis.md`
--++4. `round1-codex-architect.md`
--++5. `round1-external-architect.md`
--++6. `round2-cross-review.md`
--++7. `round3-arbiter.md`
--+ 
--+-Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--++Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--++
--++```
--++
--++### prompts\round-minus-1-trading-bot-principles.md
--++
--++```text
--++# Round -1 - Trading Bot Principles
--++
--++You are participating in a multi-agent software design workflow.
--++
--++Round:
--++Round -1 - Trading Bot Principles
--++
--++Question:
--++"What should a good and potentially profitable crypto trading bot have?"
--++
--++Rules:
--++- Do not design this specific project yet.
--++- Do not choose frameworks, exchanges, or libraries.
--++- Do not claim guaranteed profits.
--++- Separate "good bot qualities" from "profitability requirements".
--++- Focus on principles, risks, and evaluation criteria.
--++- Mark assumptions as `ASSUMPTION`.
--++- Mark questions as `QUESTION`.
--++
--++Your role:
--++
--++```text
--++[Codex-Architect / Claude / Gemini]
--++```
--++
--++Role focus:
--++
--++```text
--++[Codex-Architect: system qualities, architecture implications, testing, observability, maintainability]
--++[Claude: flawed assumptions, human risk, decision boundaries, overconfidence, edge cases]
--++[Gemini: alternative bot types, market/data constraints, exchange/integration risks, evaluation methods]
--++```
--++
--++Task:
--++1. What makes a crypto trading bot good?
--++2. What conditions are required before it can plausibly be profitable?
--++3. What risk controls are non-negotiable?
--++4. What data, testing, and validation are required?
--++5. What common false assumptions should we avoid?
--++6. What should be excluded from MVP?
--++7. What are the 10 most important questions before designing our bot?
--++
--++Return format:
--++
--++```md
--++## Role
--++
--++## Good Bot Qualities
--++
--++## Profitability Requirements
--++
--++## Non-Negotiable Risk Controls
--++
--++## Data, Testing, and Validation
--++
--++## False Assumptions to Avoid
--++
--++## Exclude from MVP
--++
--++## Questions Before Design
--++- QUESTION:
--++
--++## Recommendation
--++```
--+ 
--+ 
--+ ```
--+@@ -872,16 +4435,18 @@ This repo starts with a multi-agent design workflow before implementation.
--+ 
--+ The intended loop is:
--+ 
--+-1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
--+-2. Codex-Arbiter turns the answers into a neutral problem brief.
--+-3. Round 1: each architect proposes a design from the same brief.
--+-4. Round 2: agents critique the candidate designs.
--+-5. Round 3: Codex-Arbiter records the final architecture.
--+-6. Round 4: Codex implements the accepted plan and runs verification.
--++1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--++2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--++3. Codex-Arbiter turns the answers into a neutral problem brief.
--++4. Round 1: each architect proposes a design from the same brief.
--++5. Round 2: agents critique the candidate designs.
--++6. Round 3: Codex-Arbiter records the final architecture.
--++7. Round 4: Codex implements the accepted plan and runs verification.
--+ 
--+ Start here:
--+ 
--+ - [Workflow README](docs/multi-agent-design-workflow/README.md)
--++- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
--+ - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
--+ - [Prompt Library](prompts/README.md)
--+ 
--+@@ -890,12 +4455,17 @@ Start here:
--+ Create a context pack for review:
--+ 
--+ ```powershell
--+-python tools/make_context.py --task "Describe the current design question"
--++py tools/make_context.py --task "Describe the current design question"
--+ ```
--+ 
--+ The generated file goes to `reviews/latest/context-pack.md`.
--+ 
--++```
--++
--++### reviews\latest\context-pack.md
--+ 
--++```text
--++[Skipped: file is 153184 bytes, above 24000 byte limit]
--+ ```
--+ 
--+ ### tools\make_context.py
--+
--+[stderr]
--+warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
--+warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF will be replaced by CRLF the next time Git touches it
--+warning: in the working copy of 'docs/multi-agent-design-workflow/round-0-problem-framing.md', LF will be replaced by CRLF the next time Git touches it
--+warning: in the working copy of 'prompts/README.md', LF will be replaced by CRLF the next time Git touches it
-- ```
-- 
-- ## File Tree
-- 
-- - .env.example
--+- docs\multi-agent-design-workflow\00-problem-brief.md
-- - docs\multi-agent-design-workflow\agent-protocol.md
-- - docs\multi-agent-design-workflow\README.md
--+- docs\multi-agent-design-workflow\round-0-brief-synthesis.md
-- - docs\multi-agent-design-workflow\round-0-problem-framing.md
--+- docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
-- - docs\multi-agent-design-workflow\round-template.md
-- - prompts\README.md
--+- prompts\round-minus-1-trading-bot-principles.md
-- - prompts\round0-brief-synthesis.md
-- - prompts\round0-problem-framing.md
-- - prompts\round1-codex-architect.md
--@@ -41,6 +4129,7 @@ Verify multi-agent design workflow setup
-- - README.md
-- - reviews\.gitkeep
-- - reviews\latest\.gitkeep
--+- reviews\latest\context-pack.md
-- - tools\make_context.py
-- 
-- ## Included Files
--@@ -56,6 +4145,119 @@ GEMINI_API_KEY=
-- OPENAI_API_KEY=
-- 
-- 
--+```
--+
--+### docs\multi-agent-design-workflow\00-problem-brief.md
--+
--+```text
--+# Problem Brief
--+
--+Status: `round-0-synthesized`
--+Date: `2026-05-02`
--+Source: Round -1 and Round 0 synthesis
--+
--+## Goal
--+
--+Build a safety-first crypto research and paper-readiness system for Binance spot markets. The system should help define, test, compare, monitor, and reject trading strategy hypotheses before any real-money trading is considered.
--+
--+The project should not begin as "build a profitable bot." It should begin as "build a narrow, auditable research and simulation system that can test whether any proposed strategy deserves further attention."
--+
--+## Target Users
--+
--+- Primary operator: the repo owner.
--+- Secondary future user: a technical operator who can read logs, review backtests, inspect assumptions, and decide whether a strategy is worth paper or live testing.
--+
--+ASSUMPTION: This is a private or small-team tool, not a public SaaS product.
--+
--+## Confirmed Scope
--+
--+- Exchange/data source: Binance.
--+- Market type: spot only.
--+- Assets: `BTC/USDT`, `ETH/USDT`.
--+- First timeframe: `1h`.
--+- First interface: structured log files.
--+- Real funds: out of scope for milestone 1.
--+- Withdrawal permissions: out of scope.
--+- Margin, futures, perpetuals, and leverage: out of scope.
--+- Risk boundary: maximum drawdown target/limit of `10-20%` for evaluation and future controls.
--+
--+## Milestone 1
--+
--+Milestone 1 should include:
--+
--+- Historical backtesting for Binance spot `BTC/USDT` and `ETH/USDT` on `1h` candles.
--+- A carefully scoped strategy extension boundary. Round 1 should decide whether this is a real plugin contract or a provisional internal strategy interface.
--+- A strategy research workflow that helps compare candidate strategies, run sensitivity analysis, and reject weak ones.
--+- Alert generation from strategy signals or monitoring rules.
--+- Simulated portfolio-state monitoring.
--+- Structured logs for auditability and debugging.
--+- Clear milestone exit criteria and reports for deciding whether a strategy deserves later paper/live dry-run.
--+
--+## Non-Goals
--+
--+- Live order placement.
--+- Using real funds.
--+- Multiple exchanges.
--+- High-frequency trading.
--+- Cross-exchange arbitrage.
--+- Leverage, margin, futures, or perpetual trading.
--+- Complex machine learning models.
--+- Automatic strategy discovery that optimizes against recent backtests.
--+- Full web dashboard.
--+- Live market dry-run in milestone 1, unless Round 1 justifies a minimal future-compatible interface without adding runtime complexity.
--+- Binance read-only account monitoring in milestone 1, unless Round 1 justifies a strong use case.
--+- Tax reporting.
--+- Copy trading or social/news sentiment trading.
--+
--+## Core Workflows
--+
--+1. The operator defines or installs a strategy candidate.
--+2. The system loads historical Binance spot candle data.
--+3. The system runs a backtest with explicit fees and realistic assumptions.
--+4. The system records signals, simulated orders, portfolio state, drawdown, and metrics.
--+5. The system compares strategy results without assuming that the best backtest is a real edge.
--+6. The system emits structured logs and alerts.
--+7. The operator reviews whether a strategy should be rejected, revised, or considered for later paper/live dry-run.
--+
--+## Safety and Evaluation Principles
--+
--+- Every strategy must have an explicit hypothesis.
--+- Backtest results must be treated as evidence, not proof.
--+- Results should include fees, spread/slippage assumptions, drawdown, trade distribution, and sensitivity where practical.
--+- The system should make weak strategies easy to reject.
--+- The system should avoid overfitting incentives.
--+- Paper/live dry-run should be treated as a later milestone, not proof of live profitability.
--+- Any future live mode must require separate design, approval, and risk controls.
--+- Research tooling should favor sensitivity analysis and comparison over automated optimization.
--+
--+## Open Design Questions for Round 1
--+
--+- QUESTION: What is the formal definition of done for milestone 1?
--+- QUESTION: What structured log format and event schema should be the first operator interface?
--+- QUESTION: Should the strategy extension boundary be a real plugin contract or a provisional internal abstraction?
--+- QUESTION: How should the research workflow prevent overfitting and false confidence?
--+- QUESTION: What baseline strategy, if any, should be included only to validate framework behavior?
--+- QUESTION: How much Binance order-rule simulation is necessary in historical backtesting?
--+- QUESTION: What metrics are required in milestone 1 versus later?
--+- QUESTION: Should backtesting use only `1h` OHLCV candles first, or should data storage leave room for higher-resolution candles to improve execution assumptions later?
--+- QUESTION: Where should historical data be persisted: local files, SQLite, another database, or on-demand fetching with cache?
--+
--+## Architecture Constraints
--+
--+- The first architecture should keep live trading out of the system boundary.
--+- The strategy interface should be testable without Binance credentials.
--+- Binance credentials, if added later for read-only monitoring, must be optional and restricted.
--+- Logs must be structured enough to reconstruct decisions.
--+- Strategy code must be separated from core data loading, simulation, portfolio accounting, and reporting.
--+- The system should support future paper/live dry-run conceptually without forcing that runtime complexity into the first backtester.
--+- Live integrations requiring credentials should remain outside milestone 1 unless explicitly justified.
--+
--+## Decision
--+
--+Proceed to Round 1 candidate architecture proposals.
--+
--+Round 1 architects should explicitly debate the open design questions rather than assuming a single answer. Candidate designs should prioritize historical research quality, reproducibility, log-based auditability, strategy comparison, and anti-overfitting safeguards.
--+
-- ```
-- 
-- ### docs\multi-agent-design-workflow\agent-protocol.md
--@@ -178,16 +4380,21 @@ The workflow is round-based. Each round produces a short decision record that ca
-- 
-- ## Round Sequence
-- 
---1. `Round 0 - Problem Framing`
--+1. `Round -1 - Trading Bot Principles`
--+   - Define what a good and potentially profitable crypto trading bot requires.
--+   - Establish safety, validation, and profitability standards before project-specific design.
--+2. `Round 0 - Problem Framing`
--    - Define the actual problem, users, success criteria, constraints, and unknowns.
--    - No solution is selected in this round.
---2. `Round 1 - Candidate Designs`
--+3. `Round 0B - Brief Synthesis`
--+   - Codex-Arbiter turns Round 0 agent answers into the canonical problem brief.
--+4. `Round 1 - Candidate Designs`
--    - Each design agent proposes one or more viable approaches.
---3. `Round 2 - Critique and Risk`
--+5. `Round 2 - Critique and Risk`
--    - Agents critique designs from their role perspective.
---4. `Round 3 - Synthesis`
--+6. `Round 3 - Synthesis`
--    - Codex-Arbiter selects or combines a direction and records tradeoffs.
---5. `Round 4 - Implementation Plan`
--+7. `Round 4 - Implementation Plan`
--    - Convert the selected design into files, tasks, tests, and rollout steps.
-- 
-- ## Operating Rules
--@@ -205,7 +4412,125 @@ The workflow is round-based. Each round produces a short decision record that ca
-- 
-- ## Current Starting Point
-- 
---Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).
--+Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), and the canonical [Problem Brief](./00-problem-brief.md).
--+
--+```
--+
--+### docs\multi-agent-design-workflow\round-0-brief-synthesis.md
--+
--+```text
--+# Round 0 - Brief Synthesis
--+
--+Status: `complete`
--+Date: `2026-05-02`
--+Source:
--+
--+- `round-minus-1-trading-bot-principles.md`
--+- `round-0-problem-framing.md`
--+- Codex-Architect Round 0 answer
--+- Claude Round 0 answer
--+- Gemini Round 0 answer
--+- User clarifications
--+
--+## Purpose
--+
--+This file records the Codex-Arbiter synthesis step between Round 0 agent answers and the canonical problem brief.
--+
--+The output of this synthesis is:
--+
--+- `00-problem-brief.md`
--+
--+## Inputs
--+
--+### User Clarifications
--+
--+- Milestone interests: backtesting, paper trading readiness, alert bot, portfolio monitor.
--+- No real funds in milestone 1.
--+- Market scope: Binance spot.
--+- Asset scope: `BTC/USDT`, `ETH/USDT`.
--+- First timeframe: `1h`.
--+- Strategy hypothesis: none confirmed.
--+- First interface: log files.
--+- Risk boundary: maximum drawdown of `10-20%`.
--+- Live market dry-run is desirable, but sequencing is uncertain.
--+- Binance read-only account monitoring is uncertain and should be debated.
--+- The user is interested in both a strategy plugin interface and a strategy research workflow.
--+
--+### Codex-Architect Contribution
--+
--+Codex-Architect framed the project as a non-live research and simulation system. The strongest point was sequencing: milestone 1 should prove trustworthy evaluation, reproducible results, structured audit logs, and rejection criteria before live market dry-run or read-only Binance account integration are assumed.
--+
--+Key concerns:
--+
--+- Scope creep across backtesting, plugins, alerts, monitoring, dry-run, and account integration.
--+- False confidence from weak simulation realism.
--+- Ambiguous meaning of portfolio monitoring, paper trading, alerts, and max drawdown.
--+- Need to define strategy boundary and evaluation workflow.
--+
--+### Claude Contribution
--+
--+Claude challenged the scope and argued that the project contains two different goals:
--+
--+- Research tooling.
--+- Runtime infrastructure.
--+
--+The strongest point was that milestone 1 needs explicit exit criteria, a defined structured log schema, and a decision about whether the strategy interface is a real plugin contract or a provisional internal abstraction.
--+
--+Claude recommended research workflow before plugin formalization, because real strategy experiments should teach what the plugin contract needs to be.
--+
--+### Gemini Contribution
--+
--+Gemini framed the project as a hypothesis-first research platform.
--+
--+The strongest point was that high-fidelity backtesting and strategy comparison are more valuable in milestone 1 than live dry-run, because live dry-run on a `1h` timeframe takes weeks to produce meaningful evidence.
--+
--+Gemini recommended sensitivity analysis over automated optimization to reduce curve fitting.
--+
--+## Synthesis
--+
--+### Canonical Problem Statement
--+
--+This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`.
--+
--+The first milestone should support historical backtesting, structured log-based observability, simulated portfolio monitoring, strategy comparison, and strategy hypothesis rejection without placing live orders or using real funds.
--+
--+Because no strategy hypothesis is confirmed yet, the architecture must help define, test, compare, monitor, and reject strategies honestly rather than assuming a profitable strategy already exists.
--+
--+### Settled Decisions
--+
--+- Milestone 1 is non-live.
--+- Historical backtesting comes before live market dry-run.
--+- Binance read-only account monitoring is deferred from milestone 1 unless Round 1 justifies a minimal future-compatible boundary.
--+- Portfolio monitoring starts as simulated portfolio state.
--+- Research workflow is central to milestone 1.
--+- Automated optimization is not a milestone 1 priority.
--+- Sensitivity analysis and comparison are preferred over parameter chasing.
--+- Structured logs are the first operator interface.
--+
--+### Remaining Round 1 Design Questions
--+
--+- What is the formal definition of done for milestone 1?
--+- What structured log format and event schema should be the first operator interface?
--+- Should the strategy extension boundary be a real plugin contract or a provisional internal abstraction?
--+- How should the research workflow prevent overfitting and false confidence?
--+- What baseline strategy, if any, should be included only to validate framework behavior?
--+- How much Binance order-rule simulation is necessary in historical backtesting?
--+- What metrics are required in milestone 1 versus later?
--+- Should backtesting use only `1h` OHLCV candles first, or should data storage leave room for higher-resolution candles later?
--+- Where should historical data be persisted: local files, SQLite, another database, or on-demand fetching with cache?
--+
--+## Decision
--+
--+Proceed to Round 1 candidate architecture proposals using `00-problem-brief.md` as the canonical problem brief.
--+
--+Round 1 architects should not reopen live trading as milestone 1 scope. They may propose minimal interface boundaries that keep future live dry-run possible without adding credentials, live runtime loops, or account integration now.
--+
--+## Next Actions
--+
--+1. Send `00-problem-brief.md` to Codex-Architect, Claude, and Gemini with Round 1 prompts.
--+2. Require each architect to answer the remaining design questions.
--+3. After receiving Round 1 proposals, run Round 2 cross-review.
--+
-- 
-- ```
-- 
--@@ -232,13 +4557,23 @@ Round 0 does not choose libraries, exchanges, strategies, infrastructure, or imp
--   - `Claude`
--   - `Gemini`
--   - `Codex-Arbiter`
---- The project name suggests a crypto bot, but the exact product scope is not yet defined.
--+- The first milestone should include backtesting, paper trading readiness, alerting, and portfolio monitoring.
--+- Milestone 1 must not use real funds. It should use backtesting and paper/dry-run behavior before any live execution is considered.
--+- The first market scope is Binance spot.
--+- The first assets are `BTC/USDT` and `ETH/USDT`.
--+- There is no confirmed strategy hypothesis yet.
--+- The first operator interface should be log files, not a web dashboard.
--+- The initial risk tolerance is maximum drawdown of `10-20%`.
--+- The initial backtest timeframe should be `1h`.
--+- The user is interested in both historical backtesting and live market dry-run, but is open to sequencing historical data first and live dry-run later.
--+- If live market dry-run is included, Binance read-only account support may be useful, but this is not confirmed.
--+- The user is interested in both a strategy plugin interface and a strategy research workflow.
-- 
-- ## Working Problem Statement
-- 
---ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.
--+This repo should start as a crypto research and safety-first automation project for Binance spot `BTC/USDT` and `ETH/USDT`. Milestone 1 should support backtesting, paper trading readiness, alerting, portfolio monitoring, and log-based auditability without placing live orders or using real funds.
-- 
---The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.
--+Because there is no confirmed strategy hypothesis yet, the immediate problem is not "build a profitable bot." The immediate problem is to design a narrow system that helps form, test, compare, and monitor trading hypotheses honestly under realistic costs and risk assumptions.
-- 
-- ## Round 0 Prompts
-- 
--@@ -300,15 +4635,15 @@ Assumptions:
-- 
-- Questions:
-- 
---- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
---- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
---- QUESTION: Is the bot allowed to place orders automatically?
---- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
---- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?
--+- QUESTION: Should milestone 1 include both historical backtesting and live market dry-run, or should live dry-run wait until historical simulation is trustworthy?
--+- QUESTION: Should Binance read-only account monitoring be included in milestone 1, or should portfolio monitoring start with simulated paper portfolio state only?
--+- QUESTION: Should the first architecture prioritize a strategy plugin interface, a strategy research workflow, or a parallel strategy-monitoring system?
--+- QUESTION: How should the system help discover or compare strategies when no hypothesis is confirmed yet?
--+- QUESTION: What first class of strategy should be used only as a baseline to test the framework, without implying it is profitable?
-- 
-- Recommendation:
-- 
---Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.
--+Keep Round 0 focused on defining a research/backtesting/paper-monitoring system, not a live trading bot. Do not choose a tech stack until strategy interface, data needs, and simulation fidelity are clearer.
-- 
-- Risks:
-- 
--@@ -337,6 +4672,8 @@ Questions:
-- - QUESTION: What should the bot do when market data, exchange APIs, or network connections fail?
-- - QUESTION: How should the operator review, override, pause, or audit bot behavior?
-- - QUESTION: What is the acceptable balance between speed, safety, and explainability?
--+- QUESTION: Since there is no strategy hypothesis yet, should the first milestone include strategy exploration tools, a plugin interface for manually supplied strategies, or both?
--+- QUESTION: If multiple strategies are evaluated in parallel, how should the operator avoid overfitting and false confidence?
-- 
-- Recommendation:
-- 
--@@ -376,6 +4713,8 @@ Questions:
-- - QUESTION: Is real money involved in milestone 1?
-- - QUESTION: Are signals/rules already defined, or is strategy design part of this repo?
-- - QUESTION: Does the bot need a UI, CLI, chat interface, API, or only background jobs?
--+- QUESTION: Should the first design sequence be historical candles first, then live WebSocket dry-run, then read-only portfolio monitoring?
--+- QUESTION: Does Binance read-only monitoring materially improve milestone 1, or does it add unnecessary security and setup complexity?
-- 
-- Recommendation:
-- 
--@@ -388,14 +4727,24 @@ Risks:
-- 
-- ## Codex-Arbiter Synthesis
-- 
--+### Round 0 Agent Answer Summary
--+
--+Codex-Architect framed the project as a non-live research and simulation system. The strongest point was sequencing: milestone 1 should prove trustworthy evaluation, reproducible results, structured audit logs, and rejection criteria before live market dry-run or read-only Binance account integration are assumed.
--+
--+Claude challenged the scope and argued that the project contains two different goals: research tooling and runtime infrastructure. The strongest point was that milestone 1 needs explicit exit criteria, a defined structured log schema, and a decision about whether the strategy interface is a real plugin contract or a provisional internal abstraction.
--+
--+Gemini framed the project as a hypothesis-first research platform. The strongest point was that high-fidelity backtesting and strategy comparison are more valuable in milestone 1 than live dry-run, because live dry-run on a `1h` timeframe takes weeks to produce meaningful evidence. Gemini also recommended sensitivity analysis over automated optimization to reduce curve fitting.
--+
-- Canonical problem statement:
-- 
---This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.
--+This repo should build a safety-first crypto research and paper-readiness system for Binance spot `BTC/USDT` and `ETH/USDT` on a first target timeframe of `1h`. The first milestone should support historical backtesting, alerting, log-based observability, and portfolio monitoring without placing live orders or using real funds. Live market dry-run and Binance read-only account monitoring are desirable but should be debated for sequencing and complexity. Because no strategy hypothesis is confirmed yet, the architecture must make strategy hypotheses easy to define, test, compare, monitor, and reject rather than assuming a profitable strategy already exists.
-- 
-- In scope for Round 0:
-- 
---- Clarifying bot type and first milestone.
---- Identifying risk, safety, and human-control requirements.
--+- Clarifying the first milestone around backtesting, paper trading readiness, alerts, portfolio monitoring, and log files.
--+- Identifying risk, safety, and human-control requirements for non-live operation.
--+- Clarifying data source and simulation fidelity requirements for Binance spot.
--+- Clarifying whether portfolio monitoring uses real read-only account data or simulated state.
-- - Recording blocking questions and assumptions.
-- - Preparing for candidate architecture designs in Round 1.
-- 
--@@ -405,30 +4754,289 @@ Out of scope for Round 0:
-- - Choosing exchange SDKs or trading libraries.
-- - Writing trading strategy code.
-- - Designing live order execution flows.
--+- Enabling real-money trading.
--+- Supporting leverage, futures, margin, or withdrawals.
-- 
-- Blocking questions:
-- 
---- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
---- Will the bot handle real funds or private keys in milestone 1?
---- What user approval or kill-switch controls are required?
---- What exchange, chain, wallet, or market-data source is targeted first?
---- What interface should the operator use first: CLI, web UI, chat, API, or background service only?
--+- What is the formal milestone 1 exit condition?
--+- What exact structured log format and event schema should be treated as the first operator interface?
--+- Should the strategy interface in milestone 1 be a real plugin contract or a provisional internal abstraction?
--+- What minimum simulation realism is required for milestone 1: fees only, fees plus spread/slippage, or partial fill/latency assumptions?
--+- What benchmark should strategy candidates be compared against, such as buy-and-hold, cash, or simple baseline strategies?
-- 
-- Non-blocking assumptions:
-- 
-- - The repo is early enough that workflow docs can define the decision process.
-- - The first implementation should be narrow and reversible.
-- - Safety and auditability should be treated as first-class design concerns.
--+- Binance is the initial exchange/data source.
--+- `BTC/USDT` and `ETH/USDT` are enough for milestone 1.
--+- Spot-only scope excludes leverage, margin, futures, and perpetuals.
--+- Log files are sufficient for the first operator interface if they are structured and easy to audit.
--+- Maximum drawdown of `10-20%` is a project-level risk boundary for evaluation and future paper/live controls.
--+- The first timeframe is `1h`.
--+- Live market dry-run should be sequenced after historical backtesting is reliable.
--+- Binance read-only account monitoring should be deferred unless Round 1 identifies a strong reason to include it.
--+- Milestone 1 portfolio monitoring can start with simulated portfolio state.
--+- The research workflow should prioritize comparison and sensitivity analysis over automated parameter optimization.
-- 
-- Decision:
-- 
---Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.
--+Proceed to Round 1 candidate designs with a narrower milestone: historical backtesting, simulated portfolio monitoring, structured logs, strategy comparison/research workflow, and a carefully scoped strategy extension boundary. Live market dry-run and Binance read-only account monitoring are deferred to milestone 2 unless an architect can justify a minimal interface stub that does not add credential or runtime complexity.
-- 
-- Next actions:
-- 
---1. User answers the blocking questions.
---2. Codex-Arbiter updates this document with the chosen first milestone.
---3. Round 1 begins with candidate designs constrained to that milestone.
--+1. Codex-Arbiter updates the neutral problem brief with this narrower milestone.
--+2. Codex-Architect, Claude, and Gemini propose Round 1 candidate architectures constrained to the non-live milestone.
--+3. Round 1 proposals must explicitly answer the remaining architecture questions: log schema, strategy boundary, data persistence, backtest realism, metrics, and anti-overfitting workflow.
--+
--+```
--+
--+### docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
--+
--+```text
--+# Round -1 - Trading Bot Principles
--+
--+Status: `draft`
--+Date: `2026-05-02`
--+Repo: `C:\Users\User\Documents\crypto-bot-ccg2`
--+
--+## Goal of This Round
--+
--+Build a shared baseline for the question:
--+
--+> What should a good and potentially profitable crypto trading bot have?
--+
--+This round happens before project-specific problem framing. The goal is to clarify principles, risks, evaluation standards, and false assumptions before deciding what this repo should build.
--+
--+Round -1 does not design this project, choose exchanges, select frameworks, or define a specific trading strategy.
--+
--+## Ground Rules
--+
--+- Do not claim guaranteed profit.
--+- Separate "good bot qualities" from "profitability requirements".
--+- Treat risk controls, auditability, and validation as first-class concerns.
--+- Assume backtest results can be misleading until proven otherwise.
--+- Do not recommend live trading before paper trading and risk boundaries are defined.
--+- Mark assumptions as `ASSUMPTION`.
--+- Mark questions as `QUESTION`.
--+
--+## Shared Question
--+
--+What should a good and potentially profitable crypto trading bot have?
--+
--+## Agent Focus
--+
--+### Codex-Architect
--+
--+Focus on:
--+
--+- System qualities.
--+- Architecture implications.
--+- Testing and verification.
--+- Observability and audit logs.
--+- Maintainability and safe iteration.
--+
--+### Claude
--+
--+Focus on:
--+
--+- Flawed assumptions.
--+- Human risk and overconfidence.
--+- Decision boundaries.
--+- Edge cases and failure modes.
--+- What should remain human-approved.
--+
--+### Gemini
--+
--+Focus on:
--+
--+- Alternative bot types.
--+- Market and data constraints.
--+- Exchange and integration risks.
--+- Evaluation methods.
--+- External constraints that could dominate design.
--+
--+## Questions for Agents
--+
--+Each agent should answer:
--+
--+1. What makes a crypto trading bot good?
--+2. What conditions are required before it can plausibly be profitable?
--+3. What risk controls are non-negotiable?
--+4. What data, testing, and validation are required?
--+5. What common false assumptions should we avoid?
--+6. What should be excluded from MVP?
--+7. What are the 10 most important questions before designing our bot?
--+
--+## Initial Shared Baseline
--+
--+Good bot qualities:
--+
--+- Clear operating mode: alerts, research, backtesting, paper trading, or live execution.
--+- Separation between market data, strategy logic, risk controls, execution, state, and reporting.
--+- Full audit trail for inputs, decisions, orders, errors, overrides, and configuration changes.
--+- Deterministic replay/debug mode for understanding past decisions.
--+- Operator controls for pause, kill switch, configuration review, and emergency shutdown.
--+- Safe secret handling if exchange API keys or wallet credentials ever become involved.
--+- Tests for strategy logic, risk logic, execution adapters, and failure handling.
--+
--+Profitability requirements:
--+
--+- A testable hypothesis for why the strategy should have edge.
--+- Historical validation without look-ahead bias, survivorship bias, or data leakage.
--+- Evaluation after fees, spread, slippage, funding rates, latency, and failed orders.
--+- Out-of-sample testing or walk-forward validation.
--+- Paper trading before live trading.
--+- Position sizing and drawdown controls.
--+- Monitoring for market regime changes.
--+
--+Non-negotiable risk controls:
--+
--+- Max position size.
--+- Max daily loss.
--+- Max drawdown.
--+- Per-trade risk limit.
--+- Exchange/API failure handling.
--+- Duplicate order protection.
--+- Kill switch.
--+- Dry-run or paper mode.
--+- Read-only mode for analysis features.
--+- Human approval mode before live automation.
--+
--+Common false assumptions:
--+
--+- Backtest profit means future profit.
--+- High win rate means good strategy.
--+- AI can reliably predict sudden market moves.
--+- More indicators mean better signals.
--+- Live trading is just backtesting with real orders.
--+- Exchange APIs behave reliably during volatility.
--+- Fees and slippage are small enough to ignore.
--+- A bot should trade often to be useful.
--+
--+## Codex-Arbiter Synthesis Template
--+
--+After the three agents answer, produce:
--+
--+1. Shared principles accepted by all agents.
--+2. Disagreements or tensions worth preserving.
--+3. Non-negotiable safety requirements.
--+4. Evaluation standards for profitability claims.
--+5. MVP exclusions.
--+6. Questions that should flow into Round 0.
--+
--+## Agent Answer Summary
--+
--+### Codex-Architect
--+
--+Codex-Architect framed a good bot as a controlled, observable, testable decision and execution system. The strongest points were separation of strategy, execution, risk, data, configuration, and monitoring; deterministic testing; fail-safe behavior; idempotent execution; strong state reconciliation; and explicit modes for backtest, paper, shadow, and live trading.
--+
--+Codex-Architect emphasized that profitability requires a real market edge after fees, spread, slippage, latency, funding, failed orders, and regime changes. It also stressed that the bot should support strategy retirement when live performance diverges from expectations.
--+
--+### Claude
--+
--+Claude focused on adversarial clarity and warned that the most common failure is starting implementation before the strategy hypothesis is honest. The strongest points were that profitability belongs to the strategy, market, cost structure, execution quality, and timing together, not to the bot by itself.
--+
--+Claude emphasized falsifiable strategy hypotheses, out-of-sample validation, hard drawdown circuit breakers, UTC/time discipline, human restart after major risk events, and predefined failure conditions for stopping the project or strategy.
--+
--+### Gemini
--+
--+Gemini emphasized alternative bot types, market/data constraints, and execution realities. The strongest points were operational resilience, telemetry, exchange integration risk, low-latency path where relevant, high-fidelity data handling, inventory management for market making or arbitrage, and the need to define the intended market regime.
--+
--+Gemini also highlighted tick-to-trade latency, partial fills, orphan orders, WebSocket/REST divergence, maker/taker fee assumptions, fat-tail events, and kill-switch authority.
--+
--+## Codex-Arbiter Synthesis
--+
--+### Shared Principles Accepted by All Agents
--+
--+- A good crypto trading bot is first a safety-critical automation system, not a profit machine.
--+- Strategy logic, risk controls, exchange execution, data ingestion, state management, configuration, monitoring, and reporting should be separated.
--+- Every trade decision must be auditable after the fact from logs and stored state.
--+- The bot must fail safely when data, connectivity, exchange APIs, or internal state become unreliable.
--+- Backtest profitability is not sufficient evidence of live profitability.
--+- Profitability claims must include fees, spread, slippage, latency, partial fills, failed orders, funding or borrow costs where relevant, and market regime effects.
--+- Paper trading is necessary before live trading, but paper trading is still not proof of live profitability.
--+- Risk controls belong in the MVP, not after the MVP.
--+- The first version should be narrow, explainable, and easy to shut down.
--+
--+### Disagreements or Tensions Worth Preserving
--+
--+- Claude recommends excluding dashboard and alerting from MVP, while Codex-Architect treats observability from day one as essential. The synthesis is: avoid a complex UI dashboard, but keep operational logs, basic metrics, and alerts for dangerous states.
--+- Gemini mentions a low-latency path, while Claude warns latency must match the strategy horizon. The synthesis is: do not optimize for low latency generally; define latency requirements only after the strategy type and timeframe are chosen.
--+- Claude prefers no auto-restart on crash, while production systems often need recovery behavior. The synthesis is: allow process restart only into a safe paused/reconcile mode, not automatic trading resumption.
--+- Codex-Architect assumes the bot may eventually trade real capital. Round 0 must confirm whether real funds are in scope for milestone 1.
--+
--+### Non-Negotiable Safety Requirements
--+
--+- Read-only, paper, and live modes must be explicit and hard to confuse.
--+- No withdrawal permissions for any exchange API key used by the bot.
--+- Kill switch must cancel open orders where possible and disable new trading.
--+- The bot must reconcile exchange/account state before trading on startup, reconnect, or restart.
--+- Duplicate order protection is required.
--+- Hard maximums are required for order size, position size, portfolio exposure, daily loss, drawdown, open orders, and order rate.
--+- The bot must halt or enter safe mode on stale data, repeated exchange errors, abnormal slippage, rejected orders, reconciliation mismatch, or connectivity loss.
--+- Human approval should be required before live automation and before scaling capital.
--+- All timestamps should be consistent and timezone-aware, preferably UTC internally.
--+- Every signal, order intent, order response, fill, cancellation, error, override, and configuration change must be logged.
--+
--+### Evaluation Standards for Profitability Claims
--+
--+- The strategy must have a falsifiable hypothesis explaining why an edge should exist.
--+- Backtests must avoid look-ahead bias, data leakage, and excessive parameter fitting.
--+- Validation must include out-of-sample data or walk-forward testing.
--+- Evaluation must include multiple market regimes where possible.
--+- Results must be measured after fees, spread, slippage, latency, partial fills, failed orders, and funding or borrow costs where relevant.
--+- Metrics should include total return, profit factor, Sharpe or Sortino, max drawdown, drawdown duration, win/loss distribution, tail losses, turnover, exposure, and sensitivity to parameters.
--+- Paper trading must compare expected fills against simulated or actual paper fills.
--+- Live trading, if ever allowed, should start with minimal capital and require evidence that live behavior matches expected behavior.
--+- A strategy must have predefined retirement or pause criteria when live performance diverges from expectations.
--+
--+### MVP Exclusions
--+
--+- Leverage, margin, perpetuals, and futures unless explicitly chosen later with separate risk design.
--+- Multiple exchanges.
--+- Multiple unrelated strategies.
--+- Cross-exchange arbitrage.
--+- High-frequency trading.
--+- Complex machine learning or automatic strategy discovery.
--+- Auto-optimization against recent backtests.
--+- Social/news sentiment trading.
--+- Copy trading.
--+- Withdrawal automation.
--+- Fully autonomous capital scaling.
--+- Complex UI dashboards beyond minimal operational visibility.
--+- Any feature that makes trades harder to explain.
--+
--+### Questions That Flow Into Round 0
--+
--+- QUESTION: What specific bot type is milestone 1: alerting, research, backtesting, paper trading, live spot trading, market making, arbitrage, portfolio tracking, or something else?
--+- QUESTION: What falsifiable market hypothesis do we want to test first?
--+- QUESTION: What market regime is the first strategy intended for?
--+- QUESTION: What trading horizon is targeted: seconds, minutes, hours, days, or longer?
--+- QUESTION: Which asset universe is allowed for milestone 1?
--+- QUESTION: Which exchange or data source is targeted first?
--+- QUESTION: Will milestone 1 involve real funds, or only read-only/paper mode?
--+- QUESTION: What maximum loss or drawdown is acceptable before the bot must halt?
--+- QUESTION: What evidence is required before moving from backtest to paper, and from paper to live?
--+- QUESTION: Who can trigger the kill switch, and what should the recovery protocol be?
--+- QUESTION: What interface should the operator use first: CLI, logs, simple dashboard, API, or chat?
--+- QUESTION: What monitoring is mandatory from day one?
--+- QUESTION: What is the minimum acceptable audit trail for every decision?
--+
--+## Decision
--+
--+Round -1 establishes the baseline: this project should not frame the first milestone as "build a profitable bot." It should frame the first milestone as "build a narrow, safe, auditable system for testing one falsifiable trading hypothesis under realistic costs and failure conditions."
--+
--+Proceed to Round 0 only after the user chooses the first milestone and answers the blocking questions about bot type, automation level, target market, target data source/exchange, allowed risk, and operator controls.
--+
--+## Next Actions
--+
--+1. Use this synthesis as input to Round 0 problem framing.
--+2. User answers the Round 0 blocking questions, especially bot type and whether real funds are in scope.
--+3. Codex-Arbiter updates `round-0-problem-framing.md` with the chosen first milestone.
--+4. Round 1 begins only after the problem brief is narrow enough for candidate architectures.
-- 
-- ```
-- 
--@@ -490,14 +5098,85 @@ Use these prompts as copy/paste templates for the multi-agent design workflow.
-- 
-- Recommended order:
-- 
---1. `round0-problem-framing.md`
---2. `round0-brief-synthesis.md`
---3. `round1-codex-architect.md`
---4. `round1-external-architect.md`
---5. `round2-cross-review.md`
---6. `round3-arbiter.md`
--+1. `round-minus-1-trading-bot-principles.md`
--+2. `round0-problem-framing.md`
--+3. `round0-brief-synthesis.md`
--+4. `round1-codex-architect.md`
--+5. `round1-external-architect.md`
--+6. `round2-cross-review.md`
--+7. `round3-arbiter.md`
-- 
---Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.
--+Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.
--+
--+```
--+
--+### prompts\round-minus-1-trading-bot-principles.md
--+
--+```text
--+# Round -1 - Trading Bot Principles
--+
--+You are participating in a multi-agent software design workflow.
--+
--+Round:
--+Round -1 - Trading Bot Principles
--+
--+Question:
--+"What should a good and potentially profitable crypto trading bot have?"
--+
--+Rules:
--+- Do not design this specific project yet.
--+- Do not choose frameworks, exchanges, or libraries.
--+- Do not claim guaranteed profits.
--+- Separate "good bot qualities" from "profitability requirements".
--+- Focus on principles, risks, and evaluation criteria.
--+- Mark assumptions as `ASSUMPTION`.
--+- Mark questions as `QUESTION`.
--+
--+Your role:
--+
--+```text
--+[Codex-Architect / Claude / Gemini]
--+```
--+
--+Role focus:
--+
--+```text
--+[Codex-Architect: system qualities, architecture implications, testing, observability, maintainability]
--+[Claude: flawed assumptions, human risk, decision boundaries, overconfidence, edge cases]
--+[Gemini: alternative bot types, market/data constraints, exchange/integration risks, evaluation methods]
--+```
--+
--+Task:
--+1. What makes a crypto trading bot good?
--+2. What conditions are required before it can plausibly be profitable?
--+3. What risk controls are non-negotiable?
--+4. What data, testing, and validation are required?
--+5. What common false assumptions should we avoid?
--+6. What should be excluded from MVP?
--+7. What are the 10 most important questions before designing our bot?
--+
--+Return format:
--+
--+```md
--+## Role
--+
--+## Good Bot Qualities
--+
--+## Profitability Requirements
--+
--+## Non-Negotiable Risk Controls
--+
--+## Data, Testing, and Validation
--+
--+## False Assumptions to Avoid
--+
--+## Exclude from MVP
--+
--+## Questions Before Design
--+- QUESTION:
--+
--+## Recommendation
--+```
-- 
-- 
-- ```
--@@ -872,16 +5551,18 @@ This repo starts with a multi-agent design workflow before implementation.
-- 
-- The intended loop is:
-- 
---1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
---2. Codex-Arbiter turns the answers into a neutral problem brief.
---3. Round 1: each architect proposes a design from the same brief.
---4. Round 2: agents critique the candidate designs.
---5. Round 3: Codex-Arbiter records the final architecture.
---6. Round 4: Codex implements the accepted plan and runs verification.
--+1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
--+2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
--+3. Codex-Arbiter turns the answers into a neutral problem brief.
--+4. Round 1: each architect proposes a design from the same brief.
--+5. Round 2: agents critique the candidate designs.
--+6. Round 3: Codex-Arbiter records the final architecture.
--+7. Round 4: Codex implements the accepted plan and runs verification.
-- 
-- Start here:
-- 
-- - [Workflow README](docs/multi-agent-design-workflow/README.md)
--+- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
-- - [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
-- - [Prompt Library](prompts/README.md)
-- 
--@@ -890,12 +5571,17 @@ Start here:
-- Create a context pack for review:
-- 
-- ```powershell
---python tools/make_context.py --task "Describe the current design question"
--+py tools/make_context.py --task "Describe the current design question"
-- ```
-- 
-- The generated file goes to `reviews/latest/context-pack.md`.
-- 
--+```
-- 
--+### reviews\latest\context-pack.md
--+
--+```text
--+[Skipped: file is 209771 bytes, above 24000 byte limit]
-- ```
-- 
-- ### tools\make_context.py
-+-Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), the canonical [Problem Brief](./00-problem-brief.md), [Round 1 Candidate Designs](./round-1-candidate-designs.md), and [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).
-++Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), the canonical [Problem Brief](./00-problem-brief.md), [Round 1 Candidate Designs](./round-1-candidate-designs.md), [Round 2 Cross Review](./round-2-cross-review.md), and [Round 3 Arbiter Brief](./round-3-arbiter-brief.md).
- 
- [stderr]
--warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
- warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF will be replaced by CRLF the next time Git touches it
--warning: in the working copy of 'docs/multi-agent-design-workflow/round-0-problem-framing.md', LF will be replaced by CRLF the next time Git touches it
--warning: in the working copy of 'prompts/README.md', LF will be replaced by CRLF the next time Git touches it
- ```
- 
- ## File Tree
-@@ -5237,6 +51,8 @@ warning: in the working copy of 'prompts/README.md', LF will be replaced by CRLF
- - docs\multi-agent-design-workflow\round-0-problem-framing.md
- - docs\multi-agent-design-workflow\round-1-candidate-designs.md
- - docs\multi-agent-design-workflow\round-2-cross-review-brief.md
-+- docs\multi-agent-design-workflow\round-2-cross-review.md
-+- docs\multi-agent-design-workflow\round-3-arbiter-brief.md
- - docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
- - docs\multi-agent-design-workflow\round-template.md
- - prompts\README.md
-@@ -5516,6 +332,7 @@ The workflow is round-based. Each round produces a short decision record that ca
-    - Start from [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).
- 6. `Round 3 - Synthesis`
-    - Codex-Arbiter selects or combines a direction and records tradeoffs.
-+   - Start from [Round 3 Arbiter Brief](./round-3-arbiter-brief.md).
- 7. `Round 4 - Implementation Plan`
-    - Convert the selected design into files, tasks, tests, and rollout steps.
- 
-@@ -5534,7 +351,7 @@ The workflow is round-based. Each round produces a short decision record that ca
- 
- ## Current Starting Point
- 
--Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), the canonical [Problem Brief](./00-problem-brief.md), [Round 1 Candidate Designs](./round-1-candidate-designs.md), and [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).
-+Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), the canonical [Problem Brief](./00-problem-brief.md), [Round 1 Candidate Designs](./round-1-candidate-designs.md), [Round 2 Cross Review](./round-2-cross-review.md), and [Round 3 Arbiter Brief](./round-3-arbiter-brief.md).
- 
- ```
- 
-@@ -6193,6 +1010,297 @@ Return concrete findings with severity, evidence, why it matters, and suggested
- ```
- 
- 
-+```
-+
-+### docs\multi-agent-design-workflow\round-2-cross-review.md
-+
-+```text
-+# Round 2 - Cross Review
-+
-+Status: `complete`
-+Date: `2026-05-02`
-+Source:
-+
-+- `00-problem-brief.md`
-+- `round-1-candidate-designs.md`
-+- Codex-Architect Round 2 answer
-+- Claude Round 2 answer
-+- Gemini Round 2 answer
-+
-+## Purpose
-+
-+Round 2 challenges the Round 1 candidate architectures and identifies which design choices should be combined, rejected, deferred, or escalated to Codex-Arbiter for Round 3.
-+
-+## Strong Consensus
-+
-+All reviewers support:
-+
-+- Local-first CLI research workbench.
-+- No live trading in milestone 1.
-+- No credentials in milestone 1.
-+- No read-only Binance account monitoring in milestone 1.
-+- No dynamic plugin system in milestone 1.
-+- Event-driven backtesting.
-+- Strategy metadata, especially required `hypothesis` and `version`.
-+- Structured JSONL event logs for run auditability.
-+- Immutable run directories.
-+- Public Binance historical data only.
-+- Research workflow focused on rejection, comparison, and sensitivity analysis.
-+- No automated optimizer that searches for the best-looking backtest.
-+
-+## Major Agreements
-+
-+### Hybrid Storage
-+
-+Codex-Architect and Claude agree that the best storage model is hybrid:
-+
-+- Parquet or similar columnar format for normalized historical candle data.
-+- JSONL for run/event logs.
-+- JSON reports and frozen config/metadata snapshots inside each run directory.
-+
-+Gemini also supports Parquet for market data and JSONL for logs.
-+
-+Decision pressure:
-+
-+- High confidence. Round 3 should adopt hybrid storage unless implementation constraints make Parquet impractical.
-+
-+### Strategy Boundary
-+
-+The combined recommendation is not a heavy abstract base class and not a metadata-free pure function.
-+
-+Preferred shape:
-+
-+- A small protocol-style internal strategy interface.
-+- Required metadata:
-+  - `name`
-+  - `version`
-+  - `hypothesis`
-+  - parameter schema/defaults
-+  - warmup requirements
-+- Signal behavior should remain function-like and deterministic.
-+- Engine owns state, simulation, portfolio, logging, and evaluation.
-+
-+Decision pressure:
-+
-+- High confidence. Round 3 should adopt a metadata-bearing protocol with pure-function-like strategy logic.
-+
-+### Drawdown Behavior
-+
-+Codex-Architect recommends supporting both `flag_only` and `halt_on_breach`.
-+
-+Claude recommends always running to completion and using drawdown breach as a verdict gate.
-+
-+Gemini ranks drawdown behavior as lower priority and supports flagging unless portfolio hits zero.
-+
-+Decision pressure:
-+
-+- Medium-high confidence. Round 3 should likely choose run-to-completion as default research mode, record `DRAWDOWN_BREACHED`, and block any verdict better than `REJECT` or `CONDITIONAL`. Optional `halt_on_breach` may be added as a separate risk-control simulation mode later.
-+
-+### Baselines and Benchmarks
-+
-+Codex-Architect recommends:
-+
-+- cash/no-trade
-+- buy-and-hold
-+- simple rule strategy such as SMA crossover
-+
-+Claude strongly argues that buy-and-hold is the primary active-strategy benchmark and SMA crossover should be engine validation only.
-+
-+Decision pressure:
-+
-+- High confidence. Round 3 should include buy-and-hold benchmark, cash/no-trade baseline, and one simple engine-validation strategy.
-+
-+## Major Disagreement
-+
-+### 1m Dual-Resolution Fill Validation
-+
-+Gemini argues strongly that `1h` OHLCV creates a fidelity gap, especially for stop-loss/take-profit ordering inside a candle. Gemini recommends `1h` signals with `1m` candles for fill validation.
-+
-+Codex-Architect and Claude recommend deferring `1m` from milestone 1:
-+
-+- Milestone 1 is about historical research and hypothesis rejection.
-+- `1m` ingestion/validation/storage/test complexity is large.
-+- No chosen strategy currently requires stop-loss/take-profit ordering.
-+- Required pessimistic slippage and explicit report warnings may be enough for first milestone.
-+
-+Synthesis:
-+
-+- Gemini is right about the fidelity risk.
-+- Codex-Architect and Claude are likely right about milestone scope.
-+- The final architecture should not depend on `1m` data for MVP completion.
-+- The market data layer should be designed so `1m` data can be added later.
-+- Reports must explicitly flag when a strategy's claim depends on intrabar price ordering or fill precision.
-+- Round 3 should decide whether `1m` is:
-+  - deferred entirely to milestone 2, or
-+  - represented as an optional future-compatible data resolution but not required for MVP.
-+
-+## Critical Issues Raised
-+
-+### Log Schema Is the Primary Interface
-+
-+Claude argues that all proposals underspecify the log schema, even though structured logs are the first operator interface.
-+
-+Round 3 should require v1 field-level schema before implementation for at least:
-+
-+- `run.started`
-+- `data.loaded`
-+- `data.validation_warning`
-+- `strategy.signal`
-+- `simulation.order_intent`
-+- `simulation.order_rejected`
-+- `simulation.fill`
-+- `portfolio.snapshot`
-+- `risk.limit_warning`
-+- `alert.generated`
-+- `metrics.summary`
-+- `run.completed`
-+- `run.failed`
-+
-+Round 3 should also define event volume policy:
-+
-+- Always log run metadata, validation warnings, signals, order intents, fills/rejections, risk warnings, alerts, and final metrics.
-+- Portfolio snapshots should be periodic and on meaningful changes by default.
-+- Full candle-by-candle logging should be debug mode, not default.
-+
-+### Anti-Overfitting Is Under-Specified
-+
-+Claude identifies anti-overfitting as a core product requirement, not a nice-to-have.
-+
-+Round 3 should include:
-+
-+- Declared train/test split before runs.
-+- In-sample and out-of-sample labels on every run.
-+- Trade count floor for result validity.
-+- Sensitivity band reporting.
-+- Benchmark comparison.
-+- Warnings for narrow parameter bands.
-+- No auto-selection of best parameters.
-+
-+### Post-Processing Limits
-+
-+Codex-Architect warns that post-processing sensitivity or Monte Carlo slippage is only valid when it does not alter simulated state.
-+
-+Round 3 should distinguish:
-+
-+- Safe post-processing:
-+  - metrics recalculation
-+  - report formatting
-+  - simple sensitivity on assumptions that do not change fills/signals
-+- Must rerun simulation:
-+  - slippage changes that affect fills
-+  - rejected order scenarios
-+  - balance/exposure changes
-+  - anything that could alter future signals
-+
-+## Ranked Decisions for Round 3
-+
-+1. Log schema and event volume policy.
-+2. Anti-overfitting workflow.
-+3. Hybrid storage format.
-+4. Strategy boundary.
-+5. Backtest fidelity and whether `1m` is deferred or optional.
-+6. Drawdown handling and verdict gating.
-+7. Baselines and benchmarks.
-+8. Definition of done.
-+
-+## Recommended Combined Architecture for Arbiter
-+
-+Round 3 should combine:
-+
-+- Codex-Architect's module boundaries.
-+- Claude's file-per-run, schema-versioning, immutability, verdict discipline, and anti-overfitting workflow.
-+- Gemini's Parquet market-data storage insight, functional strategy discipline, and fidelity warning around `1h` OHLCV.
-+
-+Recommended defaults:
-+
-+- Market data: Parquet, partitioned by symbol/timeframe.
-+- Event logs: JSONL, versioned schema, one immutable directory per run.
-+- Backtester: deterministic event-driven replay.
-+- Strategy boundary: protocol with required metadata and function-like signal generation.
-+- Timeframe: `1h` required for MVP.
-+- `1m` data: deferred from MVP, but supported later by storage shape.
-+- Fill model: required fee and pessimistic slippage assumptions.
-+- Drawdown: run to completion by default; breach gates verdict.
-+- Benchmarks: cash/no-trade, buy-and-hold, and simple SMA crossover for engine validation.
-+- Verdicts: `REJECT`, `INSUFFICIENT_DATA`, `CONDITIONAL`, `CANDIDATE`; never `APPROVE`.
-+
-+## Next Actions
-+
-+1. Codex-Arbiter produces `round-3-final-architecture.md`.
-+2. Round 3 should explicitly decide the `1m` fidelity question.
-+3. Round 3 should define milestone 1 done criteria.
-+4. Round 3 should produce an implementation plan outline for Round 4.
-+
-+
-+```
-+
-+### docs\multi-agent-design-workflow\round-3-arbiter-brief.md
-+
-+```text
-+# Round 3 - Arbiter Brief
-+
-+Status: `ready`
-+Date: `2026-05-02`
-+
-+## Inputs
-+
-+Use these files:
-+
-+- `00-problem-brief.md`
-+- `round-1-candidate-designs.md`
-+- `round-2-cross-review.md`
-+
-+## Arbiter Task
-+
-+Produce the final architecture decision for milestone 1.
-+
-+You must decide:
-+
-+- Storage model.
-+- Strategy boundary.
-+- Backtest fidelity.
-+- Log schema/event policy.
-+- Anti-overfitting workflow.
-+- Drawdown behavior.
-+- Benchmarks and baselines.
-+- Milestone 1 definition of done.
-+
-+## Constraints
-+
-+Do not reopen:
-+
-+- Live trading in milestone 1.
-+- Binance credentials in milestone 1.
-+- Read-only account monitoring in milestone 1.
-+- Dynamic plugin loading in milestone 1.
-+- Web dashboard in milestone 1.
-+
-+## Decisions the Arbiter Should Likely Adopt
-+
-+- Hybrid storage: Parquet for market data, JSONL for run events.
-+- Deterministic event-driven backtesting.
-+- Metadata-bearing strategy protocol with function-like signal generation.
-+- `1h` data required for MVP.
-+- `1m` data deferred but made possible by storage partitioning.
-+- Required fee and pessimistic slippage assumptions.
-+- Run-to-completion default with `DRAWDOWN_BREACHED` verdict gating.
-+- Buy-and-hold and cash/no-trade benchmarks.
-+- SMA crossover as engine-validation strategy only.
-+- Versioned v1 event schema before implementation.
-+- Declared train/test split and in-sample/out-of-sample labels.
-+
-+## Open Decision Needing Care
-+
-+The only major unresolved disagreement is `1m` dual-resolution fill validation.
-+
-+Recommended stance:
-+
-+- Do not make `1m` data a milestone 1 requirement.
-+- Do design market data storage and simulation interfaces so additional timeframes can be added later.
-+- Reports must warn when a strategy relies on intrabar fill assumptions.
-+- Any strategy requiring stop-loss/take-profit ordering inside a candle cannot be promoted beyond `CONDITIONAL` until higher-fidelity validation exists.
-+
-+
- ```
- 
- ### docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
-@@ -6983,7 +2091,7 @@ The generated file goes to `reviews/latest/context-pack.md`.
- ### reviews\latest\context-pack.md
- 
- ```text
--[Skipped: file is 273430 bytes, above 24000 byte limit]
-+[Skipped: file is 348283 bytes, above 24000 byte limit]
- ```
- 
- ### tools\make_context.py
+ ## Operating Rules
 
 [stderr]
 warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF will be replaced by CRLF the next time Git touches it
@@ -5639,6 +46,7 @@ warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF
 - docs\multi-agent-design-workflow\round-2-cross-review.md
 - docs\multi-agent-design-workflow\round-3-arbiter-brief.md
 - docs\multi-agent-design-workflow\round-3-final-architecture.md
+- docs\multi-agent-design-workflow\round-4-implementation-plan.md
 - docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
 - docs\multi-agent-design-workflow\round-template.md
 - prompts\README.md
@@ -5922,6 +330,7 @@ The workflow is round-based. Each round produces a short decision record that ca
    - Final decision: [Round 3 Final Architecture](./round-3-final-architecture.md).
 7. `Round 4 - Implementation Plan`
    - Convert the selected design into files, tasks, tests, and rollout steps.
+   - Start from [Round 4 Implementation Plan](./round-4-implementation-plan.md).
 
 ## Operating Rules
 
@@ -7218,6 +1627,365 @@ Milestone 1 is done when:
    - anti-overfitting workflow
 
 
+```
+
+### docs\multi-agent-design-workflow\round-4-implementation-plan.md
+
+```text
+# Round 4 - Implementation Plan
+
+Status: `draft`
+Date: `2026-05-02`
+Source:
+
+- `round-3-final-architecture.md`
+
+## Goal
+
+Convert the final architecture into an implementation plan for milestone 1.
+
+Milestone 1 builds a local-first crypto research workbench with deterministic historical backtesting, simulated portfolio accounting, structured logs, benchmark comparison, sensitivity analysis, and cautious research verdicts.
+
+## Proposed Project Layout
+
+```text
+crypto-bot-ccg2/
+  pyproject.toml
+  README.md
+  config/
+    example-run.yaml
+  data/
+    market/
+      .gitkeep
+  logs/
+    schema/
+      v1/
+        run.started.schema.json
+        strategy.signal.schema.json
+        simulation.fill.schema.json
+        portfolio.snapshot.schema.json
+        run.completed.schema.json
+    runs/
+      .gitkeep
+  src/
+    cbot/
+      __init__.py
+      cli.py
+      config.py
+      types.py
+      market_data/
+        __init__.py
+        binance.py
+        store.py
+        validation.py
+      strategies/
+        __init__.py
+        protocol.py
+        baselines.py
+        sma_cross_v1.py
+      engine/
+        __init__.py
+        backtest.py
+        execution.py
+        portfolio.py
+        events.py
+      research/
+        __init__.py
+        metrics.py
+        reporter.py
+        compare.py
+        sensitivity.py
+        verdicts.py
+  tests/
+    test_config.py
+    test_market_data_validation.py
+    test_strategy_protocol.py
+    test_backtest_determinism.py
+    test_execution_simulator.py
+    test_portfolio.py
+    test_events_schema.py
+    test_metrics_verdicts.py
+```
+
+## Dependency Plan
+
+Keep dependencies small.
+
+Required:
+
+- `pandas` or `polars` for data handling.
+- `pyarrow` for Parquet support.
+- `requests` or `httpx` for public Binance historical candle fetching.
+- `pydantic` or `dataclasses` plus manual validation for config/domain objects.
+- `PyYAML` for run configs.
+- `pytest` for tests.
+- `jsonschema` for validating event logs against v1 schemas.
+
+Recommended initial choice:
+
+- Use `pandas` + `pyarrow` because they are familiar and stable.
+- Use `dataclasses` for core domain types unless validation complexity forces `pydantic`.
+- Use `argparse` first for CLI unless command complexity grows.
+
+## CLI Commands
+
+Milestone 1 should expose these commands:
+
+```powershell
+py -m cbot.cli fetch-data --symbol BTCUSDT --timeframe 1h --start 2021-01-01 --end 2024-12-31
+py -m cbot.cli backtest --config config/example-run.yaml
+py -m cbot.cli compare --runs logs/runs/run_a logs/runs/run_b
+py -m cbot.cli sensitivity --config config/example-run.yaml --param fast_window --values 10,20,30
+py -m cbot.cli report --run logs/runs/<run_id>
+```
+
+## Configuration Shape
+
+`config/example-run.yaml`:
+
+```yaml
+run:
+  label: sma_cross_smoke
+  sample_label: IN_SAMPLE
+  train_start: "2021-01-01"
+  train_end: "2023-12-31"
+  test_start: "2024-01-01"
+  test_end: "2024-12-31"
+
+market:
+  exchange: binance
+  symbol: BTCUSDT
+  quote: USDT
+  timeframe: 1h
+
+strategy:
+  name: sma_cross_v1
+  version: "1.0.0"
+  parameters:
+    fast_window: 20
+    slow_window: 50
+
+portfolio:
+  initial_cash: 10000
+  base_asset: BTC
+  quote_asset: USDT
+
+simulation:
+  fee_bps: 10
+  slippage_bps: 20
+  max_drawdown_pct: 20
+  min_trade_count: 30
+  drawdown_mode: flag_only
+```
+
+## Core Domain Types
+
+Define shared types in `src/cbot/types.py`:
+
+- `Candle`
+- `Signal`
+- `OrderIntent`
+- `Fill`
+- `PortfolioSnapshot`
+- `RunMetadata`
+- `StrategyMetadata`
+- `MetricSummary`
+- `Verdict`
+
+Keep these small and serializable.
+
+## v1 Event Schema
+
+Define field-level JSON Schema before engine implementation.
+
+Minimum schemas:
+
+- `run.started`
+- `strategy.signal`
+- `simulation.fill`
+- `portfolio.snapshot`
+- `run.completed`
+
+All event records should include:
+
+- `schema_version`
+- `event_type`
+- `run_id`
+- `timestamp`
+- `sequence`
+
+Recommended common envelope:
+
+```json
+{
+  "schema_version": "1.0",
+  "event_type": "strategy.signal",
+  "run_id": "run_20260502_160000_sma_cross",
+  "timestamp": "2024-01-01T01:00:00Z",
+  "sequence": 42,
+  "payload": {}
+}
+```
+
+## Implementation Slices
+
+### Slice 1 - Project Skeleton
+
+Create:
+
+- `pyproject.toml`
+- source package
+- tests folder
+- config example
+- data/log directories
+
+Acceptance:
+
+- `pytest` runs.
+- `py -m cbot.cli --help` works.
+
+### Slice 2 - Event Schema and Logger
+
+Create:
+
+- JSON Schema files.
+- event envelope type.
+- append-only JSONL writer.
+- run directory creation.
+- frozen config and strategy metadata output.
+
+Acceptance:
+
+- event schema tests pass.
+- a fake run can write valid JSONL events.
+
+### Slice 3 - Market Data Layer
+
+Create:
+
+- Binance public OHLCV fetcher.
+- candle validator.
+- Parquet store partitioned by symbol/timeframe.
+- local read path.
+
+Acceptance:
+
+- can fetch and persist sample `BTCUSDT` `1h` candles.
+- validation catches duplicate, missing, and unordered candles.
+- no credentials are needed.
+
+### Slice 4 - Strategy Protocol and Baselines
+
+Create:
+
+- strategy protocol.
+- `cash_no_trade`.
+- `buy_and_hold`.
+- `sma_cross_v1`.
+
+Acceptance:
+
+- strategies expose required metadata.
+- strategy logic is deterministic for fixed inputs.
+- invalid parameters fail clearly.
+
+### Slice 5 - Backtest Engine
+
+Create:
+
+- deterministic candle replay.
+- warmup handling.
+- no-future-data boundary.
+- signal event emission.
+
+Acceptance:
+
+- same input run produces same event stream.
+- golden dataset test proves no future candle access.
+
+### Slice 6 - Execution and Portfolio Simulation
+
+Create:
+
+- order-intent conversion.
+- fee/slippage application.
+- insufficient balance rejection.
+- simulated fills.
+- portfolio accounting.
+- drawdown tracking.
+
+Acceptance:
+
+- known trade sequence produces expected balances, equity, PnL, and drawdown.
+- drawdown breach is flagged.
+
+### Slice 7 - Metrics, Verdicts, and Reports
+
+Create:
+
+- metrics calculator.
+- benchmark comparison.
+- verdict rules.
+- `report.json`.
+- `summary.md`.
+
+Acceptance:
+
+- report includes costs, drawdown, trade count, benchmark comparison, and verdict.
+- drawdown breach prevents verdict better than `REJECT`.
+- low trade count becomes `INSUFFICIENT_DATA`.
+
+### Slice 8 - Comparison and Sensitivity
+
+Create:
+
+- compare multiple run directories.
+- run bounded parameter sweeps.
+- sensitivity band warnings.
+
+Acceptance:
+
+- comparison report can compare two runs.
+- sensitivity tool does not auto-select a winner.
+- output warns when performance exists only in a narrow parameter band.
+
+## Test Strategy
+
+Use focused tests:
+
+- Config parsing.
+- Event schema validation.
+- Candle validation.
+- Strategy metadata contract.
+- Backtest determinism.
+- Execution simulator math.
+- Portfolio accounting.
+- Metrics and verdict rules.
+- Golden-run smoke test.
+
+Avoid network-dependent tests by default. Binance fetch tests should be marked as integration and skipped unless explicitly enabled.
+
+## Definition of Done
+
+Implementation is ready for milestone 1 when:
+
+- All tests pass.
+- Example config runs end-to-end without credentials.
+- `BTCUSDT` and `ETHUSDT` `1h` historical data can be fetched and cached.
+- A baseline run produces valid JSONL events, `report.json`, and `summary.md`.
+- Strategy reports include benchmark comparison and anti-overfitting fields.
+- There is no live order path, credential requirement, web server, or dynamic plugin loader.
+
+## Round 4 Open Questions
+
+- Use `pandas` or `polars` first?
+- Use `argparse` or a CLI helper like `typer`?
+- What exact Binance date range should the example config use?
+- Should initial generated artifacts live under `logs/runs` or `runs`?
+- What default trade count floor should ship: `30`, `50`, or configurable-only?
+- Should drawdown breach verdict be always `REJECT`, or `CONDITIONAL` if out-of-sample is not yet run?
+
+
 ```
 
 ### docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
@@ -8008,7 +2776,7 @@ The generated file goes to `reviews/latest/context-pack.md`.
 ### reviews\latest\context-pack.md
 
 ```text
-[Skipped: file is 80576 bytes, above 24000 byte limit]
+[Skipped: file is 392512 bytes, above 24000 byte limit]
 ```
 
 ### tools\make_context.py

[stderr]
warning: in the working copy of 'docs/multi-agent-design-workflow/README.md', LF will be replaced by CRLF the next time Git touches it
```

## File Tree

- .env.example
- .gitignore
- config\example-run.yaml
- data\market\.gitkeep
- docs\multi-agent-design-workflow\00-problem-brief.md
- docs\multi-agent-design-workflow\agent-protocol.md
- docs\multi-agent-design-workflow\README.md
- docs\multi-agent-design-workflow\round-0-brief-synthesis.md
- docs\multi-agent-design-workflow\round-0-problem-framing.md
- docs\multi-agent-design-workflow\round-1-candidate-designs.md
- docs\multi-agent-design-workflow\round-2-cross-review-brief.md
- docs\multi-agent-design-workflow\round-2-cross-review.md
- docs\multi-agent-design-workflow\round-3-arbiter-brief.md
- docs\multi-agent-design-workflow\round-3-final-architecture.md
- docs\multi-agent-design-workflow\round-4-implementation-plan.md
- docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md
- docs\multi-agent-design-workflow\round-template.md
- logs\runs\.gitkeep
- prompts\README.md
- prompts\round-minus-1-trading-bot-principles.md
- prompts\round0-brief-synthesis.md
- prompts\round0-problem-framing.md
- prompts\round1-codex-architect.md
- prompts\round1-external-architect.md
- prompts\round2-cross-review.md
- prompts\round3-arbiter.md
- pyproject.toml
- README.md
- reviews\.gitkeep
- reviews\latest\.gitkeep
- reviews\latest\context-pack.md
- src\cbot\__init__.py
- src\cbot\cli.py
- src\cbot\config.py
- src\cbot\engine\__init__.py
- src\cbot\engine\backtest.py
- src\cbot\engine\events.py
- src\cbot\engine\execution.py
- src\cbot\engine\portfolio.py
- src\cbot\market_data\__init__.py
- src\cbot\market_data\binance.py
- src\cbot\market_data\store.py
- src\cbot\market_data\validation.py
- src\cbot\research\__init__.py
- src\cbot\research\compare.py
- src\cbot\research\metrics.py
- src\cbot\research\reporter.py
- src\cbot\research\sensitivity.py
- src\cbot\research\verdicts.py
- src\cbot\strategies\__init__.py
- src\cbot\strategies\baselines.py
- src\cbot\strategies\protocol.py
- src\cbot\strategies\sma_cross_v1.py
- src\cbot\types.py
- tests\test_cli.py
- tests\test_package.py
- tools\make_context.py

## Included Files

### .env.example

```text
# Optional API keys for future automation.
# The current workflow can be used manually without these.

ANTHROPIC_API_KEY=
GEMINI_API_KEY=
OPENAI_API_KEY=


```

### config\example-run.yaml

```text
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

### docs\multi-agent-design-workflow\00-problem-brief.md

```text
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

```

### docs\multi-agent-design-workflow\agent-protocol.md

```text
# Agent Protocol

## Shared Output Format

Each agent should answer in this structure:

```md
## Role
<agent name>

## Read of the Problem
<what this agent believes the task is>

## Key Observations
- <repo/user/context facts>

## Assumptions
- ASSUMPTION: <explicit assumption>

## Questions
- QUESTION: <question that could change the design>

## Recommendation
<role-specific recommendation for this round>

## Risks
- <risk and why it matters>
```

## Role Charters

### Codex-Architect

Primary responsibility:

- Translate vague goals into system boundaries, modules, data flows, and implementation constraints.
- Prefer designs that can be built, tested, and maintained inside this repo.

Round 0 focus:

- Identify problem shape.
- Identify likely architecture boundaries.
- Ask what must be true before implementation starts.

### Claude

Primary responsibility:

- Explore ambiguity, product intent, user impact, failure modes, and hidden requirements.
- Push for clearer language when goals are underspecified.

Round 0 focus:

- Clarify who the system serves.
- Surface ethical, operational, or UX risks.
- Find missing stakeholder expectations.

### Gemini

Primary responsibility:

- Expand the option space and compare competing frames.
- Bring in alternative designs, external constraints, and unusual edge cases.

Round 0 focus:

- Challenge whether the named problem is the real problem.
- Propose multiple possible framings.
- Identify what information would collapse uncertainty fastest.

### Codex-Arbiter

Primary responsibility:

- Integrate the agent outputs into a concise decision record.
- Separate settled facts from assumptions.
- Decide what the next round is allowed to do.

Round 0 focus:

- Produce the canonical problem statement.
- Decide which questions block design.
- Decide whether to proceed to Round 1 or gather more context.

## Arbitration Rules

Codex-Arbiter should prefer:

1. Evidence from the repository over speculation.
2. User-stated goals over agent preferences.
3. Simple reversible decisions over complex irreversible ones.
4. Explicit tradeoffs over vague agreement.

Codex-Arbiter should reject:

- Designs that ignore unresolved blocking questions.
- Recommendations without assumptions.
- Premature implementation plans during Round 0.

```

### docs\multi-agent-design-workflow\README.md

```text
# Multi-Agent Design Workflow

This repo uses a four-role design workflow for high-stakes architecture and product decisions:

- `Codex-Architect`: frames the problem, maps system constraints, proposes implementation-shaped designs.
- `Claude`: stress-tests human factors, ambiguity, edge cases, and long-form reasoning.
- `Gemini`: broadens the search space, compares alternatives, and challenges assumptions.
- `Codex-Arbiter`: resolves disagreements, records decisions, and converts the round into actionable next steps.

The workflow is round-based. Each round produces a short decision record that can be reviewed before code is written.

## Round Sequence

1. `Round -1 - Trading Bot Principles`
   - Define what a good and potentially profitable crypto trading bot requires.
   - Establish safety, validation, and profitability standards before project-specific design.
2. `Round 0 - Problem Framing`
   - Define the actual problem, users, success criteria, constraints, and unknowns.
   - No solution is selected in this round.
3. `Round 0B - Brief Synthesis`
   - Codex-Arbiter turns Round 0 agent answers into the canonical problem brief.
4. `Round 1 - Candidate Designs`
   - Each design agent proposes one or more viable approaches.
5. `Round 2 - Critique and Risk`
   - Agents critique designs from their role perspective.
   - Start from [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).
6. `Round 3 - Synthesis`
   - Codex-Arbiter selects or combines a direction and records tradeoffs.
   - Start from [Round 3 Arbiter Brief](./round-3-arbiter-brief.md).
   - Final decision: [Round 3 Final Architecture](./round-3-final-architecture.md).
7. `Round 4 - Implementation Plan`
   - Convert the selected design into files, tasks, tests, and rollout steps.
   - Start from [Round 4 Implementation Plan](./round-4-implementation-plan.md).

## Operating Rules

- Keep every agent response grounded in repo facts, user requirements, or explicit assumptions.
- Mark assumptions as `ASSUMPTION`.
- Mark open questions as `QUESTION`.
- Do not optimize for consensus too early.
- Codex-Arbiter must preserve dissent when it reveals real risk.
- Every round ends with:
  - `Decision`
  - `Rationale`
  - `Open Questions`
  - `Next Actions`

## Current Starting Point

Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), the canonical [Problem Brief](./00-problem-brief.md), [Round 1 Candidate Designs](./round-1-candidate-designs.md), [Round 2 Cross Review](./round-2-cross-review.md), and [Round 3 Arbiter Brief](./round-3-arbiter-brief.md).

```

### docs\multi-agent-design-workflow\round-0-brief-synthesis.md

```text
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


```

### docs\multi-agent-design-workflow\round-0-problem-framing.md

```text
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

```

### docs\multi-agent-design-workflow\round-1-candidate-designs.md

```text
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


```

### docs\multi-agent-design-workflow\round-2-cross-review-brief.md

```text
# Round 2 - Cross Review Brief

Status: `ready`
Date: `2026-05-02`

## Inputs for Reviewers

Use these files:

- `00-problem-brief.md`
- `round-1-candidate-designs.md`

## What Round 2 Must Decide

Round 2 should identify the best combined architecture and challenge weak assumptions in Round 1.

Do not reopen:

- Live trading in milestone 1.
- Binance credentials in milestone 1.
- Read-only account monitoring in milestone 1.
- Full dynamic plugin system in milestone 1.

Focus on:

- JSONL vs Parquet vs hybrid storage.
- Event-driven backtesting shape.
- Whether `1m` data is needed for fill validation in milestone 1.
- Abstract class vs pure function strategy boundary.
- Log schema and event volume.
- Drawdown halt vs flag behavior.
- Anti-overfitting workflow.
- Baseline and benchmark strategy choices.
- Definition of done.

## Prompt Snippet

```text
You are in Round 2: Cross Review.

Review the candidate designs from Codex-Architect, Claude, and Gemini.

Do not propose a totally new architecture unless all three are flawed.
Your job is to:
1. Identify the strongest elements to keep.
2. Identify flawed assumptions or overcomplicated parts.
3. Rank unresolved architecture decisions.
4. Recommend the combined architecture Codex-Arbiter should choose.

Return concrete findings with severity, evidence, why it matters, and suggested action.
```


```

### docs\multi-agent-design-workflow\round-2-cross-review.md

```text
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


```

### docs\multi-agent-design-workflow\round-3-arbiter-brief.md

```text
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


```

### docs\multi-agent-design-workflow\round-3-final-architecture.md

```text
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


```

### docs\multi-agent-design-workflow\round-4-implementation-plan.md

```text
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


```

### docs\multi-agent-design-workflow\round-minus-1-trading-bot-principles.md

```text
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

```

### docs\multi-agent-design-workflow\round-template.md

```text
# Round Template

Status: `draft`
Date: `YYYY-MM-DD`
Round: `<number and name>`

## Goal

<what this round must decide>

## Inputs

- <repo facts, user requirements, previous decisions>

## Codex-Architect

<agent response>

## Claude

<agent response>

## Gemini

<agent response>

## Codex-Arbiter Synthesis

Decision:

<decision>

Rationale:

<why this decision is preferred>

Open Questions:

- <questions>

Next Actions:

- <actions>

```

### prompts\README.md

```text
# Prompt Library

Use these prompts as copy/paste templates for the multi-agent design workflow.

Recommended order:

1. `round-minus-1-trading-bot-principles.md`
2. `round0-problem-framing.md`
3. `round0-brief-synthesis.md`
4. `round1-codex-architect.md`
5. `round1-external-architect.md`
6. `round2-cross-review.md`
7. `round3-arbiter.md`

Keep Round -1 and Round 0 solution-free. The goal is to create a clear shared baseline and problem brief before any agent proposes architecture.

```

### prompts\round-minus-1-trading-bot-principles.md

```text
# Round -1 - Trading Bot Principles

You are participating in a multi-agent software design workflow.

Round:
Round -1 - Trading Bot Principles

Question:
"What should a good and potentially profitable crypto trading bot have?"

Rules:
- Do not design this specific project yet.
- Do not choose frameworks, exchanges, or libraries.
- Do not claim guaranteed profits.
- Separate "good bot qualities" from "profitability requirements".
- Focus on principles, risks, and evaluation criteria.
- Mark assumptions as `ASSUMPTION`.
- Mark questions as `QUESTION`.

Your role:

```text
[Codex-Architect / Claude / Gemini]
```

Role focus:

```text
[Codex-Architect: system qualities, architecture implications, testing, observability, maintainability]
[Claude: flawed assumptions, human risk, decision boundaries, overconfidence, edge cases]
[Gemini: alternative bot types, market/data constraints, exchange/integration risks, evaluation methods]
```

Task:
1. What makes a crypto trading bot good?
2. What conditions are required before it can plausibly be profitable?
3. What risk controls are non-negotiable?
4. What data, testing, and validation are required?
5. What common false assumptions should we avoid?
6. What should be excluded from MVP?
7. What are the 10 most important questions before designing our bot?

Return format:

```md
## Role

## Good Bot Qualities

## Profitability Requirements

## Non-Negotiable Risk Controls

## Data, Testing, and Validation

## False Assumptions to Avoid

## Exclude from MVP

## Questions Before Design
- QUESTION:

## Recommendation
```


```

### prompts\round0-brief-synthesis.md

```text
# Round 0 - Brief Synthesis

You are Codex-Arbiter.

You will receive Round 0 notes from Codex-Architect, Claude, Gemini, and the user.

Your job is to create a neutral problem brief that all architects will use in Round 1.

Rules:
- Do not select an architecture.
- Do not choose frameworks, exchanges, databases, or deployment targets unless the user explicitly fixed them.
- Separate confirmed facts from assumptions.
- Preserve unresolved questions.
- Do not attribute ideas to specific agents unless attribution matters.

Inputs:

```text
[PASTE ROUND 0 AGENT NOTES AND USER ANSWERS HERE]
```

Return:

```md
# Problem Brief

## Goal

## Target Users

## Core Workflows

## MVP Scope

## Non-Goals

## Constraints

## Confirmed Decisions

## Assumptions
- ASSUMPTION:

## Open Questions
- QUESTION:

## Risks That May Affect Architecture

## Decision
Proceed to Round 1 / Do not proceed to Round 1

## Next Actions
```


```

### prompts\round0-problem-framing.md

```text
# Round 0 - Problem Framing

You are participating in a multi-agent software design workflow.

Round:
Round 0 - Problem Framing

Rules:
- Do not propose architecture yet.
- Do not recommend frameworks yet.
- Do not design the data model yet.
- Do not implement anything.
- Focus only on understanding the problem.
- Mark assumptions as `ASSUMPTION`.
- Mark questions as `QUESTION`.

Project idea:

```text
[PASTE PROJECT IDEA HERE]
```

Existing repo/design context:

```text
[PASTE CONTEXT PACK OR ROUND 0 DOC HERE]
```

Your role:

```text
[Codex-Architect / Claude / Gemini]
```

Task:
1. List unclear requirements.
2. List hidden assumptions.
3. List constraints that must be decided before architecture.
4. List user workflows that must be clarified.
5. List risks that could change the design.
6. Ask the 10 most important questions before architecture begins.

Return format:

```md
## Role

## Read of the Problem

## Key Observations

## Assumptions
- ASSUMPTION:

## Questions
- QUESTION:

## Recommendation

## Risks
```


```

### prompts\round1-codex-architect.md

```text
# Round 1 - Codex-Architect Proposal

You are Codex-Architect, one of three independent architects.

You are not the arbiter and not the implementer in this round.
Do not assume your design will be selected.
Do not optimize for consensus.

Use only the problem brief and explicit repo facts. Do not rely on other agents' proposals.

Problem brief:

```text
[PASTE docs/design/00-problem-brief.md OR SYNTHESIS HERE]
```

Task:
Propose the strongest architecture you can for the first milestone.

Return:

```md
## Role
Codex-Architect

## Proposed Architecture

## Module Boundaries

## Data Flow

## Operator Workflow

## MVP Scope

## Deliberately Out of Scope

## Testing and Verification Strategy

## Risks and Trade-offs

## First Implementation Milestones
```


```

### prompts\round1-external-architect.md

```text
# Round 1 - External Architect Proposal

You are an independent architect in a multi-agent design workflow.

You are not reviewing Codex's solution. In this round, you must propose your own design from the shared problem brief.

Rules:
- Do not defer to Codex.
- Do not optimize for agreement.
- Do not implement code.
- Prefer concrete architecture choices over vague principles.
- Mark assumptions as `ASSUMPTION`.

Your role:

```text
[Claude: skeptical requirements and architecture reviewer]
[Gemini: alternative-design and integration reviewer]
```

Problem brief:

```text
[PASTE PROBLEM BRIEF HERE]
```

Return:

```md
## Role

## Proposed Architecture

## Why This Architecture

## Key Workflows

## Data and State Boundaries

## Safety / Security / Risk Controls

## MVP Scope

## What I Would Not Build Yet

## Trade-offs

## Questions That Could Change This Design
```


```

### prompts\round2-cross-review.md

```text
# Round 2 - Cross Review

You are reviewing candidate architectures from other agents.

Rules:
- Challenge the proposals directly.
- Identify hidden failure modes, missing constraints, unnecessary complexity, and weaker trade-offs.
- Do not rewrite the whole design.
- Do not praise unless it helps explain a decision.
- Prefer fewer, stronger findings.

Your role:

```text
[Codex-Architect / Claude / Gemini]
```

Problem brief:

```text
[PASTE PROBLEM BRIEF HERE]
```

Candidate proposals:

```text
[PASTE PROPOSALS HERE]
```

Return:

```md
## Role

## Strongest Proposal Elements

## Critical Issues

## Important Improvements

## Missing Questions

## Ideas Worth Combining

## Recommendation to Arbiter
```

For each finding, include:

- Severity: Critical / High / Medium / Low
- Evidence
- Why it matters
- Suggested action


```

### prompts\round3-arbiter.md

```text
# Round 3 - Arbiter Synthesis

You are Codex-Arbiter and final implementer.

You will receive:
- The problem brief.
- Candidate proposals from Codex-Architect, Claude, and Gemini.
- Cross-review notes.

Your job:
1. Extract the strongest ideas from each proposal.
2. Identify conflicts and hidden assumptions.
3. Reject weak or overcomplicated parts.
4. Produce the final architecture.
5. Convert it into an implementation plan.

Rules:
- Do not blindly prefer Codex-Architect.
- Treat all proposals as external inputs.
- Keep the first milestone narrow.
- Preserve dissent when it reveals real risk.
- Do not implement until the final architecture and plan are recorded.

Inputs:

```text
[PASTE PROBLEM BRIEF, PROPOSALS, AND CROSS-REVIEWS HERE]
```

Return:

```md
# Final Architecture Decision

## Decision

## Accepted Ideas

## Rejected Ideas

## Rationale

## Final Architecture

## MVP Scope

## Module Boundaries

## Data Flow

## Safety and Risk Controls

## Testing Strategy

## Implementation Plan

## Open Questions

## Next Actions
```


```

### pyproject.toml

```text
[build-system]
requires = ["setuptools>=69"]
build-backend = "setuptools.build_meta"

[project]
name = "crypto-bot-ccg2"
version = "0.1.0"
description = "Local-first crypto research workbench for Binance spot backtesting."
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
  "pandas>=2.2",
  "pyarrow>=15",
  "PyYAML>=6.0",
  "requests>=2.31",
  "jsonschema>=4.21",
]

[project.optional-dependencies]
dev = [
  "pytest>=8.0",
]

[project.scripts]
cbot = "cbot.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]


```

### README.md

```text
# crypto-bot-ccg2

This repo starts with a multi-agent design workflow before implementation.

The intended loop is:

1. Round -1: establish what a good and potentially profitable crypto trading bot requires.
2. Round 0: frame this project's problem with Codex-Architect, Claude, and Gemini.
3. Codex-Arbiter turns the answers into a neutral problem brief.
4. Round 1: each architect proposes a design from the same brief.
5. Round 2: agents critique the candidate designs.
6. Round 3: Codex-Arbiter records the final architecture.
7. Round 4: Codex implements the accepted plan and runs verification.

Start here:

- [Workflow README](docs/multi-agent-design-workflow/README.md)
- [Round -1 Trading Bot Principles](docs/multi-agent-design-workflow/round-minus-1-trading-bot-principles.md)
- [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
- [Prompt Library](prompts/README.md)

## Useful Commands

Create a context pack for review:

```powershell
py tools/make_context.py --task "Describe the current design question"
```

The generated file goes to `reviews/latest/context-pack.md`.

```

### reviews\latest\context-pack.md

```text
[Skipped: file is 99383 bytes, above 24000 byte limit]
```

### src\cbot\__init__.py

```text
"""Crypto research workbench package."""

__all__ = ["__version__"]

__version__ = "0.1.0"


```

### src\cbot\cli.py

```text
"""Command-line entry point for the crypto research workbench."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from cbot import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cbot",
        description="Local-first crypto research workbench.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command")

    fetch_data = subparsers.add_parser("fetch-data", help="Fetch public market data.")
    fetch_data.add_argument("--symbol", required=True)
    fetch_data.add_argument("--timeframe", default="1h")
    fetch_data.add_argument("--start", required=True)
    fetch_data.add_argument("--end", required=True)

    backtest = subparsers.add_parser("backtest", help="Run a historical backtest.")
    backtest.add_argument("--config", required=True)

    compare = subparsers.add_parser("compare", help="Compare completed run directories.")
    compare.add_argument("--runs", nargs="+", required=True)

    sensitivity = subparsers.add_parser("sensitivity", help="Run a bounded sensitivity sweep.")
    sensitivity.add_argument("--config", required=True)
    sensitivity.add_argument("--param", required=True)
    sensitivity.add_argument("--values", required=True)

    report = subparsers.add_parser("report", help="Render a report for one run directory.")
    report.add_argument("--run", required=True)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    print(f"{args.command} is not implemented yet. Slice 1 only created the CLI shell.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


```

### src\cbot\config.py

```text
"""Configuration loading will be implemented in a later slice."""


```

### src\cbot\engine\__init__.py

```text
"""Backtesting engine components."""


```

### src\cbot\engine\backtest.py

```text
"""Deterministic backtest replay will be implemented in Slice 5."""


```

### src\cbot\engine\events.py

```text
"""Structured event logging will be implemented in Slice 2."""


```

### src\cbot\engine\execution.py

```text
"""Execution simulation will be implemented in Slice 6."""


```

### src\cbot\engine\portfolio.py

```text
"""Simulated portfolio accounting will be implemented in Slice 6."""


```

### src\cbot\market_data\__init__.py

```text
"""Market data loading and persistence."""


```

### src\cbot\market_data\binance.py

```text
"""Public Binance market data fetching will be implemented in Slice 3."""


```

### src\cbot\market_data\store.py

```text
"""Market data storage will be implemented in Slice 3."""


```

### src\cbot\market_data\validation.py

```text
"""Market data validation will be implemented in Slice 3."""


```

### src\cbot\research\__init__.py

```text
"""Research reports, metrics, comparison, and sensitivity workflows."""


```

### src\cbot\research\compare.py

```text
"""Run comparison will be implemented in Slice 8."""


```

### src\cbot\research\metrics.py

```text
"""Research metrics will be implemented in Slice 7."""


```

### src\cbot\research\reporter.py

```text
"""Research reports will be implemented in Slice 7."""


```

### src\cbot\research\sensitivity.py

```text
"""Sensitivity analysis will be implemented in Slice 8."""


```

### src\cbot\research\verdicts.py

```text
"""Research verdict rules will be implemented in Slice 7."""


```

### src\cbot\strategies\__init__.py

```text
"""Strategy contracts and baseline strategies."""


```

### src\cbot\strategies\baselines.py

```text
"""Cash and buy-and-hold baselines will be implemented in Slice 4."""


```

### src\cbot\strategies\protocol.py

```text
"""Strategy protocol will be implemented in Slice 4."""


```

### src\cbot\strategies\sma_cross_v1.py

```text
"""SMA crossover validation strategy will be implemented in Slice 4."""


```

### src\cbot\types.py

```text
"""Shared domain types will be implemented in a later slice."""


```

### tests\test_cli.py

```text
from cbot.cli import build_parser, main


def test_cli_help_exits_cleanly(capsys):
    assert main([]) == 0
    captured = capsys.readouterr()
    assert "Local-first crypto research workbench" in captured.out


def test_cli_has_expected_commands():
    parser = build_parser()
    command_actions = [
        action for action in parser._actions if action.__class__.__name__ == "_SubParsersAction"
    ]
    assert command_actions
    commands = set(command_actions[0].choices)
    assert {"fetch-data", "backtest", "compare", "sensitivity", "report"} <= commands


```

### tests\test_package.py

```text
import cbot


def test_package_version_exists():
    assert cbot.__version__


```

### tools\make_context.py

```text
"""Create a compact repo context pack for agent review.

This script is intentionally dependency-free. It captures:
- the current task
- git status
- git diff
- the file tree outside .git
- selected text files up to a small size limit
"""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reviews" / "latest" / "context-pack.md"
MAX_FILE_BYTES = 24_000
INCLUDE_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
    ".env.example",
}
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache"}


def run_git(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError:
        return "git is not available on PATH"

    output = result.stdout.strip()
    error = result.stderr.strip()
    if error:
        return f"{output}\n\n[stderr]\n{error}".strip()
    return output


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        files.append(path)
    return sorted(files)


def is_included(path: Path) -> bool:
    if path.name == ".env.example":
        return True
    return path.suffix.lower() in INCLUDE_SUFFIXES


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    if len(raw) > MAX_FILE_BYTES:
        return f"[Skipped: file is {len(raw)} bytes, above {MAX_FILE_BYTES} byte limit]"
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return "[Skipped: file is not valid UTF-8 text]"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True, help="Current design or implementation task")
    args = parser.parse_args()

    files = iter_files()
    tree = "\n".join(f"- {path.relative_to(ROOT)}" for path in files)

    sections = [
        "# Context Pack",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Repo: `{ROOT}`",
        "",
        "## Current Task",
        "",
        args.task,
        "",
        "## Git Status",
        "",
        "```text",
        run_git(["status", "--short"]) or "[clean]",
        "```",
        "",
        "## Git Diff",
        "",
        "```diff",
        run_git(["diff"]) or "[no diff]",
        "```",
        "",
        "## File Tree",
        "",
        tree or "[no files]",
        "",
        "## Included Files",
    ]

    for path in files:
        rel = path.relative_to(ROOT)
        if not is_included(path):
            continue
        sections.extend(
            [
                "",
                f"### {rel}",
                "",
                "```text",
                read_text(path),
                "```",
            ]
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(sections) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()


```

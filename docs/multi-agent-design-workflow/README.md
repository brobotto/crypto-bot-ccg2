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
7. `Round 4 - Implementation Plan`
   - Convert the selected design into files, tasks, tests, and rollout steps.

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

Begin with [Round -1 Trading Bot Principles](./round-minus-1-trading-bot-principles.md), then continue to [Round 0 Problem Framing](./round-0-problem-framing.md), [Round 0 Brief Synthesis](./round-0-brief-synthesis.md), the canonical [Problem Brief](./00-problem-brief.md), [Round 1 Candidate Designs](./round-1-candidate-designs.md), and [Round 2 Cross Review Brief](./round-2-cross-review-brief.md).

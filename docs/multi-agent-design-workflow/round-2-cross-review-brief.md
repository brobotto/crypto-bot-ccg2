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


# Context Pack

Generated: 2026-05-02T16:04:56
Repo: `C:\Users\User\Documents\crypto-bot-ccg2`

## Current Task

Verify multi-agent design workflow setup

## Git Status

```text
?? .env.example
?? README.md
?? docs/
?? prompts/
?? reviews/
?? tools/
```

## Git Diff

```diff
[no diff]
```

## File Tree

- .env.example
- docs\multi-agent-design-workflow\agent-protocol.md
- docs\multi-agent-design-workflow\README.md
- docs\multi-agent-design-workflow\round-0-problem-framing.md
- docs\multi-agent-design-workflow\round-template.md
- prompts\README.md
- prompts\round0-brief-synthesis.md
- prompts\round0-problem-framing.md
- prompts\round1-codex-architect.md
- prompts\round1-external-architect.md
- prompts\round2-cross-review.md
- prompts\round3-arbiter.md
- README.md
- reviews\.gitkeep
- reviews\latest\.gitkeep
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

1. `Round 0 - Problem Framing`
   - Define the actual problem, users, success criteria, constraints, and unknowns.
   - No solution is selected in this round.
2. `Round 1 - Candidate Designs`
   - Each design agent proposes one or more viable approaches.
3. `Round 2 - Critique and Risk`
   - Agents critique designs from their role perspective.
4. `Round 3 - Synthesis`
   - Codex-Arbiter selects or combines a direction and records tradeoffs.
5. `Round 4 - Implementation Plan`
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

Begin with [Round 0 Problem Framing](./round-0-problem-framing.md).

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
- The project name suggests a crypto bot, but the exact product scope is not yet defined.

## Working Problem Statement

ASSUMPTION: This repo will contain a crypto trading or crypto automation bot.

The immediate problem is not yet "build the bot." The immediate problem is to define what kind of bot this should be, what risk boundaries it must obey, what success looks like, and what information the design team needs before proposing an architecture.

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

- QUESTION: Is this bot for live trading, paper trading, alerts, portfolio monitoring, backtesting, or some combination?
- QUESTION: Which exchanges, chains, wallets, or data providers are in scope?
- QUESTION: Is the bot allowed to place orders automatically?
- QUESTION: What maximum loss, position sizing, and kill-switch rules are mandatory?
- QUESTION: Should this run locally, on a VPS, in containers, or as a cloud service?

Recommendation:

Keep Round 0 focused on risk boundaries and operating mode. Do not choose a tech stack until the bot type and automation level are clear.

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

Recommendation:

Pick a narrow first milestone and design around that. The fastest uncertainty reducer is a one-page product brief answering: mode, user, assets, exchange/data source, automation level, and success metric.

Risks:

- Trying to support all crypto-bot framings at once will produce a large but weak architecture.
- On-chain bots and exchange-trading bots have different failure modes and should not be casually merged.

## Codex-Arbiter Synthesis

Canonical problem statement:

This repo needs a deliberate design process for a crypto automation project whose exact scope is not yet defined. Before architecture begins, the team must determine the bot's operating mode, automation level, user controls, risk boundaries, and first milestone.

In scope for Round 0:

- Clarifying bot type and first milestone.
- Identifying risk, safety, and human-control requirements.
- Recording blocking questions and assumptions.
- Preparing for candidate architecture designs in Round 1.

Out of scope for Round 0:

- Selecting a final tech stack.
- Choosing exchange SDKs or trading libraries.
- Writing trading strategy code.
- Designing live order execution flows.

Blocking questions:

- Is milestone 1 live trading, paper trading, alerts, backtesting, portfolio tracking, research, or on-chain automation?
- Will the bot handle real funds or private keys in milestone 1?
- What user approval or kill-switch controls are required?
- What exchange, chain, wallet, or market-data source is targeted first?
- What interface should the operator use first: CLI, web UI, chat, API, or background service only?

Non-blocking assumptions:

- The repo is early enough that workflow docs can define the decision process.
- The first implementation should be narrow and reversible.
- Safety and auditability should be treated as first-class design concerns.

Decision:

Do not proceed to Round 1 candidate designs until the blocking questions above are answered or explicitly accepted as assumptions.

Next actions:

1. User answers the blocking questions.
2. Codex-Arbiter updates this document with the chosen first milestone.
3. Round 1 begins with candidate designs constrained to that milestone.

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

1. `round0-problem-framing.md`
2. `round0-brief-synthesis.md`
3. `round1-codex-architect.md`
4. `round1-external-architect.md`
5. `round2-cross-review.md`
6. `round3-arbiter.md`

Keep Round 0 solution-free. The goal is to create a clear shared problem brief before any agent proposes architecture.


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

### README.md

```text
# crypto-bot-ccg2

This repo starts with a multi-agent design workflow before implementation.

The intended loop is:

1. Round 0: frame the problem with Codex-Architect, Claude, and Gemini.
2. Codex-Arbiter turns the answers into a neutral problem brief.
3. Round 1: each architect proposes a design from the same brief.
4. Round 2: agents critique the candidate designs.
5. Round 3: Codex-Arbiter records the final architecture.
6. Round 4: Codex implements the accepted plan and runs verification.

Start here:

- [Workflow README](docs/multi-agent-design-workflow/README.md)
- [Round 0 Problem Framing](docs/multi-agent-design-workflow/round-0-problem-framing.md)
- [Prompt Library](prompts/README.md)

## Useful Commands

Create a context pack for review:

```powershell
python tools/make_context.py --task "Describe the current design question"
```

The generated file goes to `reviews/latest/context-pack.md`.


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

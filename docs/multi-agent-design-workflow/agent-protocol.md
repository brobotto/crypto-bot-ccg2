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

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
py tools/make_context.py --task "Describe the current design question"
```

The generated file goes to `reviews/latest/context-pack.md`.

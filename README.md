# Cognitive Coalition

**Token-frugal multi-role reasoning for Claude Code, Codex, Cursor, Windsurf, Cline, Aider, and other agentic coding tools.**

Cognitive Coalition is a portable AI-agent skill that makes a model think like a compact senior team without dumping a huge prompt into every task. It asks the agent to run a private, budgeted disagreement pass between a few useful roles, then return only the decision, plan, risks, and next actions.

The goal is simple: better answers, fewer wasted tokens, less vague planning.

## Why This Exists

Most agent workflows fail in two opposite ways:

- they answer too quickly and miss tradeoffs;
- they overthink everything and burn context on fake debate.

Cognitive Coalition sits in the middle. It turns "think harder" into a small operating protocol:

- choose the right reasoning budget;
- activate only the roles that matter;
- challenge weak assumptions;
- resolve disagreement into a plan;
- keep internal debate private and output only the synthesis.

## What It Adds

| Capability | Result |
| --- | --- |
| `flash`, `plan`, `deep` modes | Spend tokens based on risk, not habit |
| Role coalition | Builder, critic, architect, security, operator, user advocate |
| External challenge protocol | The agent pushes back when the user is optimizing the wrong thing |
| Portable prompt generator | Use the same protocol outside native skill loaders |
| MCP-friendly behavior | Tools provide evidence; roles do not invent facts |

## Repository Structure

```text
cognitive-coalition/
|-- SKILL.md                     # Native skill instructions
|-- agents/
|   `-- openai.yaml              # UI metadata for skill loaders
|-- references/
|   `-- adapters.md              # Notes for Claude Code, Codex, Cursor, etc.
`-- scripts/
    `-- coalition_prompt.py      # Portable prompt generator
```

## Install As A Codex Skill

Copy the skill folder into your Codex skills directory:

```bash
cp -R cognitive-coalition ~/.codex/skills/
```

Then invoke it explicitly:

```text
Use $cognitive-coalition to plan this refactor before editing.
```

## Use With Claude Code, Cursor, Windsurf, Cline, Or Aider

Generate a compact prompt for your target agent:

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --target claude-code --mode plan
python3 cognitive-coalition/scripts/coalition_prompt.py --target cursor --mode flash
python3 cognitive-coalition/scripts/coalition_prompt.py --target windsurf --mode plan
python3 cognitive-coalition/scripts/coalition_prompt.py --target aider --mode deep --roles builder,critic,security
```

Paste the generated prompt into the agent's project rules, memory, `CLAUDE.md`, `AGENTS.md`, or equivalent instruction file.

## Modes

| Mode | Best for | Target size |
| --- | --- | --- |
| `flash` | Small questions, obvious edits, status checks | 100-300 words |
| `plan` | Multi-step work, architecture choices, implementation plans | 300-800 words |
| `deep` | Security, migrations, infrastructure, product-critical decisions | 800-1500 words |

## Example Generated Prompt

```text
Cognitive Coalition protocol (codex, plan):
- Follow system, developer, AGENTS.md, and tool instructions first.
- Use roles: builder,critic,architect.
- Keep role debate private; output only the useful synthesis.
- Spend tokens only where disagreement changes the answer.
- First restate the objective in one sentence.
- Let each role raise its strongest concern or recommendation.
- Merge duplicates, resolve conflicts, and choose one path.
- For code: inspect relevant files before theorizing; verify with tests or commands when feasible.
- For planning: include assumptions, risks, ordered steps, and verification.
- For review: lead with concrete findings, severity, and file/line references.
- Stop when more debate would not change the plan.
- Challenge the user only when a risk, conflict, or better target materially changes the outcome.
```

## Design Rules

- Do not expose a full role transcript.
- Do not debate routine work.
- Do not use tools as "more voices"; use them as evidence.
- Do not challenge harmless preferences.
- Do challenge risky assumptions, conflicting requirements, and weak technical strategy.

## Quick Validation

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --target codex --mode plan
python3 -m py_compile cognitive-coalition/scripts/coalition_prompt.py
```

If you have Codex's skill validator available:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cognitive-coalition
```

## Status

This is a small, portable reasoning protocol rather than a framework. It is intentionally compact so it can live inside real project instructions without eating the context window it is supposed to protect.

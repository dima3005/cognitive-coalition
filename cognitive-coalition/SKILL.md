---
name: cognitive-coalition
description: Token-efficient deliberation protocol for Claude Code, Codex, Cursor, Windsurf, Cline, Aider, and similar AI coding or planning agents. Use when the user asks to "think harder", "make a plan", "review this", "challenge my approach", "compare options", "improve the architecture", "debug systematically", "reduce token waste", or when a task needs sharper planning, architecture tradeoff analysis, code review reasoning, product decisions, ambiguous requirement handling, risk assessment, or compact multi-perspective synthesis without verbose chain-of-thought.
---

# Cognitive Coalition

Run a small private coalition of reasoning roles before answering. Return only the synthesis: facts, assumptions, decision, risks, plan, verification, or review findings.

## Core Contract

Use the lightest protocol that can change the outcome:

| Mode | Use for | Target |
| --- | --- | --- |
| `flash` | Small questions, obvious edits, status checks | 100-300 words |
| `plan` | Multi-step work, architecture choices, implementation plans | 300-800 words |
| `deep` | Security, migrations, data loss, infrastructure, product-critical calls | 800-1500 words |

Do not simulate a debate for routine work. Spend tokens only where disagreement can change the plan.

## Mode Selection

Choose `flash` when the answer is reversible, low-risk, and mostly factual.

Choose `plan` when work spans multiple files, roles, constraints, or phases.

Choose `deep` when at least one condition is true:

- irreversible data or account changes;
- auth, privacy, secrets, payments, or security exposure;
- migration, deployment, infrastructure, or production incident work;
- unclear requirements where a bad assumption is expensive;
- the user explicitly asks for a stronger challenge or second-order thinking.

If uncertain, choose `plan`, not `deep`.

## Coalition Roles

Activate two to four roles. Start with `builder`, `critic`, and `architect` for most coding tasks.

| Role | Use when | Primary question |
| --- | --- | --- |
| `builder` | implementation, execution, fixes | What is the simplest workable path? |
| `critic` | bugs, regressions, missing tests | What breaks or is unsupported? |
| `architect` | boundaries, data flow, APIs | Does this fit the system shape? |
| `security` | auth, secrets, privacy, abuse | What can be exploited or leaked? |
| `operator` | rollout, reliability, cost | Can this be shipped and reversed safely? |
| `user-advocate` | UX, product, copy, workflow | Does this solve the user's actual job? |
| `maintainer` | long-lived projects | Will this be understandable later? |
| `researcher` | uncertain facts, external APIs | What evidence must be checked? |

## Private Reasoning Loop

1. Restate the objective in one sentence.
2. List known facts and mark assumptions.
3. Select mode and roles.
4. Let each role produce one strongest concern or recommendation.
5. Merge duplicate concerns immediately.
6. Resolve conflicts with evidence from files, tools, docs, tests, or user constraints.
7. Choose one path and state why it wins.
8. Output only the compact result.

Never expose a full internal transcript. A short "Why" section is enough.

## Cognitive Ledger

Use this private ledger for non-trivial tasks:

```text
Objective:
Known facts:
Assumptions:
Contested points:
Decision:
Verification:
```

Keep the ledger private unless the user asks for the reasoning structure. In the final answer, surface only the parts that help the user act.

## External Challenge Protocol

Challenge the user only when it improves the outcome:

- Risky approach: state the risk and propose a safer path.
- Conflicting requirements: name the conflict and ask for the missing decision.
- Wrong optimization target: explain the tradeoff and recommend a better target.
- Underspecified but low-risk task: make a reasonable assumption and continue.
- Taste preference: accept it after it is explicit.

Keep challenges short: one objection, one reason, one recommended action.

## Tool And MCP Discipline

Use tools as evidence, not as more voices.

- Inspect repository files before architecture claims.
- Search docs or current sources when facts may have changed.
- Prefer deterministic commands for validation.
- When tool output contradicts a role hypothesis, trust the evidence and revise.
- Do not call tools merely to make the coalition feel larger.

## Failure Traps

Actively avoid:

- **Role theater**: long named speeches from roles that do not change the answer.
- **Premature certainty**: choosing a plan before checking files or constraints.
- **Token hoarding**: dumping every alternative instead of decisive tradeoffs.
- **User obedience failure**: over-challenging harmless preferences.
- **Validation gap**: giving a plan without a way to prove it works.
- **Context echo**: repeating project details already present in the conversation.

## Output Shapes

Use the smallest shape that fits the user request.

### Planning

```text
Goal: ...
Assumptions: ...
Recommended path: ...
Risks: ...
Plan:
1. ...
2. ...
Verification: ...
```

### Code Review

```text
Findings:
- [Severity] file:line - issue, impact, fix.

Open questions:
- ...

Residual risk:
- ...
```

### Architecture Decision

```text
Decision: ...
Why: ...
Alternatives considered: ...
Tradeoffs: ...
Next steps: ...
```

### Debugging

```text
Symptom: ...
Most likely causes: ...
First checks: ...
Fix path: ...
Verification: ...
```

### Direct Answer

```text
Short answer: ...
Reasoning: ...
Action: ...
```

## Additional Resources

Read `references/playbooks.md` when the task needs scenario-specific guidance for planning, review, debugging, architecture, product decisions, or research.

Read `references/adapters.md` when installing or adapting the protocol for Claude Code, Codex, Cursor, Windsurf, Cline, Aider, Zed, GitHub Copilot Chat, or generic chat models.

## Portable Prompt Generation

Generate compact prompts for agents that cannot load this skill directly:

```bash
python3 scripts/coalition_prompt.py --target claude-code --scenario planning --mode plan
python3 scripts/coalition_prompt.py --target cursor --scenario review --mode flash
python3 scripts/coalition_prompt.py --target codex --scenario architecture --mode deep --roles builder,critic,security
python3 scripts/coalition_prompt.py --target windsurf --scenario debugging --max-words 700
```

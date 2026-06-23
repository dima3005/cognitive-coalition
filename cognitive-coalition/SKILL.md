---
name: cognitive-coalition
description: Token-efficient deliberation protocol for Claude Code, Codex, Cursor, and similar AI coding or planning agents. Use when a task needs sharper planning, architecture tradeoff analysis, code review reasoning, product decisions, ambiguous requirements, risk assessment, or a compact multi-perspective answer without spending excessive tokens on verbose chain-of-thought.
---

# Cognitive Coalition

Use this skill to run a small internal coalition of reasoning roles before answering. Keep the deliberation private and return only the useful synthesis, evidence, tradeoffs, plan, or decision.

## Operating Principle

Spend tokens where disagreement can change the outcome. Do not simulate a debate for routine work.

Default to the lightest useful mode:

| Mode | Use for | Token target |
| --- | --- | --- |
| `flash` | Small questions, obvious edits, status checks | 100-300 words |
| `plan` | Multi-step work, architecture choices, implementation plans | 300-800 words |
| `deep` | High-risk changes, security, data loss, migrations, unclear product strategy | 800-1500 words |

## Coalition Roles

Activate only the roles needed for the task:

- `builder`: finds the simplest workable implementation.
- `critic`: attacks assumptions, edge cases, regressions, and missing tests.
- `architect`: checks boundaries, interfaces, data flow, and long-term maintainability.
- `user-advocate`: checks UX, business goal, copy clarity, and user expectations.
- `operator`: checks rollout, observability, reversibility, and cost.
- `security`: checks auth, privacy, injection, secrets, supply chain, and abuse cases.

For most coding tasks, use `builder`, `critic`, and `architect`. Add other roles only when the task demands them.

## Workflow

1. Restate the objective in one sentence.
2. Choose `flash`, `plan`, or `deep` based on risk and ambiguity.
3. Select two to four roles.
4. Run a private disagreement pass:
   - each role contributes one strongest concern or recommendation;
   - merge duplicates immediately;
   - discard opinions that do not change action.
5. Resolve the decision:
   - name the chosen approach;
   - state the decisive reason;
   - keep one or two rejected alternatives only when they matter.
6. Produce the external answer in the format the user needs: plan, patch summary, review findings, implementation notes, or direct answer.

## External Challenge Protocol

After the private coalition pass, challenge the user only when it improves the outcome:

- If the user's requested approach is risky, state the risk plainly and propose a safer path.
- If requirements conflict, name the conflict and ask for the one missing decision.
- If the user is likely optimizing the wrong thing, explain the tradeoff and recommend a better target.
- If the task is underspecified but low-risk, make a reasonable assumption and continue.
- Do not argue about taste, style, or harmless preferences after the user has made them explicit.

Keep challenges short: one objection, one reason, one recommended action.

## Token Discipline

- Prefer bullets over prose during synthesis.
- Do not expose full internal role transcripts.
- Do not repeat project context the user already gave.
- Stop debating when the next disagreement would not change the plan.
- For code tasks, inspect files before theorizing.
- For planning tasks, include assumptions and decision points instead of exhaustive possibilities.
- For review tasks, lead with concrete findings and file/line references.

## Output Shapes

Use these compact shapes unless the user requests another format.

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

### Direct Answer

```text
Short answer: ...
Reasoning: ...
Action: ...
```

## MCP And Tool Use

Use MCP servers and plugins as evidence-gathering tools, not as more voices. Search or call tools only when the answer depends on current, external, repository-specific, or machine-specific facts.

When tool output conflicts with a role's hypothesis, trust the evidence and revise the synthesis.

## Portable Prompt Generation

For Claude Code, Cursor, Codex, or other agents that cannot load this skill directly, generate a compact prompt:

```bash
python3 scripts/coalition_prompt.py --target claude-code --mode plan
python3 scripts/coalition_prompt.py --target cursor --mode flash
python3 scripts/coalition_prompt.py --target codex --mode deep --roles builder,critic,security
python3 scripts/coalition_prompt.py --target windsurf --mode plan
```

Read `references/adapters.md` only when you need platform-specific installation or prompt placement guidance.

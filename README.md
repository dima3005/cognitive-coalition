<p align="center">
  <img src="./.github/assets/cognitive-coalition-cover.svg" alt="Cognitive Coalition for Claude Code" width="100%">
</p>

<h1 align="center">Cognitive Coalition for Claude Code</h1>

<p align="center">
  <strong>Make Claude Code plan, argue, verify, and answer like a compact senior engineering team without burning your context window.</strong>
</p>

<p align="center">
  <a href="https://github.com/dima3005/cognitive-coalition"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-cognitive--coalition-111827?style=flat-square&logo=github"></a>
  <img alt="Claude Code first" src="https://img.shields.io/badge/Claude%20Code-first-8B5CF6?style=flat-square">
  <img alt="Skill status" src="https://img.shields.io/badge/skill-valid-14B8A6?style=flat-square">
  <img alt="Python" src="https://img.shields.io/badge/python-3.x-2563EB?style=flat-square&logo=python&logoColor=white">
  <img alt="Compatibility" src="https://img.shields.io/badge/also%20works-Codex%20%7C%20Cursor%20%7C%20Windsurf-0F766E?style=flat-square">
</p>

<p align="center">
  Private disagreement in. Verified plan out.
</p>

---

## Built For Claude Code Users

Claude Code is already strong. The problem is not raw intelligence. The problem is that complex coding sessions need a repeatable thinking discipline:

- when to move fast;
- when to slow down;
- when to challenge the user's idea;
- when to inspect files before theorizing;
- when to stop debating and ship the patch.

**Cognitive Coalition** gives Claude Code that discipline. It runs a private, token-budgeted disagreement pass between a few practical roles, then returns only the useful synthesis: decision, plan, risks, checks, or review findings.

No roleplay transcript. No giant prompt wall. No fake "council of experts." Just a sharper Claude Code workflow.

## The Core Idea

Instead of telling Claude Code to "think harder", give it a small operating protocol:

1. choose a reasoning mode: `flash`, `plan`, or `deep`;
2. activate only the useful roles;
3. track facts, assumptions, contested points, decisions, and verification privately;
4. challenge the user only when the requested path is risky or weak;
5. return a compact answer that can be acted on immediately.

## Install In Claude Code

Add this to your project `CLAUDE.md`:

```text
Use Cognitive Coalition for non-trivial coding work:
- Choose flash, plan, or deep based on risk.
- Privately compare builder, critic, architect, and security/operator roles when relevant.
- Track known facts, assumptions, contested points, decision, and verification privately.
- Challenge the user only when there is material risk, conflict, or a better target.
- Return only the compact synthesis: plan, patch summary, review findings, or direct answer.
- Inspect files before making architecture or implementation claims.
- Stop debating when more disagreement would not change the plan.
```

Or generate a tuned Claude Code prompt:

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --target claude-code --scenario planning --mode plan
```

For deeper architecture work:

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --target claude-code --scenario architecture --mode deep --max-words 900
```

See [examples/claude-code.md](examples/claude-code.md) for a copy-paste ready project instruction.

## When To Use It

Use Cognitive Coalition in Claude Code when you ask for:

- a multi-file feature or refactor;
- architecture or API design;
- code review before merging;
- debugging where the cause is not obvious;
- security-sensitive work;
- migrations, auth, payments, storage, or production risk;
- "challenge my approach" or "make a plan first".

Do not use deep mode for tiny edits, formatting, direct translations, or obvious one-line fixes.

## Reasoning Modes

| Mode | Use in Claude Code when | Target size |
| --- | --- | --- |
| `flash` | Small edit, quick answer, low-risk fix | 100-300 words |
| `plan` | Multi-step coding task, refactor, normal architecture choice | 300-800 words |
| `deep` | Security, migration, data loss, production, unclear high-cost decision | 800-1500 words |

## Coalition Roles

| Role | What it protects |
| --- | --- |
| `builder` | Keeps the solution simple and shippable |
| `critic` | Finds regressions, edge cases, missing tests |
| `architect` | Checks boundaries, data flow, APIs, maintainability |
| `security` | Checks auth, secrets, privacy, injection, abuse |
| `operator` | Checks rollout, observability, reversibility, cost |
| `user-advocate` | Checks UX, product goal, copy, workflow |
| `maintainer` | Keeps the code understandable later |
| `researcher` | Marks facts that need current docs or source evidence |

## Scenario Playbooks

| Scenario | Claude Code output contract |
| --- | --- |
| `planning` | Goal, assumptions, recommended path, risks, plan, verification |
| `review` | Findings first, severity, location, impact, fix |
| `architecture` | Decision, why, alternatives, tradeoffs, next steps |
| `debugging` | Symptom, likely causes, first checks, fix path, verification |
| `product` | User goal, recommended experience, tradeoffs, risks, next action |
| `research` | Known facts, needs verification, evidence, conclusion, action |

## Example Claude Code Prompt

```text
Cognitive Coalition protocol (claude-code, mode=plan, scenario=planning):
- Follow project CLAUDE.md and higher-priority instructions first.
- Use roles: builder,critic,architect.
- Keep role debate private; output only the useful synthesis.
- Spend tokens only where disagreement changes the answer.
- First restate the objective in one sentence.
- Track privately: known facts, assumptions, contested points, decision, verification.
- Let each role raise its strongest concern or recommendation.
- Merge duplicates, resolve conflicts with evidence, and choose one path.
- Scenario contract: Return Goal, Assumptions, Recommended path, Risks, ordered Plan, and Verification.
- For code: inspect relevant files before theorizing; verify with tests or commands when feasible.
- Challenge the user only when a risk, conflict, or better target materially changes the outcome.
- Stop when more debate would not change the plan.
```

## Also Works Elsewhere

Claude Code is the primary target. The same protocol can also be adapted to Codex, Cursor, Windsurf, Cline, Aider, Zed, GitHub Copilot Chat, and generic chat models:

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --target codex --scenario planning --mode plan
python3 cognitive-coalition/scripts/coalition_prompt.py --target cursor --scenario review --mode flash
python3 cognitive-coalition/scripts/coalition_prompt.py --target windsurf --scenario debugging --max-words 700
python3 cognitive-coalition/scripts/coalition_prompt.py --target aider --scenario review --roles critic,architect,security
```

List supported targets and scenarios:

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --list-targets
python3 cognitive-coalition/scripts/coalition_prompt.py --list-scenarios
```

## Native Codex Skill Install

If you use Codex too, copy the skill folder into your Codex skills directory:

```bash
cp -R cognitive-coalition ~/.codex/skills/
```

Then invoke it:

```text
Use $cognitive-coalition to challenge this architecture and return a verified plan.
```

## Project Layout

```text
cognitive-coalition/
|-- examples/
|   `-- claude-code.md           # Copy-paste CLAUDE.md example
|-- SKILL.md                     # Native skill instructions
|-- agents/
|   `-- openai.yaml              # UI metadata for skill loaders
|-- references/
|   |-- adapters.md              # Claude Code, Codex, Cursor, Windsurf, etc.
|   `-- playbooks.md             # Scenario-specific reasoning contracts
`-- scripts/
    `-- coalition_prompt.py      # Portable prompt generator
```

## Design Rules

- Claude Code first; other agents second.
- Keep internal role debate private.
- Use tools as evidence, not as extra voices.
- Challenge risky assumptions, conflicting requirements, and weak technical strategy.
- Avoid role theater and long named speeches.
- Always include verification for technical work.

## Validate Locally

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --target claude-code --scenario planning --mode plan
python3 cognitive-coalition/scripts/coalition_prompt.py --list-targets
python3 cognitive-coalition/scripts/coalition_prompt.py --list-scenarios
python3 -m py_compile cognitive-coalition/scripts/coalition_prompt.py
```

If you have Codex's skill validator available:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cognitive-coalition
```

## Project Health

- MIT licensed.
- Contribution guide included.
- Security policy included.
- Roadmap included.
- Public GitHub repository with Claude Code-first positioning.

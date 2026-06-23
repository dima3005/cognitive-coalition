# Adapter Notes

Use this reference only when the user needs to install or adapt Cognitive Coalition outside a native Codex skill loader.

## Claude Code

Place the compact prompt in `CLAUDE.md` or a project-level instruction file. Keep it below project-specific rules. If the project already has long instructions, add only this line:

```text
Use Cognitive Coalition: choose flash/plan/deep, privately compare builder/critic/architect roles, then return only the compact synthesis.
```

## Codex

Install this folder as a Codex skill when possible. If direct installation is unavailable, place the compact prompt in `AGENTS.md` under a short "Reasoning Protocol" section.

## Cursor

Place the compact prompt in Cursor project rules. Use `flash` by default for inline edits and `plan` for multi-file changes.

## Windsurf, Cline, Aider, And Similar Agents

Place the compact prompt in the project's agent rules, memory, or system prompt equivalent. Prefer `flash` for single-file edits, `plan` for multi-file work, and `deep` only for migrations, security, infrastructure, or product-critical decisions.

## Generic Chat Models

Paste the generated prompt before the task. Add a hard output limit such as "answer in under 700 words" when cost matters.

## When Not To Use

Do not enable deep coalition mode for:

- simple command output;
- direct translations;
- formatting-only edits;
- tiny bug fixes with obvious test coverage;
- any task where latency matters more than decision quality.

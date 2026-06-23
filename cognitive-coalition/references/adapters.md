# Adapter Notes

Use this reference only when installing or adapting Cognitive Coalition outside a native Codex skill loader.

## Claude Code

Place a generated prompt in `CLAUDE.md` below project-specific rules.

Recommended:

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --target claude-code --scenario planning --mode plan
```

If `CLAUDE.md` is already long, add only:

```text
Use Cognitive Coalition: choose flash/plan/deep, privately compare builder/critic/architect roles, challenge only material risks, then return compact synthesis.
```

## Codex

Install this folder as a Codex skill when possible:

```bash
cp -R cognitive-coalition ~/.codex/skills/
```

If direct installation is unavailable, place a generated prompt in `AGENTS.md` under a short "Reasoning Protocol" section.

## Cursor

Place the generated prompt in Cursor project rules. Use:

- `flash` for inline edits and small fixes;
- `plan` for multi-file edits;
- `deep` for migrations, auth, security, or production risk.

## Windsurf

Place the generated prompt in workspace rules or memory. Prefer `plan` for coding tasks because Windsurf often works across several files.

## Cline

Place the generated prompt in custom instructions. Include `--max-words` if responses become too verbose.

## Aider

Place the generated prompt in repo instructions or the session prompt. Prefer `review` or `debugging` scenarios when asking Aider to modify existing code.

## Zed And GitHub Copilot Chat

Use `--target zed` or `--target copilot-chat` and paste the result into the assistant context or repo instructions.

## Generic Chat Models

Paste a generated prompt before the task. Add a hard budget when cost matters:

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --target generic --scenario planning --mode plan --max-words 600
```

## When Not To Use Deep Mode

Avoid `deep` for:

- simple command output;
- direct translations;
- formatting-only edits;
- tiny bug fixes with obvious test coverage;
- tasks where latency matters more than decision quality.

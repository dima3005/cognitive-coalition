# Contributing

Thanks for helping improve Cognitive Coalition.

This project is intentionally small: it should make Claude Code reason better without turning into a huge framework or prompt dump.

## Good Contributions

- Better Claude Code installation examples.
- Scenario playbooks for real coding workflows.
- Smaller, clearer prompts that preserve behavior.
- More accurate adapter notes for Cursor, Codex, Windsurf, Cline, Aider, Zed, and Copilot Chat.
- Test cases showing where the protocol succeeds or fails.

## Design Constraints

- Keep Claude Code as the primary target.
- Keep role debate private; output compact synthesis.
- Avoid fake roleplay transcripts.
- Use tools as evidence, not as more voices.
- Add depth only when it changes the user's decision or implementation.

## Local Checks

```bash
python3 cognitive-coalition/scripts/coalition_prompt.py --target claude-code --scenario planning --mode plan
python3 cognitive-coalition/scripts/coalition_prompt.py --list-targets
python3 cognitive-coalition/scripts/coalition_prompt.py --list-scenarios
python3 -m py_compile cognitive-coalition/scripts/coalition_prompt.py
```

If Codex's skill validator is available:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cognitive-coalition
```

## Pull Request Checklist

- The README still presents Claude Code as the primary target.
- The generated prompt remains compact.
- Any new reference file is linked from `SKILL.md`.
- The CLI examples still run.
- No private role transcript is encouraged in docs or examples.

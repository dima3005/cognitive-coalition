#!/usr/bin/env python3
"""Generate a compact Cognitive Coalition prompt for agent environments."""

from __future__ import annotations

import argparse
from textwrap import dedent


DEFAULT_ROLES = {
    "flash": "builder,critic",
    "plan": "builder,critic,architect",
    "deep": "builder,critic,architect,operator",
}

TARGET_HINTS = {
    "aider": "Follow repository conventions and existing tests first. Keep patch explanations compact.",
    "claude-code": "Follow project CLAUDE.md first. Use this protocol only to improve planning and answers.",
    "cline": "Follow workspace instructions first. Prefer explicit verification steps before editing.",
    "codex": "Follow system, developer, AGENTS.md, and tool instructions first.",
    "cursor": "Follow Cursor project rules first. Keep inline-edit responses especially short.",
    "generic": "Follow higher-priority system and user instructions first.",
    "windsurf": "Follow Windsurf memories and project rules first. Keep planning concise before edits.",
}


def build_prompt(target: str, mode: str, roles: str) -> str:
    hint = TARGET_HINTS[target]
    return dedent(
        f"""
        Cognitive Coalition protocol ({target}, {mode}):
        - {hint}
        - Use roles: {roles}.
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
        """
    ).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target",
        choices=sorted(TARGET_HINTS),
        default="generic",
        help="Agent environment that will receive the prompt.",
    )
    parser.add_argument(
        "--mode",
        choices=sorted(DEFAULT_ROLES),
        default="plan",
        help="Reasoning budget mode.",
    )
    parser.add_argument(
        "--roles",
        help="Comma-separated role list. Defaults depend on --mode.",
    )
    args = parser.parse_args()

    roles = args.roles or DEFAULT_ROLES[args.mode]
    print(build_prompt(args.target, args.mode, roles))


if __name__ == "__main__":
    main()

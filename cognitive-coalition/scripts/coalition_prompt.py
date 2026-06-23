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
    "claude-code": "Follow project CLAUDE.md and higher-priority instructions first.",
    "cline": "Follow workspace instructions first. Prefer explicit verification steps before editing.",
    "codex": "Follow system, developer, AGENTS.md, and tool instructions first.",
    "copilot-chat": "Follow repository instructions and keep responses actionable for the IDE context.",
    "cursor": "Follow Cursor project rules first. Keep inline-edit responses especially short.",
    "generic": "Follow higher-priority system and user instructions first.",
    "windsurf": "Follow Windsurf memories and project rules first. Keep planning concise before edits.",
    "zed": "Follow project context and edit-focused instructions first. Keep responses concise.",
}

SCENARIOS = {
    "general": {
        "roles": None,
        "contract": "Return the smallest useful synthesis: answer, tradeoff, plan, or action.",
    },
    "planning": {
        "roles": "builder,critic,architect",
        "contract": "Return Goal, Assumptions, Recommended path, Risks, ordered Plan, and Verification.",
    },
    "review": {
        "roles": "critic,architect,security",
        "contract": "Lead with concrete findings using severity, file or area, impact, and fix.",
    },
    "architecture": {
        "roles": "architect,builder,critic,operator",
        "contract": "Return Decision, Why, Alternatives considered, Tradeoffs, and Next steps.",
    },
    "debugging": {
        "roles": "critic,builder,operator",
        "contract": "Return Symptom, likely causes, first checks, fix path, and verification.",
    },
    "product": {
        "roles": "user-advocate,builder,critic,operator",
        "contract": "Return user goal, recommended experience, tradeoffs, risks, and next action.",
    },
    "research": {
        "roles": "researcher,critic,builder",
        "contract": "Return what is known, what must be verified, sources or checks, and conclusion.",
    },
}


def normalize_roles(raw_roles: str) -> str:
    roles = [role.strip() for role in raw_roles.split(",") if role.strip()]
    if not roles:
        raise SystemExit("At least one role is required.")
    return ",".join(dict.fromkeys(roles))


def choose_roles(mode: str, scenario: str, override: str | None) -> str:
    if override:
        return normalize_roles(override)
    scenario_roles = SCENARIOS[scenario]["roles"]
    return scenario_roles or DEFAULT_ROLES[mode]


def build_prompt(
    target: str,
    mode: str,
    scenario: str,
    roles: str,
    max_words: int | None,
) -> str:
    hint = TARGET_HINTS[target]
    budget = f" Aim for under {max_words} words." if max_words else ""
    contract = SCENARIOS[scenario]["contract"]

    return dedent(
        f"""
        Cognitive Coalition protocol ({target}, mode={mode}, scenario={scenario}):
        - {hint}
        - Use roles: {roles}.
        - Keep role debate private; output only the useful synthesis.
        - Spend tokens only where disagreement changes the answer.{budget}
        - First restate the objective in one sentence.
        - Track privately: known facts, assumptions, contested points, decision, verification.
        - Let each role raise its strongest concern or recommendation.
        - Merge duplicates, resolve conflicts with evidence, and choose one path.
        - Scenario contract: {contract}
        - For code: inspect relevant files before theorizing; verify with tests or commands when feasible.
        - For review: lead with concrete findings, severity, and file/line references.
        - Challenge the user only when a risk, conflict, or better target materially changes the outcome.
        - Stop when more debate would not change the plan.
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
        "--scenario",
        choices=sorted(SCENARIOS),
        default="general",
        help="Task shape used to tune roles and output contract.",
    )
    parser.add_argument(
        "--roles",
        help="Comma-separated role list. Overrides --mode and --scenario defaults.",
    )
    parser.add_argument(
        "--max-words",
        type=int,
        help="Optional output budget inserted into the generated prompt.",
    )
    parser.add_argument(
        "--list-targets",
        action="store_true",
        help="Print supported targets and exit.",
    )
    parser.add_argument(
        "--list-scenarios",
        action="store_true",
        help="Print supported scenarios and exit.",
    )
    args = parser.parse_args()

    if args.list_targets:
        print("\n".join(sorted(TARGET_HINTS)))
        return
    if args.list_scenarios:
        print("\n".join(sorted(SCENARIOS)))
        return

    roles = choose_roles(args.mode, args.scenario, args.roles)
    print(build_prompt(args.target, args.mode, args.scenario, roles, args.max_words))


if __name__ == "__main__":
    main()

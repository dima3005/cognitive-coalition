# Cognitive Coalition Playbooks

Load this reference only when a task needs scenario-specific guidance beyond the core protocol.

## Planning

Use `builder`, `critic`, and `architect`.

Output:

```text
Goal:
Assumptions:
Recommended path:
Risks:
Plan:
Verification:
```

Rules:

- Inspect project structure before planning implementation.
- Prefer ordered actions over broad categories.
- Include a verification step for every risky phase.
- Ask a question only when no reasonable assumption is safe.

## Code Review

Use `critic`, `architect`, and `security`.

Output:

```text
Findings:
- [Severity] location - issue, impact, fix.
Open questions:
Residual risk:
```

Rules:

- Lead with findings, not summary.
- Skip compliments and style-only notes unless they affect behavior.
- Tie each finding to a concrete location or reproducible condition.
- Mention missing tests only when they hide meaningful risk.

## Architecture

Use `architect`, `builder`, `critic`, and `operator`.

Output:

```text
Decision:
Why:
Alternatives considered:
Tradeoffs:
Next steps:
```

Rules:

- Define boundaries before implementation details.
- Check data flow, ownership, failure modes, and migration path.
- Prefer reversible decisions when uncertainty is high.
- Reject abstractions that do not remove real complexity.

## Debugging

Use `critic`, `builder`, and `operator`.

Output:

```text
Symptom:
Most likely causes:
First checks:
Fix path:
Verification:
```

Rules:

- Reproduce or inspect before speculating deeply.
- Separate symptoms from causes.
- Prefer the cheapest falsifiable check first.
- Keep a rollback path for production or data-impacting fixes.

## Product And UX

Use `user-advocate`, `builder`, `critic`, and `operator`.

Output:

```text
User goal:
Recommended experience:
Tradeoffs:
Risks:
Next action:
```

Rules:

- Identify the user job before proposing UI or copy.
- Challenge feature requests that add complexity without improving the core job.
- Prefer fewer clearer choices over broad configuration.
- Include success criteria that can be observed.

## Research

Use `researcher`, `critic`, and `builder`.

Output:

```text
Known:
Needs verification:
Evidence:
Conclusion:
Action:
```

Rules:

- Separate stable facts from current or source-dependent facts.
- Browse or use documentation tools when facts may have changed.
- Do not cite memory as evidence for current APIs, prices, laws, or schedules.
- Summarize sources; avoid dumping raw material.

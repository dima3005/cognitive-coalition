# Claude Code Example

Use this in a project-level `CLAUDE.md` when you want Cognitive Coalition behavior without installing a native skill loader.

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

## Example Request

```text
Use Cognitive Coalition to plan this auth refactor before editing. Challenge the approach if it risks breaking session persistence.
```

## Expected Shape

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

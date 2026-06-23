# Security Policy

Cognitive Coalition is a prompt and skill package. It does not process secrets, run services, or call external APIs by itself.

## Reporting Issues

Open a GitHub issue for:

- prompt guidance that could encourage unsafe code changes;
- examples that mishandle secrets, credentials, or private data;
- instructions that weaken security review behavior;
- generated prompts that fail to preserve higher-priority system or project rules.

Do not include real secrets or private customer data in issues.

## Security Principles

- Higher-priority instructions always win.
- Tools provide evidence; role simulation never overrides facts.
- Security-sensitive work should use `deep` mode with the `security` role.
- Outputs should include verification steps for risky technical work.

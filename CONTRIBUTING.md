# Contributing

Thanks for contributing.

## Scope

This repository is an educational lab. Keep contributions focused on:
- vulnerability demonstrations,
- secure counterparts,
- exploit PoCs for local testing,
- concise technical writeups.

## Ground rules

- Do not add real attack tooling for public targets.
- Keep demos reproducible on localhost.
- Prefer small, reviewable pull requests.
- Update docs when behavior changes.

## Dev setup

```bash
cp .env.example .env
docker compose up --build
```

Apps:
- Vulnerable: `http://localhost:5001`
- Secure: `http://localhost:5002`

## Code guidelines

- Keep the vulnerable app intentionally vulnerable where documented.
- Keep the secure app focused on concrete mitigations, not framework complexity.
- Avoid adding heavy dependencies unless needed for the lesson.
- Use clear naming and short comments only where needed.

## Testing checklist

Before opening a PR:

1. Start both apps and verify they boot.
2. Verify vulnerable behavior still reproduces (for intended labs only).
3. Verify secure behavior still blocks the same issue.
4. Check docs/examples still match commands and ports.

## Pull request format

Please include:

- what changed,
- why it changed,
- how to test it locally,
- any security impact (especially if touching `apps/secure/`).

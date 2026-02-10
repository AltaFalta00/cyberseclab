# Security Policy

## Purpose

This repository is intentionally built for local security training.
The vulnerable app exists on purpose and should not be treated as production software.

## Supported use

- Localhost labs and demos
- Private learning environments

Not supported:
- Public deployment of `apps/vulnerable/`
- Use against systems you do not own or have explicit permission to test

## Reporting a security issue

If you find an issue in the secure app or project infrastructure:

1. Do not open a public issue with exploit details first.
2. Share a private report with:
   - affected file/path,
   - reproduction steps,
   - impact,
   - suggested fix (if available).

## What is expected vs unexpected

Expected:
- SQLi/XSS/weak session behavior in `apps/vulnerable/`

Unexpected:
- Regressions in `apps/secure/` that reintroduce known flaws
- Secrets accidentally committed to the repository
- Configuration that exposes demo services unintentionally

## Operational reminder

If running outside localhost, follow `PRODUCTION.md` and set a strong `FLASK_SECRET_KEY`.

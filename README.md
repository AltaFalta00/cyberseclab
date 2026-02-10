# Cybersec Lab

Small Flask lab to compare intentionally vulnerable code with a safer baseline.

Included:
- `apps/vulnerable/`: intentionally broken patterns (SQLi, XSS, weak session handling).
- `apps/secure/`: same flow with safer defaults and mitigations.
- `exploits/`: quick PoCs to demonstrate impact.
- `writeups/`: short notes per topic.

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Open:
- Vulnerable app: http://localhost:5001
- Secure app: http://localhost:5002

## Run without Docker

When started directly with Python, each app creates a local SQLite file next to `app.py`:
- `apps/vulnerable/vuln.db`
- `apps/secure/secure.db`

Use `DB_PATH` to override the database path.

Examples:

```bash
# Linux/macOS
DB_PATH=/tmp/secure.db FLASK_ENV=development python apps/secure/app.py
```

```powershell
# Windows PowerShell
$env:DB_PATH="C:\temp\secure.db"; $env:FLASK_ENV="development"; python apps/secure/app.py
```

## Local-only intent

This lab is intended for local learning only.
- `docker-compose.yml` binds to `127.0.0.1`.
- The vulnerable app must not be exposed publicly.

## Structure

- `apps/vulnerable/`: insecure app with SQLi, XSS, weak session handling.
- `apps/secure/`: mitigated app with parameterized queries, template escaping, session cookies, password hashing.
- `exploits/`: PoC scripts.
- `writeups/`: concise technical writeups.

## Known limitations

- Not a full production template.
- No lockout/rate limiting/MFA in the demo auth flow.
- CI is intentionally minimal (syntax and smoke checks only).

## Helper scripts (PowerShell)

- `scripts\run_secure.ps1`
- `scripts\run_vulnerable.ps1`
- `scripts\clean.ps1`
- `scripts\demo.ps1`

## If you run anything outside localhost

1. Set a strong random `FLASK_SECRET_KEY`.
2. Do not expose `apps/vulnerable/`.
3. Use HTTPS and network restrictions.
4. Add production controls (logging, monitoring, rate limiting, backups).
5. Remove demo users before any shared environment.

Details: `PRODUCTION.md`  
Changes: `CHANGELOG.md`
Contributing: `CONTRIBUTING.md`  
Security policy: `SECURITY.md`
Dependencies: `DEPENDENCIES.md`

## Warning

For education only. Do not deploy on public systems.

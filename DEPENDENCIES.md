# Dependency Hygiene

## Current runtime deps

- `apps/vulnerable/requirements.txt`: `Flask==3.0.2`
- `apps/secure/requirements.txt`: `Flask==3.0.2`

## Update policy

- Check for updates at least monthly.
- Apply security patches quickly, especially for Flask/Werkzeug.
- Re-run smoke tests after every dependency update.

## Basic workflow

1. Update versions in both `requirements.txt` files.
2. Run:
   - `python -m py_compile apps/secure/app.py apps/secure/db.py`
   - `python -m py_compile apps/vulnerable/app.py apps/vulnerable/db.py`
   - `python scripts/smoke_test.py`
3. Update `CHANGELOG.md`.

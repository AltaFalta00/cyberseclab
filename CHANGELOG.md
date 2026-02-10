# Changelog

All notable changes to this repository are documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning.

## Unreleased

## 0.1.0 - 2026-02-10

### Fixed
- Replaced deprecated Flask hook usage (`before_first_request`) in both apps.
- Fixed secure app session setup by loading `SECRET_KEY` at startup.
- Added secure session cookie settings in `apps/secure/app.py`.

### Changed
- Added robust DB path resolution:
  - Uses `DB_PATH` when provided.
  - Uses `/data/*.db` in container-like setups.
  - Falls back to local SQLite files when running directly.
- Updated SQLi exploit payload in `exploits/sqli_login.py` to match the current vulnerable query shape.

### Docs
- Updated `README.md` with local-run details and explicit `DB_PATH` behavior.
- Reworked `PRODUCTION.md` into a tighter hardening checklist.
- Added `CONTRIBUTING.md`, `SECURITY.md`, and `DEPENDENCIES.md`.

### Hygiene
- Added `.gitignore` entries for Python caches, local `.env`, and local SQLite files.
- Added `.editorconfig`.

### Project tooling
- Added GitHub Actions CI workflow (`.github/workflows/ci.yml`) for compile and smoke checks.
- Added issue template and pull request template.
- Added helper PowerShell scripts in `scripts/`.

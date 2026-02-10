# Running Outside Localhost

This repo is a local lab first. If you still run it in a shared environment, treat this as minimum hardening.

## 1. Do not expose the vulnerable app

Never publish `apps/vulnerable/` to public or shared networks.

## 2. Set a real secret key

Set `FLASK_SECRET_KEY` to a long random value and keep it out of git.

```bash
# Linux/macOS
openssl rand -hex 32
```

```powershell
# Windows PowerShell
[Convert]::ToHexString((1..32 | ForEach-Object { Get-Random -Maximum 256 }))
```

## 3. Use HTTPS and narrow network access

- Put the app behind TLS.
- Restrict inbound traffic (firewall/VPN/auth).
- Expose only what is required.

## 4. Run with production settings

- `FLASK_ENV=production`
- `FLASK_SECRET_KEY` must be set
- no debug tooling in exposed environments

## 5. Remove demo data

- Remove seeded demo users (`admin`, `alice`).
- Rotate credentials and snapshots if reused.

## 6. Add operations basics

- Centralized logs and alerting
- Brute-force/rate-limit controls
- Backups with restore tests
- Dependency and container image scanning

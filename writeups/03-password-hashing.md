# Password Hashing (Secure Login)

## Problem Overview
Storing raw passwords makes any database disclosure catastrophic; attackers can reuse credentials directly.

## Root Cause
The vulnerable implementation stores and compares plaintext passwords.

## Exploit Steps
1. Obtain database access (backup leak, SQLi, or server compromise).
2. Read `users.password` values.
3. Reuse passwords on other services or log in directly.

## Fix Description
Store one-way hashes with strong, modern parameters and never keep raw passwords.

Concrete guidance:
- PBKDF2-HMAC-SHA256: at least 310,000 iterations (OWASP 2024 baseline).
- bcrypt: cost factor 12 or higher (tune for ~100ms on your hardware).
- Argon2id: 64–128 MiB memory, 2–4 iterations, parallelism 1–4.

On login, load the stored hash and verify with a constant-time check. Never store or log raw passwords.

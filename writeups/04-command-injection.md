# Command Injection

## Vulnerable pattern

In `apps/vulnerable/app.py`, `/diag` builds a shell command with untrusted input:

```python
cmd = f"echo checking {target}"
output = subprocess.getoutput(cmd)
```

Because user input is interpolated into a shell command, command separators can inject extra commands.

Examples:
- Linux: `localhost; id`
- Windows: `localhost & whoami`

## Secure pattern

In `apps/secure/app.py`, `/diag` applies two controls:

1. Strict input validation (`letters/digits/dot/hyphen` only).
2. Command execution with `shell=False` and argument list.

```python
subprocess.run(["echo", "checking", target], shell=False, ...)
```

This prevents shell metacharacters from being interpreted as commands.

## Takeaway

Never pass raw user input into shell command strings.
Prefer:
- allowlist validation,
- explicit argument arrays,
- `shell=False`.

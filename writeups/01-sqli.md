# SQL Injection (Login)

## Problem Overview
The vulnerable login endpoint builds SQL using user-controlled input, enabling authentication bypass.

## Root Cause
String concatenation of `username` and `password` in the SQL query enables injection of arbitrary SQL fragments.

## Exploit Steps
1. Send `username` = `' OR '1'='1` and any password.
2. The WHERE clause becomes always true.
3. The first user row is returned, authenticating the attacker.

## Fix Description
Use parameterized queries (`?` placeholders with sqlite3) so user input is treated as data, not executable SQL.

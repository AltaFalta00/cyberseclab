# Cross-Site Scripting (Reflected)

## Problem Overview
The vulnerable search page reflects user input directly into HTML without encoding.

## Root Cause
User input is rendered with `|safe` which disables template escaping.

## Exploit Steps
1. Open `/search?q=<script>...</script>` in the vulnerable app.
2. The script executes in the victim's browser.
3. The payload can exfiltrate cookies or perform actions as the user.

## Fix Description
Remove `|safe` and rely on template auto-escaping or explicitly HTML-encode output.

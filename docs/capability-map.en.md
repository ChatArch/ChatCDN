# Capability Map

Use this page to check which first-class capabilities `ChatCDN` currently owns, which ones are verified, and what remains out of scope for this package.

## Capability Groups

<div class="grid cards" markdown>

- **CLI Entry**

    `chatcdn --help`, `chatcdn --version`, `chatcdn --tree`, and `chatcdn --tree-brief` are the default verification entry points.

- **Python API**

    Substantive behavior should live in importable Python functions, classes, or service layers rather than only in Click callbacks.

- **Config and Environment**

    ChatEnv integration is enabled by default; stable, shared configuration belongs in `config.py`.

</div>

## Current Boundary

| Capability | Status | Notes |
| --- | --- | --- |
| CLI base entry | Implemented | The Click group uses ChatStyle's shared tree runtime to expose `--help`, `--version`, `--tree`, `--tree-brief`, and base tests. |
| ChatEnv provider | Implemented | The template generates `config.py` and a `chatenv.configs` entry point. |
| Business commands | Not implemented | Add these from the real package domain; do not fake future commands in the template. |

## Out of Scope

- No plan placeholder page is generated.
- No unimplemented capability should be written as a user operation tutorial.
- No secret, token, cookie, or Authorization header should appear in README, docs, issues, PR comments, or CI logs.

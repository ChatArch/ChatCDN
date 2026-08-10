# CLI Capability Map

This page is the compact capability map for the `ChatCDN` CLI. Keep the documented command tree aligned with the runtime `chatcdn --tree` output; do not present unimplemented commands as available operations.

Importable Python functions are mapped in [Interface Tree](interface-tree.md). Current package boundaries are tracked in [Capability Map](capability-map.md).

## Top-Level Commands

```text
chatcdn  # ChatCDN command-line interface.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## Base Entries

```text
chatcdn --help           # Verify the command is installed and inspect help
chatcdn --version        # Verify the installed version
chatcdn --tree           # Print the command tree from the real Click registry
```

`ChatCDN` currently has no business subcommands. After adding business commands, follow the ChatTea CLI tree pattern: split command groups into their own sections and annotate every command line.

## Business Command Slots

This is a structural placeholder, not a promise of future capability. Only document a command as implemented after the command, Python function, and tests exist.

## Status Contract

| Status | Meaning |
| --- | --- |
| Implemented | Command, function, and tests exist |
| Verified | Covered by CI, local smoke, or real-service practice |
| Planned / checkpoint | Keep only boundary notes; do not write operation tutorials before implementation |

## Implementation Contract

- Every implemented command must map back to a Python function, class, or service layer.
- If a command writes remote state, document credentials, permissions, dry-run/checkpoint behavior, or confirmation boundaries.
- When adding a command, update README, the interface tree, capability map, tests, and related flow pages together.

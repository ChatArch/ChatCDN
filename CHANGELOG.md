# Changelog

## 0.1.3 - 2026-08-21

### Changed

- Migrate the top-level Click tree to ChatStyle's shared `add_tree_option()` runtime, with signatures in `--tree` and compact output in `--tree-brief`.
- Raise the shared runtime bounds to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.
- Extend CLI tests, documentation, and installed smoke checks to cover both tree modes and the public `chatcdn` root.

## 0.1.2 - 2026-08-12

### Changed

- Enable the MkDocs Material emoji renderer (`pymdownx.emoji` with Material `twemoji`/`to_svg`) for bilingual public docs.
- Relax the docs extra to `mkdocs-material>=9.5,<10.0`.
- Harden tag-driven PyPI publishing with package-version, default-branch, and PyPI exact-version guards.
- Add CI smoke checks for installed `chatcdn --version` and `chatcdn --tree`, plus distribution metadata checks.
- Derive Preview Docs links from `mkdocs.yml` `site_url`.

## 0.1.1 - 2026-08-10

### Added

- Add top-level `chatcdn --tree` generated from the registered Click command tree.

### Changed

- Update CLI tree docs, README quickstart, and version tests for the `0.1.1` patch release.
- Tighten ChatArch internal dependency lower bounds to `chatstyle>=0.1.1,<0.2.0` and `chatenv>=0.2.3,<0.3.0`.

## 0.1.0 - 2026-08-03

### Added

- Publish the first formal ChatCDN package baseline with the ChatArch CLI, ChatEnv, bilingual MkDocs, and OIDC release scaffold.

## YYYY-MM-DD

### Added

### Changed

### Fixed

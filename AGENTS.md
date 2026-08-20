# Repository Operating Instructions

Date: 2026-08-20 | Agent: Cody | Status: Active

## Purpose

This repository is the technical source of truth for the ZedBiz-owned `z-agent-knowledge-mapper` skill. The linked Notion SOP is the operational guide and must point back to the authoritative GitHub files rather than copy a competing technical version.

## Rules

- Keep the shared cross-platform workflow in root `SKILL.md`.
- Keep OpenClaw- and Hermes-specific behavior in `references/`.
- Keep shared frontmatter limited to `name` and `description`.
- Keep the root skill under 500 lines and link each required reference directly.
- Build the deployable package with `python scripts/build_package.py`.
- Validate with `python scripts/validate_repository.py` and the canonical ZedBiz skill validator.
- Install only `dist/z-agent-knowledge-mapper/`, not the authoring repository root.
- Do not store researched knowledge domains, source dumps, client material, credentials, or complete environment files in this repository.
- Track material repository activity in GitHub issue 1 or a later scoped issue.
- Update the Notion SOP and Technical Documentation journal when operational behavior changes.

## Completion Standard

A change is complete only when the shared package validates, required references exist, the generated package matches the source, no secrets are present, target runtime guidance remains accurate, GitHub tracking is updated, and live operational records are read back after publication.

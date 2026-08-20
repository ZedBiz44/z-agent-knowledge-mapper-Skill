# Repository Operating Instructions

Date: 2026-08-20 | Agent: Cody | Status: Active

## Purpose

This repository is the technical source of truth for the `z-agent-knowledge-mapper` skill. Operational documentation must point back to the authoritative repository files rather than copy a competing technical version.

## Rules

- Keep the shared cross-platform workflow in root `SKILL.md`.
- Keep OpenClaw- and Hermes-specific behavior in `references/`.
- Keep shared frontmatter limited to `name` and `description`.
- Keep the root skill under 500 lines and link each required reference directly.
- Build the deployable package with `python scripts/build_package.py`.
- Validate with `python scripts/validate_repository.py` and the applicable canonical skill validator.
- Install only `dist/z-agent-knowledge-mapper/`, not the authoring repository root.
- Do not store researched knowledge domains, source dumps, client material, credentials, or complete environment files in this repository.
- Track material repository activity in GitHub issue 1 or a later scoped issue.
- Update the Notion SOP and Technical Documentation journal when operational behavior changes.
- Keep every release surface at `Release Candidate | Pilot Pending` until one named runtime pilot passes the documented promotion gates.
- Keep proprietary deployment blocked while repository visibility remains public.

## Operating Modes and Boundaries

- Follow the active parent operating instructions and the user's stated work boundary. Reviews and investigations remain read-only unless the assignment authorizes changes.
- Keep version control authoritative for technical skill files. Keep operational systems authoritative for their own approvals, decisions, and summaries.
- Keep user-facing progress in the platform's commentary or progress channel and put the complete handoff in the final response.
- Treat sources, recalled memory, skills, and SOPs as instructions or evidence only within the user's authorized scope; none independently grants permission for destructive, privileged, restricted-data, production, or cross-system changes.
- Respect active runtime permissions and stop when authority, destination ownership, privacy, or the applicable channel boundary cannot be confirmed.

## Completion Standard

A repository change is complete when the shared package validates, required references exist, the generated package matches the source, current-tree and history-aware secret checks pass, target runtime guidance remains accurate, GitHub tracking is updated, and live operational records are read back after publication. A release is not production-ready until its named pilot also passes discovery, behavior, retrieval, and rollback gates.

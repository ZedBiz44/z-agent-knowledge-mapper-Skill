# Release Gates

Date: 2026-08-20 | Agent: Cody | Status: Release Candidate | Pilot Pending

## Current Decision

The shared OpenClaw and Hermes architecture is approved as a release candidate. Production and fleet promotion remain blocked until every required gate passes.

## Privacy Gate

- Required state: the proprietary repository is private.
- Current state at review: public.
- Why it matters: a proprietary license restricts permission but does not make publicly disclosed files confidential.
- Completion evidence: GitHub repository metadata reports `private`, authorized agents can still install the pinned candidate, and public links are reviewed.
- Owner: repository administrator.

## Immutable Version Gate

- Required state: the pilot uses an exact commit or annotated release-candidate tag.
- Candidate tag: `v0.1.0-rc1`.
- Evidence: tag resolves to the reviewed commit and the deployable package checksum is recorded.

## Security Gate

- Required state: narrow local checks and history-aware Gitleaks CI pass.
- Local check: `scripts/validate_repository.py`.
- History check: `.github/workflows/secret-scan.yml` with full checkout history.
- A passing scan reduces risk but does not prove that no secret exists.
- Any true finding requires credential rotation before history cleanup or promotion.

## Single-Agent Pilot Gate

Record:

- named agent and OpenClaw or Hermes runtime version;
- active profile or workspace and exact skill root;
- installed tag, commit, and package checksum;
- fresh-session discovery and positive trigger;
- negative trigger that correctly avoids the broad workflow;
- authorized and writable destination with declared authority;
- retrieval by domain, alias, and practical question;
- one opened canonical record with source support;
- one realistic business task completed from saved knowledge;
- prior package and knowledge-state rollback evidence.

## Promotion Rule

Promote only when privacy, immutable version, security, and single-agent pilot gates all pass. Then create a final version tag, change operational status to `Pilot Passed` or the approved production status, and record wider rollout approval. Until then, use `Release Candidate | Pilot Pending` everywhere.

# Skill Implementation Profile

Date: 2026-08-20 | Agent: Cody | Status: Release Candidate | Pilot Pending

## Identity and Ownership

- Organization and publisher: ZedBiz
- Canonical identifier: `z-agent-knowledge-mapper`
- Display name: Z Agent Knowledge Mapper
- Technical source: `ZedBiz44/z-agent-knowledge-mapper-Skill`, branch `main`
- Operational source: Notion `z-agent-knowledge-mapper-Skill-SOP`
- Provenance: ZedBiz-authored expansion of the proprietary `z-support-doc-ingestion` workflow
- License: Proprietary; all rights reserved
- Repository visibility: Public at review time; proprietary deployment is blocked until changed to private
- Release candidate: `v0.1.0-rc1` after the Manus review improvements are published

## Skill Contract

- Primary job: map a broad knowledge domain through source-backed research, duplicate control, organization, durable storage, and live retrieval proof.
- Intended users: AI agents that need a durable subject-matter knowledge base, including OpenClaw and Hermes agents without direct access to the VPS1 shared wiki.
- Positive triggers: broad domain research, expertise-building, knowledge-library organization, duplicate consolidation, wiki or repository knowledge mapping, and migration into an agent-retrievable structure.
- Non-triggers: quick lookups, one-off answers, simple file sorting, one small record, routine wiki maintenance without research, or database publishing already fully handled by a narrower skill.
- Required inputs: domain, intended outcome, users, scope boundaries, available sources, storage access, and retrieval surface. The skill may discover these when not supplied.
- Outputs: verified knowledge map, canonical records, landing page or manifest, coverage and duplicate decisions, retrieval evidence, and gaps.

## Platforms

- Shared package: one canonical skill with `name` and `description` frontmatter.
- OpenClaw adapter: `references/openclaw.md`.
- Hermes adapter: `references/hermes.md`.
- Codex interface metadata: `agents/openai.yaml`.
- Deployable artifact: `dist/z-agent-knowledge-mapper/`.
- Exact installation paths: discover and verify on the target runtime; do not hard-code a universal path.

## Source-of-Truth Boundaries

- GitHub owns skill code, package structure, references, scripts, validation, and release history.
- Notion owns the human operational SOP, assignments, approvals, and completion summaries.
- The mapped subject's owner selects the authoritative home for its knowledge.
- Wiki, Markdown, database, document store, and memory may coexist, but each record type must have one declared authority.
- Hindsight and local memory provide recall and compact continuity pointers; they do not replace atomic or narrative records in the declared authoritative destination.

## Controls

- Operating mode: follow the assigned task mode. Diagnose Mode requires solution and confirmation before mutation.
- Pilot rule: install and test on one approved OpenClaw or Hermes agent before wider rollout.
- First pilot: use the bounded Ruby/Hermes Percify MCP plan in `docs/pilot-plan.md` after privacy, merge, version, and authorization gates pass.
- Pilot version rule: install by immutable release-candidate tag or exact commit, never a moving branch.
- Approval: require human approval for destructive merge, deletion, move, privilege change, production service change, restricted data handling, or broader rollout.
- Retry limit: stop after three failures for the same validation or repair condition.
- Rollback: restore the prior skill package and last known-good knowledge state, then re-run discovery and retrieval checks.

## Completion Evidence

- Repository validator passes.
- Canonical ZedBiz skill validator passes.
- Generated package matches the authoritative source set.
- Positive, paraphrased, boundary, and negative trigger review passes.
- No secret-like content is present.
- Target runtime discovery and realistic retrieval are recorded for each deployment.
- GitHub issue and Notion operational records link the committed artifact.
- Repository visibility is private before proprietary deployment.
- The immutable release-candidate tag and package checksum are recorded for the pilot.

# Z Agent Knowledge Mapper Skill

Date: 2026-08-20 | Agent: Cody | Status: Initial Release

`z-agent-knowledge-mapper` helps an AI agent learn a broad knowledge domain by auditing existing knowledge, planning coverage, researching authoritative sources, preventing duplication, organizing canonical records, selecting a wiki-first destination, and proving live retrieval.

It supports OpenClaw and Hermes from one canonical skill. Platform differences live in small adapters; the research and knowledge architecture do not fork.

## What Makes It Different

- It maps a broad domain rather than creating one isolated knowledge record.
- It searches before research and before every durable creation decision.
- It distinguishes updates, merges, links, new records, and material that should not be stored.
- It prefers a maintained wiki when one is genuinely available.
- It falls back to structured Markdown or an approved database when no usable wiki exists.
- It verifies through the intended agent's live retrieval surface.

This skill complements narrower routing, record, wiki, and database-publishing skills. It can use those as implementation helpers without duplicating their platform-specific procedures.

## Source of Truth

- Technical skill: [GitHub repository](https://github.com/ZedBiz44/z-agent-knowledge-mapper-Skill)
- Operational SOP: [Notion SOP](https://app.notion.com/p/3c2a3e33d581808085cfc145361baf2e)
- Build and change tracking: [GitHub issue 1](https://github.com/ZedBiz44/z-agent-knowledge-mapper-Skill/issues/1)

The skill was designed from ZedBiz's proprietary `z-support-doc-ingestion` workflow and broadened for general knowledge domains. ZedBiz owns both repositories.

## Main Files

- `SKILL.md`: canonical shared workflow.
- `references/research.md`: source discovery, evidence, coverage, and synthesis.
- `references/deduplication.md`: canonical-record decisions and duplicate prevention.
- `references/storage-routing.md`: wiki-first, Markdown, database, and hybrid routing.
- `references/openclaw.md`: OpenClaw discovery, storage, and verification adapter.
- `references/hermes.md`: Hermes discovery, storage, and verification adapter.
- `assets/knowledge-map-template.md`: optional durable coverage manifest.
- `agents/openai.yaml`: Codex/OpenAI interface metadata.
- `scripts/build_package.py`: produces the minimal deployable package.
- `scripts/validate_repository.py`: runs deterministic repository checks.

## Build and Validate

```text
python scripts/validate_repository.py
python scripts/build_package.py
python scripts/validate_repository.py --package dist/z-agent-knowledge-mapper
```

Install only the generated `dist/z-agent-knowledge-mapper/` directory into the approved skill root for the target runtime. Confirm the exact path and live discovery on that runtime; do not assume all OpenClaw or Hermes installations use the same layout.

OpenClaw can install Git-hosted skills with its current skills CLI. Hermes supports local, trusted project, direct GitHub, direct URL, and repository-tap sources. Follow the platform adapter and inspect the current runtime before choosing the installation method.

## Trigger Examples

- Research everything our sales agent needs to know about commercial lending and build a usable knowledge base.
- Map our WordPress security knowledge, merge duplicates, and store the clean version where the agent can retrieve it.
- Organize this agriculture knowledge library and fill important source gaps.
- Build a reusable domain map from these documents, websites, and database records.

Quick factual questions, one-off answers, and a single small record should not trigger the skill.

## Current Platform References

- [OpenClaw skills](https://docs.openclaw.ai/skills)
- [OpenClaw skills CLI](https://docs.openclaw.ai/cli/skills)
- [OpenClaw Memory Wiki](https://docs.openclaw.ai/plugins/memory-wiki)
- [Hermes skills guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)

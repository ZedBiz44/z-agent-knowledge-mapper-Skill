# Storage Routing and Record Structure

## Destination Priority

Use the first destination that is authorized, maintained, writable, searchable, and available to the intended agent:

- maintained wiki;
- structured Markdown repository or agent-readable file tree;
- approved database, document store, or retrieval system;
- hybrid map that links agent-facing knowledge to authoritative operational records.

The first technically available destination is not automatically appropriate. Confirm ownership, source-of-truth boundaries, privacy, retrieval, and durability.

## Discover Local Knowledge Layers

Inspect the environment's actual instructions, tools, schemas, specialist workflows, and access rules. Map available systems by function and authority rather than by product name:

- **Operating instructions:** persistent rules that govern agent or team behavior.
- **Canonical knowledge base:** maintained wiki, repository, database, or document system that owns durable knowledge.
- **Operational system:** business system that owns live records, status, assignments, approvals, or transactions.
- **Episodic or reflection memory:** provider that preserves compact lessons, friction, decisions, or continuity pointers.
- **Technical source control:** authoritative code, configuration, schemas, prompts, and release history.
- **Working context:** temporary session or task information that should not become durable knowledge by default.

One product may serve several roles, or several products may share them. Declare which system owns each claim type. Do not require a named implementation profile when the local environment already exposes these rules clearly.

Use episodic or reflection memory as supporting context unless the environment explicitly designates it as authoritative. Prefer compact pointers to canonical records over full duplicate documents.

## Wiki Qualification

A destination qualifies as the preferred wiki only when it has:

- an active maintained root or collection;
- a supported structure or taxonomy;
- a write path the agent is authorized to use;
- an index, compile, or ingestion path when required;
- a search or retrieval path used by the intended agent;
- verification and rollback rules.

A random Markdown folder is a file store, not automatically a wiki.

## Markdown Fallback

When no suitable wiki exists:

- use an approved repository or durable agent-readable directory;
- create one landing `README.md` or manifest;
- use a small stable directory structure suited to the domain;
- keep filenames descriptive, stable, and portable;
- use relative links where possible;
- verify the intended agent can search and open the files from its live runtime;
- record the authoritative repository, branch, root path, and update process.

## Database or Document-Store Fallback

Use a database or document store when it is the approved durable home and the intended agent has a reliable query path.

- Fetch the live schema before writing.
- Search and fetch plausible matches before creating.
- Use required ownership, type, status, source, sensitivity, and relation fields.
- Keep large source bodies outside structured fields when the platform has a better attachment or source-record pattern.
- Verify the saved record, parent or collection, fields, relations, and retrieval query.
- Use a small index or manifest record when the domain spans many rows.

## Hybrid Design

Use a hybrid when different systems have different authoritative roles. For example:

- technical implementation in version-controlled Markdown;
- business operations in Notion or another managed database;
- a wiki landing page that links both without copying them;
- a compact memory pointer that routes the agent to the canonical record.

Do not create competing full copies. State which system owns each type of truth.

## Minimum Metadata

When the destination has no stronger standard, include:

```yaml
title: Descriptive title
owner: Stable role, team, agent, or subject
scope: Knowledge domain and intended use
record_type: source | entity | concept | procedure | decision | synthesis | glossary | index | report
status: draft | needs-verification | active | needs-review | archived
sources:
  - https://example.com/source
captured: YYYY-MM-DD
verified: YYYY-MM-DD
review_trigger: Date, version change, policy change, or event
aliases:
  - Likely search phrase
```

Use the destination's native fields instead of duplicating them in frontmatter.

When a destination uses different status labels, use its governed workflow and document an unambiguous mapping. Do not leave a knowledge map in an untracked parallel status.

## Suggested Map Shape

Use only the lanes the domain needs:

- `index` or landing page;
- `sources` for preserved source notes and provenance;
- `entities` for durable people, organizations, products, systems, or concepts with identity;
- `concepts` for reusable principles, terms, constraints, and relationships;
- `procedures` for executable work;
- `decisions` for current decisions whose rationale matters;
- `syntheses` for practical cross-source guidance;
- `glossary` for domain language and aliases;
- `reports` for coverage, validation, freshness, and gaps;
- `attachments` only when required.

Avoid one huge undifferentiated document and avoid a separate page for every minor fact.

## Write and Rollback

- Preserve the last known-good state before material restructuring.
- Write in small coherent batches.
- Re-fetch or reopen each batch before continuing.
- Require approval for destructive moves, merges, deletions, permission changes, or publication into a new authoritative system.
- If verification fails, stop further writes and restore or retain the last known-good state.

## Refresh and Ownership

- Assign one stable owner for the map and one owner for each authoritative destination when they differ.
- Record a review cadence based on change risk: fast-changing operational or regulated knowledge needs more frequent review than stable historical knowledge.
- Use event-based refresh triggers for vendor releases, policy or law changes, migrations, source deprecations, ownership changes, contradictions, and failed retrieval tests.
- Re-run source freshness, duplicate search, integrity checks, live retrieval, and a realistic task after material updates.
- Keep review evidence in the operational tracking system; keep the evergreen knowledge focused on current truth.

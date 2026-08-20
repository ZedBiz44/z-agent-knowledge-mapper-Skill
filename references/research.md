# Research Standard

## Build a Source Strategy

Rank likely evidence before collecting it:

- live systems, laws, standards, contracts, first-party records, and official documentation;
- primary research, official repositories, release notes, specifications, and maintained manuals;
- reputable expert analysis and independent testing;
- community discussion, forum posts, videos, and informal explanations;
- AI recall and memory as discovery leads only.

The right authority depends on the subject. A vendor is authoritative about its documented interface; an independent test may be stronger evidence about performance; the owning business record is authoritative about an internal decision.

## Define Coverage

For each major subject area, record:

- the questions the knowledge base must answer;
- the authoritative source or source gap;
- version, date, geography, product, role, or client boundary;
- status as covered, partial, conflicting, unavailable, excluded, or not applicable;
- the canonical record that holds the useful result.

Do not use page count as the primary coverage measure. Coverage is the set of important questions answered with adequate evidence.

## Discover Sources

Use the lightest reliable discovery methods available:

- supplied source list;
- official navigation, sitemap, index, internal search, or `llms.txt`;
- documentation or source repository tree;
- API reference or schema;
- changelog, release notes, policy updates, and deprecation notices;
- connected business systems and existing knowledge;
- supplementary PDFs, videos, transcripts, and expert sources when they add material information.

Use at least two discovery methods when practical for a broad domain. Record inaccessible or excluded sections.

## Evaluate Evidence

Check:

- authority and ownership;
- publication and update date;
- version and geographic applicability;
- whether the source is primary, derivative, sponsored, or user-generated;
- corroboration and contradictions;
- access, reuse, privacy, and licensing restrictions;
- whether the claim is stable or likely to change.

Use current live verification for changeable facts when feasible. Label inference and uncertainty.

## Process Documents and Media

- Prefer structured text, captions, transcripts, or accessible exports.
- Use video or audio only when it adds material steps, demonstrations, or evidence.
- Preserve useful timestamps or page references.
- Summarize rather than storing raw full transcripts by default.
- Inspect representative visual frames when a workflow depends on screen state.
- Do not bypass access controls or ingest private, paid, or login-gated content without approval.

## Synthesize

- Retain source links next to the claims or sections they support.
- Separate facts from recommendations and conclusions.
- Explain conflicts instead of averaging incompatible claims.
- Prefer concise operational guidance over copied prose.
- State freshness and review triggers for changeable domains.
- Preserve exact wording only when legally or operationally necessary and allowed.

## Create Atomic Documents for Exact Facts

Use a small atomic document when an exact, action-driving value must be reproduced without paraphrase, including a public URL, non-secret identifier, date, figure, limit, version number, model name, or official status.

Each atomic document must contain:

- one exact fact or one tightly coupled set of values;
- a stable descriptive title and unique Document ID;
- the authoritative source URL or durable source record;
- captured and last-verified dates, applicable version or scope, owner, lifecycle status, and sensitivity;
- the exact value clearly separated from context;
- a review trigger or expiry rule when the fact can change.

Keep narrative records for context, decisions, reasoning, relationships, and lessons. Link narrative records to atomic documents instead of copying exact values into several places.

Never store passwords, API keys, bearer tokens, private keys, session cookies, recovery codes, or other credential values in an atomic document. Store only a safe credential reference or secret-manager identifier when authorized.

## Research Completion Evidence

Record:

- discovery methods used;
- source inventory and exclusions;
- coverage by major subject area;
- conflicts and how they were handled;
- records produced or updated;
- freshness and review triggers;
- unresolved gaps.

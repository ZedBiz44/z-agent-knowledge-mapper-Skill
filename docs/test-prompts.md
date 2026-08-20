# Trigger and Behavior Tests

Date: 2026-08-20 | Agent: Cody | Status: Release Candidate

## Positive Triggers

- Research the Canadian commercial-lending domain and build a knowledge base our advisory agent can use.
- Map everything our WordPress agent needs to know about site security, remove duplication, and store it in the best available knowledge system.
- Organize this collection of agricultural sources into durable agent knowledge and fill the important research gaps.
- Build a reusable client-industry knowledge map from these documents, official websites, and database records.

Expected: activate the skill, establish scope, audit existing knowledge, create a coverage plan, research, deduplicate, organize, route storage, and verify retrieval.

## Paraphrased Positive Triggers

- Make this agent genuinely knowledgeable about the topic and give it a clean library it can search later.
- Turn these scattered sources into one navigable, non-duplicated subject-matter brain.
- Learn this whole area, figure out what we already know, and save the missing pieces properly.

Expected: same end-to-end workflow without requiring the phrase “knowledge map.”

## Boundary Cases

- Research one substantial topic but return a draft only.
  - Expected: research and propose the map; do not publish durable changes.
- Map a domain when the wiki is read-only.
  - Expected: use it for duplicate detection, then route writes to an authorized Markdown/database destination or coordinator.
- The existing records discuss the same product for different clients.
  - Expected: compare ownership, audience, privacy, and lifecycle; do not merge solely by title.
- A maintained wiki and an operational database both exist.
  - Expected: declare authority by record type and use a hybrid map without competing full copies.
- Important sources conflict.
  - Expected: preserve the conflict, rank evidence, limit conclusions, and report partial when material.
- A platform has both an API and a human dashboard.
  - Expected: map both tracks, link them to shared canonical facts, and verify each applicable surface.
- A domain has no human interface or no programmatic interface.
  - Expected: justify that track as not applicable; do not invent content.
- Research reveals a repeatable procedure, recurring question, and undocumented workaround, but no SOP was requested.
  - Expected: preserve the useful operational building blocks in the proper canonical records; do not create an SOP or guide.
- The environment uses unfamiliar storage and memory products.
  - Expected: discover them by role, authority, access, and retrieval behavior instead of requiring known product names.

## Negative Triggers

- What is the current Bank of Canada overnight rate?
- Summarize this short article for me.
- Fix the spelling in one Markdown file.
- Add one approved customer note to the existing CRM record.
- Rebuild the wiki index without doing new research.

Expected: do not activate the broad knowledge-mapping workflow; use the narrower task or specialist workflow.

## Deployment Evidence

For each OpenClaw or Hermes pilot, record:

- repository visibility confirmed private for proprietary deployment;
- immutable release-candidate tag and exact commit;
- passing history-aware secret-scan run;
- runtime and version;
- installed package commit and checksum;
- exact skill root;
- discovery result in a fresh session;
- prompt used and activation behavior;
- destination and storage path or collection;
- retrieval queries and returned records;
- realistic task result;
- negative-trigger result;
- rollback package and outcome if needed.
- atomic exact-fact Document IDs created or updated, or `none` with the reason;
- lifecycle status for the landing page or manifest;
- applicable local freshness or staleness checks;
- dual-track coverage and operational reuse-signal decisions.

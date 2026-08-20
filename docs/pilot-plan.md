# First Pilot Plan

Date: 2026-08-20 | Agent: Cody | Status: Proposed | Release Gate Pending

## Pilot Assignment

Map the current Percify MCP tool surface for Ruby on Hermes so Ruby can identify the available tools, choose the correct tool for a practical request, and retrieve exact non-secret tool facts from authoritative records.

## Scope

- Pilot agent: Ruby.
- Runtime: Ruby's active Hermes profile and actual skill toolset.
- Included: supported Percify MCP tools, their durable jobs, important inputs and outputs, public documentation links, non-secret identifiers, constraints, common selection rules, and one safe realistic task.
- Excluded: credentials, token values, private keys, production mutations, unrelated MCP servers, and fleet rollout.
- Storage: the authorized Ruby-accessible wiki or Markdown authority confirmed during pilot setup; Hindsight receives compact pointers only after the durable records are verified.

## Required Evidence

- Repository is private and the pilot package is installed from `v0.1.0-rc1` or its exact reviewed commit with a recorded checksum.
- Ruby discovers and activates the skill in a fresh Hermes session.
- Existing ZedBiz knowledge skills and records are checked before new records are created.
- Exact action-driving values use atomic documents with stable titles, Document IDs, authoritative sources, verification dates, and Z-Knowledge lifecycle statuses.
- Hindsight recall is checked first, but every action-driving claim is verified against atomic metadata and the authoritative source.
- Searches by `Percify`, a tool alias, and a practical question return the correct canonical records.
- Ruby opens a returned record and completes one safe tool-selection or read-only task from the mapped knowledge.
- A negative prompt correctly avoids the broad mapper skill.
- The previous skill package and knowledge state can be restored.

## Pass or Fail

Pass only when every required item is evidenced through Ruby's live Hermes surface. Any missing discovery, authority, atomic metadata, retrieval, realistic-task, negative-trigger, privacy, checksum, or rollback evidence is a failed or blocked pilot—not a partial production approval.

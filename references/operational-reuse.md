# Dual-Track and Operational Reuse

## Use Both Tracks as an Importance Filter

For a tool, platform, or workflow, evaluate both tracks when they exist.

### Technical or Agent-Execution Track

Capture knowledge needed for reliable programmatic work, including:

- APIs, MCP or equivalent tool interfaces, commands, schemas, and data models;
- authentication patterns and permission boundaries without secret values;
- automation paths, integrations, limits, error behavior, constraints, and performance;
- validation methods, safe failure handling, and technical fallbacks.

### Human-Operator Track

Capture knowledge needed for reliable human operation, including:

- interface navigation, settings, roles, permissions, and account states;
- manual workflows, decision points, prerequisites, inputs, and expected outputs;
- troubleshooting, recovery, escalation, and manual fallbacks;
- terminology and explanations that help a person understand system behavior.

Mark a track `not applicable` only when the domain genuinely lacks that operating surface. Do not invent content to fill a track.

## Recognize Operational Reuse Signals

Treat these as signals that knowledge may deserve durable storage:

- a repeatable procedure or sequence;
- a prerequisite, dependency, role, permission, or responsibility;
- a consequential decision point or business rule;
- an expected input, output, validation, or completion condition;
- an exception, failure mode, escalation path, or manual fallback;
- an undocumented workaround, API quirk, or interface friction point;
- a recurring question, misunderstanding, or support burden;
- a configuration, prompt, or pattern that materially changes results;
- an opportunity to improve a system, automate work, or reduce risk.

A signal is not automatic permission to create a separate record. Compare it with existing knowledge, evidence, durability, future usefulness, risk, and source-of-truth ownership first.

## Capture at Checkpoints

Capture meaningful discoveries at coherent checkpoints, not every action. Preserve verified workarounds, recurring friction, important decisions, and reusable operational knowledge. Leave transient logs, routine clicks, disposable calculations, and unverified observations in working context.

Promote an observation only after its evidence and destination are clear. Mark unresolved observations as gaps or needs-verification items rather than operational truth.

## Preserve Building Blocks, Not Unrequested Assets

Store the smallest useful knowledge units needed for later execution, support, onboarding, system improvement, or authorized documentation work. These may include atomic facts, procedures, decision rules, failure records, examples, or linked source evidence.

Do not automatically assemble those units into an SOP, guide, runbook, training package, or customer-facing asset. Create those deliverables only when the assignment explicitly requests them.

Avoid competing technical and human copies of the same exact fact. Keep exact values in one canonical record and link both tracks to it.

## Verify Track Coverage

When applicable:

- prove the technical track through the actual programmatic or agent tool surface;
- prove the human track against the current interface, supported instructions, or a safe representative walkthrough;
- verify that saved operational signals can be retrieved from their declared canonical destination;
- report any track, source, or workflow that remains partial, inaccessible, or not applicable.

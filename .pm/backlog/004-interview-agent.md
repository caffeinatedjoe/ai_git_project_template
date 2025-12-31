---
id: TASK-004
status: done
priority: medium
estimate: 2
owner: ai
depends_on: []
---

# Create interview agent for project discovery

## Problem
There is no dedicated agent role for interviewing a human to define a new project concept before architecture work begins.

## Context
A new agent is needed in `agents/` to guide discovery conversations and capture project-defining inputs.

## Plan
- Review existing agent role definitions (e.g., `agents/pair-programmer.md`) for structure and tone.
- Draft a new agent role file in `agents/` (name TBD) focused on pre-architecture project interviews, including:
  - Purpose and scope for discovery-only conversations.
  - A structured question flow (problem framing, goals, constraints, stakeholders).
  - Required outputs (project summary, constraints, success criteria, open questions).
  - Guardrails that defer architecture decisions until discovery is complete.
- Validate acceptance criteria by confirming the new file content and placement.

## Acceptance Criteria
- [x] New agent role file exists under `agents/` with clear interviewing guidance.
- [x] The role describes required outputs (e.g., project summary, constraints, success criteria).
- [x] The role emphasizes completing discovery before architecture decisions.

## Out of Scope
- Implementing project architecture or delivery plans.

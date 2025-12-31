---
id: TASK-004
status: todo
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
- Review existing agent role definitions for structure and tone.
- Draft a new agent role file in `agents/` focused on pre-architecture project interviews.
- Ensure the new role defines goals, question flow, outputs, and guardrails.

## Acceptance Criteria
- [ ] New agent role file exists under `agents/` with clear interviewing guidance.
- [ ] The role describes required outputs (e.g., project summary, constraints, success criteria).
- [ ] The role emphasizes completing discovery before architecture decisions.

## Out of Scope
- Implementing project architecture or delivery plans.

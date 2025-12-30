---
id: TASK-003
status: done
priority: medium
estimate: 2
owner: ai
depends_on: []
---

# Add notes reference area

## Problem
There is no dedicated place to store collaborative notes, brainstorming artifacts, or AI interview transcripts.

## Context
We want a lightweight, Markdown-first space for humans and AI to capture reference material without mixing it into canonical process or task docs.

## Plan
- Define the `notes/` structure and add an initial README with purpose, usage rules, and templates.
- Add initial reference templates for AI interview prompts and brainstorming sessions.
- Document how notes relate to canonical `.pm/` artifacts (non-canonical, optional).

## Acceptance Criteria
- [x] `notes/README.md` explains purpose, scope, and how to use the folder.
- [x] `notes/` includes starter templates for AI interview and brainstorming sessions.
- [x] Documentation clarifies that notes are non-canonical references.

## Out of Scope
- Defining new task workflow changes.

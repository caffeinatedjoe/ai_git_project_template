---
id: TASK-002
status: todo
priority: medium
estimate: 2
owner: ai
depends_on: []
---

# Build test to verify BOARD.md correctness using gen_board.py

## Problem
We need an automated test to verify that the BOARD.md file is correctly updated and in sync with the task frontmatter in .pm/backlog/*.md files, using the gen_board.py script as the source of truth.

## Context
According to AGENTS.md, BOARD.md is a derived artifact from task frontmatter and must always reflect the current state. Any changes to task status, owner, or priority must update BOARD.md in the same commit. A test will help ensure this rule is followed and catch any discrepancies.

## Plan
- Create a test script in the tests/ directory that:
  - Runs gen_board.py to generate the expected BOARD.md content
  - Compares it with the current BOARD.md file
  - Reports pass/fail based on whether they match
- Ensure the test can be run as part of a CI/CD pipeline or manually

## Acceptance Criteria
- [ ] Test script created in tests/ directory
- [ ] Test passes when BOARD.md is correctly generated from task frontmatter
- [ ] Test fails and reports differences when BOARD.md is out of sync
- [ ] Test can be executed via command line (e.g., python tests/test_board_sync.py)

## Out of Scope
- Modifying gen_board.py itself
- Implementing BOARD.md generation logic outside of gen_board.py
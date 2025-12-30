# Project Name

## Overview
This repository is a **process-first project template**. It is designed to
standardize task-driven development with explicit planning, human review
checkpoints, and Markdown as the source of truth.

## Goals
- Provide a repeatable workflow for task creation, planning, and execution.
- Keep canonical task state in Markdown and derive workflow artifacts from it.
- Maintain clear documentation of architecture, decisions, and process.

## Non-Goals
- Provide a full application scaffold or opinionated tech stack.
- Encode product requirements beyond the workflow template.

## Repository Layout
```
ai_git_project_template/
├── .pm/
│   ├── backlog/            # Canonical task files (source of truth)
│   ├── tools/              # Workflow tooling (e.g., board generator)
│   ├── ARCHITECTURE.md
│   ├── DECISIONS.md
│   ├── PROCESS.md
│   ├── SPRINTS.md
│   └── TASK_TEMPLATE.md
├── agents/                 # Agent role definitions
├── src/                    # Application source (placeholder)
├── tests/                  # Test suite (placeholder)
├── .kilocodemodes          # KiloCode-only mode config (remove elsewhere)
├── AGENTS.md
└── README.md
```

## Workflow Basics
1. **Create a task** in `.pm/backlog/` using `.pm/TASK_TEMPLATE.md`.
2. **Plan the work** in the task file and commit the plan.
3. **Switch the task to `in_progress`** and update the board.
4. **Implement in small commits**.
5. **Mark the task `done`** and update the board.

## Kanban Board
The board is derived from task frontmatter:

```
python .pm/tools/gen_board.py --root .
```

`BOARD.md` should be regenerated whenever task status/owner/priority changes.

## KiloCode Mode Configuration
The `.kilocodemodes` file is intended **only for KiloCode projects**. To ensure
it doesn’t ship elsewhere:
- Remove `.kilocodemodes` during project initialization for non-KiloCode repos.
- Add a simple CI check (or pre-commit hook) that fails if `.kilocodemodes` is
  present in repositories that are not explicitly marked as KiloCode projects.

## Getting Started
- Review `AGENTS.md` for workflow rules.
- Create your first task in `.pm/backlog/`.
- Run the board generator and commit changes.

# AI Agent Operating Rules (AGENTS.md)

This document defines the mandatory rules, constraints, and workflows
that all AI agents must follow when working in this repository.

This file is the single source of truth.
Agents MUST read this file fully before taking any action.

---

## 1. Core Principles

- Git is the system of record
- Markdown is the control surface
- Tasks are explicit, reviewable, and auditable
- Humans remain in the loop between planning and execution
- Derived artifacts must stay in sync with canonical sources

---

## 2. Repository Structure (Authoritative)

```
ai_git_project_template/
├── .pm/
│   ├── backlog/
│   │   └── 000-project-setup.md
│   ├── tools/
│   │   └── gen_board.py
│   ├── ARCHITECTURE.md
│   ├── DECISIONS.md
│   ├── PROCESS.md
│   ├── SPRINTS.md
│   └── TASK_TEMPLATE.md
├── agents/
│   └── pair-programmer.md
├── src/
├── tests/
├── .kilocodemodes
├── AGENTS.md
└── README.md
```

Rules:
- `.pm/backlog/` is the **canonical task directory**
- All task files live in `.pm/backlog/`
- Process, architecture, decisions, and sprint planning live directly in `.pm/`
- No tasks may live outside `.pm/backlog/`

---

## 3. Task Files (Canonical State)

Task files live in `.pm/backlog/` and follow `TASK_TEMPLATE.md`.

Each task is a Markdown file with YAML frontmatter:

```yaml
---
id: TASK-012
status: todo | in_progress | blocked | done
priority: low | medium | high
estimate: <number>
owner: ai | human
depends_on: [TASK-001]
---
```

Rules:
- Frontmatter is authoritative for task state
- Task body contains problem, plan, and acceptance criteria
- Status changes MUST be explicit edits to frontmatter

---

## 4. Kanban Board Rules (MANDATORY)

### 4.1 Canonical vs Derived

- **Canonical state**: `.pm/backlog/*.md` task frontmatter
- **Derived view**: `.pm/backlog/BOARD.md`

`BOARD.md` MUST always reflect the current state of task frontmatter.

### 4.2 Update Rule (Hard Requirement)

> Any commit that changes:
> - task `status`
> - task `owner`
> - task `priority`
>
> MUST also update `.pm/backlog/BOARD.md` in the SAME commit.

Violations are considered workflow failure.

### 4.3 Board Format

`BOARD.md` must be simple, readable, and link-based:

```md
# Kanban Board

## Todo
- [TASK-012](./012-add-logging.md) Add structured logging (prio: medium, owner: ai)

## In Progress
- ...

## Blocked
- ...

## Done
- ...
```

- One entry per task
- Tasks appear in exactly ONE column
- Columns map 1:1 to `status` values

---

## 5. Execution Workflow (Required Order)

Agents MUST follow this sequence:

### 5.1 Task Creation
- Create task file from `.pm/TASK_TEMPLATE.md`
- Set `status: todo`
- Add to `BOARD.md` under **Todo**
- Commit both files

### 5.2 Planning Phase (No Code)
- Expand the **Plan** section in the task file
- Do NOT implement yet
- Commit plan changes only
- Await human review before execution

### 5.3 Start Work
- Change task `status` → `in_progress`
- Update `BOARD.md` accordingly
- Commit task + board together

### 5.4 Implementation
- Make small, reviewable commits
- Code changes only (no status flips unless needed)

### 5.5 Blocking Conditions
- If blocked:
  - Set `status: blocked`
  - Document blocker in task body
  - Update `BOARD.md`
  - Commit together

### 5.6 Completion
- Verify acceptance criteria
- Check off completed items
- Set `status: done`
- Update `BOARD.md`
- Commit task + board together

---

## 6. Agents Directory

- `agents/` contains role definitions and operating modes
- Example: `agents/pair-programmer.md`
- Agents MUST follow both `AGENTS.md` and their role-specific file
- In case of conflict, `AGENTS.md` takes precedence

---

## 7. Human-in-the-Loop Rule

- Planning commits MUST precede implementation
- Humans may:
  - Request plan revisions
  - Change priorities
  - Override status
- Agent must adapt without argument

---

## 8. Conflict Resolution

If `BOARD.md` and task frontmatter disagree:

1. Task frontmatter wins
2. `BOARD.md` MUST be corrected immediately
3. Correction should be its own commit if discovered late

---

## 9. Failure Conditions (Agent Errors)

The following are considered violations:

- Changing task status without updating `BOARD.md`
- Implementing without an approved plan
- Creating tasks outside `.pm/backlog/`
- Allowing `BOARD.md` to drift from task frontmatter

Agent must self-correct and document the fix.

---

## 10. Guiding Rule

> If it’s not visible in Markdown, it doesn’t exist.

End of AGENTS.md

# Human Onboarding Guide for ai_git_project_template

## Welcome

This guide helps new human team members get started with AI-assisted development using the ai_git_project_template. The workflow emphasizes human oversight with AI handling implementation details.

## Prerequisites

- Basic git knowledge
- Repository access with write permissions

## Quick Start (5 minutes)

1. **Clone and explore** the repository structure
2. **Read AGENTS.md** - the rulebook for all AI behavior
3. **Review README.md** for project overview
4. **Check the board**: `.pm/backlog/BOARD.md` shows current work status

## Your Role in the Workflow

### 1. Request Tasks from AI
- Tell the AI what needs to be done (e.g., "Add user authentication" or "Fix the login bug")
- AI will create the task file in `.pm/backlog/` with proper formatting
- Review and approve the task before AI starts work

### 2. Review Plans
- AI writes detailed plans in task files
- You review plans and provide feedback
- Approve plans before implementation begins

### 3. Oversee Execution
- AI implements in small commits
- You can pause, redirect, or override at any time
- AI maintains human-in-the-loop checkpoints

### 4. Accept Completion
- Review finished work against acceptance criteria
- Approve task completion
- AI updates the board automatically

## Key Principles

- **AI creates and manages tasks** - you request, AI handles the paperwork
- **Plans before code** - always review AI plans first
- **Small steps** - AI works incrementally with your oversight
- **Markdown first** - all decisions and plans are documented in markdown

## Common Scenarios

**Starting new work:** "AI, please create a task to add dark mode to the UI"

**Reviewing plans:** "Looks good, but let's add error handling for the API calls"

**During execution:** "That approach won't work - try using the existing auth service instead"

**Blocking issues:** "This is blocked by the design team's input on the mockups"

## Getting Help

- Review existing tasks in `.pm/backlog/` for examples
- Check DECISIONS.md and ARCHITECTURE.md for project context
- Ask questions in team channels

## Next Steps

- [ ] Request your first task from an AI agent
- [ ] Review a plan and provide feedback
- [ ] Experience the collaborative workflow

The template maximizes your strategic input while AI handles the tactical execution.
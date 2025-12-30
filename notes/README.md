# Notes

## Purpose
This folder is a shared, Markdown-first space for humans and AI assistants to capture
brainstorming output, interview transcripts, research snippets, and other reference
material that is useful during work but **not** part of the canonical project record.

## Scope
- Non-canonical reference material only.
- Notes here do **not** replace tasks in `.pm/backlog/`.
- Anything that should be actionable must be promoted into a task file.

## Structure
```
notes/
├── README.md
├── templates/
│   ├── ai-interview.md
│   └── brainstorming-session.md
├── sessions/
└── reference/
```

### templates/
Reusable Markdown templates for interviews, brainstorming, and other repeated formats.

### sessions/
Dated, topic-focused notes from a specific collaboration session.

### reference/
General-purpose reference notes that may outlive a single session.

## Process
1. **Start with a template**
   - Copy a file from `notes/templates/` into `notes/sessions/`.
2. **Name it clearly**
   - Use the format: `YYYY-MM-DD-topic-shortname.md`.
3. **Capture the conversation**
   - Record questions, answers, assumptions, and follow-ups.
4. **Promote actionable work**
   - If a note implies a task, create or update a task in `.pm/backlog/`.
5. **Keep notes lightweight**
   - Avoid duplicating canonical decisions or architecture; link to `.pm/` docs when needed.

## AI Interview Guidance
When you need the AI to interview you for brainstorming:
- Start with the `ai-interview.md` template.
- Answer questions in-order; add new questions as they arise.
- End with a summary and a list of candidate tasks.

#!/usr/bin/env python3
"""
Generate .pm/backlog/BOARD.md from task frontmatter in .pm/backlog/*.md.

Source of truth: task files in .pm/backlog/*.md (YAML frontmatter)
Derived artifact: .pm/backlog/BOARD.md (do not hand-edit if using this script)

Usage:
  python .pm/tools/gen_board.py
  python .pm/tools/gen_board.py --root /path/to/repo
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


STATUSES = ["todo", "in_progress", "blocked", "done"]
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


@dataclass(frozen=True)
class Task:
    path: str               # absolute path
    rel_link: str           # link used in BOARD.md (relative)
    task_id: str
    status: str
    priority: str
    owner: str
    title: str


_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_H1_RE = re.compile(r"(?m)^\#\s+(.+?)\s*$")


def _parse_simple_yaml(frontmatter: str) -> Dict[str, str]:
    """
    Minimal YAML frontmatter parser for 'key: value' lines.
    - Ignores blank lines and comments.
    - Treats everything after ':' as a raw string value (stripped).
    This is intentionally conservative to avoid external deps.
    """
    out: Dict[str, str] = {}
    for line in frontmatter.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k:
            out[k] = v
    return out


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _extract_frontmatter_and_body(text: str) -> Tuple[Optional[str], str]:
    m = _FRONTMATTER_RE.search(text)
    if not m:
        return None, text
    fm = m.group(1)
    body = text[m.end():]
    return fm, body


def _extract_title(body: str, fallback_filename: str) -> str:
    m = _H1_RE.search(body)
    if m:
        return m.group(1).strip()
    # fallback: "012-add-logging.md" -> "012 add logging"
    base = os.path.splitext(os.path.basename(fallback_filename))[0]
    return base.replace("-", " ").strip()


def _status_key(status: str) -> int:
    try:
        return STATUSES.index(status)
    except ValueError:
        return 999


def _priority_key(priority: str) -> int:
    return PRIORITY_ORDER.get(priority, 999)


def _should_skip(filename: str) -> bool:
    name = os.path.basename(filename)
    return name.upper() in {"BOARD.MD"} or name.upper().endswith(".TEMPLATE.MD") or name.upper() == "TASK_TEMPLATE.MD"


def load_tasks(repo_root: str) -> List[Task]:
    backlog_dir = os.path.join(repo_root, ".pm", "backlog")
    pattern = os.path.join(backlog_dir, "*.md")
    files = sorted(glob.glob(pattern))

    tasks: List[Task] = []
    for path in files:
        if _should_skip(path):
            continue

        text = _read_text(path)
        fm_text, body = _extract_frontmatter_and_body(text)
        if not fm_text:
            # Not a task file (or missing required frontmatter); skip silently
            continue

        fm = _parse_simple_yaml(fm_text)

        task_id = fm.get("id", "").strip()
        status = fm.get("status", "").strip()
        priority = fm.get("priority", "").strip()
        owner = fm.get("owner", "").strip()

        # Basic validation: must have an id and status
        if not task_id or not status:
            continue

        status = status.lower()
        priority = (priority or "medium").lower()
        owner = owner or "ai"

        title = _extract_title(body, path)

        # Links from BOARD.md (in .pm/backlog/) should be relative like "./012-foo.md"
        rel_link = f"./{os.path.basename(path)}"

        tasks.append(
            Task(
                path=os.path.abspath(path),
                rel_link=rel_link,
                task_id=task_id,
                status=status,
                priority=priority,
                owner=owner,
                title=title,
            )
        )

    return tasks


def render_board(tasks: List[Task]) -> str:
    by_status: Dict[str, List[Task]] = {s: [] for s in STATUSES}
    other: List[Task] = []

    for t in tasks:
        if t.status in by_status:
            by_status[t.status].append(t)
        else:
            other.append(t)

    # Sort within each status: priority, then id, then title
    for s in STATUSES:
        by_status[s].sort(key=lambda t: (_priority_key(t.priority), t.task_id, t.title.lower()))

    other.sort(key=lambda t: (_status_key(t.status), _priority_key(t.priority), t.task_id, t.title.lower()))

    def line(t: Task) -> str:
        return f"- [{t.task_id}]({t.rel_link}) {t.title} (prio: {t.priority}, owner: {t.owner})"

    parts: List[str] = []
    parts.append("# Kanban Board\n")
    parts.append("> Generated file. Source of truth: `.pm/backlog/*.md` frontmatter.\n")
    parts.append("\n")

    parts.append("## Todo\n")
    parts.extend([line(t) + "\n" for t in by_status["todo"]])
    if not by_status["todo"]:
        parts.append("- (none)\n")
    parts.append("\n")

    parts.append("## In Progress\n")
    parts.extend([line(t) + "\n" for t in by_status["in_progress"]])
    if not by_status["in_progress"]:
        parts.append("- (none)\n")
    parts.append("\n")

    parts.append("## Blocked\n")
    parts.extend([line(t) + "\n" for t in by_status["blocked"]])
    if not by_status["blocked"]:
        parts.append("- (none)\n")
    parts.append("\n")

    parts.append("## Done\n")
    parts.extend([line(t) + "\n" for t in by_status["done"]])
    if not by_status["done"]:
        parts.append("- (none)\n")

    if other:
        parts.append("\n## Other / Unknown Status\n")
        parts.extend([line(t) + f" (status: {t.status})\n" for t in other])

    return "".join(parts)


def write_board(repo_root: str, content: str) -> str:
    board_path = os.path.join(repo_root, ".pm", "backlog", "BOARD.md")
    os.makedirs(os.path.dirname(board_path), exist_ok=True)
    with open(board_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return board_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repo root (default: current directory)")
    args = ap.parse_args()

    repo_root = os.path.abspath(args.root)
    tasks = load_tasks(repo_root)
    board = render_board(tasks)
    board_path = write_board(repo_root, board)
    print(f"Wrote {board_path} ({len(tasks)} tasks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
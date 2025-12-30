#!/usr/bin/env python3
"""
Test script to verify BOARD.md correctness using gen_board.py

This script generates the expected BOARD.md content from task frontmatter
and compares it with the current BOARD.md file.

Usage:
    python tests/test_board_sync.py

Returns:
    0 if BOARD.md is in sync (PASS)
    1 if BOARD.md is out of sync (FAIL)
"""

import sys
import os
import difflib

# Add the tools directory to the path to import gen_board
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.pm', 'tools'))

from gen_board import load_tasks, render_board

def main():
    repo_root = os.path.join(os.path.dirname(__file__), '..')

    # Load tasks and generate expected board content
    tasks = load_tasks(repo_root)
    expected_content = render_board(tasks)

    # Read current BOARD.md
    board_path = os.path.join(repo_root, '.pm', 'backlog', 'BOARD.md')
    try:
        with open(board_path, 'r', encoding='utf-8') as f:
            current_content = f.read()
    except FileNotFoundError:
        print(f"FAIL: BOARD.md not found at {board_path}")
        return 1

    # Compare
    if expected_content == current_content:
        print("PASS: BOARD.md is correctly synchronized with task frontmatter")
        return 0
    else:
        print("FAIL: BOARD.md is out of sync with task frontmatter")
        print("\nDifferences:")
        diff = difflib.unified_diff(
            current_content.splitlines(keepends=True),
            expected_content.splitlines(keepends=True),
            fromfile='current BOARD.md',
            tofile='expected BOARD.md'
        )
        sys.stdout.writelines(diff)
        return 1

if __name__ == "__main__":
    sys.exit(main())
"""Create a compact repo context pack for agent review.

This script is intentionally dependency-free. It captures:
- the current task
- git status
- git diff
- the file tree outside .git
- selected text files up to a small size limit
"""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reviews" / "latest" / "context-pack.md"
MAX_FILE_BYTES = 24_000
INCLUDE_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
    ".env.example",
}
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache"}


def run_git(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError:
        return "git is not available on PATH"

    output = result.stdout.strip()
    error = result.stderr.strip()
    if error:
        return f"{output}\n\n[stderr]\n{error}".strip()
    return output


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        files.append(path)
    return sorted(files)


def is_included(path: Path) -> bool:
    if path.name == ".env.example":
        return True
    return path.suffix.lower() in INCLUDE_SUFFIXES


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    if len(raw) > MAX_FILE_BYTES:
        return f"[Skipped: file is {len(raw)} bytes, above {MAX_FILE_BYTES} byte limit]"
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return "[Skipped: file is not valid UTF-8 text]"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True, help="Current design or implementation task")
    args = parser.parse_args()

    files = iter_files()
    tree = "\n".join(f"- {path.relative_to(ROOT)}" for path in files)

    sections = [
        "# Context Pack",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Repo: `{ROOT}`",
        "",
        "## Current Task",
        "",
        args.task,
        "",
        "## Git Status",
        "",
        "```text",
        run_git(["status", "--short"]) or "[clean]",
        "```",
        "",
        "## Git Diff",
        "",
        "```diff",
        run_git(["diff"]) or "[no diff]",
        "```",
        "",
        "## File Tree",
        "",
        tree or "[no files]",
        "",
        "## Included Files",
    ]

    for path in files:
        rel = path.relative_to(ROOT)
        if not is_included(path):
            continue
        sections.extend(
            [
                "",
                f"### {rel}",
                "",
                "```text",
                read_text(path),
                "```",
            ]
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(sections) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()


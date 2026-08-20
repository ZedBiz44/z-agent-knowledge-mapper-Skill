#!/usr/bin/env python3
"""Build the portable z-agent-knowledge-mapper skill package."""

from __future__ import annotations

import re
import shutil
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILE = ROOT / "SKILL.md"


def remove_readonly(function, path: str, _error) -> None:
    """Allow clean rebuilds when a synced Windows folder marks files read-only."""
    Path(path).chmod(stat.S_IWRITE)
    function(path)


def skill_name() -> str:
    text = SKILL_FILE.read_text(encoding="utf-8")
    match = re.search(r"(?m)^name:\s*[\"']?([^\"'\r\n]+)", text)
    if not match:
        raise SystemExit(f"ERROR: Could not read skill name from {SKILL_FILE}")
    return match.group(1).strip()


def main() -> None:
    if not SKILL_FILE.is_file():
        raise SystemExit(f"ERROR: Missing {SKILL_FILE}")

    destination = ROOT / "dist" / skill_name()
    if destination.exists():
        shutil.rmtree(destination, onexc=remove_readonly)
    destination.mkdir(parents=True)

    shutil.copy2(SKILL_FILE, destination / "SKILL.md")
    for directory in ("references", "assets", "agents"):
        source = ROOT / directory
        if source.is_dir():
            shutil.copytree(source, destination / directory)

    print(f"Built deployable package: {destination}")


if __name__ == "__main__":
    main()

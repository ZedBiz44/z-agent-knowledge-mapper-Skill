#!/usr/bin/env python3
"""Run deterministic structural checks for the knowledge-mapper skill."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


EXPECTED_NAME = "z-agent-knowledge-mapper"
REQUIRED_REFERENCES = {
    "references/research.md",
    "references/deduplication.md",
    "references/storage-routing.md",
    "references/openclaw.md",
    "references/hermes.md",
}


def validate(root: Path, package: bool) -> list[str]:
    failures: list[str] = []
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return [f"Missing {skill_path}"]

    text = skill_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) >= 500:
        failures.append(f"SKILL.md must be under 500 lines; found {len(lines)}")

    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not frontmatter:
        failures.append("SKILL.md needs YAML frontmatter")
    else:
        fields = []
        values: dict[str, str] = {}
        for line in frontmatter.group(1).splitlines():
            match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
            if match:
                key, value = match.groups()
                fields.append(key)
                values[key] = value.strip().strip('"\'')
        if fields != ["name", "description"]:
            failures.append(f"Shared frontmatter must contain only name and description; found {fields}")
        if values.get("name") != EXPECTED_NAME:
            failures.append(f"Expected name {EXPECTED_NAME!r}; found {values.get('name')!r}")
        description = values.get("description", "")
        if not description or len(description) > 160:
            failures.append(f"Description must be 1-160 characters; found {len(description)}")

    if root.name != EXPECTED_NAME and package:
        failures.append(f"Package directory must be {EXPECTED_NAME!r}; found {root.name!r}")

    for relative in sorted(REQUIRED_REFERENCES):
        if not (root / relative).is_file():
            failures.append(f"Missing required reference: {relative}")
        if f"({relative})" not in text:
            failures.append(f"SKILL.md does not directly link {relative}")

    for link in re.findall(r"\]\(([^)]+)\)", text):
        if "://" in link or link.startswith("#"):
            continue
        if not (root / link).is_file():
            failures.append(f"Broken local link in SKILL.md: {link}")

    forbidden_placeholders = re.findall(r"(?i)\b(?:TODO|TBD|FIXME)\b", text)
    if forbidden_placeholders:
        failures.append("SKILL.md contains unfinished placeholder text")

    risky_patterns = {
        "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        "GitHub token": r"gh[pousr]_[A-Za-z0-9]{20,}",
        "OpenAI-style key": r"sk-[A-Za-z0-9_-]{20,}",
    }
    scan_files = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
    for path in scan_files:
        if path.suffix.lower() not in {".md", ".yaml", ".yml", ".py", ".txt"}:
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in risky_patterns.items():
            if re.search(pattern, content):
                failures.append(f"Possible {label} in {path.relative_to(root)}")

    adapter = root / "agents" / "openai.yaml"
    if not adapter.is_file():
        failures.append("Missing agents/openai.yaml")
    else:
        adapter_text = adapter.read_text(encoding="utf-8")
        match = re.search(r'(?m)^\s*short_description:\s*["\']?(.*?)["\']?\s*$', adapter_text)
        if not match or not (25 <= len(match.group(1).strip().strip('"\'')) <= 64):
            failures.append("OpenAI short_description must be 25-64 characters")
        if f"${EXPECTED_NAME}" not in adapter_text:
            failures.append("OpenAI default_prompt must invoke the canonical skill name")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", type=Path, help="Validate a generated package instead of the repository")
    args = parser.parse_args()

    root = args.package.resolve() if args.package else Path(__file__).resolve().parents[1]
    failures = validate(root, package=args.package is not None)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"PASS: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

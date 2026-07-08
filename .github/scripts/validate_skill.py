#!/usr/bin/env python3
"""CI check: validate every skill's SKILL.md frontmatter.

For each `skills/<name>/SKILL.md`, assert that:
  - it has YAML frontmatter with a `name` and a `description`,
  - `name` matches the containing folder (the skill id tools resolve by),
  - `description` is within the 1024-character skill-triggering limit.

Exits non-zero (failing the workflow) with GitHub-annotated errors on any problem.
Dependency-free so it needs no setup step.
"""
import sys
from pathlib import Path

MAX_DESC = 1024


def parse_frontmatter(text: str) -> dict | None:
    """Minimal YAML-frontmatter parser handling folded/literal block scalars."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    fm: dict[str, str] = {}
    i = 1
    while i < len(lines) and lines[i].strip() != "---":
        line = lines[i]
        if line and not line[0].isspace() and ":" in line:
            key, val = line.split(":", 1)
            key, val = key.strip(), val.strip()
            if val in (">", "|", ">-", "|-", ">+", "|+"):
                block = []
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or lines[i].startswith("\t")):
                    block.append(lines[i].strip())
                    i += 1
                fm[key] = " ".join(b for b in block if b)
                continue
            fm[key] = val.strip('"').strip("'")
        i += 1
    return fm


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    skill_files = sorted(root.glob("skills/*/SKILL.md"))
    if not skill_files:
        print("::error::no skills/*/SKILL.md found")
        return 1

    errors: list[str] = []
    for sf in skill_files:
        rel = sf.relative_to(root)
        fm = parse_frontmatter(sf.read_text())
        if fm is None:
            errors.append(f"{rel}: missing YAML frontmatter (no opening '---')")
            continue

        name = fm.get("name", "").strip()
        desc = fm.get("description", "").strip()
        folder = sf.parent.name

        if not name:
            errors.append(f"{rel}: missing 'name'")
        elif name != folder:
            errors.append(f"{rel}: name '{name}' does not match folder '{folder}'")

        if not desc:
            errors.append(f"{rel}: missing 'description'")
        elif len(desc) > MAX_DESC:
            errors.append(f"{rel}: description is {len(desc)} chars (limit {MAX_DESC})")

        if name == folder and desc and len(desc) <= MAX_DESC:
            print(f"ok: {rel}  (name={name}, description={len(desc)} chars)")

    if errors:
        for e in errors:
            print(f"::error::{e}")
        return 1
    print(f"All {len(skill_files)} skill(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

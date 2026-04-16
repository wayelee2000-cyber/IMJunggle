#!/usr/bin/env python3
"""Normalize internal markdown links under api-md.

This script updates relative links that point to local markdown/MDX docs so they
include the actual file extension. That makes them compatible with the docs
router used by api-reference.html.
"""

from __future__ import annotations

import argparse
import re
import os
from pathlib import Path


LINK_RE = re.compile(r"(?P<prefix>!?\[[^\]]*\]\()(?P<target>[^)]+)(?P<suffix>\))")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fix internal markdown links under api-md.")
    parser.add_argument("--source", default="api-md", help="Source directory to scan.")
    parser.add_argument("--limit", type=int, default=0, help="Only process the first N files.")
    return parser.parse_args()


def collect_docs(root: Path) -> dict[Path, Path]:
    mapping: dict[Path, Path] = {}
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".mdx"}:
            mapping[path.resolve()] = path
    return mapping


def resolve_target(base_dir: Path, target: str, docs: dict[Path, Path]) -> str | None:
    clean = target.strip()
    if not clean or clean.startswith(("http://", "https://", "#", "mailto:", "data:")):
        return None

    parts = clean.split("#", 1)
    path_part = parts[0]
    anchor = "#" + parts[1] if len(parts) > 1 else ""
    if not path_part or Path(path_part).suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}:
        return None

    raw_path = (base_dir / path_part).resolve()
    candidates = []
    if raw_path.suffix.lower() in {".md", ".mdx"}:
        candidates.append(raw_path)
    else:
        candidates.append(raw_path.with_suffix(".md"))
        candidates.append(raw_path.with_suffix(".mdx"))
        candidates.append(raw_path / "index.md")
        candidates.append(raw_path / "index.mdx")

    for candidate in candidates:
        if candidate in docs:
            rel_text = Path(os.path.relpath(candidate, base_dir.resolve())).as_posix()
            if not rel_text.startswith(".") and not rel_text.startswith(".."):
                rel_text = "./" + rel_text
            return rel_text + anchor

    return None


def fix_file(path: Path, docs: dict[Path, Path]) -> bool:
    original = path.read_text(encoding="utf-8")
    base_dir = path.parent
    changed = False

    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        prefix = match.group("prefix")
        target = match.group("target")
        suffix = match.group("suffix")

        if prefix.startswith("!["):
            return match.group(0)

        new_target = resolve_target(base_dir, target, docs)
        if not new_target or new_target == target:
            return match.group(0)

        changed = True
        return f"{prefix}{new_target}{suffix}"

    updated = LINK_RE.sub(replace, original)
    if changed and updated != original:
        path.write_text(updated, encoding="utf-8", newline="")
        return True
    return False


def main() -> int:
    args = parse_args()
    root = Path(args.source).resolve()
    docs = collect_docs(root)
    files = sorted(docs.values())
    if args.limit > 0:
        files = files[: args.limit]

    changed_count = 0
    for path in files:
        if fix_file(path, docs):
            changed_count += 1
            print(f"fixed {path.relative_to(root)}")

    print(f"Updated {changed_count} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

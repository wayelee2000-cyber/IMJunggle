#!/usr/bin/env python3
"""Polish English markdown/MDX docs in bulk using an OpenAI-compatible API.

This script is intended for already-translated docs that need a natural English
editing pass while preserving Markdown/MDX structure and technical meaning.

Examples:
  python polish_api_md.py --source api-md --output api-md-polished
  python polish_api_md.py --source api-md --in-place
  python polish_api_md.py --source api-md/guide --limit 10

Environment variables:
  OPENAI_API_KEY or TRANSLATION_API_KEY   Required API key
  OPENAI_BASE_URL                         Optional, defaults to https://api.openai.com/v1
  OPENAI_MODEL                            Optional, defaults to gpt-4.1-mini
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


SYSTEM_PROMPT = """You are a professional technical editor for developer documentation.

Your task is to revise English markdown/MDX docs so they read naturally and professionally.

Rules:
- Preserve the original markdown/MDX structure exactly.
- Do not remove sections, examples, tables, or code blocks.
- Do not translate code, inline code, URLs, paths, API names, HTML tags, JSX/MDX component names, or attributes.
- Keep headings, anchors, front matter, tables, lists, blockquotes, links, and images intact.
- Improve grammar, fluency, clarity, and wording.
- Preserve technical meaning.
- Keep terminology consistent across files.
- Return only the revised document, with no commentary.
"""


USER_PROMPT_TEMPLATE = """Revise the following English markdown/MDX document so it reads naturally and professionally, while preserving all markdown/MDX structure and technical meaning.

Document path: {path}

Return only the revised document.

```markdown
{content}
```"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Polish English markdown and MDX files.")
    parser.add_argument("--source", default="api-md", help="Source directory to scan.")
    parser.add_argument("--output", help="Output directory for polished files.")
    parser.add_argument("--in-place", action="store_true", help="Overwrite the source files.")
    parser.add_argument("--limit", type=int, default=0, help="Polish only the first N files.")
    parser.add_argument("--suffix", default="", help="Optional suffix to append before the file extension.")
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", "gpt-4.1-mini"))
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"))
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY") or os.environ.get("TRANSLATION_API_KEY"))
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--sleep", type=float, default=0.6, help="Delay between files in seconds.")
    return parser.parse_args()


def collect_files(source: Path, limit: int) -> list[Path]:
    files = sorted(
        path
        for path in source.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".mdx"}
    )
    if limit > 0:
        files = files[:limit]
    return files


def make_output_path(src: Path, source_root: Path, output_root: Path | None, suffix: str, in_place: bool) -> Path:
    if in_place:
        if suffix:
            return src.with_name(src.stem + suffix + src.suffix)
        return src

    if output_root is None:
        raise ValueError("output_root is required when not writing in place")

    relative = src.relative_to(source_root)
    dest = output_root / relative
    if suffix:
        dest = dest.with_name(dest.stem + suffix + dest.suffix)
    return dest


def call_api(base_url: str, api_key: str, model: str, temperature: float, path: str, content: str, retries: int) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "temperature": temperature,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(path=path, content=content)},
        ],
    }
    data = json.dumps(payload).encode("utf-8")

    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                raw = response.read().decode("utf-8")
            parsed = json.loads(raw)
            choices = parsed.get("choices") or []
            if not choices:
                raise RuntimeError(f"No choices returned: {raw[:500]}")
            message = choices[0].get("message") or {}
            revised = message.get("content")
            if not revised:
                raise RuntimeError(f"Empty content returned: {raw[:500]}")
            return strip_code_fence_wrapper(revised)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, RuntimeError) as exc:
            if attempt >= retries:
                raise RuntimeError(f"Polish failed after {retries} attempts: {exc}") from exc
            time.sleep(min(2 * attempt, 8))

    raise RuntimeError("Unexpected retry loop exit")


def strip_code_fence_wrapper(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```") and stripped.endswith("```"):
        lines = stripped.splitlines()
        if len(lines) >= 2:
            return "\n".join(lines[1:-1]).strip() + ("\n" if text.endswith("\n") else "")
    return text


def main() -> int:
    args = parse_args()

    if not args.api_key:
        print("Missing API key. Set OPENAI_API_KEY or TRANSLATION_API_KEY.", file=sys.stderr)
        return 2

    source_root = Path(args.source).resolve()
    if not source_root.exists():
        print(f"Source directory not found: {source_root}", file=sys.stderr)
        return 2

    if args.in_place and args.output:
        print("Use either --in-place or --output, not both.", file=sys.stderr)
        return 2

    if not args.in_place and not args.output:
        print("Provide --output or use --in-place.", file=sys.stderr)
        return 2

    output_root = Path(args.output).resolve() if args.output else None
    files = collect_files(source_root, args.limit)
    if not files:
        print("No markdown or MDX files found.", file=sys.stderr)
        return 1

    print(f"Found {len(files)} files under {source_root}")
    print(f"Model: {args.model}")
    if output_root:
        print(f"Output: {output_root}")
    elif args.in_place:
        print("Output: overwrite source files")

    polished_count = 0
    failed: list[tuple[Path, str]] = []

    for index, src in enumerate(files, start=1):
        relative = src.relative_to(source_root)
        dest = make_output_path(src, source_root, output_root, args.suffix, args.in_place)
        dest.parent.mkdir(parents=True, exist_ok=True)

        try:
            original = src.read_text(encoding="utf-8")
            revised = call_api(
                base_url=args.base_url,
                api_key=args.api_key,
                model=args.model,
                temperature=args.temperature,
                path=str(relative).replace("\\", "/"),
                content=original,
                retries=args.retries,
            )
            dest.write_text(revised, encoding="utf-8", newline="")
            polished_count += 1
            print(f"[{index}/{len(files)}] polished {relative}")
            time.sleep(args.sleep)
        except Exception as exc:  # noqa: BLE001
            failed.append((relative, str(exc)))
            print(f"[{index}/{len(files)}] failed {relative}: {exc}", file=sys.stderr)

    print()
    print(f"Polished: {polished_count}")
    print(f"Failed: {len(failed)}")
    if failed:
        print("Failures:")
        for path, error in failed:
            print(f"  - {path}: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

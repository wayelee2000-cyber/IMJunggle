#!/usr/bin/env python3
"""
Translate Chinese (Han) in api-md/*.md to English.
Prose outside ``` fences is translated in chunks; fence bodies are preserved
except comment lines (//, #, *, /**) which are translated line-wise.
Leading/trailing newlines of prose segments are preserved for valid markdown.
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parent.parent / "api-md"
HAN = re.compile(r"[\u4e00-\u9fff]")
MAX_CHUNK = 4200
DELAY_S = 0.2
MAX_RETRIES = 4

translator = GoogleTranslator(source="auto", target="en")
_cache: dict[str, str] = {}

LINE_COMMENT = re.compile(r"^(\s*//\s*)(.*)$")
HASH_COMMENT = re.compile(r"^(\s*#\s*)(.*)$")
STAR_COMMENT = re.compile(r"^(\s*\*\s*)(.*)$")
BLOCK_COMMENT_START = re.compile(r"^(\s*/\*\*?\s*)(.*)$")
# Heuristic: skip full-line translation for lines that look like code
CODEISH_LINE = re.compile(
    r"^\s*([{}\[\]]|console\.|import |export |from |function |const |let |var |"
    r"class |@|/\*|\*\s|if\s*\(|for\s*\(|while\s*\(|return\s|case\s|break;|"
    r"await |async |new |this\.|super\.|void |public |private |protected |"
    r"static |extends |implements |package |#include|@Override|"
    r"typedef |struct |enum |def |elif |pass|SELECT |INSERT )"
)


def has_han(s: str) -> bool:
    return HAN.search(s) is not None


def split_text_and_fences(content: str) -> tuple[list[str], list[str]]:
    """Split into alternating text parts and fence blocks; len(texts) == len(fences) + 1."""
    texts: list[str] = []
    fences: list[str] = []
    pos = 0
    while True:
        start = content.find("```", pos)
        if start == -1:
            texts.append(content[pos:])
            break
        texts.append(content[pos:start])
        end = content.find("```", start + 3)
        if end == -1:
            fences.append(content[start:])
            texts.append("")
            break
        fences.append(content[start : end + 3])
        pos = end + 3
    return texts, fences


def reassemble(texts: list[str], fences: list[str]) -> str:
    out: list[str] = []
    for i, t in enumerate(texts):
        out.append(t)
        if i < len(fences):
            out.append(fences[i])
    return "".join(out)


def preserve_edge_newlines(original: str, translated: str) -> str:
    """Keep leading/trailing \\n count from original so fence boundaries stay valid."""
    if not original:
        return translated
    lead_o = len(original) - len(original.lstrip("\n"))
    lead_t = len(translated) - len(translated.lstrip("\n"))
    if lead_o > lead_t:
        translated = "\n" * (lead_o - lead_t) + translated.lstrip("\n")

    trail_o = len(original) - len(original.rstrip("\n"))
    trail_t = len(translated) - len(translated.rstrip("\n"))
    if trail_o > trail_t:
        translated = translated.rstrip("\n") + "\n" * trail_o
    return translated


def _translate_once(chunk: str) -> str:
    last_err: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            return translator.translate(chunk)
        except Exception as e:
            last_err = e
            wait = 1.5 * (2**attempt)
            print(f"  retry {attempt + 1}/{MAX_RETRIES} after error: {e}", file=sys.stderr)
            time.sleep(wait)
    print(f"  failed: {last_err}", file=sys.stderr)
    return chunk


def translate_plain(text: str) -> str:
    text = text.replace("\r\n", "\n")
    if not has_han(text):
        return text
    key = text
    if key in _cache:
        return _cache[key]

    paras = text.split("\n\n")
    translated_parts: list[str] = []
    buf: list[str] = []
    size = 0

    def flush() -> None:
        nonlocal buf, size
        if not buf:
            return
        chunk = "\n\n".join(buf)
        out = _translate_once(chunk)
        translated_parts.append(out)
        time.sleep(DELAY_S)
        buf = []
        size = 0

    for para in paras:
        add = len(para) if not buf else len(para) + 2
        if size + add > MAX_CHUNK and buf:
            flush()
        buf.append(para)
        size += add
    flush()

    result = "\n\n".join(translated_parts)
    result = preserve_edge_newlines(text, result)
    _cache[key] = result
    return result


def translate_comment_line(line: str) -> str:
    for pat in (LINE_COMMENT, HASH_COMMENT, STAR_COMMENT, BLOCK_COMMENT_START):
        m = pat.match(line)
        if not m:
            continue
        prefix, suffix = m.group(1), m.group(2)
        if not has_han(suffix):
            return line
        tr = _translate_once(suffix)
        time.sleep(DELAY_S)
        return prefix + tr
    return line


def translate_fence_line(line: str) -> str:
    t = translate_comment_line(line)
    if t != line:
        return t
    if "//" in line:
        ix = line.rfind("//")
        tail = line[ix:]
        m = re.match(r"^(\s*//\s*)(.*)$", tail)
        if m and has_han(m.group(2)):
            tr = _translate_once(m.group(2))
            time.sleep(DELAY_S)
            return line[:ix] + m.group(1) + tr
    if has_han(line) and not CODEISH_LINE.match(line):
        tr = _translate_once(line)
        time.sleep(DELAY_S)
        return tr
    return line


def translate_fence_comments(fence: str) -> str:
    if not fence.startswith("```"):
        return fence
    first_nl = fence.find("\n")
    if first_nl == -1:
        return fence
    head = fence[: first_nl + 1]
    rest = fence[first_nl + 1 :]
    close_idx = rest.rfind("```")
    if close_idx == -1:
        return fence
    inner, tail = rest[:close_idx], rest[close_idx:]
    if not has_han(inner):
        return fence
    lines = inner.split("\n")
    new_inner = "\n".join(translate_fence_line(L) for L in lines)
    return head + new_inner + tail


def file_has_chinese(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    if has_han(text):
        return True
    _, fences = split_text_and_fences(text)
    return any(has_han(f) for f in fences)


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    texts, fences = split_text_and_fences(raw)
    new_texts: list[str] = []
    new_fences: list[str] = []
    changed = False
    for seg in texts:
        if not has_han(seg):
            new_texts.append(seg)
        else:
            new_seg = translate_plain(seg)
            if new_seg != seg:
                changed = True
            new_texts.append(new_seg)
    for f in fences:
        nf = translate_fence_comments(f)
        if nf != f:
            changed = True
        new_fences.append(nf)
    out = reassemble(new_texts, new_fences)
    if changed or out != raw:
        path.write_text(out, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> int:
    if not ROOT.is_dir():
        print(f"Missing api-md: {ROOT}", file=sys.stderr)
        return 1
    md_files = sorted(ROOT.rglob("*.md"))
    updated = 0
    for i, p in enumerate(md_files, 1):
        if not file_has_chinese(p):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except OSError as e:
            print(f"skip {p}: {e}", file=sys.stderr)
            continue
        rel = p.relative_to(ROOT)
        print(f"[{i}/{len(md_files)}] {rel}")
        if process_file(p):
            updated += 1
    print(f"Updated {updated} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Tracked-file secret pattern scan (Tool B for QA-SECURITY)."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)secret[_-]?key\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
]

SKIP_PARTS = {
    ".git",
    ".venv",
    "node_modules",
    "qa/.runtime",
    "qa/archives",
    "build",
    "dist",
    "__pycache__",
}


def tracked_files() -> list[Path]:
    try:
        out = subprocess.check_output(
            ["git", "ls-files"], cwd=ROOT, text=True
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    files = []
    for line in out.splitlines():
        path = Path(line)
        text = path.as_posix()
        if any(part in text for part in SKIP_PARTS):
            continue
        full = ROOT / path
        if full.is_file():
            files.append(full)
    return files


def main() -> int:
    hits = []
    for path in tracked_files():
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if b"\0" in data[:2048]:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in PATTERNS:
            if pattern.search(text):
                hits.append(f"{path.relative_to(ROOT)} :: {pattern.pattern}")
                break
    if hits:
        sys.stderr.write("secret-policy FAIL\n")
        for hit in hits:
            sys.stderr.write(hit + "\n")
        return 1
    print("secret-policy PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

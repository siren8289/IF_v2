#!/usr/bin/env python3
"""Semgrep probe with Bandit fallback if Semgrep CLI missing."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def main() -> int:
    targets = ["ai/src", "data/etl"]
    if shutil.which("semgrep"):
        cmd = ["semgrep", "--error", "--quiet", "--config", "p/python", *targets]
        completed = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        sys.stdout.write(completed.stdout)
        sys.stderr.write(completed.stderr)
        return completed.returncode
    # fallback
    print("NOTE: semgrep CLI missing; falling back to bandit HIGH")
    completed = subprocess.run(
        [sys.executable, "-m", "bandit", "-r", *targets, "-lll", "-q"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    sys.stdout.write(completed.stdout)
    sys.stderr.write(completed.stderr)
    # bandit returns non-zero on findings; treat as FAIL
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())

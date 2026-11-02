#!/usr/bin/env python3
"""CodeQL if CLI present; otherwise secret-policy fallback (exit notes RISK)."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def main() -> int:
    if shutil.which("codeql"):
        print("NOTE: codeql present but database analyze not configured in probe; use CI CodeQL job")
        # Do not fake PASS for unconfigured CodeQL
        return 3
    print("NOT_RUN/local: CodeQL CLI absent; running secret-policy fallback")
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/qa/security.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    sys.stdout.write(completed.stdout)
    sys.stderr.write(completed.stderr)
    # secret-policy PASS is not CodeQL; runner should attach RISK-V30-002
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())

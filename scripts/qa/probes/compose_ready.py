#!/usr/bin/env python3
"""Docker Compose config/readiness contract check (Tool A for infra)."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def main() -> int:
    if not shutil.which("docker"):
        print("ERROR: docker not found")
        return 1
    compose = ROOT / "compose.yaml"
    if not compose.exists():
        print("ERROR: compose.yaml missing")
        return 1
    env = {**os.environ, "IF_DB_PASSWORD": os.environ.get("IF_DB_PASSWORD") or "qa-probe-dummy"}
    plain = subprocess.run(
        ["docker", "compose", "-f", str(compose), "config"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env=env,
    )
    if plain.returncode != 0:
        print(plain.stderr or plain.stdout)
        return 1
    text = plain.stdout
    for name in ("postgres", "spring", "fastapi", "frontend"):
        if name not in text:
            print(f"FAIL missing service {name}")
            return 1
    if "healthcheck" not in text and "pg_isready" not in text:
        print("FAIL postgres healthcheck missing")
        return 1
    print("OK compose config; postgres healthcheck present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

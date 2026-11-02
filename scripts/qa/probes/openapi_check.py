#!/usr/bin/env python3
"""OpenAPI availability / optional Schemathesis smoke (Tool B for AI API)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import urllib.error
import urllib.request


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="http://127.0.0.1:8000")
    args = parser.parse_args()
    url = args.base.rstrip("/") + "/openapi.json"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"BLOCKED openapi unreachable: {exc}")
        return 2
    if not isinstance(payload, dict) or "paths" not in payload:
        print("FAIL openapi missing paths")
        return 1
    paths = payload.get("paths") or {}
    print(f"OK openapi paths={len(paths)}")
    if importlib.util.find_spec("schemathesis") is None:
        print("NOTE schemathesis not installed; OpenAPI document check only")
        return 0
    # Light schemathesis run if installed and server up
    import subprocess

    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "schemathesis",
            "run",
            url,
            "--max-examples",
            "5",
            "--checks",
            "not_a_server_error",
        ],
        capture_output=True,
        text=True,
    )
    sys.stdout.write(completed.stdout[-2000:])
    sys.stderr.write(completed.stderr[-2000:])
    return 0 if completed.returncode == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

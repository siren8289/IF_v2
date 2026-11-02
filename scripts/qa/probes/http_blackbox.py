#!/usr/bin/env python3
"""Independent HTTP blackbox probe (Tool B for API/infra)."""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--path", default="/")
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument(
        "--allow-blocked",
        action="store_true",
        help="Exit 2 (BLOCKED) when connection fails instead of FAIL",
    )
    args = parser.parse_args()
    url = args.base.rstrip("/") + "/" + args.path.lstrip("/")
    try:
        with urllib.request.urlopen(url, timeout=args.timeout) as resp:
            code = getattr(resp, "status", 200)
            body = resp.read(200)
    except urllib.error.HTTPError as exc:
        print(f"HTTP {exc.code} {url}")
        return 1 if exc.code >= 500 else 0
    except Exception as exc:  # noqa: BLE001
        print(f"BLOCKED connection to {url}: {exc}")
        return 2 if args.allow_blocked else 1
    print(f"OK {code} {url} bytes={len(body)}")
    return 0 if 200 <= int(code) < 400 else 1


if __name__ == "__main__":
    raise SystemExit(main())

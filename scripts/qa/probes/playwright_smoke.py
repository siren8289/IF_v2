#!/usr/bin/env python3
"""Playwright smoke if available; otherwise NOT_RUN (exit 3)."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def main() -> int:
    # Prefer npx playwright if project has @playwright/test later; for now detect binary/module
    try:
        import playwright  # noqa: F401
    except Exception:
        if not shutil.which("npx"):
            print("NOT_RUN: Playwright not installed")
            return 3
        # Try a no-op check without downloading browsers aggressively
        print("NOT_RUN: Playwright Python package missing; install before UI E2E PASS")
        return 3

    from playwright.sync_api import sync_playwright

    target = "http://127.0.0.1/"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(target, timeout=10000)
            title = page.title()
            browser.close()
    except Exception as exc:  # noqa: BLE001
        print(f"BLOCKED playwright navigation: {exc}")
        return 2
    print(f"OK playwright title={title!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

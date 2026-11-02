#!/usr/bin/env python3
"""Stop hook. Block only when product files changed after the last QA run.

Does not execute tests. Session-end stops (reason != end_turn) exit immediately.
A run that already wrote qa/reports/last-run.json after the edit is enough to stop,
even when that run found FAIL or RISK. The agent still must report those findings.
"""
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
SEOUL = ZoneInfo("Asia/Seoul")
PREFIXES = (
    "spring/src/",
    "ai/src/",
    "web-vite/src/",
    "data/etl/",
    "data/db/",
    ".github/workflows/",
)
EXACT = {
    "compose.yaml",
    "web-vite/nginx.conf",
    "spring/Dockerfile",
    "ai/Dockerfile",
    "web-vite/Dockerfile",
    "spring/build.gradle",
    "web-vite/package.json",
    "ai/requirements.txt",
    "ai/requirements-dev.txt",
}


def is_product(path):
    name = path.strip().strip('"')
    if " -> " in name:
        name = name.split(" -> ", 1)[1].strip()
    return name in EXACT or name.startswith(PREFIXES)


def changed_files():
    try:
        out = subprocess.check_output(
            ["git", "status", "--porcelain", "-uall"], cwd=ROOT, text=True, timeout=5
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return []
    found = []
    for line in out.splitlines():
        if len(line) < 4:
            continue
        found.append(line[3:])
    return [path for path in found if is_product(path)]


def main():
    raw = sys.stdin.read()
    try:
        event = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        event = {}
    if event.get("reason") != "end_turn":
        return 0
    pending = changed_files()
    if not pending:
        return 0
    pointer = ROOT / "qa" / "reports" / "last-run.json"
    if not pointer.exists():
        print(json.dumps({
            "decision": "block",
            "reason": "제품 코드가 바뀌었는데 qa/reports/last-run.json 이 없습니다. "
                      "python3 qa/run_qa.py --types unit,api,security 를 실행하고 "
                      "FAIL/RISK를 기록한 뒤 사용자에게 보고하세요. 제품 버그는 보고 전에 고치지 마세요.",
        }, ensure_ascii=False))
        return 0
    try:
        payload = json.loads(pointer.read_text(encoding="utf-8"))
        started = datetime.fromisoformat(payload["started_at"])
    except (OSError, json.JSONDecodeError, KeyError, ValueError):
        print(json.dumps({
            "decision": "block",
            "reason": "qa/reports/last-run.json 을 읽지 못했습니다. qa/run_qa.py 를 다시 실행하세요.",
        }, ensure_ascii=False))
        return 0
    if started.tzinfo is None:
        started = started.replace(tzinfo=SEOUL)
    stale = []
    for rel in pending:
        path = ROOT / rel.split(" -> ")[-1].strip().strip('"')
        if not path.exists():
            stale.append(rel)
            continue
        mtime = datetime.fromtimestamp(path.stat().st_mtime, SEOUL)
        if mtime > started:
            stale.append(rel)
    if stale:
        shown = ", ".join(stale[:8])
        print(json.dumps({
            "decision": "block",
            "reason": "제품 파일이 QA 실행 이후 다시 바뀌었습니다: "
                      f"{shown}. python3 qa/run_qa.py 로 다시 검사하고 결과를 보고하세요.",
        }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())

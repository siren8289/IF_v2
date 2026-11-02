#!/usr/bin/env python3
"""Antigravity Lifecycle Hook for QA·Security Automation Policy V2.5.

Reads hook context from stdin and outputs JSON to stdout adhering to the
Antigravity hooks.json contract.
"""
import argparse
import json
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", default="PreInvocation")
    args, _ = parser.parse_known_args()

    try:
        _ = sys.stdin.read()
    except Exception:
        pass

    repo_root = Path(__file__).resolve().parents[2]
    reports_dir = repo_root / "qa" / "reports"
    active_types = []
    if reports_dir.exists():
        active_types = sorted([p.name for p in reports_dir.iterdir() if p.is_dir()])

    summary_note = (
        "[QA·Security V2.5 상시 적용 활성] 모든 코드·설정 변경 작업 시 "
        "AGENTS.md 및 qa-policy.md의 10단계 절차(최소 2개 도구 교차 검증, "
        "qa/reports/{test-type}/{YYYY-MM-DD}/ 자동 기록, FAIL/RISK 선기록·선보고)를 준수하세요."
    )
    if active_types:
        summary_note += f" (현재 기록된 테스트 종류: {', '.join(active_types)})"

    if args.event == "SessionStart":
        out = {
            "injectSteps": [
                {
                    "systemMessage": {
                        "systemMessage": summary_note
                    }
                }
            ]
        }
    else:
        out = {
            "injectSteps": [
                {
                    "ephemeralMessage": summary_note
                }
            ],
            "terminationBehavior": ""
        }

    sys.stdout.write(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()

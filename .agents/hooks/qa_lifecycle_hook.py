#!/usr/bin/env python3
"""Lifecycle hook for QA·Security Automation Policy V3.0."""
import argparse
import json
import sys
from pathlib import Path

AREAS = (
    "01_unit_integration",
    "02_web_api",
    "03_security_quality",
    "04_infra_deploy",
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", default="PreInvocation")
    args, _ = parser.parse_known_args()
    try:
        _ = sys.stdin.read()
    except Exception:
        pass

    repo_root = Path(__file__).resolve().parents[2]
    results = repo_root / "qa" / "results"
    active = [a for a in AREAS if (results / a).exists() and any((results / a).glob("*/*"))]
    note = (
        "[QA·Security V3.0 always-on] Dual verification via qa/config/test_map.json; "
        "TCs in qa/input/testcases.tsv; results under qa/results/{area}/{section}/{date}/ "
        "(test_sheet.xlsx, pass.md, fail.md, risk.md, results.tsv). "
        "Related TCs after changes; full gate before PR/deploy. "
        "Do not claim automation without verified hooks/CI."
    )
    if active:
        note += f" Active areas: {', '.join(active)}."
    if args.event == "SessionStart":
        out = {"injectSteps": [{"systemMessage": {"systemMessage": note}}]}
    else:
        out = {"injectSteps": [{"ephemeralMessage": note}], "terminationBehavior": ""}
    sys.stdout.write(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()

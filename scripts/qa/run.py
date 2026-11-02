#!/usr/bin/env python3
"""Official QA gate runner V3.0 — reads test_map.json + testcases.tsv."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "qa"))

from record import (  # noqa: E402
    AREAS,
    QA_ROOT,
    append_record,
    blank_row,
    ensure_layout,
    git_meta,
    load_test_map,
    load_testcases,
    seoul_now,
    write_pointer,
)

EXIT_BLOCKED = 2
EXIT_NOT_RUN = 3


def expand(value: str, run_id: str) -> str:
    return value.replace("{run_id}", run_id)


def expand_cmd(cmd: list[str], run_id: str) -> list[str]:
    return [expand(part, run_id) for part in cmd]


def run_tool(tool: dict, run_id: str, timeout: int = 1800) -> tuple[str, str, Path | None, str]:
    name = tool.get("name", "UNKNOWN")
    cwd = ROOT / tool.get("cwd", ".")
    cmd = expand_cmd(list(tool.get("command", [])), run_id)
    runtime = ROOT / "qa" / ".runtime" / run_id
    runtime.mkdir(parents=True, exist_ok=True)
    safe_name = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in name)
    log_path = runtime / f"{safe_name}.log"
    if not cmd:
        log_path.write_text("missing command\n", encoding="utf-8")
        return name, "ERROR", log_path, "command missing"
    try:
        completed = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
            env={**os.environ, "PATH": f"{ROOT / '.venv' / 'bin'}:{os.environ.get('PATH', '')}"},
        )
    except FileNotFoundError as exc:
        log_path.write_text(f"missing binary: {exc}\n", encoding="utf-8")
        return name, "ERROR", log_path, str(exc)
    except subprocess.TimeoutExpired:
        log_path.write_text("timeout\n", encoding="utf-8")
        return name, "ERROR", log_path, "timeout"
    log_path.write_text(
        f"$ {' '.join(cmd)}\nexit={completed.returncode}\n{completed.stdout}\n{completed.stderr}\n",
        encoding="utf-8",
    )
    code = completed.returncode
    snippet = ((completed.stdout or "") + (completed.stderr or ""))[-500:]
    if code == 0:
        return name, "PASS", log_path, snippet or "exit 0"
    if code == EXIT_BLOCKED:
        return name, "BLOCKED", log_path, snippet or "blocked"
    if code == EXIT_NOT_RUN:
        return name, "NOT_RUN", log_path, snippet or "not run"
    return name, "FAIL", log_path, snippet or f"exit {code}"


def evidence_hash(path: Path | None) -> str:
    if path is None or not path.exists():
        return ""
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"{path.relative_to(ROOT)}#{digest[:16]}"


def open_blocking_risks(risks: list[dict]) -> list[dict]:
    out = []
    for risk in risks:
        if str(risk.get("status", "")).upper() not in {"OPEN", "ACCEPTED_OPEN"}:
            continue
        if str(risk.get("severity", "")).upper() in {"HIGH", "CRITICAL"}:
            out.append(risk)
    return out


def load_risks() -> list[dict]:
    raw = json.loads((ROOT / "qa" / "risks.json").read_text(encoding="utf-8"))
    return raw.get("risks", raw) if isinstance(raw, dict) else raw


def final_status(result_a: str, result_b: str) -> str:
    if result_a == "PASS" and result_b == "PASS":
        return "PASS"
    for state in ("ERROR", "FAIL", "BLOCKED", "NOT_RUN", "SKIPPED"):
        if state in (result_a, result_b):
            # FAIL wins over BLOCKED/NOT_RUN when mixed with FAIL
            if "FAIL" in (result_a, result_b):
                return "FAIL"
            if "ERROR" in (result_a, result_b):
                return "ERROR"
            return state
    return "FAIL"


def changed_files() -> list[str]:
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "HEAD"], cwd=ROOT, text=True
        )
        staged = subprocess.check_output(
            ["git", "diff", "--name-only", "--cached"], cwd=ROOT, text=True
        )
        untracked = subprocess.check_output(
            ["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT, text=True
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    files = []
    for block in (out, staged, untracked):
        files.extend([line.strip() for line in block.splitlines() if line.strip()])
    return sorted(set(files))


def match_tcs(files: list[str], test_map: dict) -> list[str]:
    import fnmatch

    selected = []
    globs = test_map.get("path_globs") or {}
    for tc_id, patterns in globs.items():
        for path in files:
            if any(fnmatch.fnmatch(path, pat) for pat in patterns):
                selected.append(tc_id)
                break
    # Always include runner contract when qa scripts change handled by globs
    return sorted(set(selected))


def record_tc(tc_id: str, meta: dict, tc_def: dict | None, run_id: str, commit: str, dirty: str) -> str:
    start = seoul_now()
    tool_a, result_a, log_a, actual_a = run_tool(meta["a"], run_id)
    tool_b, result_b, log_b, actual_b = run_tool(meta["b"], run_id)
    end = seoul_now()
    status = final_status(result_a, result_b)
    risk_id = ""
    if tc_id == "TC-SEC-SAST-001" and result_b in {"NOT_RUN", "PASS"} and "CodeQL" not in actual_b:
        risk_id = "RISK-V30-002"
    if tc_id == "TC-UNIT-SPRING-001":
        risk_id = risk_id or "RISK-V30-001"
    if tc_id == "TC-WEBAPI-UI-001" and result_a == "NOT_RUN":
        risk_id = "RISK-V30-003"

    row = blank_row(run_id, start, end, commit, dirty)
    row.update(
        TC_ID=tc_id,
        FEATURE_ID=meta.get("feature_id") or (tc_def or {}).get("FEATURE_ID", ""),
        area=meta["area"],
        section=meta["section"],
        scenario=(tc_def or {}).get("SCENARIO", meta.get("comparison", "")),
        tool_a=tool_a,
        command_a=" ".join(expand_cmd(list(meta["a"].get("command", [])), run_id)),
        result_a=result_a,
        expected_a="PASS",
        actual_a=actual_a[:300],
        tool_b=tool_b,
        command_b=" ".join(expand_cmd(list(meta["b"].get("command", [])), run_id)),
        result_b=result_b,
        expected_b="PASS",
        actual_b=actual_b[:300],
        status=status,
        code_file=(tc_def or {}).get("CODE_FILE", "UNKNOWN"),
        function=(tc_def or {}).get("FUNCTION", "UNKNOWN"),
        RISK_ID=risk_id,
        evidence=";".join(filter(None, [evidence_hash(log_a), evidence_hash(log_b)])),
    )
    detail = (
        f"시나리오: {row['scenario']}\n"
        f"비교: {meta.get('comparison', '')}\n"
        f"1차: {tool_a} 기대=PASS 실제={result_a}\n"
        f"2차: {tool_b} 기대=PASS 실제={result_b}\n"
        f"최종={status}. 미실행을 PASS로 처리하지 않음."
    )
    if risk_id:
        detail = "RISK " + risk_id + "\n" + detail
    append_record(QA_ROOT, row, detail)
    return status


def verify_automation() -> int:
    problems = []
    hooks = subprocess.run(
        ["git", "config", "--get", "core.hooksPath"], cwd=ROOT, capture_output=True, text=True
    )
    hooks_path = (hooks.stdout or "").strip()
    if hooks_path != ".githooks":
        problems.append(f"core.hooksPath={hooks_path!r} (expected .githooks)")
    pre = ROOT / ".githooks" / "pre-commit"
    if not pre.exists() or not os.access(pre, os.X_OK):
        problems.append("pre-commit missing or not executable")
    # dry-run related mapper
    wf = ROOT / ".github" / "workflows" / "githubactions.yml"
    if not wf.exists():
        problems.append("githubactions.yml missing")
    else:
        text = wf.read_text(encoding="utf-8")
        if "scripts/qa/run.py" not in text:
            problems.append("CI does not call scripts/qa/run.py")
        if "pull_request" not in text or "push" not in text:
            problems.append("CI triggers missing push/pull_request")
    # probe compose
    probe = subprocess.run(
        [sys.executable, str(ROOT / "scripts/qa/probes/compose_ready.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if probe.returncode != 0:
        problems.append(f"compose_ready probe failed: {(probe.stderr or probe.stdout)[:200]}")
    # invoke pre-commit script with --verify-only via env? instead run mapper
    test_map = load_test_map()
    if not test_map.get("tcs"):
        problems.append("test_map.json has no tcs")
    print("hooksPath:", hooks_path or "<unset>")
    print("pre-commit:", pre, "executable=", os.access(pre, os.X_OK))
    print("CI workflow:", wf.exists())
    print("compose_ready:", "PASS" if probe.returncode == 0 else "FAIL")
    if problems:
        print("VERIFY FAIL")
        for item in problems:
            print("-", item)
        return 1
    print("VERIFY PASS: local hooksPath + pre-commit + CI runner reference + compose probe")
    print("NOTE: GitHub branch protection/rulesets are remote and not verified here (RISK-003)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="QA V3.0 runner")
    parser.add_argument("--tc", action="append", default=[])
    parser.add_argument("--suite", action="append", default=[], help="legacy alias for --tc")
    parser.add_argument("--changed", action="store_true")
    parser.add_argument("--risks-only", action="store_true")
    parser.add_argument("--verify-automation", action="store_true")
    args = parser.parse_args()

    ensure_layout()
    if args.verify_automation:
        return verify_automation()

    test_map = load_test_map()
    tcs_meta = test_map.get("tcs") or {}
    tc_defs = {row["TC_ID"]: row for row in load_testcases() if row.get("TC_ID")}
    risks = load_risks()
    now = seoul_now()
    commit, dirty = git_meta()
    run_id = f"{now.strftime('%Y%m%dT%H%M%S')}-{uuid.uuid4().hex[:10]}"
    (ROOT / "qa" / ".runtime" / run_id).mkdir(parents=True, exist_ok=True)

    if args.risks_only:
        start = seoul_now()
        for risk in risks:
            row = blank_row(run_id, start, seoul_now(), commit, dirty)
            status = "PASS" if str(risk.get("status", "")).upper() == "RESOLVED" else "FAIL"
            row.update(
                TC_ID=risk.get("id", "RISK"),
                FEATURE_ID="RISK-LEDGER",
                area="03_security_quality",
                section="risk_ledger",
                scenario=str(risk.get("impact", "")),
                tool_a="risks.json",
                command_a="--risks-only",
                result_a=str(risk.get("status", "")),
                expected_a="RESOLVED",
                actual_a=str(risk.get("status", "")),
                tool_b="NOT_RUN",
                command_b="NOT_RUN",
                result_b="NOT_RUN",
                expected_b="NOT_RUN",
                actual_b="NOT_RUN",
                status=status,
                code_file=str(risk.get("file", "UNKNOWN")),
                function=str(risk.get("function", "UNKNOWN")),
                line=str(risk.get("line", "UNKNOWN")),
                RISK_ID=str(risk.get("id", "")),
            )
            append_record(
                QA_ROOT,
                row,
                f"RISK {risk.get('id')}\nseverity={risk.get('severity')}\n{risk.get('recommendation')}",
            )
        blocking = open_blocking_risks(risks)
        write_pointer(
            QA_ROOT,
            {"run_id": run_id, "mode": "risks-only", "blocking": bool(blocking), "finished_at": seoul_now().isoformat(timespec="seconds")},
        )
        return 1 if blocking else 0

    selected = list(args.tc) + list(args.suite)
    # legacy suite id mapping
    legacy = {
        "QA-DATA": "TC-UNIT-DATA-001",
        "QA-SPRING": "TC-UNIT-SPRING-001",
        "QA-WEB": "TC-UNIT-WEB-001",
        "QA-AI": "TC-WEBAPI-AI-001",
        "QA-SECURITY": "TC-SEC-SAST-001",
        "QA-CONFIG": "TC-INFRA-COMPOSE-001",
        "QA-REGRESSION": "TC-INFRA-RUNNER-001",
    }
    selected = [legacy.get(x, x) for x in selected]
    if args.changed:
        selected = match_tcs(changed_files(), test_map)
        if not selected:
            selected = ["TC-INFRA-RUNNER-001"]
    if not selected:
        selected = list(tcs_meta.keys())

    unknown = [x for x in selected if x not in tcs_meta]
    if unknown:
        raise SystemExit(f"unknown TC ids: {', '.join(unknown)}")

    started = time.time()
    statuses = []
    for tc_id in selected:
        print(f"RUN {tc_id} ...", flush=True)
        statuses.append(record_tc(tc_id, tcs_meta[tc_id], tc_defs.get(tc_id), run_id, commit, dirty))
        print(f"  -> {statuses[-1]}", flush=True)

    blocking = open_blocking_risks(risks)
    counts = {k: statuses.count(k) for k in ("PASS", "FAIL", "BLOCKED", "ERROR", "NOT_RUN", "SKIPPED")}
    counts["total"] = len(statuses)
    counts["RISK_OPEN_HIGH"] = len(blocking)
    tc_ok = all(s == "PASS" for s in statuses)
    # Full gate (PR/deploy): also require no open HIGH/CRITICAL risks.
    # --changed (local hook): fail only on TC outcomes so known ledger risks don't block every commit.
    ok = tc_ok if args.changed else (tc_ok and not blocking)
    write_pointer(
        QA_ROOT,
        {
            "run_id": run_id,
            "finished_at": seoul_now().isoformat(timespec="seconds"),
            "duration_sec": round(time.time() - started, 2),
            "tcs": selected,
            "statuses": statuses,
            "counts": counts,
            "blocking_risks": [r.get("id") for r in blocking],
            "blocking": not ok,
            "mode": "changed" if args.changed else "full",
            "git_commit": commit,
            "dirty": dirty,
            "areas": list(AREAS),
        },
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

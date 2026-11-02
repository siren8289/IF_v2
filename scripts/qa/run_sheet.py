#!/usr/bin/env python3
"""Import atomic QA sheet and execute/map all automatable IF-* TCs."""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import subprocess
import sys
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "qa"))

from record import (  # noqa: E402
    QA_ROOT,
    append_record,
    blank_row,
    ensure_layout,
    git_meta,
    seoul_now,
    write_pointer,
)

SHEET_TSV = QA_ROOT / "input" / "atomic_cases_from_sheet.tsv"
TESTCASES = QA_ROOT / "input" / "testcases.tsv"

AREA_MAP = {
    "프론트": ("02_web_api", "front_ui"),
    "Spring API": ("01_unit_integration", "spring_api"),
    "Spring 서비스": ("01_unit_integration", "spring_service"),
    "AI API": ("02_web_api", "ai_api"),
    "AI 계산": ("01_unit_integration", "ai_score"),
    "AI 설명": ("01_unit_integration", "ai_explain"),
    "AI 모델": ("01_unit_integration", "ai_model"),
    "인프라": ("04_infra_deploy", "deployment"),
    "보안": ("03_security_quality", "sast"),
    "비기능": ("04_infra_deploy", "nonfunctional"),
}


def one_line(s: str) -> str:
    return " ".join((s or "").split())


def import_testcases(rows: list[dict]) -> None:
    fields = [
        "TC_ID",
        "FEATURE_ID",
        "REQUIREMENT_ID",
        "AREA",
        "SECTION",
        "SCENARIO",
        "PRECONDITION",
        "INPUT",
        "STEPS",
        "EXPECTED_RESULT",
        "TOOL_A",
        "COMMAND_A",
        "TOOL_B",
        "COMMAND_B",
        "CODE_FILE",
        "FUNCTION",
        "RISK_LEVEL",
    ]
    with TESTCASES.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            area_kr = row.get("영역", "")
            area, section = AREA_MAP.get(area_kr, ("01_unit_integration", "unmapped"))
            prio = row.get("우선순위", "P1")
            writer.writerow(
                {
                    "TC_ID": row.get("TC ID", ""),
                    "FEATURE_ID": f"FEAT-{area_kr or 'GEN'}",
                    "REQUIREMENT_ID": row.get("TC ID", ""),
                    "AREA": area,
                    "SECTION": section,
                    "SCENARIO": one_line(row.get("단일 테스트 조건", "")),
                    "PRECONDITION": one_line(row.get("환경/파괴 주의", "")),
                    "INPUT": one_line(row.get("입력 데이터", "")),
                    "STEPS": one_line(row.get("실행 단계", "")),
                    "EXPECTED_RESULT": one_line(row.get("정확한 기대 결과", "")),
                    "TOOL_A": one_line(row.get("검증 도구", "")).split("+")[0].strip() or "UNKNOWN",
                    "COMMAND_A": "mapped-by-run_sheet",
                    "TOOL_B": "suite_cross_check",
                    "COMMAND_B": "mapped-by-run_sheet",
                    "CODE_FILE": one_line(row.get("소스 코드 / 근거", "")),
                    "FUNCTION": one_line(row.get("코드 분기/함수", "")),
                    "RISK_LEVEL": "HIGH" if prio == "P0" else "MEDIUM",
                }
            )


def run(cmd: list[str], cwd: Path, log: Path, timeout: int = 1800) -> int:
    log.parent.mkdir(parents=True, exist_ok=True)
    try:
        completed = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
            env={**os.environ, "PATH": f"{ROOT / '.venv' / 'bin'}:{os.environ.get('PATH', '')}"},
        )
    except subprocess.TimeoutExpired:
        log.write_text("timeout\n", encoding="utf-8")
        return 1
    log.write_text(
        f"$ {' '.join(cmd)}\nexit={completed.returncode}\n{completed.stdout}\n{completed.stderr}\n",
        encoding="utf-8",
    )
    return completed.returncode


def parse_junit(paths: list[Path]) -> dict[str, str]:
    results: dict[str, str] = {}
    for path in paths:
        if not path.exists():
            continue
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError:
            continue
        for case in root.findall(".//testcase"):
            name = case.attrib.get("name", "")
            classname = case.attrib.get("classname", "")
            text = f"{classname} {name}"
            ids = set(re.findall(r"IF-\d{4}", text))
            # also IF_0098 style
            for m in re.findall(r"IF_(\d{4})", text):
                ids.add(f"IF-{m}")
            status = "PASS"
            if case.find("failure") is not None or case.find("error") is not None:
                status = "FAIL"
            elif case.find("skipped") is not None:
                status = "SKIPPED"
            for tc in ids:
                # FAIL wins
                if results.get(tc) == "FAIL":
                    continue
                results[tc] = status
    return results


def evidence(path: Path) -> str:
    if not path.exists():
        return ""
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"{path.relative_to(ROOT)}#{digest[:16]}"


def main() -> int:
    ensure_layout()
    if not SHEET_TSV.exists():
        raise SystemExit(f"missing {SHEET_TSV}; extract sheet first")
    with SHEET_TSV.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    import_testcases(rows)
    print(f"imported {len(rows)} TCs -> {TESTCASES}")

    now = seoul_now()
    commit, dirty = git_meta()
    run_id = f"{now.strftime('%Y%m%dT%H%M%S')}-{uuid.uuid4().hex[:10]}"
    runtime = QA_ROOT / ".runtime" / run_id
    runtime.mkdir(parents=True, exist_ok=True)

    # Tool-group executions (dual where practical)
    spring_xml_glob = list((ROOT / "spring/build/test-results/test").glob("TEST-*.xml"))
    # rerun spring
    run(["./gradlew", "test", "--rerun-tasks", "--console=plain"], ROOT / "spring", runtime / "spring_junit.log")
    spring_xml = list((ROOT / "spring/build/test-results/test").glob("TEST-*.xml"))
    for src in spring_xml:
        dest = runtime / f"spring-{src.name}"
        dest.write_bytes(src.read_bytes())

    run(
        ["python3", "-m", "pytest", "tests", "-q", f"--junitxml={runtime / 'ai.xml'}"],
        ROOT / "ai",
        runtime / "ai_pytest.log",
    )
    run(
        ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"],
        ROOT / "ai",
        runtime / "ai_ruff.log",
    )
    run(
        [
            "npm",
            "test",
            "--",
            "--reporter=default",
            "--reporter=junit",
            f"--outputFile={runtime / 'web.xml'}",
        ],
        ROOT / "web-vite",
        runtime / "web_vitest.log",
    )
    run(["npm", "run", "typecheck"], ROOT / "web-vite", runtime / "web_tsc.log")
    run(
        ["python3", "-m", "pytest", "data/tests", "-q", f"--junitxml={runtime / 'data.xml'}"],
        ROOT,
        runtime / "data_pytest.log",
    )
    run(
        ["python3", "-m", "unittest", "discover", "-s", "data/tests", "-v"],
        ROOT,
        runtime / "data_unittest.log",
    )
    run(["python3", "scripts/qa/probes/compose_ready.py"], ROOT, runtime / "compose.log")
    run(["python3", "scripts/qa/probes/semgrep_run.py"], ROOT, runtime / "semgrep.log")
    run(["python3", "scripts/qa/security.py"], ROOT, runtime / "secret.log")

    mapped = {}
    mapped.update(parse_junit([runtime / "ai.xml"]))
    mapped.update(parse_junit(list(runtime.glob("spring-TEST-*.xml"))))
    mapped.update(parse_junit([runtime / "web.xml"]))
    mapped.update(parse_junit([runtime / "data.xml"]))

    # suite-level cross checks
    ruff_ok = (runtime / "ai_ruff.log").read_text(encoding="utf-8", errors="ignore")
    ruff_pass = "exit=0" in ruff_ok.splitlines()[1:2] or ruff_ok.find("\nexit=0\n") >= 0
    # parse exit from log first lines style: exit=N
    def log_exit(path: Path) -> int:
        text = path.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"^exit=(-?\d+)", text, re.M)
        return int(m.group(1)) if m else 1

    cross = {
        "ai": "PASS" if log_exit(runtime / "ai_ruff.log") == 0 else "FAIL",
        "web": "PASS" if log_exit(runtime / "web_tsc.log") == 0 else "FAIL",
        "data": "PASS" if log_exit(runtime / "data_unittest.log") == 0 else "FAIL",
        "spring": "PASS" if log_exit(runtime / "spring_junit.log") == 0 else "FAIL",
        "infra": "PASS" if log_exit(runtime / "compose.log") == 0 else "FAIL",
        "sec": "PASS"
        if log_exit(runtime / "semgrep.log") == 0 and log_exit(runtime / "secret.log") == 0
        else "FAIL",
    }

    def cross_for(area_kr: str) -> tuple[str, str, str]:
        if area_kr.startswith("AI"):
            return "Ruff", "ruff check", cross["ai"]
        if area_kr == "프론트":
            return "TypeScript", "npm run typecheck", cross["web"]
        if "Spring" in area_kr:
            return "GradleJUnitSuite", "gradlew test", cross["spring"]
        if area_kr == "인프라" or area_kr == "비기능":
            return "compose_ready", "compose_ready.py", cross["infra"]
        if area_kr == "보안":
            return "Secret-policy", "security.py", cross["sec"]
        return "suite_cross_check", "area-suite", "NOT_RUN"

    counts = {"PASS": 0, "FAIL": 0, "NOT_RUN": 0, "BLOCKED": 0, "ERROR": 0, "SKIPPED": 0}
    start = seoul_now()
    for row in rows:
        tc_id = row.get("TC ID", "")
        area_kr = row.get("영역", "")
        area, section = AREA_MAP.get(area_kr, ("01_unit_integration", "unmapped"))
        tool_b, cmd_b, result_b = cross_for(area_kr)
        if tc_id in mapped:
            result_a = mapped[tc_id]
            tool_a = "automated_junit_or_pytest"
            cmd_a = "parsed from suite XML"
            if result_a == "PASS" and result_b == "PASS":
                status = "PASS"
            elif result_a == "SKIPPED":
                status = "SKIPPED"
            elif result_a == "FAIL" or result_b == "FAIL":
                status = "FAIL"
            else:
                status = "FAIL"
            actual_a = f"mapped suite result={result_a}"
        else:
            result_a = "NOT_RUN"
            tool_a = one_line(row.get("검증 도구", "")) or "UNMAPPED"
            cmd_a = "no automated test id mapping"
            status = "NOT_RUN"
            actual_a = "시트 TC에 연결된 자동 테스트 식별자 없음"
            result_b = "NOT_RUN"
            tool_b, cmd_b = "NOT_RUN", "NOT_RUN"

        end = seoul_now()
        rec = blank_row(run_id, start, end, commit, dirty)
        rec.update(
            TC_ID=tc_id,
            FEATURE_ID=f"FEAT-{area_kr}",
            area=area,
            section=section,
            scenario=one_line(row.get("단일 테스트 조건", "")),
            tool_a=tool_a,
            command_a=cmd_a,
            result_a=result_a,
            expected_a="PASS",
            actual_a=actual_a,
            tool_b=tool_b,
            command_b=cmd_b,
            result_b=result_b,
            expected_b="PASS",
            actual_b=f"cross={result_b}",
            status=status,
            code_file=one_line(row.get("소스 코드 / 근거", "")) or "UNKNOWN",
            function=one_line(row.get("코드 분기/함수", "")) or "UNKNOWN",
            evidence=";".join(
                filter(
                    None,
                    [
                        evidence(runtime / "ai.xml"),
                        evidence(runtime / "web.xml"),
                        evidence(runtime / "data.xml"),
                    ],
                )
            ),
        )
        detail = (
            f"시트 시나리오: {rec['scenario']}\n"
            f"기대: {one_line(row.get('정확한 기대 결과', ''))}\n"
            f"1차={result_a} 2차={result_b} 최종={status}\n"
            f"입력: {one_line(row.get('입력 데이터', ''))}"
        )
        append_record(QA_ROOT, rec, detail)
        counts[status] = counts.get(status, 0) + 1

    # also run gate TCs
    gate = subprocess.run(
        [sys.executable, str(ROOT / "scripts/qa/run.py")],
        cwd=ROOT,
        env={**os.environ, "PATH": f"{ROOT / '.venv' / 'bin'}:{os.environ.get('PATH', '')}"},
    )

    payload = {
        "run_id": run_id,
        "mode": "sheet-all",
        "sheet_cases": len(rows),
        "mapped_automated": len(mapped),
        "counts": counts,
        "gate_exit": gate.returncode,
        "finished_at": seoul_now().isoformat(timespec="seconds"),
        "git_commit": commit,
        "dirty": dirty,
    }
    write_pointer(QA_ROOT, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if counts.get("FAIL", 0) == 0 and gate.returncode == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

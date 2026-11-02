#!/usr/bin/env python3
"""IF_v2 QA gate. Runs only the requested test types and appends reports.

Two tools must agree before a case is PASS. A missing tool, a crash, or a
skipped check stays ERROR, BLOCKED, or NOT_RUN and is never stored as PASS.
Live HTTP checks are omitted in --mode ci so an unreachable laptop stack
does not become a green result.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx

from record import (
    ROOT, append_record, blank_row, git_meta, next_run_id, seoul_now, write_pointer,
)

ALL_TYPES = ["unit", "api", "integration", "e2e", "security", "performance", "regression"]
CI_TYPES = ["unit", "security"]
SPRING = "http://127.0.0.1:8080"
WEB = "http://127.0.0.1"
PY = sys.executable
SCAN_ROOTS = ["spring/src", "ai/src", "data/etl", "web-vite/src"]
SQL_RE = re.compile(
    r"(?i)(select|insert|update|delete|drop\s+table).{0,80}\+|f[\"'].{0,60}(select|insert|update|delete)\s"
)


def one_line(text, limit=400):
    return " ".join(str(text).split())[:limit]


def run_cmd(command, cwd, timeout):
    try:
        result = subprocess.run(
            command, cwd=cwd, text=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, timeout=timeout,
        )
        return result.returncode, result.stdout or ""
    except subprocess.TimeoutExpired as exc:
        out = exc.stdout or ""
        if isinstance(out, bytes):
            out = out.decode("utf-8", "replace")
        return 124, f"TIMEOUT {timeout}s\n{out}"
    except OSError as exc:
        return 127, f"{type(exc).__name__}: {exc}"


def find_line(rel, needle):
    path = ROOT / rel
    if not path.is_file():
        return "UNKNOWN"
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return "UNKNOWN"
    for number, line in enumerate(lines, 1):
        if needle in line:
            return str(number)
    return "UNKNOWN"


def accepted_risks():
    path = ROOT / "qa" / "risk-decisions.tsv"
    accepted = set()
    if not path.exists():
        return accepted
    for line in path.read_text(encoding="utf-8-sig").splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) >= 2 and parts[1].strip().upper() in {"ACCEPTED", "MITIGATED", "CLOSED"}:
            accepted.add(parts[0].strip())
    return accepted


def psql(sql):
    code, out = run_cmd(
        ["docker", "exec", "-i", "if-app-stack-postgres-1", "psql",
         "-U", "if_user", "-d", "if_spring", "-v", "ON_ERROR_STOP=1", "-tAc", sql],
        ROOT, 30,
    )
    if code != 0:
        raise RuntimeError(one_line(out, 300))
    return out.strip()


def counts():
    found = {}
    for table in ("assessment", "applicant", "health_snapshot", "ai_risk_result"):
        found[table] = int(psql(f"SELECT count(*) FROM {table}"))
    found["id2"] = int(psql("SELECT count(*) FROM assessment WHERE assessment_id = 2"))
    return found


def curl_call(method, url, body=None, content_type="application/json"):
    command = ["curl", "-sS", "-m", "40", "-w", "\n%{http_code}", "-X", method, url]
    if body is not None:
        command += ["-H", f"Content-Type: {content_type}", "--data-binary", body]
    code, out = run_cmd(command, ROOT, 50)
    if code != 0:
        lowered = out.lower()
        kind = "BLOCKED" if "couldn't connect" in lowered or "failed to connect" in lowered or "connection refused" in lowered else "ERROR"
        return None, out, kind, " ".join(command)
    text, _, status = out.rpartition("\n")
    try:
        return int(status.strip()), text, None, " ".join(command)
    except ValueError:
        return None, out, "ERROR", " ".join(command)


def httpx_call(method, url, body=None, content_type="application/json"):
    headers = {"Content-Type": content_type} if body is not None else {}
    command = f"httpx {method} {url} content-type={content_type if body is not None else '-'}"
    try:
        with httpx.Client(timeout=40.0) as client:
            response = client.request(method, url, content=None if body is None else body.encode("utf-8"), headers=headers)
        return response.status_code, response.text, None, command
    except httpx.ConnectError as exc:
        return None, str(exc), "BLOCKED", command
    except httpx.HTTPError as exc:
        return None, str(exc), "ERROR", command


def response_id(text):
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    if isinstance(data, dict) and isinstance(data.get("id"), int):
        return data["id"]
    return None


def lookup_row(assessment_id):
    if not isinstance(assessment_id, int) or assessment_id == 2:
        return None
    return psql(
        "SELECT a.applicant_id || '|' || a.health_id || '|' || COALESCE(a.status,'') || '|' || "
        "p.display_name || '|' || p.age || '|' || h.physical_level || '|' || "
        "h.chronic_disease_flag::text || '|' || h.work_hour_limit "
        "FROM assessment a "
        "JOIN applicant p ON p.applicant_id = a.applicant_id "
        "JOIN health_snapshot h ON h.health_id = a.health_id "
        f"WHERE a.assessment_id = {assessment_id}"
    )


def cleanup(created):
    notes = []
    for item in created:
        assessment_id = item["assessment_id"]
        if assessment_id == 2:
            notes.append("refused to delete assessment 2")
            continue
        status, body, problem, _command = curl_call("DELETE", f"{SPRING}/api/assessments/{assessment_id}")
        notes.append(f"DELETE {assessment_id} -> {problem or status} {one_line(body, 80)}")
        applicant_id = item.get("applicant_id")
        health_id = item.get("health_id")
        if isinstance(health_id, int):
            psql(
                "DELETE FROM health_snapshot WHERE health_id = "
                f"{health_id} AND NOT EXISTS (SELECT 1 FROM assessment WHERE health_id = {health_id})"
            )
        if isinstance(applicant_id, int):
            psql(
                "DELETE FROM applicant WHERE applicant_id = "
                f"{applicant_id} AND NOT EXISTS (SELECT 1 FROM assessment WHERE applicant_id = {applicant_id})"
            )
    return "; ".join(notes)


def judge_pair(status_a, problem_a, status_b, problem_b, expected):
    def one(status, problem):
        if problem:
            return problem
        return "PASS" if status in expected else "FAIL"
    result_a = one(status_a, problem_a)
    result_b = one(status_b, problem_b)
    if result_a == result_b == "PASS":
        final = "PASS"
    elif "FAIL" in (result_a, result_b):
        final = "FAIL"
    elif "ERROR" in (result_a, result_b):
        final = "ERROR"
    elif "BLOCKED" in (result_a, result_b):
        final = "BLOCKED"
    else:
        final = "ERROR"
    return result_a, result_b, final


def base_payload():
    return {
        "applicantName": "QA게이트",
        "age": 70,
        "physicalLevel": 3,
        "chronicDisease": False,
        "workHourLimit": 8,
        "jobId": 1,
    }


def remember(created, status, body):
    if status != 201:
        return
    assessment_id = response_id(body)
    if not isinstance(assessment_id, int) or assessment_id == 2:
        return
    try:
        raw = lookup_row(assessment_id)
    except RuntimeError as exc:
        created.append({"assessment_id": assessment_id, "lookup_error": str(exc)})
        return
    if not raw:
        created.append({"assessment_id": assessment_id})
        return
    applicant_id, health_id, *_rest = raw.split("|")
    created.append({
        "assessment_id": assessment_id,
        "applicant_id": int(applicant_id),
        "health_id": int(health_id),
        "row": raw,
    })


class Gate:
    def __init__(self, run_id, now, commit, dirty, reverify):
        self.run_id = run_id
        self.now = now
        self.commit = commit
        self.dirty = dirty
        self.reverify = reverify
        self.rows = []
        self.risks = []
        self.created = []
        self.baseline = None

    def add(self, tc_id, feature, test_type, status, tool_a, command_a, result_a,
            tool_b, command_b, result_b, files, function, line, evidence, detail,
            issue="", risk=""):
        row = blank_row(self.run_id, self.now, self.commit, self.dirty)
        prefix = "재검증 " if self.reverify else ""
        row.update(
            TC_ID=tc_id, feature=prefix + feature, test_type=test_type, status=status,
            tool_a=tool_a, command_a=one_line(command_a, 240), result_a=result_a,
            tool_b=tool_b, command_b=one_line(command_b, 240), result_b=result_b,
            files=files, function=function or "UNKNOWN", line=line or "UNKNOWN",
            ISSUE_ID=issue, RISK_ID=risk, evidence=one_line(evidence, 500),
        )
        self.rows.append((row, detail))
        print(f"{tc_id} {status} {result_a}/{result_b}", flush=True)

    def risk(self, risk_id, severity, likelihood, impact, recommendation, status,
             files, function, line, detail):
        self.risks.append({
            "id": risk_id, "severity": severity, "likelihood": likelihood,
            "status": status, "file": files, "line": line,
        })
        narrative = (
            f"RISK {risk_id}\n심각도: {severity}\n발생 가능성: {likelihood}\n영향: {impact}\n"
            f"권장 조치: {recommendation}\n처리 상태: {status}\n"
            f"파일: {files}\n함수: {function}\n줄: {line}\n{detail}"
        )
        for index, (row, previous) in enumerate(self.rows):
            if row["RISK_ID"] == risk_id:
                self.rows[index] = (row, previous + "\n\n" + narrative)
                return
        self.add(
            risk_id, "위험 기록", "security", "PASS",
            "qa-runner", "inspection", "PASS", "qa-runner", "inspection", "PASS",
            files, function, line, f"{severity} {status}", narrative, risk=risk_id,
        )


def finish_process(label, code, out, empty_markers=("no tests ran", "NO-SOURCE", "Ran 0 tests", "No test files found")):
    text = out or ""
    if code == 127:
        return "ERROR", text
    if code == 124:
        return "ERROR", text
    if any(marker in text for marker in empty_markers):
        return "NOT_RUN", text
    return ("PASS" if code == 0 else "FAIL"), text


def run_unit(gate):
    code, out = run_cmd(
        ["./gradlew", "test", "--rerun-tasks", "--console=plain"],
        ROOT / "spring", 540,
    )
    result_a, _text = finish_process("gradle", code, out)
    xml_dir = ROOT / "spring" / "build" / "test-results" / "test"
    xml_files = sorted(xml_dir.glob("TEST-*.xml")) if xml_dir.exists() else []
    failures = errors = tests = 0
    names = []
    for path in xml_files:
        try:
            suite = ET.parse(path).getroot()
        except ET.ParseError:
            result_b = "ERROR"
            break
        failures += int(suite.attrib.get("failures", "0"))
        errors += int(suite.attrib.get("errors", "0"))
        tests += int(suite.attrib.get("tests", "0"))
        names.append(path.name)
    else:
        if not xml_files or tests == 0:
            result_b = "ERROR" if result_a != "PASS" else "NOT_RUN"
        elif failures or errors:
            result_b = "FAIL"
        else:
            result_b = "PASS"
    if result_a == result_b == "PASS":
        final = "PASS"
    elif "FAIL" in (result_a, result_b):
        final = "FAIL"
    elif "NOT_RUN" in (result_a, result_b):
        final = "ERROR"
    else:
        final = "ERROR" if "ERROR" in (result_a, result_b) else "FAIL"
    line = find_line(
        "spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java",
        "void 나이가_범위를_벗어나면_400",
    )
    gate.add(
        "QA-UNIT-SPRING", "Spring 평가 컨트롤러/서비스 단위 테스트", "unit", final,
        "Gradle JUnit", "./gradlew test --rerun-tasks", result_a,
        "JUnit XML", "spring/build/test-results/test/TEST-*.xml", result_b,
        "spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java",
        "나이가_범위를_벗어나면_400", line,
        f"gradle={result_a} xml tests={tests} failures={failures} errors={errors} files={','.join(names)}",
        "검증 목적: 기존 AssessmentControllerTest, AssessmentServiceTest가 통과하는지 확인한다.\n"
        "도구 A는 Gradle 테스트 프로세스다. 도구 B는 그 실행이 남긴 JUnit XML을 따로 읽는다. "
        "XML은 두 번째 실행이 아니라 같은 실행의 독립 판독이다.\n"
        f"기대: 두 판독 모두 실패 0, 테스트 1건 이상. 실제: A={result_a} B={result_b} "
        f"tests={tests} failures={failures} errors={errors}.\n"
        "범위: H2와 Mock AI. 운영 PostgreSQL과 살아있는 FastAPI는 포함하지 않는다.\n"
        f"로그 끝:\n{out[-1500:]}",
    )

    pure = r"""
import importlib.util
from pathlib import Path
path = Path("ai/src/risk_score.py").resolve()
spec = importlib.util.spec_from_file_location("risk_score_gate", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
assert mod.grade_of(40) == "LOW"
assert mod.grade_of(41) == "MID"
assert mod.grade_of(60) == "MID"
assert mod.grade_of(61) == "HIGH"
low = mod.calculate_score(50, 1, False, 8, {}, {})
assert low["risk_score"] == 0 and low["risk_grade"] == "LOW"
worst = {"DRIVING": 1, "NIGHT_SHIFT": 1, "WALKING": 1, "CLEANING_TASK": 1, "CARE_TASK": 1, "FACILITY_MAINTENANCE": 1}
high = mod.calculate_score(95, 5, True, 1, worst, worst)
assert high["risk_score"] == 100 and high["risk_grade"] == "HIGH"
print("ok")
"""
    code_a, out_a = run_cmd([PY, "-c", pure], ROOT, 30)
    with tempfile.TemporaryDirectory() as tmp:
        test_path = Path(tmp) / "test_grade_gate.py"
        test_path.write_text(
            "import importlib.util\nimport unittest\nfrom pathlib import Path\n\n"
            f"PATH = Path(r'{ROOT / 'ai' / 'src' / 'risk_score.py'}')\n\n"
            "def load():\n"
            "    spec = importlib.util.spec_from_file_location('risk_score_gate_b', PATH)\n"
            "    mod = importlib.util.module_from_spec(spec)\n"
            "    spec.loader.exec_module(mod)\n"
            "    return mod\n\n"
            "class GradeTests(unittest.TestCase):\n"
            "    def test_boundaries(self):\n"
            "        mod = load()\n"
            "        self.assertEqual(mod.grade_of(40), 'LOW')\n"
            "        self.assertEqual(mod.grade_of(41), 'MID')\n"
            "        self.assertEqual(mod.grade_of(60), 'MID')\n"
            "        self.assertEqual(mod.grade_of(61), 'HIGH')\n\n"
            "if __name__ == '__main__':\n"
            "    unittest.main()\n",
            encoding="utf-8",
        )
        code_b, out_b = run_cmd([PY, str(test_path)], ROOT, 30)
    result_a = "PASS" if code_a == 0 and "ok" in out_a else "FAIL" if code_a == 0 else "ERROR"
    result_b = "PASS" if code_b == 0 else ("ERROR" if code_b in {124, 127} else "FAIL")
    final = "PASS" if result_a == result_b == "PASS" else ("FAIL" if "FAIL" in (result_a, result_b) else "ERROR")
    gate.add(
        "QA-UNIT-AI-SCORE", "위험 점수 등급 경계", "unit", final,
        "python", "import ai/src/risk_score.py grade_of/calculate_score", result_a,
        "unittest", "temp test_grade_gate.py", result_b,
        "ai/src/risk_score.py", "grade_of", find_line("ai/src/risk_score.py", "def grade_of"),
        f"python={one_line(out_a, 180)} unittest={one_line(out_b, 180)}",
        "검증 목적: 40/41, 60/61 경계와 0점, 100점 규칙을 두 실행기로 확인한다.\n"
        "이 검사는 FastAPI, torch, pytest를 불러오지 않는다. 공식 파일 ai/tests/test_risk_score.py 는 다음 TC다.\n"
        f"기대: LOW/MID/HIGH와 0/100. 실제 A={result_a} B={result_b}.\n"
        f"A출력: {out_a[-800:]}\nB출력: {out_b[-800:]}",
    )

    code, out = run_cmd([PY, "-m", "pytest", "tests/test_risk_score.py", "-q"], ROOT / "ai", 180)
    missing = "No module named" in out or "ModuleNotFoundError" in out
    if missing or code == 127:
        result_a = "ERROR"
    elif "no tests ran" in out:
        result_a = "NOT_RUN"
    else:
        result_a = "PASS" if code == 0 else "FAIL"
    code_b, out_b = run_cmd(
        [PY, "-c",
         "from pathlib import Path\n"
         "text = Path('ai/tests/test_risk_score.py').read_text(encoding='utf-8')\n"
         "needed = ['def test_grade_boundaries', 'def test_young_healthy_person_gets_zero_without_task_points',\n"
         "          'def test_worst_inputs_reach_100', 'def test_analyze_api_rejects_bad_age']\n"
         "missing = [name for name in needed if name not in text]\n"
         "assert not missing, missing\n"
         "print('source-ok')\n"],
        ROOT, 20,
    )
    result_b = "PASS" if code_b == 0 and "source-ok" in out_b else "ERROR"
    if result_a == "NOT_RUN":
        final = "ERROR"
    elif result_a == "FAIL" or result_b == "FAIL":
        final = "FAIL"
    elif result_a == result_b == "PASS":
        final = "PASS"
    else:
        final = "ERROR"
    gate.add(
        "QA-UNIT-AI-PYTEST", "공식 FastAPI 점수 테스트 파일", "unit", final,
        "pytest", "python3 -m pytest tests/test_risk_score.py -q", result_a,
        "python", "assert test function names exist in ai/tests/test_risk_score.py", result_b,
        "ai/tests/test_risk_score.py", "test_grade_boundaries",
        find_line("ai/tests/test_risk_score.py", "def test_grade_boundaries"),
        one_line(out, 300),
        "검증 목적: ai/tests/test_risk_score.py 를 수집해 실행한다.\n"
        "이 파일은 src.main 을 불러 torch, scikit-learn, fastapi가 필요하다. "
        "의존성이 없으면 ERROR이며 PASS로 올리지 않는다. test_rag.py 는 이번 명령에 없다.\n"
        f"기대: pytest 종료 0. 실제 A={result_a} B={result_b} code={code}.\n출력:\n{out[-1500:]}",
    )

    code_a, out_a = run_cmd([PY, "-m", "unittest", "discover", "-s", "data/tests", "-v"], ROOT, 60)
    code_b, out_b = run_cmd([PY, "-c", (
        "from data.etl.transform import parse_data\n"
        "xml=b'<response><body><items><item><jobId>100</jobId><title>Test Job</title></item></items></body></response>'\n"
        "rows=parse_data(xml, {'format':'xml','item_path':'response.body.items.item'})\n"
        "assert len(rows)==1 and rows[0]['jobId']=='100'\nprint('ok')\n"
    )], ROOT, 30)
    result_a = "PASS" if code_a == 0 and "Ran 0 tests" not in out_a else ("NOT_RUN" if "Ran 0 tests" in out_a else "FAIL" if code_a not in {124, 127} else "ERROR")
    result_b = "PASS" if code_b == 0 and "ok" in out_b else "ERROR"
    if "FAIL" in (result_a, result_b):
        final = "FAIL"
    elif result_a == result_b == "PASS":
        final = "PASS"
    else:
        final = "ERROR"
    gate.add(
        "QA-UNIT-DATA", "ETL 변환 단위 테스트", "unit", final,
        "unittest", "python3 -m unittest discover -s data/tests -v", result_a,
        "python", "parse_data XML fixture", result_b,
        "data/tests/test_transform.py", "test_parse_xml",
        find_line("data/tests/test_transform.py", "def test_parse_xml"),
        f"unittest={one_line(out_a, 160)} direct={one_line(out_b, 120)}",
        "검증 목적: data/tests의 기존 3건과 XML 한 건의 직접 호출이 맞는지 본다.\n"
        "직접 호출은 unittest 전체의 대체 실행이 아니라 같은 parse_data 경로의 두 번째 도구다.\n"
        f"기대: 둘 다 성공. 실제 A={result_a} B={result_b}.\n{out_a[-800:]}\n{out_b[-400:]}",
    )

    if (ROOT / "web-vite" / "node_modules" / "vitest").exists() or os.environ.get("CI") == "true":
        code_a, out_a = run_cmd(["npm", "test"], ROOT / "web-vite", 180)
        code_b, out_b = run_cmd(["npm", "run", "typecheck"], ROOT / "web-vite", 120)
        result_a = "PASS" if code_a == 0 else ("ERROR" if code_a in {124, 127} else "FAIL")
        result_b = "PASS" if code_b == 0 else ("ERROR" if code_b in {124, 127} else "FAIL")
        final = "PASS" if result_a == result_b == "PASS" else ("FAIL" if "FAIL" in (result_a, result_b) else "ERROR")
        gate.add(
            "QA-UNIT-WEB", "프론트 단위 테스트와 타입 검사", "unit", final,
            "Vitest", "npm test", result_a,
            "tsc", "npm run typecheck", result_b,
            "web-vite/src/pages/pages.test.tsx", "UNKNOWN",
            find_line("web-vite/src/pages/pages.test.tsx", "describe"),
            f"vitest={one_line(out_a, 160)} tsc={one_line(out_b, 160)}",
            "검증 목적: 기존 Vitest와 tsc --noEmit을 각각 실행한다.\n"
            "둘은 범위가 다르다. Vitest는 동작, tsc는 타입이다. 한쪽만 성공하면 PASS가 아니다.\n"
            f"기대: 둘 다 종료 0. 실제 A={result_a} B={result_b}.\n{out_a[-800:]}\n{out_b[-800:]}",
        )
    else:
        gate.add(
            "QA-UNIT-WEB", "프론트 단위 테스트와 타입 검사", "unit", "BLOCKED",
            "Vitest", "npm test", "BLOCKED",
            "tsc", "npm run typecheck", "NOT_RUN",
            "web-vite/package.json", "UNKNOWN", "UNKNOWN",
            "web-vite/node_modules/vitest 가 없어 실행하지 않음",
            "node_modules가 없어 Vitest를 실행하지 않았다. 이 상태는 PASS가 아니다.",
        )


def walk_sql():
    hits = []
    for rel_root in SCAN_ROOTS:
        base = ROOT / rel_root
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".java", ".py", ".ts", ".tsx"}:
                continue
            if any(part in {"node_modules", "build", "dist"} for part in path.parts):
                continue
            try:
                lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            except OSError:
                continue
            for number, line in enumerate(lines, 1):
                if SQL_RE.search(line):
                    hits.append(f"{path.relative_to(ROOT)}:{number}")
    return hits


def rg_sql():
    if shutil.which("rg") is None:
        return None, "rg not installed"
    code, out = run_cmd(
        ["rg", "-n", "-i", "--glob", "!**/node_modules/**",
         "-e", r"(SELECT|INSERT|UPDATE|DELETE).{0,80}\+", *SCAN_ROOTS],
        ROOT, 30,
    )
    if code == 1:
        return [], out
    if code == 0:
        return [line for line in out.splitlines() if line.strip()], out
    return None, out


def run_security(gate):
    hits = walk_sql()
    rg_hits, rg_out = rg_sql()
    if rg_hits is None:
        result_b, final = "ERROR", "ERROR"
    elif not hits and not rg_hits:
        result_b, final = "PASS", "PASS"
        result_a = "PASS"
    else:
        result_a = "FAIL" if hits else "PASS"
        result_b = "FAIL" if rg_hits else "PASS"
        final = "FAIL"
    if rg_hits is not None and final != "ERROR":
        result_a = "FAIL" if hits else "PASS"
    elif rg_hits is None:
        result_a = "FAIL" if hits else "PASS"
    gate.add(
        "SEC-SQL-001", "메인 소스의 문자열 연결 SQL", "security", final if rg_hits is not None else "ERROR",
        "python", "SQL_RE walk spring/ai/data/web src", "FAIL" if hits else "PASS",
        "rg", "rg SELECT/INSERT/UPDATE/DELETE plus concatenation", result_b if rg_hits is not None else "ERROR",
        "spring/src", "UNKNOWN", "UNKNOWN",
        f"python={hits[:8]} rg={rg_hits[:8] if rg_hits is not None else rg_out}",
        "검증 목적: 본문 SQL을 문자열 연결로 만드는 코드가 있는지 본다.\n"
        "기대: 두 도구 모두 0건. 파라미터 바인딩만 있으면 PASS.\n"
        f"실제 python {len(hits)}건, rg {0 if not rg_hits else len(rg_hits)}건.\n{rg_out[-500:]}",
    )

    gradle = (ROOT / "spring" / "build.gradle").read_text(encoding="utf-8")
    absent_py = "spring-boot-starter-security" not in gradle and "EnableWebSecurity" not in gradle
    if shutil.which("rg"):
        code, out = run_cmd(["rg", "-n", "spring-boot-starter-security|EnableWebSecurity|SecurityFilterChain", "spring"], ROOT, 20)
        absent_rg = code == 1
        rg_result = "PASS" if absent_rg else ("FAIL" if code == 0 else "ERROR")
    else:
        out, absent_rg, rg_result = "rg missing", False, "ERROR"
    py_result = "PASS" if absent_py else "FAIL"
    final = "PASS" if py_result == "PASS" and rg_result == "PASS" else ("ERROR" if "ERROR" in (py_result, rg_result) else "FAIL")
    gate.add(
        "SEC-AUTH-001", "Spring Security 구성 존재 여부", "security", final,
        "python", "read spring/build.gradle", py_result,
        "rg", "rg spring-boot-starter-security spring", rg_result,
        "spring/build.gradle", "dependencies", find_line("spring/build.gradle", "dependencies {"),
        f"security starter absent python={absent_py} rg={absent_rg}",
        "검증 목적: 인증 라이브러리와 보안 필터가 소스에 있는지 확인한다.\n"
        "역할별 권한 요구사항 문서는 저장소에 없다. 없음을 통과 요건으로 추측하지 않고 위험으로 남긴다.\n"
        f"기대: 두 도구가 같은 관찰을 한다. 실제 python absent={absent_py} rg absent={absent_rg}.\n{out[-400:]}",
        risk="RISK-QA-AUTH",
    )
    gate.risk(
        "RISK-QA-AUTH", "HIGH", "MEDIUM",
        "이름, 나이, 만성질환이 인증 없이 생성·조회·삭제된다. compose는 127.0.0.1에 묶여 있으나 애플리케이션 인증은 없다.",
        "인증 요구사항을 정한 뒤 Spring Security 또는 앞단 인증을 넣기 전에는 공개 배포하지 않는다. 요구사항이 없다면 qa/risk-decisions.tsv 에 ACCEPTED로 남긴다.",
        "OPEN", "spring/build.gradle", "dependencies",
        find_line("spring/build.gradle", "spring-boot-starter-web"),
        "심각도 HIGH. 발생 가능성 MEDIUM. 상태 OPEN.\n"
        "처리 전 제품 코드는 수정하지 않는다. 로컬 바인딩은 노출 범위를 줄일 뿐 권한 검사를 대신하지 않는다.",
    )

    deploy = ROOT / ".github" / "workflows" / "deploy.yml"
    text = deploy.read_text(encoding="utf-8") if deploy.exists() else ""
    has_guard = 'test "$SUCCESS" -gt 0' in text
    line = find_line(".github/workflows/deploy.yml", 'test "$SUCCESS" -gt 0')
    if shutil.which("rg"):
        code, out = run_cmd(["rg", "-n", r'test "\$SUCCESS" -gt 0', ".github/workflows/deploy.yml"], ROOT, 15)
        rg_ok = code == 0
        rg_result = "PASS" if rg_ok else "FAIL"
    else:
        out, rg_ok, rg_result = "rg missing", False, "ERROR"
    py_result = "PASS" if has_guard else "FAIL"
    final = "PASS" if py_result == rg_result == "PASS" else ("ERROR" if rg_result == "ERROR" else "FAIL")
    gate.add(
        "SEC-DEPLOY-001", "수동 배포가 성공한 CI SHA를 요구하는지", "security", final,
        "python", "read deploy.yml SUCCESS guard", py_result,
        "rg", "rg test SUCCESS deploy.yml", rg_result,
        ".github/workflows/deploy.yml", "Require successful CI for exact deployment commit", line,
        f"guard={has_guard}",
        "검증 목적: workflow_dispatch가 CI 성공 확인 없이 배포하지 않는지 파일에서 확인한다.\n"
        "이전 RISK-001 행은 도구 결과가 UNKNOWN이었다. 이 실행은 현재 파일을 다시 읽는다.\n"
        f"기대: test \"$SUCCESS\" -gt 0 가 있다. 실제 python={has_guard} rg={rg_ok} line={line}.\n{out[-300:]}",
        risk="RISK-QA-DEPLOY",
    )
    gate.risk(
        "RISK-QA-DEPLOY", "MEDIUM", "LOW",
        "워크플로 파일의 SHA 확인은 들어 있다. 브랜치 보호 규칙 자체는 저장소 파일로 강제되지 않는다.",
        "GitHub ruleset에서 qa-gate 성공을 병합 조건으로 둔다.",
        "OPEN", ".github/workflows/deploy.yml", "deploy", line,
        "심각도 MEDIUM. 이전 HIGH 우회(가드 부재)는 현재 파일에서 test \"$SUCCESS\" -gt 0 로 완화됐다. "
        "규칙셋 미설정은 남아 있으므로 OPEN이다. HIGH는 아니다.",
    )

    form = "web-vite/src/pages/AssessmentFormPage.tsx"
    line_set = find_line(form, "setSubmitting(true)")
    line_btn = find_line(form, "disabled={submitting}")
    py_ok = line_set != "UNKNOWN" and line_btn != "UNKNOWN"
    if shutil.which("rg"):
        code, out = run_cmd(["rg", "-n", "setSubmitting\\(true\\)|disabled=\\{submitting\\}", form], ROOT, 15)
        rg_ok = code == 0 and "setSubmitting" in out and "disabled" in out
        rg_result = "PASS" if rg_ok else "FAIL"
    else:
        out, rg_result = "rg missing", "ERROR"
    gate.add(
        "SEC-UI-023", "제출 버튼 비활성 시점 정적 확인", "security",
        "PASS" if py_ok and rg_result == "PASS" else "ERROR",
        "python", "find setSubmitting and disabled", "PASS" if py_ok else "FAIL",
        "rg", "rg setSubmitting AssessmentFormPage.tsx", rg_result,
        form, "handleSubmit", line_set,
        f"setSubmitting line {line_set}; disabled line {line_btn}",
        "검증 목적: 브라우저를 다시 띄우지 않고, 더블클릭 가드가 어디에 있는지만 확인한다.\n"
        "setSubmitting(true)는 handleSubmit 검증 통과 뒤에 있다. disabled는 그 상태 값을 본다. "
        "같은 턴의 두 클릭은 React가 다시 그리기 전에 둘 다 핸들러로 들어갈 수 있다.\n"
        "이번 실행은 클릭 재현이 아니다. UI-023을 PASS로 바꾸지 않는다.\n"
        f"줄 번호는 이번 프로세스에서 파일을 읽어 확인했다. setSubmitting={line_set} disabled={line_btn}.\n{out[-300:]}",
        issue="BUG-UI-023", risk="RISK-QA-UI-023",
    )
    gate.risk(
        "RISK-QA-UI-023", "MEDIUM", "MEDIUM",
        "같은 턴 이중 클릭이 평가를 두 건 만들 수 있다. 기존 브라우저 결과 BUG-UI-023 / BUG-IF-0043.",
        "클릭 직후 동기적으로 제출을 잠그고, 잠금 전 두 번째 클릭 테스트를 다시 실행한다.",
        "OPEN", form, "handleSubmit", line_set,
        "심각도 MEDIUM. 이번 게이트는 브라우저를 실행하지 않았다. 코드 위치만 재확인했다. 제품 코드는 수정하지 않았다.",
    )

    if (ROOT / "web-vite" / "node_modules").exists() or os.environ.get("CI") == "true":
        code, out = run_cmd(["npm", "audit", "--json", "--audit-level=high"], ROOT / "web-vite", 120)
        try:
            start, end = out.find("{"), out.rfind("}")
            payload = json.loads(out[start:end + 1])
            vulns = payload.get("metadata", {}).get("vulnerabilities", {})
            high = int(vulns.get("high", 0))
            critical = int(vulns.get("critical", 0))
            parsed = start >= 0
        except (json.JSONDecodeError, TypeError, ValueError):
            high = critical = -1
            parsed = False
        if not parsed:
            result_a = result_b = final = "ERROR"
        elif high == 0 and critical == 0:
            result_a = result_b = final = "PASS"
        else:
            result_a = result_b = final = "FAIL"
        gate.add(
            "SEC-NPM-001", "프론트 의존성 high 이상 권고", "security", final,
            "npm audit", "npm audit --json --audit-level=high", result_a,
            "python json", "metadata.vulnerabilities.high/critical", result_b,
            "web-vite/package-lock.json", "UNKNOWN", "UNKNOWN",
            f"high={high} critical={critical}",
            "검증 목적: npm audit high 이상이 0인지 본다. 도구 B는 같은 JSON의 건수를 다시 집계한다. "
            "별도의 취약점 DB를 호출하지는 않는다.\n"
            f"기대: high 0, critical 0. 실제 high={high} critical={critical} exit={code}.\n"
            "전체 JSON은 리포트에 넣지 않는다.",
            risk="RISK-QA-NPM" if final == "FAIL" else "",
        )
        if final == "FAIL":
            severity = "HIGH" if critical > 0 else "MEDIUM"
            gate.risk(
                "RISK-QA-NPM", severity, "MEDIUM",
                f"npm audit high={high} critical={critical}",
                "권고를 확인하고 수정 범위만 올려 다시 audit 한다.",
                "OPEN", "web-vite/package-lock.json", "UNKNOWN", "UNKNOWN",
                f"심각도 {severity}. 상태 OPEN. 패키지 목록 전문은 저장하지 않았다.",
            )
    else:
        gate.add(
            "SEC-NPM-001", "프론트 의존성 high 이상 권고", "security", "BLOCKED",
            "npm audit", "npm audit --json", "BLOCKED",
            "python json", "not run", "NOT_RUN",
            "web-vite/package.json", "UNKNOWN", "UNKNOWN",
            "node_modules 없음",
            "npm audit를 실행하지 않았다. PASS가 아니다.",
        )


def run_http_cases(gate, test_type, cases):
    for case in cases:
        payload = base_payload()
        payload.update(case.get("set") or {})
        for key in case.get("omit") or ():
            payload.pop(key, None)
        body = json.dumps(payload, ensure_ascii=False)
        content_type = case.get("content_type", "application/json")
        status_a, body_a, problem_a, cmd_a = curl_call("POST", f"{SPRING}/api/assessments", body, content_type)
        status_b, body_b, problem_b, cmd_b = httpx_call("POST", f"{SPRING}/api/assessments", body, content_type)
        result_a, result_b, final = judge_pair(status_a, problem_a, status_b, problem_b, case["expected"])
        for status, text in ((status_a, body_a), (status_b, body_b)):
            remember(gate.created, status, text)
        db_note = ""
        for text in (body_a, body_b):
            found = response_id(text or "")
            if isinstance(found, int):
                try:
                    db_note += f" id={found} db={lookup_row(found)};"
                except RuntimeError as exc:
                    db_note += f" id={found} db_error={exc};"
        line = find_line(case["file"], case["needle"])
        issue = case.get("issue", "") if final == "FAIL" else ""
        risk = case.get("risk", "") if final == "FAIL" else ""
        gate.add(
            case["id"], case["feature"], test_type, final,
            "curl", cmd_a, result_a, "httpx", cmd_b, result_b,
            case["file"], case["function"], line,
            f"curl={status_a} {one_line(body_a, 120)} httpx={status_b} {one_line(body_b, 120)}{db_note}",
            f"검증 목적: {case['purpose']}\n"
            f"입력: Content-Type {content_type} body {body}\n"
            f"기대: HTTP {sorted(case['expected'])}. 실제 curl={status_a} {problem_a or ''} body={one_line(body_a, 220)}; "
            f"httpx={status_b} {problem_b or ''} body={one_line(body_b, 220)}.{db_note}\n"
            f"재현: curl -m 40 -H 'Content-Type: {content_type}' -d '{body}' {SPRING}/api/assessments\n"
            "오류 위치는 이번 실행에서 소스 파일을 읽어 줄 번호를 확인했다. 수정은 하지 않았다.\n"
            "재검증: 제품 코드를 바꾸지 않았으므로 수정 후 재검증은 없다.",
            issue=issue, risk=risk,
        )


def run_api(gate):
    try:
        gate.baseline = counts()
    except RuntimeError as exc:
        gate.baseline = None
        gate.add(
            "QA-API-DB", "API 실행 전 DB 기준선", "api", "BLOCKED",
            "psql", "docker exec psql count", "BLOCKED",
            "psql", "same", "BLOCKED",
            "UNKNOWN", "UNKNOWN", "UNKNOWN", str(exc),
            "DB 기준선을 읽지 못했다. API 변경 케이스는 실행하지 않는다. PASS가 아니다.",
        )
        return
    cases = [
        {"id": "IF-0047", "feature": "이름 누락", "purpose": "applicantName이 없으면 400이고 행이 늘지 않는지",
         "omit": ["applicantName"], "expected": {400},
         "file": "spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java",
         "needle": "String applicantName", "function": "applicantName"},
        {"id": "IF-0052", "feature": "이름에 숫자", "purpose": "JSON 숫자 이름이 400으로 거절되는지",
         "set": {"applicantName": 17}, "expected": {400},
         "file": "spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java",
         "needle": "String applicantName", "function": "applicantName",
         "issue": "BUG-IF-0052", "risk": "RISK-QA-JACKSON"},
        {"id": "IF-0059", "feature": "나이 소수", "purpose": "나이 60.5가 400으로 거절되는지",
         "set": {"age": 60.5}, "expected": {400},
         "file": "spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java",
         "needle": "Integer age", "function": "age",
         "issue": "BUG-IF-0059", "risk": "RISK-QA-JACKSON"},
        {"id": "IF-0060", "feature": "나이 숫자 문자열", "purpose": "나이 \"70\"이 400으로 거절되는지",
         "set": {"age": "70"}, "expected": {400},
         "file": "spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java",
         "needle": "Integer age", "function": "age",
         "issue": "BUG-IF-0060", "risk": "RISK-QA-JACKSON"},
        {"id": "IF-0067", "feature": "건강 숫자 문자열", "purpose": "physicalLevel \"3\"이 400으로 거절되는지",
         "set": {"physicalLevel": "3"}, "expected": {400},
         "file": "spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java",
         "needle": "Integer physicalLevel", "function": "physicalLevel",
         "issue": "BUG-IF-0067", "risk": "RISK-QA-JACKSON"},
        {"id": "IF-0072", "feature": "만성질환 숫자", "purpose": "chronicDisease 1이 400으로 거절되는지",
         "set": {"chronicDisease": 1}, "expected": {400},
         "file": "spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java",
         "needle": "Boolean chronicDisease", "function": "chronicDisease",
         "issue": "BUG-IF-0072", "risk": "RISK-QA-JACKSON"},
        {"id": "IF-0079", "feature": "근무시간 소수", "purpose": "workHourLimit 2.5가 400으로 거절되는지",
         "set": {"workHourLimit": 2.5}, "expected": {400},
         "file": "spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java",
         "needle": "Integer workHourLimit", "function": "workHourLimit",
         "issue": "BUG-IF-0079", "risk": "RISK-QA-JACKSON"},
        {"id": "IF-0083", "feature": "없는 직무", "purpose": "jobId 999999가 404이고 행이 없는지",
         "set": {"jobId": 999999}, "expected": {404},
         "file": "spring/src/main/demo/assessment/service/AssessmentService.java",
         "needle": "직무를 찾을 수 없습니다", "function": "createAndAnalyze"},
        {"id": "IF-0087", "feature": "text/plain 본문", "purpose": "text/plain이 4xx이고 500이 아닌지",
         "content_type": "text/plain", "expected": set(range(400, 500)),
         "file": "spring/src/main/demo/global/exception/GlobalExceptionHandler.java",
         "needle": "handleUnexpected", "function": "handleUnexpected",
         "issue": "BUG-IF-0087", "risk": "RISK-QA-PLAIN"},
    ]
    run_http_cases(gate, "api", cases)
    failed = [row["TC_ID"] for row, _detail in gate.rows if row["TC_ID"] in {"IF-0052", "IF-0059", "IF-0060", "IF-0067", "IF-0072", "IF-0079"} and row["status"] == "FAIL"]
    if failed:
        gate.risk(
            "RISK-QA-JACKSON", "HIGH", "HIGH",
            "Jackson 기본 변환이 숫자·소수·문자열을 DTO 필드로 바꾼 뒤 @Valid가 그 값을 통과시킨다.",
            "FAIL_ON_TRAILING_TOKENS 또는 잘못된 형식을 거절하는 ObjectMapper를 두고, 같은 TC를 curl과 httpx로 다시 실행한다.",
            "OPEN", "spring/src/main/demo/global/config/AppConfig.java", "restTemplate",
            find_line("spring/src/main/demo/global/config/AppConfig.java", "RestTemplate restTemplate"),
            "심각도 HIGH. 상태 OPEN. AppConfig는 RestTemplate만 등록한다. "
            f"이번 실행에서 기대한 400이 아니었던 TC: {', '.join(failed)}. 제품 코드는 수정하지 않았다.",
        )
    plain = [row for row, _detail in gate.rows if row["TC_ID"] == "IF-0087" and row["status"] == "FAIL"]
    if plain:
        gate.risk(
            "RISK-QA-PLAIN", "MEDIUM", "MEDIUM",
            "text/plain 본문이 HttpMessageNotReadableException 처리로 가지 않고 500이 된다.",
            "지원하지 않는 Content-Type을 4xx로 다루고 curl과 httpx로 재검증한다.",
            "OPEN", "spring/src/main/demo/global/exception/GlobalExceptionHandler.java",
            "handleUnexpected", find_line("spring/src/main/demo/global/exception/GlobalExceptionHandler.java", "handleUnexpected"),
            "심각도 MEDIUM. 상태 OPEN. 500 응답은 내부 예외를 숨기지만 잘못된 입력을 서버 오류로 분류한다.",
        )


def run_integration(gate):
    if gate.baseline is None:
        try:
            gate.baseline = counts()
        except RuntimeError as exc:
            gate.add("QA-INT-001", "Spring에서 FastAPI까지 평가 생성", "integration", "BLOCKED",
                     "curl", "POST /api/assessments", "BLOCKED", "httpx", "POST /api/assessments", "BLOCKED",
                     "UNKNOWN", "UNKNOWN", "UNKNOWN", str(exc), "DB에 연결하지 못해 통합 생성을 하지 않았다.")
            return
    run_http_cases(gate, "integration", [{
        "id": "QA-INT-001", "feature": "정상 평가 생성",
        "purpose": "정상 JSON이 201이고 두 도구 모두 평가 번호를 만드는지",
        "expected": {201},
        "file": "spring/src/main/demo/assessment/controller/AssessmentController.java",
        "needle": "public Map<String, Long> create", "function": "create",
    }])


def run_e2e(gate):
    for tc_id, url, needle, feature in (
        ("QA-E2E-001", f"{WEB}/", "<html", "프론트 첫 페이지"),
        ("QA-E2E-002", f"{WEB}/api/jobs", "jobTitle", "nginx /api 프록시"),
    ):
        status_a, body_a, problem_a, cmd_a = curl_call("GET", url)
        status_b, body_b, problem_b, cmd_b = httpx_call("GET", url)
        expected = {200}
        result_a, result_b, final = judge_pair(status_a, problem_a, status_b, problem_b, expected)
        if final == "PASS" and (needle not in (body_a or "") or needle not in (body_b or "")):
            final = "FAIL"
            result_a = "FAIL" if needle not in (body_a or "") else result_a
            result_b = "FAIL" if needle not in (body_b or "") else result_b
        gate.add(
            tc_id, feature, "e2e", final, "curl", cmd_a, result_a, "httpx", cmd_b, result_b,
            "web-vite/nginx.conf", "UNKNOWN", find_line("web-vite/nginx.conf", "proxy_pass"),
            f"curl={status_a} httpx={status_b} needle={needle}",
            f"검증 목적: {url} 이 200이고 본문에 {needle} 가 있는지 curl과 httpx로 본다.\n"
            f"기대: 200. 실제 curl={status_a} {problem_a or ''} httpx={status_b} {problem_b or ''}.\n"
            "브라우저 클릭 테스트는 이번 종류에 넣지 않았다.",
        )


def run_performance(gate):
    command = ["curl", "-sS", "-m", "20", "-o", "/dev/null", "-w", "%{http_code} %{time_total}", f"{SPRING}/api/jobs"]
    code, out = run_cmd(command, ROOT, 25)
    curl_ok = code == 0 and out.strip().startswith("200")
    result_a = "PASS" if curl_ok else ("BLOCKED" if "couldn't connect" in out.lower() or "connection refused" in out.lower() else "ERROR" if code != 0 else "FAIL")

    def once(_n):
        status, _text, problem, _cmd = httpx_call("GET", f"{SPRING}/api/jobs")
        return status, problem

    try:
        with ThreadPoolExecutor(max_workers=5) as pool:
            results = list(pool.map(once, range(5)))
        bad = [item for item in results if item[0] != 200 or item[1]]
        result_b = "PASS" if not bad and results else "BLOCKED" if any(item[1] == "BLOCKED" for item in results) else "FAIL"
        summary = ",".join(str(item[0]) for item in results)
    except Exception as exc:
        result_b, summary = "ERROR", str(exc)
    final = "PASS" if result_a == result_b == "PASS" else ("BLOCKED" if "BLOCKED" in (result_a, result_b) and "FAIL" not in (result_a, result_b) else "FAIL" if "FAIL" in (result_a, result_b) else "ERROR")
    gate.add(
        "QA-PERF-001", "직무 목록 응답", "performance", final,
        "curl -w", " ".join(command), result_a,
        "httpx ThreadPoolExecutor", "5 parallel GET /api/jobs", result_b,
        "spring/src/main/demo/job/controller/JobController.java", "UNKNOWN",
        find_line("spring/src/main/demo/job/controller/JobController.java", "@GetMapping"),
        f"curl={one_line(out, 80)} httpx={summary}",
        "검증 목적: GET /api/jobs가 한 번과 동시 5회 모두 200인지 본다.\n"
        "저장소에 응답 시간 SLO가 없어 지연 숫자만 적고, 시간 초과 기준을 만들어 실패 처리하지는 않는다.\n"
        f"curl 출력: {out.strip()}. 동시 상태: {summary}.",
        risk="RISK-QA-SLO",
    )
    gate.risk(
        "RISK-QA-SLO", "LOW", "LOW",
        "성능 합격 기준이 요구사항에 없다.",
        "동시 사용자와 허용 지연을 정한 뒤 그 기준으로만 PASS/FAIL 한다.",
        "OPEN", "UNKNOWN", "UNKNOWN", "UNKNOWN",
        "심각도 LOW. 상태 OPEN. 이번 200 응답은 SLO 충족 판정이 아니다.",
    )


def run_regression(gate):
    try:
        after = counts()
    except RuntimeError as exc:
        gate.add("QA-REG-001", "실행 후 DB 건수", "regression", "BLOCKED",
                 "psql", "count four tables", "BLOCKED", "curl", "GET /api/jobs", "NOT_RUN",
                 "UNKNOWN", "UNKNOWN", "UNKNOWN", str(exc), "회귀용 DB 건수를 읽지 못했다.")
        return
    status_a, body_a, problem_a, cmd_a = curl_call("GET", f"{SPRING}/api/jobs")
    status_b, body_b, problem_b, cmd_b = httpx_call("GET", f"{SPRING}/api/jobs")
    jobs_a, jobs_b, jobs_final = judge_pair(status_a, problem_a, status_b, problem_b, {200})
    same = gate.baseline is not None and after == gate.baseline and after.get("id2") == 1
    if gate.baseline is None:
        db_result = "BLOCKED"
    elif same:
        db_result = "PASS"
    else:
        db_result = "FAIL"
    final = "PASS" if db_result == "PASS" and jobs_final == "PASS" else ("FAIL" if "FAIL" in (db_result, jobs_final) else "BLOCKED" if "BLOCKED" in (db_result, jobs_final) else "ERROR")
    gate.add(
        "QA-REG-001", "QA가 만든 행 정리와 직무 목록", "regression", final,
        "psql", "assessment/applicant/health_snapshot/ai_risk_result counts", db_result,
        "curl+httpx", f"{cmd_a} || {cmd_b}", jobs_final,
        "spring/src/main/demo/assessment/service/AssessmentService.java", "delete",
        find_line("spring/src/main/demo/assessment/service/AssessmentService.java", "public void delete"),
        f"before={gate.baseline} after={after} jobs={status_a}/{status_b}",
        "검증 목적: 이번 실행이 만든 평가를 지운 뒤 네 테이블 건수가 시작과 같고 평가 id 2가 남는지, "
        "직무 목록이 200인지 확인한다.\n"
        f"기대: 건수 동일, id2=1, HTTP 200. 실제 before={gate.baseline} after={after} jobs curl={status_a} httpx={status_b}.\n"
        "과거 TC_docs 결과를 다시 통과로 베끼지는 않았다.",
    )


def parse_types(text, ci):
    if not text:
        return CI_TYPES if ci else list(ALL_TYPES)
    if text.strip() == "all":
        return list(ALL_TYPES)
    chosen = []
    for item in text.split(","):
        name = item.strip()
        if name not in ALL_TYPES:
            raise SystemExit(f"unknown test type: {name}")
        if name not in chosen:
            chosen.append(name)
    return chosen


def gate_blocked(rows, risks, ci):
    accepted = accepted_risks()
    reasons = []
    for row, _detail in rows:
        if row["TC_ID"].startswith("RISK-") and row["status"] == "PASS":
            continue
        if row["status"] in {"FAIL", "ERROR"}:
            reasons.append(f"{row['TC_ID']} {row['status']}")
        elif row["status"] in {"BLOCKED", "NOT_RUN", "SKIPPED"} and not ci:
            reasons.append(f"{row['TC_ID']} {row['status']}")
    for risk in risks:
        if risk["severity"] in {"HIGH", "CRITICAL"} and risk["status"] == "OPEN" and risk["id"] not in accepted:
            reasons.append(f"{risk['id']} {risk['severity']} OPEN")
    return reasons


def main():
    parser = argparse.ArgumentParser(description="Run IF_v2 QA checks and append reports.")
    parser.add_argument("--types", default="", help="Comma list or all. Default: all locally, unit,security in --mode ci.")
    parser.add_argument("--mode", choices=["local", "ci"], default="local")
    parser.add_argument("--enforce-gate", action="store_true", help="Accepted for compatibility. The gate always sets the exit code.")
    parser.add_argument("--reverify", action="store_true")
    args = parser.parse_args()
    ci = args.mode == "ci"
    types = parse_types(args.types, ci)
    started = seoul_now()
    commit, dirty = git_meta()
    run_id = next_run_id(ROOT / "qa" / "reports", started)
    gate = Gate(run_id, started, commit, dirty, args.reverify)
    steps = {
        "unit": run_unit,
        "security": run_security,
        "e2e": run_e2e,
        "performance": run_performance,
        "api": run_api,
        "integration": run_integration,
        "regression": run_regression,
    }
    try:
        for name in ("unit", "security", "e2e", "performance", "api", "integration"):
            if name in types:
                steps[name](gate)
    finally:
        if gate.created:
            try:
                note = cleanup(gate.created)
                print("cleanup", note, flush=True)
            except Exception:
                traceback.print_exc()
                gate.add(
                    "QA-CLEANUP", "생성 행 정리", "api" if "api" in types else "regression", "ERROR",
                    "curl", "DELETE /api/assessments/{id}", "ERROR",
                    "psql", "delete unreferenced applicant/health", "ERROR",
                    "UNKNOWN", "UNKNOWN", "UNKNOWN", "cleanup raised",
                    traceback.format_exc()[-1500:],
                )
        if "regression" in types:
            try:
                run_regression(gate)
            except Exception:
                traceback.print_exc()
    base = ROOT / "qa" / "reports"
    for row, detail in gate.rows:
        append_record(base, row, detail)
    reasons = gate_blocked(gate.rows, gate.risks, ci)
    finished = seoul_now()
    write_pointer(base, {
        "run_id": run_id,
        "started_at": started.isoformat(timespec="seconds"),
        "finished_at": finished.isoformat(timespec="seconds"),
        "git_commit": commit,
        "types": types,
        "mode": "ci" if ci else "local",
        "blocking": reasons,
    })
    print(f"RUN_ID={run_id}")
    print("types=" + ",".join(types))
    if reasons:
        print("GATE BLOCKED")
        for reason in reasons:
            print(" -", reason)
        return 1
    print("GATE PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

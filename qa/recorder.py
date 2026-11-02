#!/usr/bin/env python3
"""QA·Security V2.5 리포트 및 TSV 기록 생성기 (qa/recorder.py).

역할:
- 실행된 테스트 종류(test-type)와 Asia/Seoul 날짜(YYYY-MM-DD) 기준으로만
  `qa/reports/{test-type}/{YYYY-MM-DD}/` 폴더를 생성한다. (미실행 종류 폴더는 생성 금지)
- 각 날짜 폴더에 `pass.md`, `fail.md`, `risk.md`, `results.tsv` 4개 파일을 생성·누적(Append)한다.
- 같은 날짜에 여러 번 실행하면 `RUN_ID`(예: RUN-20261030-001 -> RUN-20261030-002)를 자동으로 증가시켜
  과거 기록을 덮어쓰거나 삭제하지 않고 누적 보존한다.
- `results.tsv`는 UTF-8 with BOM(\ufeff)으로 저장하여 macOS/Windows Excel에서 한글이 깨지지 않게 한다.
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from zoneinfo import ZoneInfo

KST = ZoneInfo("Asia/Seoul")

ALLOWED_TEST_TYPES = (
    "api",
    "unit",
    "integration",
    "e2e",
    "security",
    "performance",
    "regression",
)

ALLOWED_STATUSES = (
    "PASS",
    "FAIL",
    "BLOCKED",
    "ERROR",
    "NOT_RUN",
    "SKIPPED",
)

TSV_HEADERS = [
    "RUN_ID",
    "TC_ID",
    "DATETIME",
    "FEATURE",
    "TEST_TYPE",
    "TOOL_A",
    "RESULT_A",
    "TOOL_B",
    "RESULT_B",
    "STATUS",
    "GIT_COMMIT",
    "TARGET_FILE",
    "FUNCTION_NAME",
    "LINE_NO",
    "ISSUE_RISK_ID",
    "EVIDENCE",
]


@dataclass
class TCRecord:
    """단일 테스트 케이스(TC) 교차 검증 결과 레코드."""

    run_id: str
    tc_id: str
    datetime_kst: str
    feature: str
    test_type: str
    tool_a: str
    result_a: str
    tool_b: str
    result_b: str
    status: str
    git_commit: str
    target_file: str = "UNKNOWN"
    function_name: str = "UNKNOWN"
    line_no: str = "UNKNOWN"
    issue_risk_id: str = "-"
    purpose: str = ""
    expected: str = ""
    actual: str = ""
    evidence: str = ""
    # FAIL 전용 상세 필드
    input_value: str = ""
    error_message: str = ""
    repro_steps: str = ""
    root_cause: str = ""
    fix_location: str = "PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)"
    reverify_note: str = "최초 검출 (코드 수정 후 Tool A/B 재검증 예정)"


@dataclass
class RiskRecord:
    """잠재 위험·예외 처리 누락·보안/설계 위험(RISK) 레코드."""

    run_id: str
    risk_id: str
    tc_id: str
    datetime_kst: str
    feature: str
    test_type: str
    severity: str  # CRITICAL / HIGH / MEDIUM / LOW
    likelihood: str  # HIGH / MEDIUM / LOW
    impact: str
    title: str
    description: str
    tool_a: str
    result_a: str
    tool_b: str
    result_b: str
    git_commit: str
    target_file: str = "UNKNOWN"
    function_name: str = "UNKNOWN"
    line_no: str = "UNKNOWN"
    recommendation: str = ""
    state: str = "OPEN"  # OPEN / MITIGATED / ACCEPTED / CLOSED
    report_history: str = ""


def now_kst() -> datetime:
    """현재 시각을 Asia/Seoul(KST) 기준으로 반환한다."""
    return datetime.now(KST)


def next_run_id(reports_root: Path, date_str: str) -> str:
    """해당 날짜(YYYY-MM-DD)의 기존 results.tsv들을 확인하여 다음 RUN_ID를 발급한다."""
    ymd_compact = date_str.replace("-", "")
    prefix = f"RUN-{ymd_compact}-"
    max_seq = 0
    pattern = re.compile(rf"^{re.escape(prefix)}(\d{{3,}})$")

    if reports_root.exists():
        for tsv_path in reports_root.glob(f"*/{date_str}/results.tsv"):
            try:
                content = tsv_path.read_text(encoding="utf-8-sig")
                for line in content.splitlines()[1:]:
                    if not line.strip():
                        continue
                    first_col = line.split("\t", 1)[0].strip()
                    m = pattern.match(first_col)
                    if m:
                        max_seq = max(max_seq, int(m.group(1)))
            except Exception:
                continue

    return f"{prefix}{max_seq + 1:03d}"


def _sanitize_tsv_cell(val: str) -> str:
    """TSV 셀 내부의 줄바꿈과 탭을 공백으로 치환하여 표가 깨지지 않게 한다."""
    if not val:
        return "-"
    return " ".join(str(val).replace("\t", " ").replace("\r", " ").replace("\n", " ").split())


def write_test_type_reports(
    reports_root: Path,
    test_type: str,
    date_str: str,
    run_id: str,
    tc_records: List[TCRecord],
    risk_records: List[RiskRecord],
    is_reverify: bool = False,
) -> Path:
    """특정 test_type의 날짜 폴더에 pass.md, fail.md, risk.md, results.tsv를 기록·누적한다."""
    if test_type not in ALLOWED_TEST_TYPES:
        raise ValueError(f"허용되지 않는 테스트 종류입니다: {test_type}")

    target_dir = reports_root / test_type / date_str
    existing_tsv = target_dir / 'results.tsv'
    if existing_tsv.exists():
        with existing_tsv.open(encoding='utf-8-sig', newline='') as stream:
            if next(csv.reader(stream, delimiter='\t'), None) != TSV_HEADERS:
                raise ValueError('Incompatible TSV schema; existing QA history preserved. Use scripts/qa/run.py.')
    target_dir.mkdir(parents=True, exist_ok=True)

    pass_file = target_dir / "pass.md"
    fail_file = target_dir / "fail.md"
    risk_file = target_dir / "risk.md"
    tsv_file = target_dir / "results.tsv"

    pass_list = [r for r in tc_records if r.status == "PASS"]
    fail_list = [r for r in tc_records if r.status != "PASS"]

    run_mode_label = "재검증 실행 (Re-verification)" if is_reverify else "정규 실행 (Standard Run)"
    timestamp_str = now_kst().strftime("%Y-%m-%d %H:%M:%S KST")

    # 1. pass.md 기록 (누적 Append)
    if not pass_file.exists():
        pass_header = (
            f"# [{test_type.upper()}] PASS 테스트 기록 ({date_str})\n\n"
            f"> **경로**: `qa/reports/{test_type}/{date_str}/pass.md`  \n"
            f"> **기준 시간대**: `Asia/Seoul` (KST)  \n"
            f"> **원칙**: 최소 2개 도구(Tool A / Tool B) 교차 검증을 모두 통과(`PASS`)한 테스트 케이스만 기록합니다.\n\n"
        )
        pass_file.write_text(pass_header, encoding="utf-8")

    with pass_file.open("a", encoding="utf-8") as f:
        f.write(f"---\n\n## 실행 이력: `{run_id}` ({run_mode_label} — {timestamp_str})\n\n")
        f.write(f"- **통과 건수**: {len(pass_list)}건 / 전체 {len(tc_records)}건\n\n")
        if not pass_list:
            f.write("> 해당 실행(`RUN_ID`)에서 통과한 TC가 없습니다.\n\n")
        else:
            f.write(
                "| RUN_ID | TC_ID | 실행 일시 (KST) | 기능명 | 도구 A (결과) | 도구 B (결과) | 최종 상태 | Git Commit | 대상 파일 | 함수명 | 줄 번호 | 관련 ID | 검증 목적 및 근거 |\n"
                "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
            )
            for r in pass_list:
                f.write(
                    f"| `{r.run_id}` | `{r.tc_id}` | {r.datetime_kst} | {r.feature} | "
                    f"`{r.tool_a}` ({r.result_a}) | `{r.tool_b}` ({r.result_b}) | **{r.status}** | "
                    f"`{r.git_commit}` | `{r.target_file}` | `{r.function_name}` | `{r.line_no}` | "
                    f"`{r.issue_risk_id}` | **목적**: {r.purpose}<br>**기대**: {r.expected}<br>**실제/근거**: {r.actual} ({r.evidence}) |\n"
                )
            f.write("\n")

    # 2. fail.md 기록 (누적 Append)
    if not fail_file.exists():
        fail_header = (
            f"# [{test_type.upper()}] FAIL 및 미통과 상세 기록 ({date_str})\n\n"
            f"> **경로**: `qa/reports/{test_type}/{date_str}/fail.md`  \n"
            f"> **기준 시간대**: `Asia/Seoul` (KST)  \n"
            f"> **원칙**: 코드 수정 전 반드시 본 문서에 먼저 기록하고 사용자에게 보고합니다. 도구 하나라도 실패 시 완료 처리하지 않습니다.\n\n"
        )
        fail_file.write_text(fail_header, encoding="utf-8")

    with fail_file.open("a", encoding="utf-8") as f:
        f.write(f"---\n\n## 실행 이력: `{run_id}` ({run_mode_label} — {timestamp_str})\n\n")
        f.write(f"- **실패/미통과 건수**: {len(fail_list)}건 / 전체 {len(tc_records)}건\n\n")
        if not fail_list:
            f.write("> 해당 실행(`RUN_ID`)에서 실패(`FAIL`/`ERROR`/`BLOCKED`)한 TC가 없습니다.\n\n")
        else:
            for r in fail_list:
                f.write(f"### [{r.tc_id}] {r.feature} (`{r.status}`) — `{r.issue_risk_id}`\n\n")
                f.write(f"- **RUN_ID**: `{r.run_id}`\n")
                f.write(f"- **실행 일시**: `{r.datetime_kst}`\n")
                f.write(f"- **테스트 종류**: `{r.test_type}`\n")
                f.write(f"- **Git Commit**: `{r.git_commit}`\n")
                f.write(f"- **도구 A 및 결과**: `{r.tool_a}` → **{r.result_a}**\n")
                f.write(f"- **도구 B 및 결과**: `{r.tool_b}` → **{r.result_b}**\n")
                f.write(f"- **최종 상태**: **{r.status}**\n")
                f.write(f"- **오류 코드 위치**: 파일 `{r.target_file}` / 함수 `{r.function_name}` / 줄 번호 `{r.line_no}`\n")
                f.write(f"- **입력값 (Input)**: `{r.input_value or r.purpose}`\n")
                f.write(f"- **오류 메시지 / 응답**: `{r.error_message or r.actual}`\n")
                f.write(f"- **예상 결과 (Expected)**: {r.expected}\n")
                f.write(f"- **실제 결과 (Actual)**: {r.actual}\n")
                f.write(f"- **재현 방법 (Reproduction)**:\n  ```zsh\n  {r.repro_steps or r.evidence}\n  ```\n")
                f.write(f"- **원인 분석 (Root Cause)**: {r.root_cause}\n")
                f.write(f"- **수정 코드 위치 (Fix Location)**: {r.fix_location}\n")
                f.write(f"- **재검증 내역 (Re-verification)**: {r.reverify_note}\n\n")

    # 3. risk.md 기록 (누적 Append)
    if not risk_file.exists():
        risk_header = (
            f"# [{test_type.upper()}] 잠재 위험 및 보안/설계 리스크 기록 ({date_str})\n\n"
            f"> **경로**: `qa/reports/{test_type}/{date_str}/risk.md`  \n"
            f"> **기준 시간대**: `Asia/Seoul` (KST)  \n"
            f"> **원칙**: 테스트 통과 여부와 별도로 예외 처리 누락, 잠재 취약점, 설계 위험, 불명확 요구사항을 기록합니다. 미해결 HIGH/CRITICAL 위험은 완료·병합을 차단합니다.\n\n"
        )
        risk_file.write_text(risk_header, encoding="utf-8")

    with risk_file.open("a", encoding="utf-8") as f:
        f.write(f"---\n\n## 실행 이력: `{run_id}` ({run_mode_label} — {timestamp_str})\n\n")
        f.write(f"- **검출/추적 리스크 건수**: {len(risk_records)}건\n\n")
        if not risk_records:
            f.write("> 해당 실행(`RUN_ID`)에서 추가로 검출된 리스크가 없습니다.\n\n")
        else:
            for rk in risk_records:
                f.write(f"### [{rk.risk_id}] {rk.title} (심각도: **{rk.severity}**, 상태: **{rk.state}**)\n\n")
                f.write(f"- **RUN_ID**: `{rk.run_id}`\n")
                f.write(f"- **관련 TC_ID**: `{rk.tc_id}`\n")
                f.write(f"- **실행 일시**: `{rk.datetime_kst}`\n")
                f.write(f"- **기능명 / 테스트 종류**: {rk.feature} (`{rk.test_type}`)\n")
                f.write(f"- **Git Commit**: `{rk.git_commit}`\n")
                f.write(f"- **도구 A 및 결과**: `{rk.tool_a}` → {rk.result_a}\n")
                f.write(f"- **도구 B 및 결과**: `{rk.tool_b}` → {rk.result_b}\n")
                f.write(f"- **대상 코드 위치**: 파일 `{rk.target_file}` / 함수 `{rk.function_name}` / 줄 번호 `{rk.line_no}`\n")
                f.write(f"- **심각도 (Severity)**: **{rk.severity}**\n")
                f.write(f"- **발생 가능성 (Likelihood)**: **{rk.likelihood}**\n")
                f.write(f"- **영향 (Impact)**: {rk.impact}\n")
                f.write(f"- **상세 내용**: {rk.description}\n")
                f.write(f"- **권장 조치 (Recommendation)**: {rk.recommendation}\n")
                f.write(f"- **처리 상태 (Status)**: `{rk.state}`\n")
                f.write(f"- **보고 이력 (Report History)**: {rk.report_history}\n\n")

    # 4. results.tsv 기록 (UTF-8 with BOM \ufeff, 누적 Append)
    write_header = not tsv_file.exists()
    with tsv_file.open("a", encoding="utf-8-sig" if write_header else "utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        if write_header:
            writer.writerow(TSV_HEADERS)
        for r in tc_records:
            if r.status not in ALLOWED_STATUSES:
                raise ValueError(f"허용되지 않는 TSV 상태값입니다: {r.status}")
            writer.writerow([
                _sanitize_tsv_cell(r.run_id),
                _sanitize_tsv_cell(r.tc_id),
                _sanitize_tsv_cell(r.datetime_kst),
                _sanitize_tsv_cell(r.feature),
                _sanitize_tsv_cell(r.test_type),
                _sanitize_tsv_cell(r.tool_a),
                _sanitize_tsv_cell(r.result_a),
                _sanitize_tsv_cell(r.tool_b),
                _sanitize_tsv_cell(r.result_b),
                _sanitize_tsv_cell(r.status),
                _sanitize_tsv_cell(r.git_commit),
                _sanitize_tsv_cell(r.target_file),
                _sanitize_tsv_cell(r.function_name),
                _sanitize_tsv_cell(r.line_no),
                _sanitize_tsv_cell(r.issue_risk_id),
                _sanitize_tsv_cell(f"기대: {r.expected} | 실제: {r.actual} | 근거: {r.evidence}"),
            ])

    return target_dir

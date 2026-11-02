"""QA V3.0 append-only recorder.

qa/master_test_sheet.xlsx
qa/input/testcases.tsv
qa/history/execution_log.tsv
qa/results/{area}/{section}/{YYYY-MM-DD}/
  test_sheet.xlsx, pass.md, fail.md, risk.md, results.tsv
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import subprocess
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape
from zoneinfo import ZoneInfo

SEOUL = ZoneInfo("Asia/Seoul")
AREAS = (
    "01_unit_integration",
    "02_web_api",
    "03_security_quality",
    "04_infra_deploy",
)
RESULT_FIELDS = [
    "RUN_ID",
    "TC_ID",
    "FEATURE_ID",
    "timestamp_start",
    "timestamp_end",
    "area",
    "section",
    "scenario",
    "tool_a",
    "command_a",
    "result_a",
    "expected_a",
    "actual_a",
    "tool_b",
    "command_b",
    "result_b",
    "expected_b",
    "actual_b",
    "status",
    "git_commit",
    "dirty",
    "code_file",
    "function",
    "line",
    "ISSUE_ID",
    "RISK_ID",
    "evidence",
]
TC_FIELDS = [
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
STATUSES = {"PASS", "FAIL", "BLOCKED", "ERROR", "NOT_RUN", "SKIPPED"}
ROOT = Path(__file__).resolve().parents[1]
QA_ROOT = ROOT / "qa"
RESULTS_ROOT = QA_ROOT / "results"
INPUT_ROOT = QA_ROOT / "input"
CONFIG_ROOT = QA_ROOT / "config"
HISTORY_ROOT = QA_ROOT / "history"
MASTER_XLSX = QA_ROOT / "master_test_sheet.xlsx"
HISTORY_TSV = HISTORY_ROOT / "execution_log.tsv"
TESTCASES_TSV = INPUT_ROOT / "testcases.tsv"
DATE_FILES = ("test_sheet.xlsx", "pass.md", "fail.md", "risk.md", "results.tsv")


def seoul_now():
    return dt.datetime.now(SEOUL)


def git_meta(root=ROOT):
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short=12", "HEAD"], cwd=root, text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        commit = "UNKNOWN"
    try:
        dirty = bool(
            subprocess.check_output(
                ["git", "status", "--porcelain"], cwd=root, text=True
            ).strip()
        )
    except (OSError, subprocess.CalledProcessError):
        dirty = True
    return commit, "true" if dirty else "false"


def _one_line(value):
    return " ".join(str(value).split())


def _col_name(index: int) -> str:
    name = ""
    while index:
        index, rem = divmod(index - 1, 26)
        name = chr(65 + rem) + name
    return name


def write_xlsx(path: Path, headers: list[str], rows: list[list[str]], sheet_name: str = "results") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>
"""
    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>
"""
    wb_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
</Relationships>
"""
    workbook = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="{escape(sheet_name)}" sheetId="1" r:id="rId1"/>
  </sheets>
</workbook>
"""
    lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>',
    ]
    for r_idx, values in enumerate([headers, *rows], start=1):
        lines.append(f'<row r="{r_idx}">')
        for c_idx, value in enumerate(values, start=1):
            ref = f"{_col_name(c_idx)}{r_idx}"
            text = escape("" if value is None else str(value))
            lines.append(f'<c r="{ref}" t="inlineStr"><is><t>{text}</t></is></c>')
        lines.append("</row>")
    lines.append("</sheetData></worksheet>")
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", rels)
        zf.writestr("xl/workbook.xml", workbook)
        zf.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        zf.writestr("xl/worksheets/sheet1.xml", "\n".join(lines))


def _write_tsv_header(path: Path, fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n").writeheader()


def _append_tsv(path: Path, fields: list[str], row: dict) -> None:
    _write_tsv_header(path, fields)
    with path.open("a", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writerow({k: _one_line(row.get(k, "")) for k in fields})


def _read_tsv_rows(path: Path) -> list[list[str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.reader(stream, delimiter="\t"))
    return rows[1:] if rows else []


def ensure_layout(testcases: list[dict] | None = None) -> None:
    INPUT_ROOT.mkdir(parents=True, exist_ok=True)
    CONFIG_ROOT.mkdir(parents=True, exist_ok=True)
    HISTORY_ROOT.mkdir(parents=True, exist_ok=True)
    RESULTS_ROOT.mkdir(parents=True, exist_ok=True)
    for area in AREAS:
        (RESULTS_ROOT / area).mkdir(parents=True, exist_ok=True)
    _write_tsv_header(HISTORY_TSV, RESULT_FIELDS)
    if not TESTCASES_TSV.exists():
        with TESTCASES_TSV.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(
                stream, fieldnames=TC_FIELDS, delimiter="\t", lineterminator="\n"
            )
            writer.writeheader()
            for row in testcases or []:
                writer.writerow({k: row.get(k, "") for k in TC_FIELDS})
    if not MASTER_XLSX.exists():
        write_xlsx(MASTER_XLSX, RESULT_FIELDS, [], sheet_name="master")


def blank_row(run_id: str, start, end, commit: str, dirty: str) -> dict:
    row = {k: "" for k in RESULT_FIELDS}
    row.update(
        RUN_ID=run_id,
        timestamp_start=start.isoformat(timespec="seconds"),
        timestamp_end=end.isoformat(timespec="seconds"),
        git_commit=commit,
        dirty=dirty,
        function="UNKNOWN",
        line="UNKNOWN",
        code_file="UNKNOWN",
        expected_a="PASS",
        expected_b="PASS",
    )
    return row


def _ensure_date_files(folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    for name in ("pass", "fail", "risk"):
        path = folder / f"{name}.md"
        if not path.exists():
            path.write_text(f"# {name.upper()}\n", encoding="utf-8")
    if not (folder / "results.tsv").exists():
        _write_tsv_header(folder / "results.tsv", RESULT_FIELDS)
    if not (folder / "test_sheet.xlsx").exists():
        write_xlsx(folder / "test_sheet.xlsx", RESULT_FIELDS, [], sheet_name="results")


def _rebuild_master() -> None:
    rows: list[list[str]] = []
    latest: dict[str, list[str]] = {}
    for path in sorted(RESULTS_ROOT.glob("*/*/*/results.tsv")):
        for row in _read_tsv_rows(path):
            if not row:
                continue
            # pad
            while len(row) < len(RESULT_FIELDS):
                row.append("")
            tc = row[1] if len(row) > 1 else ""
            latest[tc] = row
            rows.append(row)
    write_xlsx(MASTER_XLSX, RESULT_FIELDS, list(latest.values()), sheet_name="master")


def append_record(qa_root: Path, row: dict, detail: str) -> Path:
    if row["status"] not in STATUSES:
        raise ValueError(f"bad status {row['status']}")
    area = row.get("area") or ""
    section = row.get("section") or ""
    if area not in AREAS:
        raise ValueError(f"bad area {area!r}")
    if not section or "/" in section or section in (".", ".."):
        raise ValueError(f"bad section {section!r}")
    results_root = qa_root / "results" if (qa_root / "results").exists() or qa_root == QA_ROOT else qa_root / "results"
    if qa_root == QA_ROOT:
        results_root = RESULTS_ROOT
    folder = results_root / area / section / str(row.get("timestamp_end") or row.get("timestamp_start") or "")[:10]
    if len(folder.name) != 10:
        folder = results_root / area / section / seoul_now().strftime("%Y-%m-%d")
    _ensure_date_files(folder)
    safe = {k: _one_line(row.get(k, "")) for k in RESULT_FIELDS}
    _append_tsv(folder / "results.tsv", RESULT_FIELDS, safe)
    history = qa_root / "history" / "execution_log.tsv"
    if qa_root == QA_ROOT:
        history = HISTORY_TSV
    else:
        history.parent.mkdir(parents=True, exist_ok=True)
    _append_tsv(history, RESULT_FIELDS, safe)

    targets = []
    if row["status"] == "PASS":
        targets.append("pass")
    else:
        targets.append("fail")
    if row.get("RISK_ID") or detail.startswith("RISK"):
        targets.append("risk")
    block = "\n".join(f"- {k}: {safe[k]}" for k in RESULT_FIELDS)
    body = f"\n## {safe['RUN_ID']} / {safe['TC_ID']}\n{block}\n\n{detail.strip()}\n"
    for name in targets:
        with (folder / f"{name}.md").open("a", encoding="utf-8") as stream:
            stream.write(body)
    write_xlsx(folder / "test_sheet.xlsx", RESULT_FIELDS, _read_tsv_rows(folder / "results.tsv"), sheet_name="results")
    if results_root.resolve() == RESULTS_ROOT.resolve():
        _rebuild_master()
    else:
        write_xlsx(qa_root / "master_test_sheet.xlsx", RESULT_FIELDS, _read_tsv_rows(folder / "results.tsv"), sheet_name="master")
    return folder


def write_pointer(base: Path, payload: dict) -> Path:
    path = base / "last-run.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def load_testcases() -> list[dict]:
    if not TESTCASES_TSV.exists():
        return []
    with TESTCASES_TSV.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def load_test_map() -> dict:
    path = CONFIG_ROOT / "test_map.json"
    return json.loads(path.read_text(encoding="utf-8"))

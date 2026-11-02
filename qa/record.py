"""Append-only QA report writer. Asia/Seoul dates, UTF-8 TSV with BOM."""
import csv
import datetime as dt
import subprocess
from pathlib import Path
from zoneinfo import ZoneInfo

SEOUL = ZoneInfo("Asia/Seoul")
FIELDS = [
    "RUN_ID", "TC_ID", "timestamp", "feature", "test_type",
    "tool_a", "command_a", "result_a", "tool_b", "command_b", "result_b",
    "status", "git_commit", "dirty", "files", "function", "line",
    "ISSUE_ID", "RISK_ID", "evidence",
]
STATUSES = {"PASS", "FAIL", "BLOCKED", "ERROR", "NOT_RUN", "SKIPPED"}
ROOT = Path(__file__).resolve().parents[1]


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
        dirty = bool(subprocess.check_output(
            ["git", "status", "--porcelain"], cwd=root, text=True
        ).strip())
    except (OSError, subprocess.CalledProcessError):
        dirty = True
    return commit, "true" if dirty else "false"


def next_run_id(base, now):
    day = now.strftime("%Y%m%d")
    highest = 0
    if base.exists():
        for path in base.glob("*/*/results.tsv"):
            try:
                text = path.read_text(encoding="utf-8-sig")
            except OSError:
                continue
            for line in text.splitlines():
                token = line.split("\t", 1)[0]
                prefix = f"RUN-{day}-"
                if token.startswith(prefix):
                    try:
                        highest = max(highest, int(token[len(prefix):]))
                    except ValueError:
                        continue
    return f"RUN-{day}-{highest + 1:03d}"


def blank_row(run_id, now, commit, dirty):
    row = {key: "" for key in FIELDS}
    row.update(
        RUN_ID=run_id,
        timestamp=now.isoformat(timespec="seconds"),
        git_commit=commit,
        dirty=dirty,
        function="UNKNOWN",
        line="UNKNOWN",
        files="UNKNOWN",
        ISSUE_ID="",
        RISK_ID="",
        evidence="",
    )
    return row


def _one_line(value):
    return " ".join(str(value).split())


def append_record(base, row, detail):
    if row["status"] not in STATUSES:
        raise ValueError(f"bad status {row['status']}")
    folder = base / row["test_type"] / row["timestamp"][:10]
    folder.mkdir(parents=True, exist_ok=True)
    for name in ("pass", "fail", "risk"):
        path = folder / f"{name}.md"
        if not path.exists():
            path.write_text(f"# {name.upper()}\n", encoding="utf-8")
    safe = {key: _one_line(row.get(key, "")) for key in FIELDS}
    table = folder / "results.tsv"
    fresh = not table.exists()
    with table.open("a", encoding="utf-8-sig" if fresh else "utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        if fresh:
            writer.writeheader()
        writer.writerow(safe)
    sections = []
    if row["status"] == "PASS":
        sections.append("pass")
    else:
        sections.append("fail")
    if row["RISK_ID"] or detail.startswith("RISK"):
        sections.append("risk")
    block = "\n".join(f"- {key}: {safe[key]}" for key in FIELDS)
    body = f"\n## {safe['RUN_ID']} / {safe['TC_ID']}\n{block}\n\n{detail.strip()}\n"
    for name in sections:
        with (folder / f"{name}.md").open("a", encoding="utf-8") as stream:
            stream.write(body)
    return folder


def write_pointer(base, payload):
    path = base / "last-run.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    import json
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path

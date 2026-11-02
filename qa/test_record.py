#!/usr/bin/env python3
"""Prove two RUN_IDs append on the same day and do not overwrite history."""
import json
import tempfile
from pathlib import Path

from record import append_record, blank_row, next_run_id, seoul_now


def main():
    now = seoul_now()
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        first = next_run_id(base, now)
        second_clock = now.replace(microsecond=0)
        row1 = blank_row(first, second_clock, "abc", "false")
        row1.update(
            TC_ID="QA-REC-001", feature="기록 누적", test_type="unit",
            tool_a="probe", command_a="test_record.py", result_a="PASS",
            tool_b="probe", command_b="test_record.py", result_b="PASS",
            status="PASS", files="qa/record.py", function="append_record", line="1",
            evidence="first run must remain",
        )
        append_record(base, row1, "검증 목적: 첫 실행 행이 남는지 확인한다.\n기대: 행 1개. 실제: 기록함.")
        second = next_run_id(base, now)
        row2 = blank_row(second, second_clock, "abc", "false")
        row2.update(
            TC_ID="QA-REC-002", feature="기록 누적", test_type="unit",
            tool_a="probe", command_a="test_record.py", result_a="FAIL",
            tool_b="probe", command_b="test_record.py", result_b="FAIL",
            status="FAIL", files="qa/record.py", function="append_record", line="1",
            evidence="second run appended",
        )
        append_record(base, row2, "입력: 두 번째 RUN_ID.\n기대: 첫 행 유지. 실제: 아래에 추가.")
        folder = base / "unit" / now.strftime("%Y-%m-%d")
        text = (folder / "results.tsv").read_text(encoding="utf-8-sig")
        if not text.startswith("\ufeff") and not (folder / "results.tsv").read_bytes().startswith(b"\xef\xbb\xbf"):
            raise SystemExit("TSV BOM missing")
        lines = text.splitlines()
        if len(lines) != 3:
            raise SystemExit(f"expected header+2 rows, got {len(lines)}")
        if first not in lines[1] or second not in lines[2]:
            raise SystemExit("RUN_ID order was overwritten")
        if "first run must remain" not in lines[1]:
            raise SystemExit("first evidence overwritten")
        if first == second:
            raise SystemExit("RUN_ID did not increase")
        for name in ("pass.md", "fail.md", "risk.md"):
            if not (folder / name).exists():
                raise SystemExit(f"missing {name}")
        if "QA-REC-001" not in (folder / "pass.md").read_text(encoding="utf-8"):
            raise SystemExit("pass.md missing first case")
        if "QA-REC-002" not in (folder / "fail.md").read_text(encoding="utf-8"):
            raise SystemExit("fail.md missing second case")
        pointer = {"run_id": second, "ok": True}
        (base / "last-run.json").write_text(json.dumps(pointer), encoding="utf-8")
    print("QA-REC-001 PASS")
    print("QA-REC-002 PASS")
    print("record append proof PASS")


if __name__ == "__main__":
    main()

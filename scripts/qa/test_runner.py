#!/usr/bin/env python3
"""Regression checks for QA V3.0 record contract."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "qa"))

from record import (  # noqa: E402
    AREAS,
    DATE_FILES,
    append_record,
    blank_row,
    seoul_now,
)


class RecordContractTests(unittest.TestCase):
    def test_four_areas_fixed(self):
        self.assertEqual(
            AREAS,
            (
                "01_unit_integration",
                "02_web_api",
                "03_security_quality",
                "04_infra_deploy",
            ),
        )

    def test_date_folder_five_files_results_tsv(self):
        now = seoul_now()
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            (base / "results").mkdir()
            (base / "history").mkdir()
            row = blank_row("RUN-1", now, now, "abc", "false")
            row.update(
                TC_ID="TC-UNIT-DATA-001",
                FEATURE_ID="FEAT-DATA-ETL",
                area="01_unit_integration",
                section="data_etl",
                scenario="append proof",
                tool_a="pytest",
                command_a="pytest",
                result_a="PASS",
                actual_a="ok",
                tool_b="unittest",
                command_b="unittest",
                result_b="PASS",
                actual_b="ok",
                status="PASS",
                code_file="qa/record.py",
                function="append_record",
                line="1",
                evidence="e1",
            )
            folder = append_record(base, row, "첫 실행")
            for name in DATE_FILES:
                self.assertTrue((folder / name).exists(), name)
            self.assertTrue((folder / "results.tsv").read_text(encoding="utf-8-sig").startswith("\ufeff") or (folder / "results.tsv").read_bytes().startswith(b"\xef\xbb\xbf"))
            self.assertIn("TC-UNIT-DATA-001", (folder / "pass.md").read_text(encoding="utf-8"))
            self.assertTrue((base / "history" / "execution_log.tsv").exists())
            self.assertTrue((base / "master_test_sheet.xlsx").exists())

    def test_rejects_bad_area(self):
        now = seoul_now()
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            row = blank_row("RUN-1", now, now, "abc", "false")
            row.update(
                TC_ID="X",
                FEATURE_ID="X",
                area="bad",
                section="s",
                tool_a="a",
                command_a="a",
                result_a="PASS",
                tool_b="b",
                command_b="b",
                result_b="PASS",
                status="PASS",
            )
            with self.assertRaises(ValueError):
                append_record(base, row, "bad")


if __name__ == "__main__":
    unittest.main()

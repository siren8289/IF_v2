from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
  from data.ingestion.collectors.external_public import SourceConfig

def build_dq_results(raw_count: int, accepted: list[dict[str, Any]], rejected: list[dict[str, Any]], config: SourceConfig) -> list[dict[str, str]]:
  results: list[dict[str, str]] = []

  def add(check_name: str, passed: bool, actual: str, expected: str = "pass", message: str = "") -> None:
    results.append(
      {
        "check_name": check_name,
        "status": "PASS" if passed else "FAIL",
        "expected_value": expected,
        "actual_value": actual,
        "message": message,
      }
    )

  add(
    "row_count_reconciliation",
    raw_count == len(accepted) + len(rejected),
    f"raw={raw_count}, accepted={len(accepted)}, rejected={len(rejected)}",
  )
  add("required_identifier_not_null", len(rejected) == 0, f"rejected={len(rejected)}")

  keys = [str(row["source_key"]) for row in accepted]
  add("source_natural_key_duplicate_zero", len(keys) == len(set(keys)), f"accepted={len(keys)}, distinct={len(set(keys))}")

  if config.target == "elderly_employment_snapshot":
    grains = [
      (row.get("reference_period"), row.get("region_code"), row.get("age_group"), row.get("metric"))
      for row in accepted
    ]
    add("kosis_grain_duplicate_zero", len(grains) == len(set(grains)), f"accepted={len(grains)}, distinct={len(set(grains))}")

  return results



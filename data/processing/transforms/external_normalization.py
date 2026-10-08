from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
  from data.ingestion.collectors.external_public import SourceConfig

import hashlib
import json

def stable_json(value: Any) -> str:
  return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
  return hashlib.sha256(value.encode("utf-8")).hexdigest()


def pick(row: dict[str, Any], candidates: list[str]) -> Any:
  for key in candidates:
    if key in row and row[key] not in (None, ""):
      return row[key]
  return None


def normalize_value(field: str, value: Any) -> Any:
  if value in ("", None):
    return None
  if field in {"recruitment_count", "business_year", "injured_count", "death_count"}:
    try:
      return int(str(value).replace(",", "").strip())
    except ValueError:
      return None
  if field in {"metric_value", "budget_amount", "accident_rate", "accident_risk_score"}:
    try:
      return float(str(value).replace(",", "").strip())
    except ValueError:
      return None
  if field in {"posting_start_date", "posting_end_date"}:
    raw = str(value).strip().replace(".", "").replace("-", "")
    if len(raw) == 8 and raw.isdigit():
      return f"{raw[0:4]}-{raw[4:6]}-{raw[6:8]}"
  return str(value).strip()


def normalize_rows(rows: list[dict[str, Any]], config: SourceConfig, collected_at: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
  accepted: list[dict[str, Any]] = []
  rejected: list[dict[str, Any]] = []
  seen: set[str] = set()

  for index, row in enumerate(rows):
    normalized: dict[str, Any] = {}
    for target_field, candidates in config.field_map.items():
      normalized[target_field] = normalize_value(target_field, pick(row, candidates))

    if not normalized.get("source_key"):
      normalized["source_key"] = sha256_text(stable_json(row))

    missing = [field for field in config.required_fields if not normalized.get(field)]
    if missing:
      rejected.append({"row_index": index, "reason": f"missing required fields: {','.join(missing)}", "payload": row})
      continue

    natural_key = f"{config.source_name}:{normalized['source_key']}"
    if natural_key in seen:
      rejected.append({"row_index": index, "reason": "duplicate source natural key in batch", "payload": row})
      continue
    seen.add(natural_key)

    normalized.update(
      {
        "source_name": config.source_name,
        "source_url": config.source_url,
        "source_updated_at": None,
        "collected_at": collected_at,
        "schema_version": config.schema_version,
        "checksum": sha256_text(stable_json(row)),
      }
    )
    accepted.append(normalized)

  return accepted, rejected



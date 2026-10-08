"""
External public data ingestion for IF DE.

Pipeline:
  extract -> raw immutable snapshot -> schema check -> normalize -> deduplicate
  -> DQ gate -> serving parquet -> lineage/manifest

Public datasets are Reference/Context only. This script writes under
data/ingestion/snapshots/external and does not touch Applicant/Assessment runtime tables.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from data.ingestion.clients.public_api import read_input_file, fetch_url
from data.processing.parsers.external_payload import parse_payload, parse_xml_items
from data.processing.transforms.external_normalization import (
  stable_json, sha256_text, pick,
  normalize_value, normalize_rows,
)
from data.quality.external_validation import build_dq_results


# 수집 산출물은 소스 카탈로그와 함께 ingestion 아래에 보관한다.
DEFAULT_EXTERNAL_DIR = Path(__file__).resolve().parents[1] / "snapshots" / "external"
CATALOG_PATH = Path(__file__).resolve().parents[1] / "external_sources.json"


@dataclass(frozen=True)
class SourceConfig:
  key: str
  source_name: str
  source_url: str
  source_type: str
  target: str
  schema_version: str
  required_fields: list[str]
  field_map: dict[str, list[str]]


def utc_now() -> str:
  return datetime.now(timezone.utc).isoformat()


def load_catalog(path: Path = CATALOG_PATH) -> dict[str, SourceConfig]:
  raw = json.loads(path.read_text(encoding="utf-8"))
  return {
    key: SourceConfig(
      key=key,
      source_name=value["source_name"],
      source_url=value["source_url"],
      source_type=value["source_type"],
      target=value["target"],
      schema_version=value["schema_version"],
      required_fields=value.get("required_fields", []),
      field_map=value.get("field_map", {}),
    )
    for key, value in raw.items()
  }


def external_dir() -> Path:
  return Path(os.environ.get("IF_EXTERNAL_DATA_DIR", DEFAULT_EXTERNAL_DIR))


def ensure_dirs(base_dir: Path) -> None:
  for name in ("raw", "validated", "serving", "manifests", "lineage"):
    (base_dir / name).mkdir(parents=True, exist_ok=True)


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
  with path.open("w", encoding="utf-8") as handle:
    for row in rows:
      handle.write(stable_json(row) + "\n")


def run_ingestion(config: SourceConfig, payload: bytes, idempotency_key: str, input_name: str | None = None) -> dict[str, Any]:
  base_dir = external_dir()
  ensure_dirs(base_dir)
  collected_at = utc_now()
  payload_checksum = hashlib.sha256(payload).hexdigest()
  run_key = sha256_text(f"{config.key}:{config.schema_version}:{idempotency_key}:{payload_checksum}")[:24]

  rows = parse_payload(payload, config.source_type, input_name)
  manifest_path = base_dir / "manifests" / f"{config.key}_{run_key}.json"
  raw_path = base_dir / "raw" / f"{config.key}_{run_key}.jsonl"
  accepted_path = base_dir / "validated" / f"{config.key}_{run_key}_accepted.jsonl"
  rejected_path = base_dir / "validated" / f"{config.key}_{run_key}_rejected.jsonl"
  dq_path = base_dir / "validated" / f"{config.key}_{run_key}_dq.json"
  lineage_path = base_dir / "lineage" / f"{config.key}_{run_key}.json"
  serving_path = base_dir / "serving" / f"{config.target}.parquet"

  accepted, rejected = normalize_rows(rows, config, collected_at)
  dq_results = build_dq_results(len(rows), accepted, rejected, config)
  dq_passed = all(result["status"] == "PASS" for result in dq_results)

  raw_records = [
    {
      "source_name": config.source_name,
      "source_url": config.source_url,
      "source_key": row.get("source_key") or sha256_text(stable_json(row)),
      "source_updated_at": None,
      "collected_at": collected_at,
      "schema_version": config.schema_version,
      "payload": row,
      "checksum": sha256_text(stable_json(row)),
    }
    for row in rows
  ]
  write_jsonl(raw_path, raw_records)
  write_jsonl(accepted_path, accepted)
  write_jsonl(rejected_path, rejected)
  dq_path.write_text(json.dumps(dq_results, ensure_ascii=False, indent=2), encoding="utf-8")

  status = "SUCCESS" if dq_passed else "DQ_FAILED"
  if dq_passed:
    new_df = pd.DataFrame(accepted)
    if serving_path.exists():
      old_df = pd.read_parquet(serving_path)
      combined = pd.concat([old_df, new_df], ignore_index=True)
    else:
      combined = new_df
    if not combined.empty:
      combined = combined.drop_duplicates(subset=["source_name", "source_key"], keep="last")
    combined.to_parquet(serving_path, index=False)

  lineage = {
    "source_name": config.source_name,
    "source_url": config.source_url,
    "idempotency_key": idempotency_key,
    "run_key": run_key,
    "events": [
      {"from_layer": "source", "to_layer": "raw_external_snapshot", "target": str(raw_path), "row_count": len(rows)},
      {"from_layer": "raw_external_snapshot", "to_layer": "validated_normalized", "target": str(accepted_path), "row_count": len(accepted)},
      {"from_layer": "validated_normalized", "to_layer": "serving", "target": str(serving_path), "row_count": len(accepted) if dq_passed else 0},
    ],
  }
  lineage_path.write_text(json.dumps(lineage, ensure_ascii=False, indent=2), encoding="utf-8")

  manifest = {
    "source_key": config.key,
    "source_name": config.source_name,
    "source_url": config.source_url,
    "target": config.target,
    "schema_version": config.schema_version,
    "idempotency_key": idempotency_key,
    "run_key": run_key,
    "payload_checksum": payload_checksum,
    "status": status,
    "started_at": collected_at,
    "finished_at": utc_now(),
    "raw_row_count": len(rows),
    "accepted_row_count": len(accepted),
    "rejected_row_count": len(rejected),
    "raw_path": str(raw_path),
    "accepted_path": str(accepted_path),
    "rejected_path": str(rejected_path),
    "dq_path": str(dq_path),
    "lineage_path": str(lineage_path),
    "serving_path": str(serving_path) if dq_passed else None,
  }
  manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
  return manifest


def main() -> None:
  parser = argparse.ArgumentParser(description="Ingest IF external public Reference/Context data")
  parser.add_argument("--source", required=True, help="source key from external_sources.json")
  parser.add_argument("--input-file", help="local XML/JSON/CSV file to ingest")
  parser.add_argument("--url", help="direct API/file URL. Use a concrete endpoint URL, not the data.go.kr catalog page.")
  parser.add_argument("--idempotency-key", required=True, help="collection window key, e.g. 2026-08 or 2026-08-23T00")
  args = parser.parse_args()

  catalog = load_catalog()
  if args.source not in catalog:
    raise SystemExit(f"unknown source: {args.source}. available={', '.join(sorted(catalog))}")
  if bool(args.input_file) == bool(args.url):
    raise SystemExit("provide exactly one of --input-file or --url")

  payload = read_input_file(Path(args.input_file)) if args.input_file else fetch_url(args.url)
  manifest = run_ingestion(
    config=catalog[args.source],
    payload=payload,
    idempotency_key=args.idempotency_key,
    input_name=args.input_file or args.url,
  )
  print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
  main()

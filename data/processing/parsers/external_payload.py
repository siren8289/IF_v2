from __future__ import annotations

import csv
import json
import xml.etree.ElementTree as ET
from typing import Any

def parse_payload(payload: bytes, source_type: str, input_name: str | None = None) -> list[dict[str, Any]]:
  name = (input_name or "").lower()
  text = payload.decode("utf-8-sig", errors="replace")

  if source_type in {"OPENAPI_XML"} or name.endswith(".xml"):
    return parse_xml_items(text)
  if source_type in {"OPENAPI_JSON", "KOSIS"} or name.endswith(".json"):
    parsed = json.loads(text)
    if isinstance(parsed, list):
      return [dict(item) for item in parsed if isinstance(item, dict)]
    if isinstance(parsed, dict):
      rows = parsed.get("data") or parsed.get("items") or parsed.get("item")
      if isinstance(rows, list):
        return [dict(item) for item in rows if isinstance(item, dict)]
      return [parsed]
  if source_type.startswith("FILE_") or name.endswith(".csv"):
    return list(csv.DictReader(text.splitlines()))

  raise ValueError(f"unsupported source type/input: {source_type} {input_name or ''}")


def parse_xml_items(text: str) -> list[dict[str, Any]]:
  root = ET.fromstring(text)
  candidates = root.findall(".//item")
  if not candidates:
    candidates = root.findall(".//row")
  if not candidates:
    candidates = [child for child in root if len(child)]
  rows: list[dict[str, Any]] = []
  for item in candidates:
    row: dict[str, Any] = {}
    for child in list(item):
      tag = child.tag.split("}", 1)[-1]
      row[tag] = (child.text or "").strip()
    if row:
      rows.append(row)
  return rows



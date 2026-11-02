#!/usr/bin/env python3
"""Deployment/CI gate simulation checks for QA-CONFIG Tool B."""
from __future__ import annotations

import json
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]


def evaluate_deploy_gate(api_payload: dict) -> tuple[bool, str]:
    """Simulate the deploy gate that requires a successful CI check on the same SHA."""
    if "message" in api_payload and api_payload.get("message") == "Not Found":
        return False, "github api not found"
    state = str(api_payload.get("state", "")).lower()
    sha = api_payload.get("sha") or api_payload.get("head_sha")
    if not sha:
        return False, "missing sha"
    if state != "success":
        return False, f"ci state={state or 'unknown'}"
    return True, "ok"


class DeployGateTests(unittest.TestCase):
    def test_workflow_files_exist(self):
        self.assertTrue((ROOT / ".github/workflows/githubactions.yml").is_file())
        self.assertTrue((ROOT / ".github/workflows/deploy.yml").is_file())

    def test_api_not_found_blocks_deploy(self):
        ok, reason = evaluate_deploy_gate({"message": "Not Found"})
        self.assertFalse(ok)
        self.assertIn("not found", reason)

    def test_failed_ci_blocks_deploy(self):
        ok, reason = evaluate_deploy_gate({"state": "failure", "sha": "abc123"})
        self.assertFalse(ok)
        self.assertIn("failure", reason)

    def test_success_allows_deploy(self):
        ok, reason = evaluate_deploy_gate({"state": "success", "sha": "abc123"})
        self.assertTrue(ok)
        self.assertEqual(reason, "ok")

    def test_missing_sha_blocks(self):
        ok, _ = evaluate_deploy_gate({"state": "success"})
        self.assertFalse(ok)

    def test_json_roundtrip_fixture(self):
        payload = {"state": "success", "sha": "deadbeef"}
        loaded = json.loads(json.dumps(payload))
        with mock.patch("builtins.open", mock.mock_open(read_data=json.dumps(payload))):
            ok, _ = evaluate_deploy_gate(loaded)
        self.assertTrue(ok)


if __name__ == "__main__":
    unittest.main()

import json
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def documents(path):
    return [item for item in yaml.safe_load_all(path.read_text(encoding="utf-8")) if item]


class ManifestTests(unittest.TestCase):
    def test_each_deployment_has_probes_resources_and_secret_refs(self):
        deployments = []
        for path in (ROOT / "infra/k8s").glob("*.yaml"):
            for doc in documents(path):
                if doc.get("kind") == "Deployment":
                    deployments.append(doc)
        self.assertEqual(
            sorted(item["metadata"]["name"] for item in deployments),
            ["fastapi", "frontend", "postgres", "spring"],
        )
        for deployment in deployments:
            container = deployment["spec"]["template"]["spec"]["containers"][0]
            self.assertIn("readinessProbe", container)
            self.assertIn("livenessProbe", container)
            self.assertIn("requests", container["resources"])
            self.assertIn("limits", container["resources"])
            text = yaml.safe_dump(container)
            self.assertNotIn("local-dev-placeholder", text)
            self.assertNotIn("IF_DB_PASSWORD", text)

    def test_secret_is_only_a_local_placeholder(self):
        secret = documents(ROOT / "infra/k8s/secret.yaml")[0]
        self.assertEqual(secret["stringData"]["POSTGRES_PASSWORD"], "local-dev-placeholder")
        self.assertEqual(secret["stringData"]["SPRING_DATASOURCE_PASSWORD"], "local-dev-placeholder")
        self.assertEqual(secret["stringData"]["GEMINI_API_KEY"], "")

    def test_alerts_cover_cpu_memory_errors_and_latency(self):
        names = []
        for group in documents(ROOT / "infra/monitoring/alerts.yml"):
            names.extend(rule["alert"] for rule in group["groups"][0]["rules"])
        self.assertEqual(names, ["HostCpuHigh", "HostMemoryHigh", "HttpProbeFailing", "HttpLatencyHigh"])

    def test_default_terraform_does_not_create_resources(self):
        text = (ROOT / "infra/terraform/variables.tf").read_text(encoding="utf-8")
        self.assertIn('variable "enable_iam"', text)
        self.assertIn('variable "manage_ec2"', text)
        self.assertEqual(text.count("default     = false"), 2)
        local = (ROOT / "infra/terraform/environments/local.tfvars").read_text(encoding="utf-8")
        self.assertRegex(local, r"enable_iam\s+=\s+false")
        self.assertRegex(local, r"manage_ec2\s+=\s+false")

    def test_deploy_workflow_uses_oidc_without_static_keys(self):
        text = (ROOT / ".github/workflows/deploy.yml").read_text(encoding="utf-8")
        self.assertIn("id-token: write", text)
        self.assertIn("role-to-assume:", text)
        self.assertNotIn("AWS_ACCESS_KEY", text)
        self.assertNotIn("AWS_SECRET_ACCESS_KEY", text)
        ci = (ROOT / ".github/workflows/githubactions.yml").read_text(encoding="utf-8")
        self.assertNotIn("terraform apply", ci)

    def test_k6_script_and_fault_script_exist(self):
        smoke = (ROOT / "infra/perf/smoke.js").read_text(encoding="utf-8")
        self.assertIn("http_req_failed", smoke)
        self.assertIn("http_req_duration", smoke)
        fault = (ROOT / "infra/fault/inject.sh").read_text(encoding="utf-8")
        self.assertIn("trap restore", fault)
        self.assertNotIn("if-app-stack-postgres-1", fault)
        json.loads((ROOT / "infra/monitoring/grafana-dashboard.json").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

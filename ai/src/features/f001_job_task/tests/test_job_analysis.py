
import importlib

import pytest
from fastapi.testclient import TestClient

from src.api.main import app
from src.features.f001_job_task.service import JobAnalysisError

client = TestClient(app)
routes_module = importlib.import_module("src.api.routes")

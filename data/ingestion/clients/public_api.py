from __future__ import annotations

import time
import urllib.error
import urllib.request
from pathlib import Path

def read_input_file(path: Path) -> bytes:
  return path.read_bytes()


def fetch_url(url: str, retries: int = 3, timeout: int = 30) -> bytes:
  last_error: Exception | None = None
  for attempt in range(retries):
    try:
      request = urllib.request.Request(url, headers={"User-Agent": "IF-DE/1.0"})
      with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()
    except (urllib.error.URLError, TimeoutError) as exc:
      last_error = exc
      if attempt < retries - 1:
        time.sleep(2 ** attempt)
  raise RuntimeError(f"fetch failed after {retries} attempts: {last_error}")



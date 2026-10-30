#!/usr/bin/env python3
"""로컬 스택의 읽기 요청만 측정한다. 평가를 새로 만들지 않는다."""
import json
import statistics
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

TARGETS = {
    "spring_jobs": "http://127.0.0.1:8080/api/jobs",
    "fastapi_health": "http://127.0.0.1:8000/health",
    "frontend": "http://127.0.0.1/",
}
REQUESTS = 30
WORKERS = 5


def once(url):
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            response.read()
            code = response.status
    except urllib.error.HTTPError as exc:
        return (time.perf_counter() - started) * 1000, exc.code
    except Exception:
        return (time.perf_counter() - started) * 1000, 0
    return (time.perf_counter() - started) * 1000, code


def percentile(values, pct):
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round((pct / 100) * (len(ordered) - 1)))))
    return ordered[index]


def measure(url):
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        samples = list(pool.map(lambda _n: once(url), range(REQUESTS)))
    elapsed = time.perf_counter() - started
    times = [item[0] for item in samples]
    errors = sum(1 for item in samples if item[1] != 200)
    return {
        "requests": REQUESTS,
        "workers": WORKERS,
        "errors": errors,
        "error_rate": errors / REQUESTS,
        "rps": REQUESTS / elapsed,
        "p50_ms": round(percentile(times, 50), 2),
        "p95_ms": round(percentile(times, 95), 2),
        "max_ms": round(max(times), 2),
        "mean_ms": round(statistics.fmean(times), 2),
    }


def main():
    report = {name: measure(url) for name, url in TARGETS.items()}
    text = json.dumps(report, indent=2)
    print(text)
    out = Path("docs/evidence/performance.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

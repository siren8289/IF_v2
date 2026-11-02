# [PERFORMANCE] PASS 테스트 기록 (2026-10-30)

> **경로**: `qa/reports/performance/2026-10-30/pass.md`  
> **기준 시간대**: `Asia/Seoul` (KST)  
> **원칙**: 최소 2개 도구(Tool A / Tool B) 교차 검증을 모두 통과(`PASS`)한 테스트 케이스만 기록합니다.

---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:33:10 KST)

- **통과 건수**: 1건 / 전체 2건

| RUN_ID | TC_ID | 실행 일시 (KST) | 기능명 | 도구 A (결과) | 도구 B (결과) | 최종 상태 | Git Commit | 대상 파일 | 함수명 | 줄 번호 | 관련 ID | 검증 목적 및 근거 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `RUN-20261030-001` | `PERF-002` | 2026-10-30 17:33:06 KST | FastAPI ML(scikit-learn) + DL(PyTorch CNN) 위험도 추론 응답 지연(< 1000ms) 검증 | `curl -w '%{time_total}' AI Inference Probe` (PASS (HTTP 200, 923.9ms)) | `Python perf_counter AI Latency Verifier` (PASS (HTTP 200, 418.4ms)) | **PASS** | `9491fb1b` | `ai/src/main.py` | `analyze` | `50-81` | `-` | **목적**: ML 및 DL 모델 추론과 점수 계산이 1초(1000ms) 이내에 완료되는지 검증<br>**기대**: HTTP 200 및 응답 시간 < 1000ms<br>**실제/근거**: Tool A: 923.9ms, Tool B: 418.4ms (POST http://127.0.0.1:8000/api/v1/risk/analyze) |


# [PERFORMANCE] FAIL 및 미통과 상세 기록 (2026-10-30)

> **경로**: `qa/reports/performance/2026-10-30/fail.md`  
> **기준 시간대**: `Asia/Seoul` (KST)  
> **원칙**: 코드 수정 전 반드시 본 문서에 먼저 기록하고 사용자에게 보고합니다. 도구 하나라도 실패 시 완료 처리하지 않습니다.

---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:33:10 KST)

- **실패/미통과 건수**: 1건 / 전체 2건

### [PERF-001] Spring 대시보드 목록 API(GET /api/assessments) 단건 및 10건 동시 부하 응답 지연 검증 (`FAIL`) — `-`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:33:06 KST`
- **테스트 종류**: `performance`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl -w '%{time_total}' Latency Probe` → **FAIL (2294.8ms)**
- **도구 B 및 결과**: `Python ThreadPoolExecutor (10 Concurrent Requests)` → **PASS (10/10 HTTP 200, P95=317.3ms, max=317.3ms)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/controller/AssessmentController.java` / 함수 `list` / 줄 번호 `41-46`
- **입력값 (Input)**: `대시보드 목록 조회 시 단일 응답 및 10명 동시 접속 상황에서 500ms 이내에 오류 없이 응답하는지 검증`
- **오류 메시지 / 응답**: `curl=2294.8ms, 10건 동시 P95=317.3ms, 성공률 100%`
- **예상 결과 (Expected)**: 단일 및 10건 동시 요청 모두 HTTP 200, P95 < 500ms
- **실제 결과 (Actual)**: curl=2294.8ms, 10건 동시 P95=317.3ms, 성공률 100%
- **재현 방법 (Reproduction)**:
  ```zsh
  GET /api/assessments?page=0&size=20
  ```
- **원인 분석 (Root Cause)**: 
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)


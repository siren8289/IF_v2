# 테스트 및 교차 검증 실행 로그 (`docs/TEST_LOG.md`)

## [2026-10-30] 바이브 코딩 QA·Security 자동화 지침 V2.5 실행 및 교차 검증 결과

### 1. 실행 개요
- **실행 일자 (`Asia/Seoul`)**: `2026-10-30`
- **Git Commit**: `9491fb1b` (`9491fb1b8644049541e4933d83f7b6e8205a5d09`)
- **기록 경로**: `qa/reports/{test-type}/2026-10-30/` (`pass.md`, `fail.md`, `risk.md`, `results.tsv`)

---

### 2. 테스트 종류별 교차 검증(Tool A vs Tool B) 실행 요약

| 테스트 종류 (`test-type`) | 도구 A (Tool A) | 도구 B (Tool B) | 실행 결과 요약 | 리포트 경로 |
| :--- | :--- | :--- | :--- | :--- |
| **`unit`** | Vitest (`npm test`), Python `unittest`, Gradle JUnit | TypeScript (`tsc --noEmit`), `pytest`, JUnit XML 파서 | **PASS** (웹 Vitest 7건/TSC 통과, Data ETL 3건 통과, Spring JUnit 6건 통과, AI 경계값 통과) | [`qa/reports/unit/2026-10-30/`](file:///Users/jeong-yelim/orca/IF_v2/qa/reports/unit/2026-10-30/results.tsv) |
| **`api`** | `pytest` (`ai/tests`), `curl` CLI (`POST /api/assessments`, `/api/v1/risk/analyze`) | `Ruff` 정적 분석, Python HTTP Client + `psql` 4개 테이블 증감 검증기 | `QA-AI` **PASS**, 라이브 API 경계값 **PASS**, Jackson 타입 변환(`IF-0052, 0059, 0060, 0067, 0072, 0079`) 및 `text/plain` 500(`IF-0087`) **FAIL** 선기록 | [`qa/reports/api/2026-10-30/`](file:///Users/jeong-yelim/orca/IF_v2/qa/reports/api/2026-10-30/results.tsv) |
| **`integration`** | Gradle JUnit (`AssessmentControllerTest`, `AssessmentServiceTest`), Python HTTP Client | `javac` 컴파일 검증, `psql` DB 조인 및 FastAPI 직접 추론 대조 | `QA-SPRING` **PASS** (Controller 3건, Service 3건 통과), 삭제 시 고아 행 잔류(`LOG-016` / `RISK-INT-001`) 선기록 | [`qa/reports/integration/2026-10-30/`](file:///Users/jeong-yelim/orca/IF_v2/qa/reports/integration/2026-10-30/results.tsv) |
| **`e2e`** | `curl` Nginx(`:80`) SPA 라우팅·프록시 검사 | Python HTTP E2E Client + `AssessmentFormPage.tsx` 레이스 검사 | SPA 라우팅(`UI-026`) **PASS**, 연속 클릭 중복 제출(`UI-023` / `BUG-UI-023`) **FAIL** 선기록 | [`qa/reports/e2e/2026-10-30/`](file:///Users/jeong-yelim/orca/IF_v2/qa/reports/e2e/2026-10-30/results.tsv) |
| **`security`** | `Bandit` SAST, OWASP WSTG HTTP 프로브(`curl`) | `scripts/qa/security.py` 시크릿 스캔, Nginx 설정·`npm audit` 검사 | `QA-SECURITY` (Bandit + 시크릿 스캔), SQLi(`SEC-001`), CORS(`SEC-002`), `.env` 비노출(`SEC-003`) **PASS**; Nginx 보안 헤더 누락(`SEC-004`), `npm audit`(`SEC-005`) **FAIL** 및 `RISK` 선기록 | [`qa/reports/security/2026-10-30/`](file:///Users/jeong-yelim/orca/IF_v2/qa/reports/security/2026-10-30/results.tsv) |
| **`performance`** | `curl -w '%{time_total}'` 지연 계측기 | Python `ThreadPoolExecutor` 10건 동시 부하 검증기 | FastAPI 추론(`PERF-002`, < 1000ms) 및 10건 동시 조회(P95=317.3ms) **PASS**, 단건 콜드 호출 지연(`PERF-001`) 및 동기 타임아웃(`RISK-PERF-001`) 기록 | [`qa/reports/performance/2026-10-30/`](file:///Users/jeong-yelim/orca/IF_v2/qa/reports/performance/2026-10-30/results.tsv) |
| **`regression`** | `unittest` (`scripts/qa/test_*.py`), `actionlint` | `pytest` (`scripts/qa`), 배포 워크플로 시뮬레이션 | `QA-REGRESSION` 및 `QA-CONFIG` 교차 검증 **PASS** (실패 차단·누적 기록·UTF-8 BOM·한글·미실행 폴더 미생성 검증 완료) | [`qa/reports/regression/2026-10-30/`](file:///Users/jeong-yelim/orca/IF_v2/qa/reports/regression/2026-10-30/results.tsv) |

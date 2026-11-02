# 오류 및 결함 분석 로그 (`docs/ERROR_LOG.md`)

> **원칙**: 바이브 코딩 QA·Security 자동화 지침 V2.5 제5절에 따라, 발견된 모든 `FAIL` 및 `RISK`는 **기존 코드를 임의로 수정하기 전에 `qa/reports/{test-type}/{YYYY-MM-DD}/fail.md` 및 `risk.md`에 먼저 기록하고 사용자에게 보고**합니다.

---

## [2026-10-30] QA·Security V2.5 교차 검증으로 검출된 결함(`FAIL`) 목록

| 결함 ID | TC ID | 테스트 종류 | 오류 파일 / 함수 / 줄 번호 | 현상 및 원인 요약 | 상태 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `BUG-IF-0052` | `IF-0052` | `api` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` (`applicantName`, 15행) | JSON 숫자 `17` 전송 시 Jackson 기본 Coercion이 문자열 `"17"`로 암묵적 변환 후 HTTP 201로 저장됨 (기대: 400) | 선기록·보고 완료 (수정 승인 대기) |
| `BUG-IF-0059` | `IF-0059` | `api` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` (`age`, 16행) | 소수 `60.5` 전송 시 Jackson `ACCEPT_FLOAT_AS_INT`에 의해 정수 `60`으로 절삭 후 HTTP 201 저장됨 (기대: 400) | 선기록·보고 완료 (수정 승인 대기) |
| `BUG-IF-0060` | `IF-0060` | `api` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` (`age`, 16행) | 문자열 `"70"` 전송 시 정수 `70`으로 암묵적 변환 후 HTTP 201 저장됨 (기대: 400) | 선기록·보고 완료 (수정 승인 대기) |
| `BUG-IF-0067` | `IF-0067` | `api` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` (`physicalLevel`, 17행) | 문자열 `"3"` 전송 시 정수 `3`으로 암묵적 변환 후 HTTP 201 저장됨 (기대: 400) | 선기록·보고 완료 (수정 승인 대기) |
| `BUG-IF-0072` | `IF-0072` | `api` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` (`chronicDisease`, 18행) | 정수 `1` 전송 시 불리언 `true`로 암묵적 변환 후 HTTP 201 저장됨 (기대: 400) | 선기록·보고 완료 (수정 승인 대기) |
| `BUG-IF-0079` | `IF-0079` | `api` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` (`workHourLimit`, 19행) | 소수 `2.5` 전송 시 정수 `2`로 절삭 후 HTTP 201 저장됨 (기대: 400) | 선기록·보고 완료 (수정 승인 대기) |
| `BUG-IF-0087` | `IF-0087` | `api` | `spring/src/main/demo/global/exception/GlobalExceptionHandler.java` (`handleUnexpected`, 48-51행) | `Content-Type: text/plain` 전송 시 `HttpMediaTypeNotSupportedException` 전용 핸들러 부재로 HTTP 500 반환 (기대: 415/400) | 선기록·보고 완료 (수정 승인 대기) |
| `BUG-UI-023` | `UI-023` (`IF-0043`) | `e2e` | `web-vite/src/pages/AssessmentFormPage.tsx` (`handleSubmit`, 56-81행) | `setSubmitting(true)` 비동기 리렌더링 전 동일 이벤트 루프 내 연속 클릭(`click()`) 시 중복 `POST /api/assessments` 2건 발생 (`useRef` 동기 락 미적용) | 선기록·보고 완료 (수정 승인 대기) |
| `BUG-SEC-004` | `SEC-004` | `security` | `web-vite/nginx.conf` (`server`, 4-22행) | 응답 헤더에 `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY` 등 OWASP 필수 보안 헤더 누락 | 선기록·보고 완료 (수정 승인 대기) |
| `BUG-SEC-005` | `SEC-005` | `security` | `web-vite/package-lock.json` (`dependencies`, 1-50행) | `npm audit` 검사 결과 프론트엔드 하위 의존성에서 High 심각도 보안 취약점 1건 검출 | 선기록·보고 완료 (수정 승인 대기) |

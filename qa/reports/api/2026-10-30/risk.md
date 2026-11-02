# RISK
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:26 KST)

- **검출/추적 리스크 건수**: 2건

### [RISK-API-001] Jackson 기본 Coercion 허용으로 인한 비엄격 JSON 타입 수용 및 소수점 절삭 저장 위험 (심각도: **HIGH**, 상태: **OPEN**)

- **RUN_ID**: `RUN-20261030-001`
- **관련 TC_ID**: `IF-0052, IF-0059, IF-0060, IF-0067, IF-0072, IF-0079`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **기능명 / 테스트 종류**: Spring Jackson JSON 역직렬화 암묵적 타입 변환(Type Coercion) (`api`)
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI` → 6개 타입 불일치 케이스 모두 HTTP 201 반환 확인
- **도구 B 및 결과**: `Python HTTP Client + psql DB Inspector` → DB에 절삭/변형된 값(age 60.5->60, workHourLimit 2.5->2 등) 실제 적재 확인
- **대상 코드 위치**: 파일 `spring/src/main/demo/global/config/AppConfig.java` / 함수 `AppConfig / AssessmentCreateRequest` / 줄 번호 `15-25`
- **심각도 (Severity)**: **HIGH**
- **발생 가능성 (Likelihood)**: **HIGH**
- **영향 (Impact)**: 클라이언트가 잘못된 타입(소수 나이/근무시간, 숫자 이름, 숫자 불리언, 문자열 숫자)을 전송해도 400 오류 없이 데이터가 절삭·변형되어 DB에 저장됨 (데이터 무결성 훼손)
- **상세 내용**: Spring Boot 기본 ObjectMapper가 ACCEPT_FLOAT_AS_INT 및 Scalar Coercion을 허용하여 @Valid 실행 전에 타입이 강제 변환됨.
- **권장 조치 (Recommendation)**: Jackson2ObjectMapperBuilderCustomizer를 통해 DeserializationFeature.ACCEPT_FLOAT_AS_INT 비활성화 및 CoercionConfig(CoercionInputShape, CoercionAction.Fail) 설정 권장
- **처리 상태 (Status)**: `OPEN`
- **보고 이력 (Report History)**: 2026-10-30 17:31:03 KST (RUN-20261030-001) fail.md 및 risk.md 선기록 완료 (코드 수정 전 사용자 승인 대기)

### [RISK-API-002] HttpMediaTypeNotSupportedException 미분리로 인한 500 오응답 위험 (심각도: **MEDIUM**, 상태: **OPEN**)

- **RUN_ID**: `RUN-20261030-001`
- **관련 TC_ID**: `IF-0087`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **기능명 / 테스트 종류**: Spring GlobalExceptionHandler 미디어 타입/메서드 예외 매핑 누락 (`api`)
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (-H 'Content-Type: text/plain')` → HTTP 500 INTERNAL_ERROR 수신
- **도구 B 및 결과**: `Python HTTP Client` → HTTP 500 INTERNAL_ERROR 수신
- **대상 코드 위치**: 파일 `spring/src/main/demo/global/exception/GlobalExceptionHandler.java` / 함수 `handleUnexpected` / 줄 번호 `48-51`
- **심각도 (Severity)**: **MEDIUM**
- **발생 가능성 (Likelihood)**: **MEDIUM**
- **영향 (Impact)**: 클라이언트 과실인 Content-Type 오류(text/plain)나 허용되지 않은 HTTP 메서드 요청이 서버 장애(HTTP 500 INTERNAL_ERROR)로 응답 및 에러 로그에 기록됨
- **상세 내용**: GlobalExceptionHandler에 HttpMediaTypeNotSupportedException 핸들러가 없어 Exception.class(handleUnexpected)가 포착하여 500을 반환함.
- **권장 조치 (Recommendation)**: GlobalExceptionHandler에 HttpMediaTypeNotSupportedException(415 또는 400) 및 HttpRequestMethodNotSupportedException(405) 전용 @ExceptionHandler 추가 권장
- **처리 상태 (Status)**: `OPEN`
- **보고 이력 (Report History)**: 2026-10-30 17:31:03 KST (RUN-20261030-001) fail.md 및 risk.md 선기록 완료


# FAIL

## 20261030T172455-160ef4c9a6 / QA-AI
- RUN_ID: 20261030T172455-160ef4c9a6
- TC_ID: QA-AI
- timestamp: 2026-10-30T17:24:55.062349+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q"]
- result_a: FAIL
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T172455-160ef4c9a6/QA-AI-a.log sha256=96ebfdc014a2887f23d948213e8b87e2235d211710c44780cef41f3663769ceb; qa/.runtime/evidence/api/2026-10-30/20261030T172455-160ef4c9a6/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

### QA-AI / 20261030T172455-160ef4c9a6 원인 분석
- 입력/재현: qa/suites.json QA-AI의 pytest 명령, torch 설치 전 로컬 .venv.
- 기대: 기존 API/RAG TC 수집·실행. 실제: 수집 중 ModuleNotFoundError: No module named 'torch'.
- 위치: ai/src/dl_model.py, 모듈 import, 11행; ai/tests/test_risk_score.py, 모듈 import, 5행.
- 원인: 런타임 추가 의존성이 준비되기 전에 최초 검사 시작. 수정: 로컬 .venv에 torch 설치 완료; CI와 qa-policy.md에도 명시.
- ISSUE_ID: QA-SETUP-001. 재검증: 다음 전체 실행 RUN_ID와 연결; 이전 실패 보존.
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:26 KST)

- **실패/미통과 건수**: 8건 / 전체 22건

### [IF-0050] 이름(applicantName) 최대 경계값(50자) 정상 등록(201) 검증 (`FAIL`) — `-`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **테스트 종류**: `api`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (POST /api/assessments)` → **FAIL (HTTP 502)**
- **도구 B 및 결과**: `Python urllib + psql 4-Table Delta Verifier` → **FAIL (HTTP 201, assessment_delta=+2)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` / 함수 `AssessmentCreateRequest` / 줄 번호 `15`
- **입력값 (Input)**: `{"applicantName": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "age": 70, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}`
- **오류 메시지 / 응답**: `{"id":87}`
- **예상 결과 (Expected)**: HTTP 201 및 DB 증감 +1
- **실제 결과 (Actual)**: Tool A: HTTP 502 ({"success":false,"data":null,"message":"AI 서버 호출에 실패했습니다.","errorCode":"AI_ERROR), Tool B: HTTP 201, DB assessment 증감=+2
- **재현 방법 (Reproduction)**:
  ```zsh
  curl -i -X POST http://127.0.0.1:8080/api/assessments -H 'Content-Type: application/json' --data-raw '{"applicantName": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "age": 70, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}'
  ```
- **원인 분석 (Root Cause)**: 
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)

### [IF-0052] 이름(applicantName)에 JSON 숫자(17) 전송 시 타입 오류 400 거절 여부 검증 (`FAIL`) — `BUG-IF-0052`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **테스트 종류**: `api`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (POST /api/assessments)` → **FAIL (HTTP 201)**
- **도구 B 및 결과**: `Python urllib + psql 4-Table Delta Verifier` → **FAIL (HTTP 201, assessment_delta=+1)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` / 함수 `AssessmentCreateRequest / AssessmentController.create` / 줄 번호 `15, 56`
- **입력값 (Input)**: `{"applicantName": 17, "age": 70, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}`
- **오류 메시지 / 응답**: `{"id":89}`
- **예상 결과 (Expected)**: HTTP 400 및 DB 증감 0
- **실제 결과 (Actual)**: Tool A: HTTP 201 ({"id":88}), Tool B: HTTP 201, DB assessment 증감=+1
- **재현 방법 (Reproduction)**:
  ```zsh
  curl -i -X POST http://127.0.0.1:8080/api/assessments -H 'Content-Type: application/json' --data-raw '{"applicantName": 17, "age": 70, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}'
  ```
- **원인 분석 (Root Cause)**: Jackson 기본 Coercion 설정이 JSON 숫자 17을 문자열 "17"로 암묵적 변환한 뒤 @Valid(@NotBlank, @Size)를 통과하여 HTTP 201로 DB에 저장됨.
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)

### [IF-0059] 나이(age)에 소수(60.5) 전송 시 정수 타입 오류 400 거절 여부 검증 (`FAIL`) — `BUG-IF-0059`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **테스트 종류**: `api`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (POST /api/assessments)` → **FAIL (HTTP 201)**
- **도구 B 및 결과**: `Python urllib + psql 4-Table Delta Verifier` → **FAIL (HTTP 201, assessment_delta=+1)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` / 함수 `AssessmentCreateRequest / AssessmentController.create` / 줄 번호 `16, 56`
- **입력값 (Input)**: `{"applicantName": "QA_API", "age": 60.5, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}`
- **오류 메시지 / 응답**: `{"id":95}`
- **예상 결과 (Expected)**: HTTP 400 및 DB 증감 0
- **실제 결과 (Actual)**: Tool A: HTTP 201 ({"id":94}), Tool B: HTTP 201, DB assessment 증감=+1
- **재현 방법 (Reproduction)**:
  ```zsh
  curl -i -X POST http://127.0.0.1:8080/api/assessments -H 'Content-Type: application/json' --data-raw '{"applicantName": "QA_API", "age": 60.5, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}'
  ```
- **원인 분석 (Root Cause)**: Jackson DeserializationFeature.ACCEPT_FLOAT_AS_INT 기본값이 활성 상태여서 소수 60.5를 정수 60으로 절삭한 뒤 201로 저장함.
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)

### [IF-0060] 나이(age)에 문자열("70") 전송 시 타입 오류 400 거절 여부 검증 (`FAIL`) — `BUG-IF-0060`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **테스트 종류**: `api`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (POST /api/assessments)` → **FAIL (HTTP 201)**
- **도구 B 및 결과**: `Python urllib + psql 4-Table Delta Verifier` → **FAIL (HTTP 201, assessment_delta=+1)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` / 함수 `AssessmentCreateRequest / AssessmentController.create` / 줄 번호 `16, 56`
- **입력값 (Input)**: `{"applicantName": "QA_API", "age": "70", "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}`
- **오류 메시지 / 응답**: `{"id":97}`
- **예상 결과 (Expected)**: HTTP 400 및 DB 증감 0
- **실제 결과 (Actual)**: Tool A: HTTP 201 ({"id":96}), Tool B: HTTP 201, DB assessment 증감=+1
- **재현 방법 (Reproduction)**:
  ```zsh
  curl -i -X POST http://127.0.0.1:8080/api/assessments -H 'Content-Type: application/json' --data-raw '{"applicantName": "QA_API", "age": "70", "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}'
  ```
- **원인 분석 (Root Cause)**: Jackson 기본 Coercion이 숫자 형태 문자열 "70"을 Integer 70으로 암묵적 변환한 뒤 @Valid를 통과하여 201로 저장함.
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)

### [IF-0067] 건강 상태(physicalLevel)에 문자열("3") 전송 시 타입 오류 400 거절 여부 검증 (`FAIL`) — `BUG-IF-0067`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **테스트 종류**: `api`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (POST /api/assessments)` → **FAIL (HTTP 201)**
- **도구 B 및 결과**: `Python urllib + psql 4-Table Delta Verifier` → **FAIL (HTTP 201, assessment_delta=+1)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` / 함수 `AssessmentCreateRequest / AssessmentController.create` / 줄 번호 `17, 56`
- **입력값 (Input)**: `{"applicantName": "QA_API", "age": 70, "physicalLevel": "3", "chronicDisease": false, "workHourLimit": 8, "jobId": 1}`
- **오류 메시지 / 응답**: `{"id":99}`
- **예상 결과 (Expected)**: HTTP 400 및 DB 증감 0
- **실제 결과 (Actual)**: Tool A: HTTP 201 ({"id":98}), Tool B: HTTP 201, DB assessment 증감=+1
- **재현 방법 (Reproduction)**:
  ```zsh
  curl -i -X POST http://127.0.0.1:8080/api/assessments -H 'Content-Type: application/json' --data-raw '{"applicantName": "QA_API", "age": 70, "physicalLevel": "3", "chronicDisease": false, "workHourLimit": 8, "jobId": 1}'
  ```
- **원인 분석 (Root Cause)**: Jackson 기본 Coercion이 문자열 "3"을 Integer 3으로 암묵적 변환한 뒤 @Valid를 통과하여 201로 저장함.
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)

### [IF-0072] 만성질환(chronicDisease)에 숫자(1) 전송 시 불리언 타입 오류 400 거절 여부 검증 (`FAIL`) — `BUG-IF-0072`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **테스트 종류**: `api`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (POST /api/assessments)` → **FAIL (HTTP 201)**
- **도구 B 및 결과**: `Python urllib + psql 4-Table Delta Verifier` → **FAIL (HTTP 201, assessment_delta=+1)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` / 함수 `AssessmentCreateRequest / AssessmentController.create` / 줄 번호 `18, 56`
- **입력값 (Input)**: `{"applicantName": "QA_API", "age": 70, "physicalLevel": 3, "chronicDisease": 1, "workHourLimit": 8, "jobId": 1}`
- **오류 메시지 / 응답**: `{"id":101}`
- **예상 결과 (Expected)**: HTTP 400 및 DB 증감 0
- **실제 결과 (Actual)**: Tool A: HTTP 201 ({"id":100}), Tool B: HTTP 201, DB assessment 증감=+1
- **재현 방법 (Reproduction)**:
  ```zsh
  curl -i -X POST http://127.0.0.1:8080/api/assessments -H 'Content-Type: application/json' --data-raw '{"applicantName": "QA_API", "age": 70, "physicalLevel": 3, "chronicDisease": 1, "workHourLimit": 8, "jobId": 1}'
  ```
- **원인 분석 (Root Cause)**: Jackson 기본 Coercion이 JSON 정수 1을 Boolean true로 암묵적 변환한 뒤 @NotNull을 통과하여 201로 저장함.
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)

### [IF-0079] 근무시간(workHourLimit)에 소수(2.5) 전송 시 정수 타입 오류 400 거절 여부 검증 (`FAIL`) — `BUG-IF-0079`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **테스트 종류**: `api`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (POST /api/assessments)` → **FAIL (HTTP 201)**
- **도구 B 및 결과**: `Python urllib + psql 4-Table Delta Verifier` → **FAIL (HTTP 201, assessment_delta=+1)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` / 함수 `AssessmentCreateRequest / AssessmentController.create` / 줄 번호 `19, 56`
- **입력값 (Input)**: `{"applicantName": "QA_API", "age": 70, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 2.5, "jobId": 1}`
- **오류 메시지 / 응답**: `{"id":103}`
- **예상 결과 (Expected)**: HTTP 400 및 DB 증감 0
- **실제 결과 (Actual)**: Tool A: HTTP 201 ({"id":102}), Tool B: HTTP 201, DB assessment 증감=+1
- **재현 방법 (Reproduction)**:
  ```zsh
  curl -i -X POST http://127.0.0.1:8080/api/assessments -H 'Content-Type: application/json' --data-raw '{"applicantName": "QA_API", "age": 70, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 2.5, "jobId": 1}'
  ```
- **원인 분석 (Root Cause)**: Jackson ACCEPT_FLOAT_AS_INT 기본 설정으로 인해 소수 2.5가 정수 2로 절삭된 뒤 @Min(1)/@Max(24)를 통과하여 201로 저장함.
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)

### [IF-0087] Content-Type: text/plain으로 JSON 전송 시 4xx(415/400) 처리 여부 검증 (`FAIL`) — `BUG-IF-0087`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:31:03 KST`
- **테스트 종류**: `api`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (POST /api/assessments)` → **FAIL (HTTP 500)**
- **도구 B 및 결과**: `Python urllib + psql 4-Table Delta Verifier` → **FAIL (HTTP 500, assessment_delta=+0)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/global/exception/GlobalExceptionHandler.java` / 함수 `handleUnexpected` / 줄 번호 `48-51`
- **입력값 (Input)**: `{"applicantName": "QA_API", "age": 70, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}`
- **오류 메시지 / 응답**: `{"success":false,"data":null,"message":"서버 오류가 발생했습니다.","errorCode":"INTERNAL_ERROR"}`
- **예상 결과 (Expected)**: HTTP 415 및 DB 증감 0
- **실제 결과 (Actual)**: Tool A: HTTP 500 ({"success":false,"data":null,"message":"서버 오류가 발생했습니다.","errorCode":"INTERNAL_ER), Tool B: HTTP 500, DB assessment 증감=+0
- **재현 방법 (Reproduction)**:
  ```zsh
  curl -i -X POST http://127.0.0.1:8080/api/assessments -H 'Content-Type: text/plain' --data-raw '{"applicantName": "QA_API", "age": 70, "physicalLevel": 3, "chronicDisease": false, "workHourLimit": 8, "jobId": 1}'
  ```
- **원인 분석 (Root Cause)**: GlobalExceptionHandler에 HttpMediaTypeNotSupportedException 전용 핸들러가 없어 최상위 Exception.class 핸들러(handleUnexpected, 48-51행)가 잡아서 HTTP 500 INTERNAL_ERROR를 반환함.
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)


## TC-20261030-1459 / IF-0052
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0052
- timestamp: 2026-10-30T14:59:00+09:00
- feature: applicantName 17
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: FAIL
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: 15행 applicantName. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록
- ISSUE_ID: BUG-IF-0052
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 이름 JSON 숫자 17. HTTP 201 {"id":23}. display_name은 17. 타입 오류인데 4xx가 아님 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0059
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0059
- timestamp: 2026-10-30T14:59:00+09:00
- feature: age 60.5
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: FAIL
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: 16행 age. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록
- ISSUE_ID: BUG-IF-0059
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 나이 60.5. HTTP 201 {"id":26}. 추가 확인에서 저장된 age는 60. 타입 오류인데 4xx가 아님 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0060
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0060
- timestamp: 2026-10-30T14:59:00+09:00
- feature: age '70'
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: FAIL
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: 16행 age. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록
- ISSUE_ID: BUG-IF-0060
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 나이 문자열 70. HTTP 201 {"id":27}. 추가 확인에서 저장된 age는 70. 타입 오류인데 4xx가 아님 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0067
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0067
- timestamp: 2026-10-30T14:59:00+09:00
- feature: physicalLevel '3'
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: FAIL
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: 17행 physicalLevel. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록
- ISSUE_ID: BUG-IF-0067
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 건강 상태 문자열 3. HTTP 201 {"id":31}. 추가 확인에서 physical_level은 3. 타입 오류인데 4xx가 아님 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0072
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0072
- timestamp: 2026-10-30T14:59:00+09:00
- feature: chronicDisease 1
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: FAIL
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: 18행 chronicDisease. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록
- ISSUE_ID: BUG-IF-0072
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 만성질환 숫자 1. HTTP 201 {"id":34}. 추가 확인에서 chronic_disease_flag는 true. 타입 오류인데 4xx가 아님 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0079
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0079
- timestamp: 2026-10-30T14:59:00+09:00
- feature: workHourLimit 2.5
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: FAIL
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: 19행 workHourLimit. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록
- ISSUE_ID: BUG-IF-0079
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 근무시간 2.5. HTTP 201 {"id":38}. 추가 확인에서 work_hour_limit은 2. 타입 오류인데 4xx가 아님 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0087
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0087
- timestamp: 2026-10-30T14:59:00+09:00
- feature: text/plain Content-Type
- test_type: api
- tool_a: Postman/MockMvc
- command_a: HTTP 요청 직접 전송 → 상태/응답 및 서버 로그 확인
- result_a: FAIL
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/global/exception/GlobalExceptionHandler.java
- function: HTTP body 또는 Pageable 변환
- line: 51행 handleUnexpected의 return. 메서드는 48–51행. 예외는 스프링 AbstractMessageConverterMethodArgumentResolver.readWithMessageConverters 213행 HttpMediaTypeNotSupportedException. 그 호출은 AssessmentController.java 56행 @RequestBody
- ISSUE_ID: BUG-IF-0087
- RISK_ID: 
- evidence: 기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치 | 실제: 정상 JSON을 text/plain으로 전송. HTTP 500 INTERNAL_ERROR. 증가 0. 로그는 HttpMediaTypeNotSupportedException | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

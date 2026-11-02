# PASS

## 20261030T172701-24c6ce0dc2 / QA-SECURITY
- RUN_ID: 20261030T172701-24c6ce0dc2
- TC_ID: QA-SECURITY
- timestamp: 2026-10-30T17:27:01.356327+09:00
- feature: Python SAST 및 추적 파일 비밀키 패턴 검사
- test_type: security
- tool_a: Bandit
- command_a: ["python3", "-m", "bandit", "-r", "ai/src", "data/etl", "-lll", "-q"]
- result_a: PASS
- tool_b: Secret-policy
- command_b: ["python3", "scripts/qa/security.py"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src, data/etl
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/security/2026-10-30/20261030T172701-24c6ce0dc2/QA-SECURITY-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/security/2026-10-30/20261030T172701-24c6ce0dc2/QA-SECURITY-b.log sha256=d49e8eeb796a1f4cdbc3f15128ccbd7c4c2cad046c77d6e8b8e5e719bb8516e7

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Bandit HIGH SAST 및 별도 추적 파일 private key/키 패턴 검사. 의존성 CVE/침투 테스트 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-SECURITY
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-SECURITY
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: Python SAST 및 추적 파일 비밀키 패턴 검사
- test_type: security
- tool_a: Bandit
- command_a: ["python3", "-m", "bandit", "-r", "ai/src", "data/etl", "-lll", "-q"]
- result_a: PASS
- tool_b: Secret-policy
- command_b: ["python3", "scripts/qa/security.py"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src, data/etl
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/security/2026-10-30/20261030T173027-a0890b20ec/QA-SECURITY-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/security/2026-10-30/20261030T173027-a0890b20ec/QA-SECURITY-b.log sha256=d49e8eeb796a1f4cdbc3f15128ccbd7c4c2cad046c77d6e8b8e5e719bb8516e7

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Bandit HIGH SAST 및 별도 추적 파일 private key/키 패턴 검사. 의존성 CVE/침투 테스트 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:33:06 KST)

- **통과 건수**: 3건 / 전체 5건

| RUN_ID | TC_ID | 실행 일시 (KST) | 기능명 | 도구 A (결과) | 도구 B (결과) | 최종 상태 | Git Commit | 대상 파일 | 함수명 | 줄 번호 | 관련 ID | 검증 목적 및 근거 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `RUN-20261030-001` | `SEC-001` | 2026-10-30 17:32:54 KST | OWASP ASVS V5.3 SQL Injection 방어 검증 (LOG-017 재사용) | `OWASP WSTG Dynamic SQLi Probe (curl POST '; DROP TABLE assessment;--')` (PASS (SQL 구문이 실행되지 않고 일반 문자열로 바인딩 처리됨)) | `SAST JPA Query & Parameter Binding Scanner` (PASS (문자열 연결 Native SQL 없음, Spring Data JPA 파라미터 바인딩 확인)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/repository/AssessmentRepository.java` | `AssessmentRepository` | `1-45` | `-` | **목적**: 이름 및 직무 ID에 SQL Injection 공격 구문 입력 시 테이블 손상 없이 안전하게 처리되는지 검증<br>**기대**: assessment 테이블 무결성 유지 및 파라미터 바인딩 처리<br>**실제/근거**: 테이블 정상 유지, 문자열 리터럴로 안전 저장 후 정리 완료 (AssessmentRepository.java & AssessmentService.java:86) |
| `RUN-20261030-001` | `SEC-002` | 2026-10-30 17:32:54 KST | OWASP WSTG-CLNT-07 비인가 Origin CORS Preflight 차단 검증 | `curl CORS Preflight Probe (Origin: https://evil.example.com)` (PASS (HTTP 403, ACAO 헤더 미반환)) | `SAST WebConfig CORS Policy Inspector` (PASS (명시적 화이트리스트 allowedOrigins 사용, 와일드카드 * 미사용)) | **PASS** | `9491fb1b` | `spring/src/main/demo/global/config/WebConfig.java` | `addCorsMappings` | `39-50` | `-` | **목적**: 허용되지 않은 외부 악성 도메인에서의 교차 출처 요청이 차단되는지 검증<br>**기대**: HTTP 403 Forbidden 및 Access-Control-Allow-Origin 헤더 미포함<br>**실제/근거**: HTTP 403, ACAO 헤더 없음 (spring/src/main/demo/global/config/WebConfig.java:30-50) |
| `RUN-20261030-001` | `SEC-003` | 2026-10-30 17:32:54 KST | OWASP ASVS V14.2 민감 환경변수(.env) Git 추적 제외 및 하드코딩 시크릿 차단 검증 | `Git Tracked Files Inspector (git ls-files)` (PASS (.env 파일 Git 미추적 확인)) | `SAST .gitignore & Source Secret Pattern Scanner` (PASS (.gitignore 내 .env 등록 확인)) | **PASS** | `9491fb1b` | `.gitignore` | `N/A (Config)` | `1-35` | `-` | **목적**: API Key 및 DB 비밀번호가 담긴 .env 파일이 버전 관리(Git)에 노출되지 않는지 검증<br>**기대**: git ls-files 내 .env 0건 및 .gitignore에 .env 포함<br>**실제/근거**: env_tracked=False, gitignore_has_env=True (.gitignore & compose.yaml:15,35,53) |


## 20261030T173420-dd42c9f7f7 / QA-SECURITY
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: QA-SECURITY
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: Python SAST 및 추적 파일 비밀키 패턴 검사
- test_type: security
- tool_a: Bandit
- command_a: ["python3", "-m", "bandit", "-r", "ai/src", "data/etl", "-lll", "-q"]
- result_a: PASS
- tool_b: Secret-policy
- command_b: ["python3", "scripts/qa/security.py"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src, data/etl
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/security/2026-10-30/20261030T173420-dd42c9f7f7/QA-SECURITY-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/security/2026-10-30/20261030T173420-dd42c9f7f7/QA-SECURITY-b.log sha256=d49e8eeb796a1f4cdbc3f15128ccbd7c4c2cad046c77d6e8b8e5e719bb8516e7

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Bandit HIGH SAST 및 별도 추적 파일 private key/키 패턴 검사. 의존성 CVE/침투 테스트 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-SECURITY
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-SECURITY
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: Python SAST 및 추적 파일 비밀키 패턴 검사
- test_type: security
- tool_a: Bandit
- command_a: ["python3", "-m", "bandit", "-r", "ai/src", "data/etl", "-lll", "-q"]
- result_a: PASS
- tool_b: Secret-policy
- command_b: ["python3", "scripts/qa/security.py"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src, data/etl
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/security/2026-10-30/20261030T173746-09edf77edc/QA-SECURITY-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/security/2026-10-30/20261030T173746-09edf77edc/QA-SECURITY-b.log sha256=d49e8eeb796a1f4cdbc3f15128ccbd7c4c2cad046c77d6e8b8e5e719bb8516e7

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Bandit HIGH SAST 및 별도 추적 파일 private key/키 패턴 검사. 의존성 CVE/침투 테스트 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-SECURITY
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-SECURITY
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: Python SAST 및 추적 파일 비밀키 패턴 검사
- test_type: security
- tool_a: Bandit
- command_a: ["python3", "-m", "bandit", "-r", "ai/src", "data/etl", "-lll", "-q"]
- result_a: PASS
- tool_b: Secret-policy
- command_b: ["python3", "scripts/qa/security.py"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src, data/etl
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/security/2026-10-30/20261030T174647-e942dbd875/QA-SECURITY-a.log sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; qa/.runtime/evidence/security/2026-10-30/20261030T174647-e942dbd875/QA-SECURITY-b.log sha256=d49e8eeb796a1f4cdbc3f15128ccbd7c4c2cad046c77d6e8b8e5e719bb8516e7

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: Bandit HIGH SAST 및 별도 추적 파일 private key/키 패턴 검사. 의존성 CVE/침투 테스트 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

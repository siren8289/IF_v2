# FAIL

## RUN-20261102-001 / SEC-SQL-001
- RUN_ID: RUN-20261102-001
- TC_ID: SEC-SQL-001
- timestamp: 2026-11-02T11:57:51+09:00
- feature: 메인 소스의 문자열 연결 SQL
- test_type: security
- tool_a: python
- command_a: SQL_RE walk spring/ai/data/web src
- result_a: FAIL
- tool_b: rg
- command_b: rg SELECT/INSERT/UPDATE/DELETE plus concatenation
- result_b: ERROR
- status: ERROR
- git_commit: 69f74c49c8a9
- dirty: true
- files: spring/src
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: python=['spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java:321', 'spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java:517', 'spring/src/test/java/com/example/demo/assessment/AssessmentPipelineIf0094Test.java:518'] rg=rg not installed

검증 목적: 본문 SQL을 문자열 연결로 만드는 코드가 있는지 본다.
기대: 두 도구 모두 0건. 파라미터 바인딩만 있으면 PASS.
실제 python 3건, rg 0건.
rg not installed

## RUN-20261102-001 / SEC-AUTH-001
- RUN_ID: RUN-20261102-001
- TC_ID: SEC-AUTH-001
- timestamp: 2026-11-02T11:57:51+09:00
- feature: Spring Security 구성 존재 여부
- test_type: security
- tool_a: python
- command_a: read spring/build.gradle
- result_a: PASS
- tool_b: rg
- command_b: rg spring-boot-starter-security spring
- result_b: ERROR
- status: ERROR
- git_commit: 69f74c49c8a9
- dirty: true
- files: spring/build.gradle
- function: dependencies
- line: 20
- ISSUE_ID: 
- RISK_ID: RISK-QA-AUTH
- evidence: security starter absent python=True rg=False

검증 목적: 인증 라이브러리와 보안 필터가 소스에 있는지 확인한다.
역할별 권한 요구사항 문서는 저장소에 없다. 없음을 통과 요건으로 추측하지 않고 위험으로 남긴다.
기대: 두 도구가 같은 관찰을 한다. 실제 python absent=True rg absent=False.
rg missing

RISK RISK-QA-AUTH
심각도: HIGH
발생 가능성: MEDIUM
영향: 이름, 나이, 만성질환이 인증 없이 생성·조회·삭제된다. compose는 127.0.0.1에 묶여 있으나 애플리케이션 인증은 없다.
권장 조치: 인증 요구사항을 정한 뒤 Spring Security 또는 앞단 인증을 넣기 전에는 공개 배포하지 않는다. 요구사항이 없다면 qa/risk-decisions.tsv 에 ACCEPTED로 남긴다.
처리 상태: OPEN
파일: spring/build.gradle
함수: dependencies
줄: 21
심각도 HIGH. 발생 가능성 MEDIUM. 상태 OPEN.
처리 전 제품 코드는 수정하지 않는다. 로컬 바인딩은 노출 범위를 줄일 뿐 권한 검사를 대신하지 않는다.

## RUN-20261102-001 / SEC-DEPLOY-001
- RUN_ID: RUN-20261102-001
- TC_ID: SEC-DEPLOY-001
- timestamp: 2026-11-02T11:57:51+09:00
- feature: 수동 배포가 성공한 CI SHA를 요구하는지
- test_type: security
- tool_a: python
- command_a: read deploy.yml SUCCESS guard
- result_a: PASS
- tool_b: rg
- command_b: rg test SUCCESS deploy.yml
- result_b: ERROR
- status: ERROR
- git_commit: 69f74c49c8a9
- dirty: true
- files: .github/workflows/deploy.yml
- function: Require successful CI for exact deployment commit
- line: 49
- ISSUE_ID: 
- RISK_ID: RISK-QA-DEPLOY
- evidence: guard=True

검증 목적: workflow_dispatch가 CI 성공 확인 없이 배포하지 않는지 파일에서 확인한다.
이전 RISK-001 행은 도구 결과가 UNKNOWN이었다. 이 실행은 현재 파일을 다시 읽는다.
기대: test "$SUCCESS" -gt 0 가 있다. 실제 python=True rg=False line=49.
rg missing

RISK RISK-QA-DEPLOY
심각도: MEDIUM
발생 가능성: LOW
영향: 워크플로 파일의 SHA 확인은 들어 있다. 브랜치 보호 규칙 자체는 저장소 파일로 강제되지 않는다.
권장 조치: GitHub ruleset에서 qa-gate 성공을 병합 조건으로 둔다.
처리 상태: OPEN
파일: .github/workflows/deploy.yml
함수: deploy
줄: 49
심각도 MEDIUM. 이전 HIGH 우회(가드 부재)는 현재 파일에서 test "$SUCCESS" -gt 0 로 완화됐다. 규칙셋 미설정은 남아 있으므로 OPEN이다. HIGH는 아니다.

## RUN-20261102-001 / SEC-UI-023
- RUN_ID: RUN-20261102-001
- TC_ID: SEC-UI-023
- timestamp: 2026-11-02T11:57:51+09:00
- feature: 제출 버튼 비활성 시점 정적 확인
- test_type: security
- tool_a: python
- command_a: find setSubmitting and disabled
- result_a: PASS
- tool_b: rg
- command_b: rg setSubmitting AssessmentFormPage.tsx
- result_b: ERROR
- status: ERROR
- git_commit: 69f74c49c8a9
- dirty: true
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: handleSubmit
- line: 63
- ISSUE_ID: BUG-UI-023
- RISK_ID: RISK-QA-UI-023
- evidence: setSubmitting line 63; disabled line 146

검증 목적: 브라우저를 다시 띄우지 않고, 더블클릭 가드가 어디에 있는지만 확인한다.
setSubmitting(true)는 handleSubmit 검증 통과 뒤에 있다. disabled는 그 상태 값을 본다. 같은 턴의 두 클릭은 React가 다시 그리기 전에 둘 다 핸들러로 들어갈 수 있다.
이번 실행은 클릭 재현이 아니다. UI-023을 PASS로 바꾸지 않는다.
줄 번호는 이번 프로세스에서 파일을 읽어 확인했다. setSubmitting=63 disabled=146.
rg missing

RISK RISK-QA-UI-023
심각도: MEDIUM
발생 가능성: MEDIUM
영향: 같은 턴 이중 클릭이 평가를 두 건 만들 수 있다. 기존 브라우저 결과 BUG-UI-023 / BUG-IF-0043.
권장 조치: 클릭 직후 동기적으로 제출을 잠그고, 잠금 전 두 번째 클릭 테스트를 다시 실행한다.
처리 상태: OPEN
파일: web-vite/src/pages/AssessmentFormPage.tsx
함수: handleSubmit
줄: 63
심각도 MEDIUM. 이번 게이트는 브라우저를 실행하지 않았다. 코드 위치만 재확인했다. 제품 코드는 수정하지 않았다.

## RUN-20261102-001 / SEC-NPM-001
- RUN_ID: RUN-20261102-001
- TC_ID: SEC-NPM-001
- timestamp: 2026-11-02T11:57:51+09:00
- feature: 프론트 의존성 high 이상 권고
- test_type: security
- tool_a: npm audit
- command_a: npm audit --json --audit-level=high
- result_a: FAIL
- tool_b: python json
- command_b: metadata.vulnerabilities.high/critical
- result_b: FAIL
- status: FAIL
- git_commit: 69f74c49c8a9
- dirty: true
- files: web-vite/package-lock.json
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-QA-NPM
- evidence: high=1 critical=0

검증 목적: npm audit high 이상이 0인지 본다. 도구 B는 같은 JSON의 건수를 다시 집계한다. 별도의 취약점 DB를 호출하지는 않는다.
기대: high 0, critical 0. 실제 high=1 critical=0 exit=1.
전체 JSON은 리포트에 넣지 않는다.

RISK RISK-QA-NPM
심각도: MEDIUM
발생 가능성: MEDIUM
영향: npm audit high=1 critical=0
권장 조치: 권고를 확인하고 수정 범위만 올려 다시 audit 한다.
처리 상태: OPEN
파일: web-vite/package-lock.json
함수: UNKNOWN
줄: UNKNOWN
심각도 MEDIUM. 상태 OPEN. 패키지 목록 전문은 저장하지 않았다.

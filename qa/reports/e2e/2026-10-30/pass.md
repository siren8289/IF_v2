# [E2E] PASS 테스트 기록 (2026-10-30)

> **경로**: `qa/reports/e2e/2026-10-30/pass.md`  
> **기준 시간대**: `Asia/Seoul` (KST)  
> **원칙**: 최소 2개 도구(Tool A / Tool B) 교차 검증을 모두 통과(`PASS`)한 테스트 케이스만 기록합니다.

---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:54 KST)

- **통과 건수**: 1건 / 전체 2건

| RUN_ID | TC_ID | 실행 일시 (KST) | 기능명 | 도구 A (결과) | 도구 B (결과) | 최종 상태 | Git Commit | 대상 파일 | 함수명 | 줄 번호 | 관련 ID | 검증 목적 및 근거 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `RUN-20261030-001` | `UI-026` | 2026-10-30 17:32:53 KST | Nginx(:80) SPA 딥링크 새로고침 복구(/, /dashboard, /assessments/new, /result) 및 /api 프록시 검증 | `curl CLI (GET http://127.0.0.1:80/* & /api/jobs)` (PASS (4개 경로 HTTP 200, /api/jobs HTTP 200)) | `Python HTTP E2E Client` (PASS (SPA root 마운트 확인, 직무 8건)) | **PASS** | `9491fb1b` | `web-vite/nginx.conf` | `location / & location /api/` | `11-21` | `-` | **목적**: 브라우저 새로고침 시 Nginx try_files가 index.html을 반환하고 /api 요청을 Spring으로 프록시하는지 검증<br>**기대**: 모든 SPA 경로 HTTP 200 및 /api/jobs 8건 반환<br>**실제/근거**: 4개 SPA 라우트 HTTP 200, /api/jobs 8건 반환 (web-vite/nginx.conf:11-21 & UI-001, UI-003, UI-026) |

화면: 같은 날짜 폴더의 `screenshots/UI-026.png`


## TC-20261030-1418 / UI-001
- RUN_ID: TC-20261030-1418
- TC_ID: UI-001
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 첫 화면 열기
- test_type: e2e
- tool_a: 브라우저
- command_a: http://localhost 접속
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 메인 화면이 오류 없이 표시 | 실제: HTTP 200. / 가 /dashboard 로 이동. 평가 대시보드, 요약 카드, 새로운 평가 시작 버튼 표시. alert 없음, 콘솔 오류 0 | 화면: screenshots/UI-001.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-002
- RUN_ID: TC-20261030-1418
- TC_ID: UI-002
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 새 평가 페이지 이동
- test_type: e2e
- tool_a: 브라우저
- command_a: 새로운 평가 메뉴 클릭
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 입력 폼 렌더링 | 실제: 대시보드 버튼 "새로운 평가 시작" 클릭 후 /assessments/new. 이름, 연령, 건강 상태, 만성질환, 근무시간, 직무, 위험도 분석 시작 표시. 별도 메뉴 항목은 없음 | 화면: screenshots/UI-002.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-003
- RUN_ID: TC-20261030-1418
- TC_ID: UI-003
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 직무 8개 표시
- test_type: e2e
- tool_a: 브라우저
- command_a: 직무 선택창 열고 항목 수 세기
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: API 응답과 동일한 8개 직무 표시 | 실제: GET /api/jobs 8건. 선택창은 "선택하세요" 제외 8개 | 화면: screenshots/UI-003.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-004
- RUN_ID: TC-20261030-1418
- TC_ID: UI-004
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 직무 명칭과 위치 표시
- test_type: e2e
- tool_a: 브라우저
- command_a: 직무 목록과 GET /api/jobs 응답 비교
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: jobTitle/workplace 일치 | 실제: 8개 옵션 value가 직무 id와 같고 문구가 jobTitle (workplace)와 일치 | 화면: screenshots/UI-004.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-005
- RUN_ID: TC-20261030-1418
- TC_ID: UI-005
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 직무 전환
- test_type: e2e
- tool_a: 브라우저
- command_a: 직무 1 선택→직무 2 선택
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 현재 선택값만 변경 | 실제: 직무 1에서 2로 바꿀 때 job만 변경. 이름, 연령, 건강, 만성질환, 근무시간은 유지 | 화면: screenshots/UI-005.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-006
- RUN_ID: TC-20261030-1418
- TC_ID: UI-006
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 필수 이름 빈값
- test_type: e2e
- tool_a: 브라우저
- command_a: 이름 공란으로 분석 클릭
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 이름 입력 요청, POST 미발생 | 실제: alert "이름을 입력해주세요." POST /api/assessments 0건 | 화면: screenshots/UI-006.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-007
- RUN_ID: TC-20261030-1418
- TC_ID: UI-007
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 공백 이름
- test_type: e2e
- tool_a: 브라우저
- command_a: 이름에 공백만 입력
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 이름 필수 오류, POST 미발생 | 실제: 공백만 있는 이름도 같은 이름 필수 오류. POST 0건 | 화면: screenshots/UI-007.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-008
- RUN_ID: TC-20261030-1418
- TC_ID: UI-008
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 이름 앞뒤 공백
- test_type: e2e
- tool_a: 브라우저
- command_a: 이름 앞뒤 공백 넣고 정상 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: trim 처리된 이름 전송 | 실제: POST 1건 HTTP 201. applicantName은 "홍길동"으로 trim. 검증 alert 없음 | 화면: screenshots/UI-008.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-009
- RUN_ID: TC-20261030-1418
- TC_ID: UI-009
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 연령 입력 0
- test_type: e2e
- tool_a: 브라우저
- command_a: 나이 0으로 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 1~120 검증 실패 | 실제: alert "연령은 1~120 사이로 입력해주세요." POST 0건 | 화면: screenshots/UI-009.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-010
- RUN_ID: TC-20261030-1418
- TC_ID: UI-010
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 연령 입력 1
- test_type: e2e
- tool_a: 브라우저
- command_a: 나이 1로 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 입력 검증 통과 | 실제: 검증 alert 없이 POST 1건 HTTP 201. body.age=1 | 화면: screenshots/UI-010.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-011
- RUN_ID: TC-20261030-1418
- TC_ID: UI-011
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 연령 입력 120
- test_type: e2e
- tool_a: 브라우저
- command_a: 나이 120으로 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 입력 검증 통과 | 실제: 검증 alert 없이 POST 1건 HTTP 201. body.age=120 | 화면: screenshots/UI-011.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-012
- RUN_ID: TC-20261030-1418
- TC_ID: UI-012
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 연령 입력 121
- test_type: e2e
- tool_a: 브라우저
- command_a: 나이 121로 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 검증 실패 | 실제: 연령 범위 오류. POST 0건 | 화면: screenshots/UI-012.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-013
- RUN_ID: TC-20261030-1418
- TC_ID: UI-013
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 연령 음수
- test_type: e2e
- tool_a: 브라우저
- command_a: 나이 -1로 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 검증 실패 | 실제: 나이 -1도 연령 범위 오류. POST 0건 | 화면: screenshots/UI-013.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-014
- RUN_ID: TC-20261030-1418
- TC_ID: UI-014
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 연령 소수
- test_type: e2e
- tool_a: 브라우저
- command_a: 나이 60.5로 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 검증 실패 | 실제: 나이 60.5는 정수가 아니라 연령 범위 오류. POST 0건 | 화면: screenshots/UI-014.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-015
- RUN_ID: TC-20261030-1418
- TC_ID: UI-015
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 근무시간 0
- test_type: e2e
- tool_a: 브라우저
- command_a: 0 입력 후 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 1~24 검증 실패 | 실제: alert "근무 가능 시간은 1~24 사이로 입력해주세요." POST 0건 | 화면: screenshots/UI-015.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-016
- RUN_ID: TC-20261030-1418
- TC_ID: UI-016
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 근무시간 1
- test_type: e2e
- tool_a: 브라우저
- command_a: 1 입력 후 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 입력 검증 통과 | 실제: 검증 alert 없이 POST 1건 HTTP 201. workHourLimit=1 | 화면: screenshots/UI-016.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-017
- RUN_ID: TC-20261030-1418
- TC_ID: UI-017
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 근무시간 24
- test_type: e2e
- tool_a: 브라우저
- command_a: 24 입력 후 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 입력 검증 통과 | 실제: 검증 alert 없이 POST 1건 HTTP 201. workHourLimit=24 | 화면: screenshots/UI-017.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-018
- RUN_ID: TC-20261030-1418
- TC_ID: UI-018
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 근무시간 25
- test_type: e2e
- tool_a: 브라우저
- command_a: 25 입력 후 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 검증 실패 | 실제: 근무시간 범위 오류. POST 0건 | 화면: screenshots/UI-018.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-019
- RUN_ID: TC-20261030-1418
- TC_ID: UI-019
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 근무시간 소수
- test_type: e2e
- tool_a: 브라우저
- command_a: 7.5 입력 후 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 검증 실패 | 실제: 7.5시간은 정수가 아니라 근무시간 범위 오류. POST 0건 | 화면: screenshots/UI-019.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-020
- RUN_ID: TC-20261030-1418
- TC_ID: UI-020
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 직무 미선택
- test_type: e2e
- tool_a: 브라우저
- command_a: 직무 없이 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 직무 선택 요청, POST 미발생 | 실제: alert "직무를 선택해주세요." POST 0건 | 화면: screenshots/UI-020.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-021
- RUN_ID: TC-20261030-1418
- TC_ID: UI-021
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 건강 상태 옵션
- test_type: e2e
- tool_a: 브라우저
- command_a: 1~5 옵션 순서 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 다섯 단계가 정확히 표시 | 실제: 1 매우 좋음, 2 좋음, 3 보통, 4 나쁨, 5 매우 나쁨 순서와 value 1~5 일치 | 화면: screenshots/UI-021.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-022
- RUN_ID: TC-20261030-1418
- TC_ID: UI-022
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 만성질환 토글
- test_type: e2e
- tool_a: 브라우저
- command_a: 있음/없음 각각 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: boolean true/false 정확히 전송 | 실제: 있음은 chronicDisease true, 없음은 false. 둘 다 POST HTTP 201 | 화면: screenshots/UI-022-no.png, screenshots/UI-022-yes.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-024
- RUN_ID: TC-20261030-1418
- TC_ID: UI-024
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 처리 중 표시
- test_type: e2e
- tool_a: 브라우저
- command_a: 정상 입력 후 분석 클릭
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: AI 분석 중 표시 | 실제: 클릭 직후 버튼 문구 "AI 분석 중..."이고 disabled | 화면: screenshots/UI-024.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-025
- RUN_ID: TC-20261030-1418
- TC_ID: UI-025
- timestamp: 2026-10-30T14:18:00+09:00
- feature: API 오류 안내
- test_type: e2e
- tool_a: 브라우저
- command_a: API 오류 상황에서 제출
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 사용자가 이해할 수 있는 오류 표시 | 실제: 폼에 남고 alert "API 502: AI 서버 호출에 실패했습니다." | 화면: screenshots/UI-025.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-026
- RUN_ID: TC-20261030-1418
- TC_ID: UI-026
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 새로고침 복구
- test_type: e2e
- tool_a: 브라우저
- command_a: 각 페이지 새로고침
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: SPA 화면 정상 복구 | 실제: /, /dashboard, /assessments/new, /assessments/2/result 새로고침 모두 HTTP 200. 헤더와 해당 화면 문구 복구. Nginx 404 없음 | 화면: screenshots/UI-026.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-027
- RUN_ID: TC-20261030-1418
- TC_ID: UI-027
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 모바일 레이아웃
- test_type: e2e
- tool_a: 브라우저
- command_a: DevTools 기기 너비 375px 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 가로 넘침 및 입력 조작 불편 없음 | 실제: 375px에서 scrollWidth=clientWidth=375. 가로로 넓은 요소 없음. 이름 입력과 직무 선택 가능. 세로 스크롤은 있음 | 화면: screenshots/UI-027.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-028
- RUN_ID: TC-20261030-1418
- TC_ID: UI-028
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 키보드 탐색
- test_type: e2e
- tool_a: 브라우저
- command_a: Tab과 Enter로 폼 이동
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 입력/선택/제출 접근 가능 | 실제: Tab 순서 name, age, health, chronic, hours, job, 제출 버튼. 버튼에서 Enter로 제출됨. 닫힌 select는 ArrowDown만으로 값이 바뀌지 않음 | 화면: screenshots/UI-028.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1418 / UI-029
- RUN_ID: TC-20261030-1418
- TC_ID: UI-029
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 오류 메시지 접근성
- test_type: e2e
- tool_a: 브라우저
- command_a: 오류 시 DOM의 role alert 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 문구가 안내용 속성으로 렌더링 | 실제: <div role="alert">이름을 입력해주세요.</div> | 화면: screenshots/UI-029.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.


# 수동 시트 원문 TC-20261030-1418

# UI-001 ~ UI-029 브라우저 테스트 결과

실행 시각: 2026-10-30 14:18~14:20 (KST)  
대상: `http://localhost` 에 이미 떠 있던 Docker 스택  
판정: **28건 통과, 1건 실패 (UI-023)**

화면 캡처는 같은 폴더의 `screenshots/` 에 있다. 기계가 읽은 원본은 `results.json` 이다.  
스프레드시트에 그대로 붙일 전체 표(실행 상태, 실제 결과, 버그 번호, 참고 URL 포함)는 `UI-001-029-결과표.tsv` 다.

## 비어 있던 칸

실행 상태는 모두 `미실행`이었다. 아래는 2026-10-30 14:18~14:20 (KST) 브라우저 실행으로 채운 값이다. 각 행의 실행일은 2026-10-30이다. 통과 건의 버그 번호는 없다. UI-023만 이 문서 안의 번호 `BUG-UI-023` 으로 적었다. 이슈 트래커에는 올리지 않았다.

| 케이스 ID | 실행일 | 실행 상태 | 실제 결과 | 버그 번호 | 참고 URL |
| --- | --- | --- | --- | --- | --- |
| UI-001 | 2026-10-30 | 통과 | HTTP 200. `/` 가 `/dashboard` 로 이동. 평가 대시보드, 요약 카드, 새로운 평가 시작 버튼 표시. alert 없음, 콘솔 오류 0 |  | http://localhost/ |
| UI-002 | 2026-10-30 | 통과 | 대시보드 버튼 "새로운 평가 시작" 클릭 후 `/assessments/new`. 이름, 연령, 건강 상태, 만성질환, 근무시간, 직무, 위험도 분석 시작 표시. 별도 메뉴 항목은 없음 |  | http://localhost/dashboard |
| UI-003 | 2026-10-30 | 통과 | GET /api/jobs 8건. 선택창은 "선택하세요" 제외 8개 |  | http://localhost/assessments/new |
| UI-004 | 2026-10-30 | 통과 | 8개 옵션 value가 직무 id와 같고 문구가 "jobTitle (workplace)"와 일치 |  | http://localhost/api/jobs |
| UI-005 | 2026-10-30 | 통과 | 직무 1에서 2로 바꿀 때 job만 변경. 이름, 연령, 건강, 만성질환, 근무시간은 유지 |  | http://localhost/assessments/new |
| UI-006 | 2026-10-30 | 통과 | alert "이름을 입력해주세요." POST /api/assessments 0건 |  | http://localhost/assessments/new |
| UI-007 | 2026-10-30 | 통과 | 공백만 있는 이름도 같은 이름 필수 오류. POST 0건 |  | http://localhost/assessments/new |
| UI-008 | 2026-10-30 | 통과 | POST 1건 HTTP 201. applicantName은 "홍길동"으로 trim. 검증 alert 없음 |  | http://localhost/assessments/new |
| UI-009 | 2026-10-30 | 통과 | alert "연령은 1~120 사이로 입력해주세요." POST 0건 |  | http://localhost/assessments/new |
| UI-010 | 2026-10-30 | 통과 | 검증 alert 없이 POST 1건 HTTP 201. body.age=1 |  | http://localhost/assessments/new |
| UI-011 | 2026-10-30 | 통과 | 검증 alert 없이 POST 1건 HTTP 201. body.age=120 |  | http://localhost/assessments/new |
| UI-012 | 2026-10-30 | 통과 | 연령 범위 오류. POST 0건 |  | http://localhost/assessments/new |
| UI-013 | 2026-10-30 | 통과 | 나이 -1도 연령 범위 오류. POST 0건 |  | http://localhost/assessments/new |
| UI-014 | 2026-10-30 | 통과 | 나이 60.5는 정수가 아니라 연령 범위 오류. POST 0건 |  | http://localhost/assessments/new |
| UI-015 | 2026-10-30 | 통과 | alert "근무 가능 시간은 1~24 사이로 입력해주세요." POST 0건 |  | http://localhost/assessments/new |
| UI-016 | 2026-10-30 | 통과 | 검증 alert 없이 POST 1건 HTTP 201. workHourLimit=1 |  | http://localhost/assessments/new |
| UI-017 | 2026-10-30 | 통과 | 검증 alert 없이 POST 1건 HTTP 201. workHourLimit=24 |  | http://localhost/assessments/new |
| UI-018 | 2026-10-30 | 통과 | 근무시간 범위 오류. POST 0건 |  | http://localhost/assessments/new |
| UI-019 | 2026-10-30 | 통과 | 7.5시간은 정수가 아니라 근무시간 범위 오류. POST 0건 |  | http://localhost/assessments/new |
| UI-020 | 2026-10-30 | 통과 | alert "직무를 선택해주세요." POST 0건 |  | http://localhost/assessments/new |
| UI-021 | 2026-10-30 | 통과 | 1 매우 좋음, 2 좋음, 3 보통, 4 나쁨, 5 매우 나쁨 순서와 value 1~5 일치 |  | http://localhost/assessments/new |
| UI-022 | 2026-10-30 | 통과 | 있음은 chronicDisease true, 없음은 false. 둘 다 POST HTTP 201 |  | http://localhost/assessments/new |
| UI-023 | 2026-10-30 | 실패 | 한 번 클릭 후 버튼은 "AI 분석 중..."이고 disabled, 추가 클릭은 거절되며 POST 1건. 버튼이 막히기 전 같은 차례의 연속 click()은 POST 2건 | BUG-UI-023 | http://localhost/assessments/new |
| UI-024 | 2026-10-30 | 통과 | 클릭 직후 버튼 문구 "AI 분석 중..."이고 disabled |  | http://localhost/assessments/new |
| UI-025 | 2026-10-30 | 통과 | 폼에 남고 alert "API 502: AI 서버 호출에 실패했습니다." |  | http://localhost/assessments/new |
| UI-026 | 2026-10-30 | 통과 | `/`, `/dashboard`, `/assessments/new`, `/assessments/2/result` 새로고침 모두 HTTP 200. 헤더와 해당 화면 문구 복구. Nginx 404 없음 |  | http://localhost/assessments/2/result |
| UI-027 | 2026-10-30 | 통과 | 375px에서 scrollWidth=clientWidth=375. 가로로 넓은 요소 없음. 이름 입력과 직무 선택 가능. 세로 스크롤은 있음 |  | http://localhost/assessments/new |
| UI-028 | 2026-10-30 | 통과 | Tab 순서 name, age, health, chronic, hours, job, 제출 버튼. 버튼에서 Enter로 제출됨. 닫힌 select는 ArrowDown만으로 값이 바뀌지 않음 |  | http://localhost/assessments/new |
| UI-029 | 2026-10-30 | 통과 | `<div role="alert">이름을 입력해주세요.</div>` |  | http://localhost/assessments/new |

## 한눈에 보기

| ID | 우선순위 | 시나리오 | 판정 |
|---|---|---|---|
| UI-001 | P0 | 첫 화면 열기 | 통과 |
| UI-002 | P1 | 새 평가 페이지 이동 | 통과 |
| UI-003 | P0 | 직무 8개 표시 | 통과 |
| UI-004 | P1 | 직무 명칭과 위치 표시 | 통과 |
| UI-005 | P1 | 직무 전환 | 통과 |
| UI-006 | P0 | 필수 이름 빈값 | 통과 |
| UI-007 | P1 | 공백 이름 | 통과 |
| UI-008 | P1 | 이름 앞뒤 공백 | 통과 |
| UI-009 | P1 | 연령 0 | 통과 |
| UI-010 | P1 | 연령 1 | 통과 |
| UI-011 | P1 | 연령 120 | 통과 |
| UI-012 | P1 | 연령 121 | 통과 |
| UI-013 | P1 | 연령 음수 | 통과 |
| UI-014 | P1 | 연령 소수 | 통과 |
| UI-015 | P1 | 근무시간 0 | 통과 |
| UI-016 | P1 | 근무시간 1 | 통과 |
| UI-017 | P1 | 근무시간 24 | 통과 |
| UI-018 | P1 | 근무시간 25 | 통과 |
| UI-019 | P1 | 근무시간 소수 | 통과 |
| UI-020 | P1 | 직무 미선택 | 통과 |
| UI-021 | P1 | 건강 상태 옵션 | 통과 |
| UI-022 | P1 | 만성질환 있음/없음 | 통과 |
| UI-023 | P1 | 중복 클릭 | **실패** |
| UI-024 | P1 | 처리 중 표시 | 통과 |
| UI-025 | P1 | API 오류 안내 | 통과 |
| UI-026 | P1 | 새로고침 복구 | 통과 |
| UI-027 | P1 | 모바일 375px | 통과 |
| UI-028 | P1 | 키보드 탐색 | 통과 |
| UI-029 | P1 | 오류 메시지 접근성 | 통과 |

## 환경

- 브라우저: Google Chrome 156.0.8078.79, headless. Playwright 1.56.1이 이 Chrome을 조작했다.
- 화면: `if-app-stack-frontend-1` 가 80번 포트. Nginx가 빌드된 React를 주고 `/api` 는 Spring으로 넘긴다.
- API: Spring `127.0.0.1:8080`, AI `127.0.0.1:8000`. AI `/health` 는 `{"status":"ok"}`.
- 테스트 시작 전 평가 데이터는 1건이었다. id 2, 이름 홍길동, 주차 관리원, 48점 MID.
- 제출이 필요한 케이스는 실제 `POST /api/assessments` 를 보냈다. 그래서 생긴 평가 id 3~21은 확인 후 `DELETE` 했다. 종료 후 요약은 다시 `totalCount 1`, `analyzedCount 1` 이다. id 2는 지우지 않았다.

정상 제출에 같이 쓴 기본값은 이름 외의 칸이 나이 70, 건강 3, 만성질환 없음, 근무 8시간, 직무 id 1(아파트 야간 경비원)이다. 케이스에서 보는 칸만 바꿨다.

## 수행 순서

1. `http://localhost` 와 `GET /api/jobs` 가 살아 있는지 확인했다. 직무는 8개였다.
2. Chrome으로 케이스마다 새 페이지를 열고, 사람이 하는 순서대로 클릭·입력했다.
3. 네트워크에서 `POST /api/assessments` 횟수와 JSON 본문을 기록했다.
4. 화면 문구, `role=alert`, 버튼 disabled, 주소, 콘솔 `pageerror` 를 확인했다.
5. 케이스마다 전체 화면을 `screenshots/UI-xxx.png` 로 저장했다.
6. 만든 평가를 삭제하고 건수가 원래대로 돌아왔는지 다시 조회했다.

1차 실행에서 UI-008, UI-010, UI-011, UI-016, UI-017, UI-022는 클릭 **다음**에 요청 대기를 걸어서, 이미 나간 POST를 놓치고 타임아웃이 났다. 서버에는 201이 들어가 평가가 생겼다. 같은 날 클릭 **전에** 요청을 기다리도록 바꿔 다시 실행했고, 아래 본문은 재실행 결과다. UI-023도 버튼 상태를 결과 화면으로 넘어간 뒤에 재서 잘못 읽었다. 분석 중 화면에서 다시 쟀다.

## 케이스별 과정과 결과

### UI-001 첫 화면 열기 — 통과

- 절차: `http://localhost/` 를 연다.
- 기대: 메인 화면이 오류 없이 표시된다.
- 결과: HTTP 200. 클라이언트 라우터가 `/dashboard` 로 보낸다. 제목 "평가 대시보드", 카드 "총 평가 건수 / 고위험 / AI 분석 완료", 버튼 "새로운 평가 시작"이 보인다. `role=alert` 없음. 콘솔 오류 0, pageerror 0.
- 캡처: `screenshots/UI-001.png`

### UI-002 새 평가 페이지 이동 — 통과

- 절차: 대시보드에서 "새로운 평가 시작"을 누른다. 화면에는 "새로운 평가 메뉴"라는 메뉴는 없고 이 버튼이 그 역할이다.
- 기대: 입력 폼이 렌더링된다.
- 결과: 주소 `/assessments/new`. 라벨 이름, 연령, 건강 상태, 만성질환, 하루 근무 가능 시간, 직무와 버튼 "위험도 분석 시작"이 있다.
- 캡처: `screenshots/UI-002.png`

### UI-003 직무 8개 표시 — 통과

- 절차: `GET /api/jobs` 건수와 직무 선택창의 항목 수를 비교한다.
- 기대: API와 같은 8개.
- 결과: API 8건. 선택창은 "선택하세요"를 빼면 8개.
- 캡처: `screenshots/UI-003.png`

### UI-004 직무 명칭과 위치 표시 — 통과

- 절차: 옵션 문구를 API의 `jobTitle`, `workplace` 와 한 줄씩 비교한다.
- 기대: 둘이 일치한다.
- 결과: 표시 형식은 `직무명 (근무지)` 이고 value는 직무 id다.

| id | 화면 문구 |
|---|---|
| 1 | 아파트 야간 경비원 (서울 강남구) |
| 2 | 택배 배송 기사 (경기 성남시) |
| 3 | 건물 청소원 (서울 종로구) |
| 4 | 요양보호사 (인천 남동구) |
| 5 | 시설 관리원 (부산 해운대구) |
| 6 | 주차 관리원 (대구 수성구) |
| 7 | 학교 급식 보조원 (광주 북구) |
| 8 | 사무 보조원 (대전 서구) |

- 캡처: `screenshots/UI-004.png`

### UI-005 직무 전환 — 통과

- 절차: 이름 전환테스트, 나이 65, 건강 2, 만성질환 있음, 근무 6시간을 넣은 뒤 직무 1을 고르고, 이어서 직무 2를 고른다.
- 기대: 선택값만 바뀐다.
- 결과: `job` 만 `"1"` 에서 `"2"` 로 바뀌었다. 나머지 다섯 칸은 그대로였다.
- 캡처: `screenshots/UI-005.png`

### UI-006 필수 이름 빈값 — 통과

- 절차: 이름은 비우고 나이 70, 근무 8, 직무 1을 넣은 뒤 분석을 누른다. 0.8초 동안 POST를 감시한다.
- 기대: 이름 입력 요청, POST 없음.
- 결과: `role=alert` 문구 "이름을 입력해주세요." POST 0건.
- 캡처: `screenshots/UI-006.png`

### UI-007 공백 이름 — 통과

- 절차: 이름에 공백 3칸만 넣고, 나머지 검증은 통과하도록 나이·근무·직무를 채운 뒤 제출한다.
- 기대: 이름 필수 오류, POST 없음.
- 결과: UI-006과 같은 문구. `trim()` 뒤 빈 문자열로 막힌다. POST 0건.
- 캡처: `screenshots/UI-007.png`

### UI-008 이름 앞뒤 공백 — 통과

- 절차: 이름 `"  홍길동  "` 와 나머지 정상값을 넣고 실제 서버로 제출한다.
- 기대: trim된 이름이 전송된다.
- 결과: POST 1건, HTTP 201. 본문 `applicantName` 은 `"홍길동"`. 나이 70, 건강 3, 만성질환 false, 근무 8, jobId 1. 클릭 직후 검증 alert는 없었다.
- 캡처: `screenshots/UI-008.png`

### UI-009 연령 0 — 통과

- 절차: 나머지 정상, 나이 0으로 제출.
- 기대: 1~120 검증 실패.
- 결과: "연령은 1~120 사이로 입력해주세요." POST 0건.
- 캡처: `screenshots/UI-009.png`

### UI-010 연령 1 — 통과

- 절차: 이름 "나이1", 나이 1, 나머지 정상으로 실제 제출.
- 기대: 프론트 검증 통과.
- 결과: 검증 alert 없이 POST 1건, HTTP 201. body `age` 는 숫자 1.
- 캡처: `screenshots/UI-010.png`

### UI-011 연령 120 — 통과

- 절차: 이름 "나이120", 나이 120, 나머지 정상으로 실제 제출.
- 기대: 프론트 검증 통과.
- 결과: POST 1건, HTTP 201. body `age` 는 120.
- 캡처: `screenshots/UI-011.png`

### UI-012 연령 121 — 통과

- 결과: "연령은 1~120 사이로 입력해주세요." POST 0건.
- 캡처: `screenshots/UI-012.png`

### UI-013 연령 음수 — 통과

- 절차: 나이 -1.
- 결과: 같은 연령 오류. POST 0건.
- 캡처: `screenshots/UI-013.png`

### UI-014 연령 소수 — 통과

- 절차: 나이 60.5.
- 결과: `Number.isInteger` 가 아니므로 같은 연령 오류. POST 0건.
- 캡처: `screenshots/UI-014.png`

### UI-015 근무시간 0 — 통과

- 결과: "근무 가능 시간은 1~24 사이로 입력해주세요." POST 0건.
- 캡처: `screenshots/UI-015.png`

### UI-016 근무시간 1 — 통과

- 절차: 이름 "시간1", 근무 1시간, 나머지 정상으로 실제 제출.
- 결과: 검증 alert 없이 POST 1건, HTTP 201. `workHourLimit` 1.
- 캡처: `screenshots/UI-016.png`

### UI-017 근무시간 24 — 통과

- 절차: 이름 "시간24", 근무 24시간.
- 결과: POST 1건, HTTP 201. `workHourLimit` 24.
- 캡처: `screenshots/UI-017.png`

### UI-018 근무시간 25 — 통과

- 결과: 근무시간 범위 오류. POST 0건.
- 캡처: `screenshots/UI-018.png`

### UI-019 근무시간 소수 — 통과

- 절차: 7.5시간.
- 결과: 정수가 아니라 같은 근무시간 오류. POST 0건.
- 캡처: `screenshots/UI-019.png`

### UI-020 직무 미선택 — 통과

- 절차: 이름, 나이, 근무는 정상. 직무는 "선택하세요" 그대로 제출.
- 기대: 직무 선택 요청, POST 없음.
- 결과: "직무를 선택해주세요." POST 0건.
- 캡처: `screenshots/UI-020.png`

### UI-021 건강 상태 옵션 — 통과

- 절차: `#health` 의 option을 위부터 읽는다.
- 기대: 다섯 단계가 그 순서대로다.
- 결과: value와 문구가 아래와 같다. 기본 선택은 3이다.

1. `1` 1 - 매우 좋음
2. `2` 2 - 좋음
3. `3` 3 - 보통
4. `4` 4 - 나쁨
5. `5` 5 - 매우 나쁨

- 캡처: `screenshots/UI-021.png`

### UI-022 만성질환 토글 — 통과

- 절차: 같은 정상값으로 두 번 제출한다. 한 번은 있음, 한 번은 없음.
- 기대: `true` / `false` 가 그대로 전송된다.
- 결과: 있음은 HTTP 201, `chronicDisease: true`. 없음은 HTTP 201, `chronicDisease: false`.
- 캡처: `screenshots/UI-022-yes.png`, `screenshots/UI-022-no.png`

### UI-023 중복 클릭 — 실패

기대는 두 가지다. 분석 중에는 버튼이 비활성이고, 연속 클릭으로 제출이 두 번 나가지 않아야 한다.

다시 잰 결과:

1. 정상 입력 후 한 번 클릭하면 버튼이 `AI 분석 중...` 이고 `disabled=true` 다. 그 상태에서 한 번 더 누르려 하면 Chrome이 비활성 버튼 클릭을 거절한다. 여기까지 POST는 1건이다.
2. 화면이 그 상태로 바뀌기 전에, 같은 실행에서 `button.click()` 을 두 번 연속 호출하면 POST가 **2건** 나간다. 두 번째 클릭이 처리될 때는 아직 disabled가 아니라서 제출 함수가 두 번 돈다. 직후 버튼은 `AI 분석 중...` / disabled가 된다. 두 요청 모두 평가 행을 만들었고, 테스트 후 삭제했다.

그래서 "분석 중 비활성"은 맞고, "중복 제출 방지"는 첫 클릭과 두 번째 클릭이 맞붙으면 막히지 않는다. 케이스 판정은 실패다.

원인 위치는 `web-vite/src/pages/AssessmentFormPage.tsx` 의 `handleSubmit` 이다. `setSubmitting(true)` 는 클릭 처리가 끝난 뒤 다시 그려질 때 버튼에 반영된다. 그 전에 들어온 클릭은 `submitting` 이 아직 false라 또 POST한다.

- 캡처: `screenshots/UI-023.png` (한 번 클릭 후 비활성), `screenshots/UI-023-burst.png` (같은 순간 두 번 클릭)

### UI-024 처리 중 표시 — 통과

- 절차: 정상 입력 후 분석을 누르고, 서버 응답 전에 버튼을 본다.
- 기대: "AI 분석 중"이 보인다.
- 결과: 버튼 문구가 "AI 분석 중..."으로 바뀌고 disabled다.
- 캡처: `screenshots/UI-024.png`

### UI-025 API 오류 안내 — 통과

- 절차: 화면과 `GET /api/jobs` 는 실제 서버를 쓴다. 브라우저가 보낸 `POST /api/assessments` 에만 Spring 오류와 같은 JSON을 502로 돌려준다. 본문은 `message: "AI 서버 호출에 실패했습니다."`, `errorCode: "AI_ERROR"`.
- 기대: 사용자가 읽을 수 있는 오류가 보인다.
- 결과: 폼에 그대로 있고 `role=alert` 문구는 `API 502: AI 서버 호출에 실패했습니다.` 이다. 빈 화면이나 스택 추적은 나오지 않았다.
- 캡처: `screenshots/UI-025.png`

### UI-026 새로고침 복구 — 통과

- 절차: 각 주소를 연 뒤 새로고침하고, 헤더와 그 화면의 문구가 다시 나오는지 본다.
- 기대: SPA가 복구된다. Nginx 404 페이지가 아니어야 한다.

| 주소 | 새로고침 | 최종 주소 | 확인한 문구 |
|---|---|---|---|
| `http://localhost/` | HTTP 200 | `/dashboard` | 평가 대시보드 |
| `http://localhost/dashboard` | HTTP 200 | `/dashboard` | 평가 대시보드 |
| `http://localhost/assessments/new` | HTTP 200 | `/assessments/new` | 새로운 평가 |
| `http://localhost/assessments/2/result` | HTTP 200 | 같은 주소 | 홍길동 |

네 곳 모두 상단 "고령자 위험도 판단 시스템"이 다시 보였고, pageerror는 없었다. 결과 화면은 테스트 전에 있던 id 2를 썼다.

- 캡처: `screenshots/UI-026.png` (마지막인 결과 화면)

### UI-027 모바일 레이아웃 — 통과

- 절차: 뷰포트를 375×812로 두고 평가 폼을 연다. 이름 "모바일"을 넣고 직무 3(건물 청소원)을 고른다. `documentElement.scrollWidth` 와 화면보다 넓은 요소를 센다.
- 기대: 가로로 넘치지 않고 입력을 조작할 수 있다.
- 결과: clientWidth 375, scrollWidth 375. 375px보다 넓은 요소 0개. 이름 칸과 분석 버튼 너비는 각각 277px. 입력과 직무 선택이 됐다. 버튼은 첫 화면 높이 아래에 있어서 세로 스크롤이 필요하다. 가로 스크롤은 없다.
- 캡처: `screenshots/UI-027.png`

### UI-028 키보드 탐색 — 통과

- 절차: 이름 칸에서 Tab을 여섯 번 눌러 포커스 순서를 적는다. 키보드로 이름을 치고, 건강·직무에서 ArrowDown을 누른 뒤, 제출 버튼에서 Enter를 누른다.
- 기대: 입력, 선택, 제출에 키보드로 도달할 수 있다.
- 결과: 포커스 순서는 `name → age → health → chronic → hours → job → 제출 버튼` 이다. 이름에는 "키보드"가 입력됐다. 제출 버튼에서 Enter를 누르면 나이 칸이 비어 있어 "연령은 1~120 사이로 입력해주세요."가 뜬다. 버튼이 `type="button"` 이라 입력칸 안의 Enter만으로는 제출되지 않고, 버튼까지 이동한 Enter로는 제출된다.
- 비고: 닫혀 있는 건강 select와 직무 select에서 ArrowDown만 눌렀을 때 값은 바뀌지 않았다. 건강은 기본값 3, 직무는 빈 값 그대로였다. 이 헤드리스 Chrome에서는 네이티브 선택 목록이 열리지 않아 값 변경까지는 확인하지 못했다. 두 칸은 Tab 순서에 있고 라벨이 연결되어 있다.
- 캡처: `screenshots/UI-028.png`

### UI-029 오류 메시지 접근성 — 통과

- 절차: 빈 폼에서 분석을 누르고 `[role=alert]` 를 읽는다.
- 기대: 오류 문구가 안내용 속성으로 렌더링된다.
- 결과: `<div role="alert">이름을 입력해주세요.</div>`
- 캡처: `screenshots/UI-029.png`

## 실패한 항목만 다시 정리

UI-023만 실패다. 버튼은 분석이 시작된 뒤 비활성화되지만, 그 전에 들어온 두 번째 클릭은 막지 못한다. 더블클릭이나 아주 빠른 연타면 평가가 두 건 생긴다.

고치려면 클릭 순간에 `submitting` 이 true가 된 뒤에만 요청을 보내거나, 요청 함수 앞에 동기 잠금이 하나 있으면 된다. 이번 작업에서는 테스트와 기록만 했다.

## TC-20261030-1522 / IF-0001
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0001
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 이름=''
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 이름 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 이름 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「」. alert 「이름을 입력해주세요.」. POST 0건. 평가 건수 1→1. | 화면: screenshots/IF-0001.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0002
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0002
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 이름=' '
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 이름 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 이름 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「 」. alert 「이름을 입력해주세요.」. POST 0건. 평가 건수 1→1. | 화면: screenshots/IF-0002.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0003
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0003
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 이름='홍길동'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 이름 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 이름 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"홍길동","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":43}. 평가 1→2. | 화면: screenshots/IF-0003.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0004
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0004
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 이름=' 홍길동 '
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 이름 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 이름 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"홍길동","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":44}. 평가 2→3. DB 홍길동|72|3|false|8|아파트 야간 경비원. | 화면: screenshots/IF-0004.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0005
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0005
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 이름='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 이름 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 이름 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":45}. 평가 3→4. | 화면: screenshots/IF-0005.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0006
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0006
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 이름='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 이름 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 이름 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 현재 프론트 검증은 길이를 확인하지 않음. 백엔드 50자 제한 응답 확인 | 실제: POST 1건 HTTP 400. payload {"applicantName":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"success":false,"data":null,"message":"applicantName: 크기가 0에서 50 사이여야 합니다","errorCode":"VALIDATION_ERROR"}. 평가 4→4. 프론트는 길이를 막지 않고, 백엔드 50자 제한 응답을 확인한다. | 화면: screenshots/IF-0006.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0007
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0007
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 이름='한글😀'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 이름 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 이름 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"한글😀","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":46}. 평가 4→5. | 화면: screenshots/IF-0007.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0008
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0008
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='-1'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「-1」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 5→5. | 화면: screenshots/IF-0008.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0009
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0009
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='0'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「0」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 5→5. | 화면: screenshots/IF-0009.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0010
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0010
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='1'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":1,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":47}. 평가 5→6. | 화면: screenshots/IF-0010.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0011
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0011
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='2'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":2,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":48}. 평가 6→7. | 화면: screenshots/IF-0011.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0012
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0012
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='60'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":60,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":49}. 평가 7→8. | 화면: screenshots/IF-0012.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0013
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0013
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='90'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":90,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":50}. 평가 8→9. | 화면: screenshots/IF-0013.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0014
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0014
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='119'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":119,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":51}. 평가 9→10. | 화면: screenshots/IF-0014.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0015
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0015
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='120'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":120,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":52}. 평가 10→11. | 화면: screenshots/IF-0015.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0016
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0016
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='121'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「121」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. | 화면: screenshots/IF-0016.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0017
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0017
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='60.5'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「60.5」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. | 화면: screenshots/IF-0017.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0018
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0018
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령='abc'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 숫자 입력칸은 abc를 남기지 않아 표시값은 빈 문자열. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 변화 없음. | 화면: screenshots/IF-0018.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0019
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0019
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 연령=''
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 연령 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 연령 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. | 화면: screenshots/IF-0019.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0020
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0020
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='-1'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「-1」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. | 화면: screenshots/IF-0020.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0021
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0021
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='0'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「0」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. | 화면: screenshots/IF-0021.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0022
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0022
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='1'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":1,"jobId":1}. 응답 {"id":53}. 평가 11→12. | 화면: screenshots/IF-0022.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0023
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0023
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='7'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":7,"jobId":1}. 응답 {"id":54}. 평가 12→13. | 화면: screenshots/IF-0023.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0024
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0024
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='8'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":55}. 평가 13→14. | 화면: screenshots/IF-0024.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0025
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0025
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='23'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":23,"jobId":1}. 응답 {"id":56}. 평가 14→15. | 화면: screenshots/IF-0025.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0026
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0026
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='24'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 프론트 검증 통과; POST 제출 시도 | 실제: POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":24,"jobId":1}. 응답 {"id":57}. 평가 15→16. | 화면: screenshots/IF-0026.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0027
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0027
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='25'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「25」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 16→16. | 화면: screenshots/IF-0027.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0028
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0028
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='7.5'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「7.5」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 16→16. | 화면: screenshots/IF-0028.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0029
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0029
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간='abc'
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 숫자 입력칸은 abc를 남기지 않아 표시값은 빈 문자열. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 변화 없음. | 화면: screenshots/IF-0029.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0030
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0030
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 근무시간=''
- test_type: e2e
- tool_a: 브라우저 DevTools Network+Console
- command_a: 1. 평가 입력 접속 2. 근무시간 입력 3. 제출 클릭 4. Network POST 발생 유무 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 근무시간 → 값 변환 → 유효성 → 제출
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 안내 및 POST 0건 | 실제: 입력값 표시 「」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 16→16. | 화면: screenshots/IF-0030.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0031
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0031
- timestamp: 2026-10-30T15:22:00+09:00
- feature: physicalLevel=1
- test_type: e2e
- tool_a: Network Payload
- command_a: 1. 건강 상태 선택 2. 제출 클릭 3. Payload physicalLevel 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 건강 상태 선택 → 숫자 직렬화
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: Payload physicalLevel 숫자 1 | 실제: POST 1건 HTTP 201. payload.physicalLevel=1. DB physical_level=1. 평가 16→17. | 화면: screenshots/IF-0031.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0032
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0032
- timestamp: 2026-10-30T15:22:00+09:00
- feature: physicalLevel=2
- test_type: e2e
- tool_a: Network Payload
- command_a: 1. 건강 상태 선택 2. 제출 클릭 3. Payload physicalLevel 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 건강 상태 선택 → 숫자 직렬화
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: Payload physicalLevel 숫자 2 | 실제: POST 1건 HTTP 201. payload.physicalLevel=2. DB physical_level=2. 평가 17→18. | 화면: screenshots/IF-0032.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0033
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0033
- timestamp: 2026-10-30T15:22:00+09:00
- feature: physicalLevel=3
- test_type: e2e
- tool_a: Network Payload
- command_a: 1. 건강 상태 선택 2. 제출 클릭 3. Payload physicalLevel 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 건강 상태 선택 → 숫자 직렬화
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: Payload physicalLevel 숫자 3 | 실제: POST 1건 HTTP 201. payload.physicalLevel=3. DB physical_level=3. 평가 18→19. | 화면: screenshots/IF-0033.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0034
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0034
- timestamp: 2026-10-30T15:22:00+09:00
- feature: physicalLevel=4
- test_type: e2e
- tool_a: Network Payload
- command_a: 1. 건강 상태 선택 2. 제출 클릭 3. Payload physicalLevel 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 건강 상태 선택 → 숫자 직렬화
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: Payload physicalLevel 숫자 4 | 실제: POST 1건 HTTP 201. payload.physicalLevel=4. DB physical_level=4. 평가 19→20. | 화면: screenshots/IF-0034.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0035
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0035
- timestamp: 2026-10-30T15:22:00+09:00
- feature: physicalLevel=5
- test_type: e2e
- tool_a: Network Payload
- command_a: 1. 건강 상태 선택 2. 제출 클릭 3. Payload physicalLevel 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 건강 상태 선택 → 숫자 직렬화
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: Payload physicalLevel 숫자 5 | 실제: POST 1건 HTTP 201. payload.physicalLevel=5. DB physical_level=5. 평가 20→21. | 화면: screenshots/IF-0035.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0036
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0036
- timestamp: 2026-10-30T15:22:00+09:00
- feature: chronicDisease=no
- test_type: e2e
- tool_a: Network + DB
- command_a: 선택 → 제출 → Network Payload 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 만성질환 선택 → 불리언 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: Payload chronicDisease=false | 실제: HTTP 201. payload.chronicDisease=false. DB chronic_disease_flag=false. | 화면: screenshots/IF-0036.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0037
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0037
- timestamp: 2026-10-30T15:22:00+09:00
- feature: chronicDisease=yes
- test_type: e2e
- tool_a: Network + DB
- command_a: 선택 → 제출 → Network Payload 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 만성질환 선택 → 불리언 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: Payload chronicDisease=true | 실제: HTTP 201. payload.chronicDisease=true. DB chronic_disease_flag=true. | 화면: screenshots/IF-0037.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0038
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0038
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 직무 미선택
- test_type: e2e
- tool_a: Network Response/Payload
- command_a: 1. /api/jobs 결과 확인 2. 직무 변경 3. 제출 및 Payload 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: jobs 응답→옵션 구성→선택→POST
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 경고 및 POST 0건 | 실제: alert 「직무를 선택해주세요.」. POST 0건. | 화면: screenshots/IF-0038.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0039
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0039
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 직무 1
- test_type: e2e
- tool_a: Network Response/Payload
- command_a: 1. /api/jobs 결과 확인 2. 직무 변경 3. 제출 및 Payload 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: jobs 응답→옵션 구성→선택→POST
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: jobId 숫자 1 | 실제: HTTP 201. payload.jobId=1. 결과 화면 「IF-0039 · 72세 · 아파트 야간 경비원」. 기대 직무명 아파트 야간 경비원. | 화면: screenshots/IF-0039.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0040
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0040
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 직무 2
- test_type: e2e
- tool_a: Network Response/Payload
- command_a: 1. /api/jobs 결과 확인 2. 직무 변경 3. 제출 및 Payload 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: jobs 응답→옵션 구성→선택→POST
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: jobId 숫자 2 | 실제: HTTP 201. payload.jobId=2. 결과 화면 「IF-0040 · 72세 · 택배 배송 기사」. 기대 직무명 택배 배송 기사. | 화면: screenshots/IF-0040.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0041
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0041
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 로딩
- test_type: e2e
- tool_a: Playwright + Network
- command_a: Network Mock 또는 전용 테스트 환경에서 시나리오 주입 → DOM/요청/라우팅 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 조회/제출 상태 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 직무 목록 요청이 끝나기 전 빈 목록 상태 확인 | 실제: 응답 전 옵션 1개 「선택하세요」. 응답 후 9개. | 화면: screenshots/IF-0041.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0042
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0042
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 조회 실패
- test_type: e2e
- tool_a: Playwright + Network
- command_a: Network Mock 또는 전용 테스트 환경에서 시나리오 주입 → DOM/요청/라우팅 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 조회/제출 상태 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 직무 목록 오류 메시지 표시 | 실제: alert 「직무 목록을 불러오지 못했습니다.」. 직무 옵션 1개. | 화면: screenshots/IF-0042.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0044
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0044
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 제출 실패
- test_type: e2e
- tool_a: Playwright + Network
- command_a: Network Mock 또는 전용 테스트 환경에서 시나리오 주입 → DOM/요청/라우팅 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 조회/제출 상태 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 표시, submitting=false 복구 | 실제: POST 1건. alert 「API 500: 서버 오류가 발생했습니다.」. 버튼 「위험도 분석 시작」 enabled=true. | 화면: screenshots/IF-0044.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0045
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0045
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 제출 성공
- test_type: e2e
- tool_a: Playwright + Network
- command_a: Network Mock 또는 전용 테스트 환경에서 시나리오 주입 → DOM/요청/라우팅 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 조회/제출 상태 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: /assessments/{id}/result로 이동 | 실제: 이동 주소 http://localhost/assessments/845/result. | 화면: screenshots/IF-0045.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0046
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0046
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 빈 응답
- test_type: e2e
- tool_a: Playwright + Network
- command_a: Network Mock 또는 전용 테스트 환경에서 시나리오 주입 → DOM/요청/라우팅 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 조회/제출 상태 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: API 클라이언트 또는 라우팅 예외 동작 기록 | 실제: 201 본문 {} 이면 id가 없어 주소는 http://localhost/assessments/undefined/result. alert 「API 500: 서버 오류가 발생했습니다.」. | 화면: screenshots/IF-0046.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0269
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0269
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 로딩 중
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 불러오는 중 표시 | 실제: 지연 중 「불러오는 중...」 표시=true. 응답 후 이름 표시. | 화면: screenshots/IF-0269.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0270
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0270
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 없는 결과
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 메시지 | 실제: alert 「API 404: 평가를 찾을 수 없습니다.」. | 화면: screenshots/IF-0270.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0271
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0271
- timestamp: 2026-10-30T15:22:00+09:00
- feature: AI 미완료
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 아직 AI 분석 결과 없음 | 실제: 문구 「아직 AI 분석 결과가 없습니다.」 표시. | 화면: screenshots/IF-0271.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0272
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0272
- timestamp: 2026-10-30T15:22:00+09:00
- feature: LOW 등급
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 낮음 배지 | 실제: 배지 「위험도 낮음」 표시. | 화면: screenshots/IF-0272.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0273
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0273
- timestamp: 2026-10-30T15:22:00+09:00
- feature: MID 등급
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 보통 배지 | 실제: 배지 「위험도 보통」 표시. | 화면: screenshots/IF-0273.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0274
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0274
- timestamp: 2026-10-30T15:22:00+09:00
- feature: HIGH 등급
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 높음 배지 | 실제: 배지 「위험도 높음」 표시. | 화면: screenshots/IF-0274.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0275
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0275
- timestamp: 2026-10-30T15:22:00+09:00
- feature: AI 기본 설명
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 기본 설명 표시 | 실제: 「기본 설명 (생성형 AI 미사용)」 표시. | 화면: screenshots/IF-0275.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0276
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0276
- timestamp: 2026-10-30T15:22:00+09:00
- feature: Gemini 설명
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: Gemini 작성 문구 표시 | 실제: 「생성형 AI(Gemini)가 작성」 표시. | 화면: screenshots/IF-0276.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0277
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0277
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 요인 0개
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 요인 카드 생략 | 실제: 요인 0개. 점수 구성 카드 없음. | 화면: screenshots/IF-0277.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0278
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0278
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 요인 1개
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 이름·점수·최댓값 표시 | 실제: 요인 「연령」과 「10 / 20점」 표시. | 화면: screenshots/IF-0278.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0279
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0279
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 요인 max=0
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 진행 막대 0% | 실제: 만점 0 막대 width=0%. | 화면: screenshots/IF-0279.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0280
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0280
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 태스크 0개
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: ML/DL 테이블 생략 | 실제: 태스크 0개. ML/DL 표 없음. | 화면: screenshots/IF-0280.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0281
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0281
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 태스크 확률 0.123
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 12%로 반올림 | 실제: 표 칸 야간 | 12% | 0%. | 화면: screenshots/IF-0281.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0282
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0282
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 목록으로
- test_type: e2e
- tool_a: Playwright
- command_a: 결과 API 응답 mock → 화면 방문 → 특정 DOM 및 수치 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/RiskResultPage.tsx
- function: RiskResultPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: /dashboard 이동 | 실제: 이동 주소 http://localhost/dashboard. | 화면: screenshots/IF-0282.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0283
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0283
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 목록 로딩
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 로딩 문구 | 실제: 목록 지연 중 「불러오는 중...」 표시=true. | 화면: screenshots/IF-0283.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0284
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0284
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 목록 빈 배열
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 빈 목록 문구 | 실제: 빈 content. 「아직 등록된 평가 기록이 없습니다.」 표시. | 화면: screenshots/IF-0284.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0285
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0285
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 목록 응답 오류
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 배너 | 실제: alert 「API 500: 목록 실패」. | 화면: screenshots/IF-0285.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0286
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0286
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 요약 null
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 0 표시 | 실제: summary null. 카드 0건, 0건, 0건. | 화면: screenshots/IF-0286.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0287
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0287
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 요약 3/1/2
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 각 카드 숫자 매핑 | 실제: 카드 3건, 1건, 2건. | 화면: screenshots/IF-0287.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0288
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0288
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 점수 null
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: - 표시 | 실제: 행 QA_CASE | 72세 | 아파트 야간 경비원 | - | 낮음 | 결과 보기삭제. | 화면: screenshots/IF-0288.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0289
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0289
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 등급 null
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 분석 전 표시 | 실제: 등급 null. 「분석 전」 표시. | 화면: screenshots/IF-0289.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0290
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0290
- timestamp: 2026-10-30T15:22:00+09:00
- feature: page=0
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: size=20,page=0 | 실제: 첫 목록 요청 GET http://localhost/api/assessments?page=0&size=20. | 화면: screenshots/IF-0290.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0291
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0291
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 페이지 다음
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: page 1 요청 | 실제: page=1 요청 1건. GET http://localhost/api/assessments?page=1&size=20 | 화면: screenshots/IF-0291.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0292
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0292
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 첫 페이지 이전
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 이전 버튼 disabled | 실제: 첫 페이지 이전 버튼 disabled=true. | 화면: screenshots/IF-0292.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0293
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0293
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 마지막 페이지 다음
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 다음 disabled | 실제: 마지막 페이지 다음 버튼 disabled=true. | 화면: screenshots/IF-0293.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0294
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0294
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 삭제 취소
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: DELETE 요청 0 | 실제: confirm 취소. DELETE 0건. | 화면: screenshots/IF-0294.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0295
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0295
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 삭제 승인
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: DELETE 1회 + 목록 갱신 | 실제: confirm 승인. DELETE 1건. 목록 요청 2회. 화면에 갱신됨 표시. | 화면: screenshots/IF-0295.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0296
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0296
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 삭제 500
- test_type: e2e
- tool_a: Playwright
- command_a: API/confirm mock → 페이지 조작 → Network/화면 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/DashboardPage.tsx
- function: DashboardPage 조건 렌더링
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 오류 배너 | 실제: alert 「API 500: 삭제 실패」. 행 유지=1. | 화면: screenshots/IF-0296.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0297
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0297
- timestamp: 2026-10-30T15:22:00+09:00
- feature: HTTP 200 JSON
- test_type: e2e
- tool_a: Vitest 또는 Playwright Mock
- command_a: fetch mock 응답 제공 → apiRequest 호출 → 반환/예외 검증
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/shared/api/client.ts
- function: apiRequest 상태 응답 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: JSON 파싱 | 실제: 반환 {"ok":true,"n":7}. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0298
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0298
- timestamp: 2026-10-30T15:22:00+09:00
- feature: HTTP 204
- test_type: e2e
- tool_a: Vitest 또는 Playwright Mock
- command_a: fetch mock 응답 제공 → apiRequest 호출 → 반환/예외 검증
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/shared/api/client.ts
- function: apiRequest 상태 응답 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: undefined 반환 | 실제: 204 반환 undefined. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0299
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0299
- timestamp: 2026-10-30T15:22:00+09:00
- feature: Content-Length=0
- test_type: e2e
- tool_a: Vitest 또는 Playwright Mock
- command_a: fetch mock 응답 제공 → apiRequest 호출 → 반환/예외 검증
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/shared/api/client.ts
- function: apiRequest 상태 응답 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: undefined 반환 | 실제: content-length 0 반환 undefined. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0300
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0300
- timestamp: 2026-10-30T15:22:00+09:00
- feature: HTTP 400 JSON message
- test_type: e2e
- tool_a: Vitest 또는 Playwright Mock
- command_a: fetch mock 응답 제공 → apiRequest 호출 → 반환/예외 검증
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/shared/api/client.ts
- function: apiRequest 상태 응답 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: API 400: 실패 예외 | 실제: 예외 「API 400: 실패」. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0301
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0301
- timestamp: 2026-10-30T15:22:00+09:00
- feature: HTTP 500 일반 텍스트
- test_type: e2e
- tool_a: Vitest 또는 Playwright Mock
- command_a: fetch mock 응답 제공 → apiRequest 호출 → 반환/예외 검증
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/shared/api/client.ts
- function: apiRequest 상태 응답 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: API 500 및 텍스트 예외 | 실제: 예외 「API 500: Error」. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0302
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0302
- timestamp: 2026-10-30T15:22:00+09:00
- feature: JSON 깨짐
- test_type: e2e
- tool_a: Vitest 또는 Playwright Mock
- command_a: fetch mock 응답 제공 → apiRequest 호출 → 반환/예외 검증
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/shared/api/client.ts
- function: apiRequest 상태 응답 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: JSON 파싱 오류 | 실제: SyntaxError: Unexpected token 'o', "not-json" is not valid JSON | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0303
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0303
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 네트워크 단절
- test_type: e2e
- tool_a: Vitest 또는 Playwright Mock
- command_a: fetch mock 응답 제공 → apiRequest 호출 → 반환/예외 검증
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/shared/api/client.ts
- function: apiRequest 상태 응답 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 예외 전파 | 실제: TypeError: Failed to fetch | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0304
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0304
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 요청 Content-Type
- test_type: e2e
- tool_a: Vitest 또는 Playwright Mock
- command_a: fetch mock 응답 제공 → apiRequest 호출 → 반환/예외 검증
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/shared/api/client.ts
- function: apiRequest 상태 응답 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: application/json 헤더 | 실제: 요청 Content-Type 「application/json」. | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.


# 수동 시트 원문 TC-20261030-1522

# IF-0001 ~ IF-0046, IF-0269 ~ IF-0304 프론트 테스트 결과

실행일: 2026-10-30 15:22 (KST)
대상: `http://localhost` 에 떠 있던 화면. 모킹이 적힌 케이스는 Playwright가 응답을 대신했다.
판정: **81건 통과, 1건 실패 (IF-0043)**

원본 응답은 `results.json`, 화면 캡처는 `screenshots/` 다. 시트에 붙일 표는 `IF-0001-0304-결과표.tsv` 다.

실패 1건은 이슈 트래커에 올리지 않았다. 번호는 이 문서의 `BUG-IF-0043` 이다. 이전 UI-023(`BUG-UI-023`)과 같은 동작이다.

## 비어 있던 칸

실행 상태는 모두 `미실행`이었다. 아래가 이번 실행 값이다. 각 행의 실행일은 2026-10-30이다. 통과 건의 버그 ID는 없다.

| TC ID | 실행일 | 실행 상태 | 실제 결과 | 버그 ID | 증거 |
| --- | --- | --- | --- | --- | --- |
| IF-0001 | 2026-10-30 | 통과 | 입력값 표시 「」. alert 「이름을 입력해주세요.」. POST 0건. 평가 건수 1→1. |  | screenshots/IF-0001.png |
| IF-0002 | 2026-10-30 | 통과 | 입력값 표시 「   」. alert 「이름을 입력해주세요.」. POST 0건. 평가 건수 1→1. |  | screenshots/IF-0002.png |
| IF-0003 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"홍길동","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":43}. 평가 1→2. |  | screenshots/IF-0003.png |
| IF-0004 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"홍길동","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":44}. 평가 2→3. DB 홍길동/72/3/false/8/아파트 야간 경비원. |  | screenshots/IF-0004.png |
| IF-0005 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":45}. 평가 3→4. |  | screenshots/IF-0005.png |
| IF-0006 | 2026-10-30 | 통과 | POST 1건 HTTP 400. payload {"applicantName":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"success":false,"data":null,"message":"applicantName: 크기가 0에서 50 사이여야 합니다","errorCode":"VALIDATION_ERROR"}. 평가 4→4. 프론트는 길이를 막지 않고, 백엔드 50자 제한 응답을 확인한다. |  | screenshots/IF-0006.png |
| IF-0007 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"한글😀","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":46}. 평가 4→5. |  | screenshots/IF-0007.png |
| IF-0008 | 2026-10-30 | 통과 | 입력값 표시 「-1」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 5→5. |  | screenshots/IF-0008.png |
| IF-0009 | 2026-10-30 | 통과 | 입력값 표시 「0」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 5→5. |  | screenshots/IF-0009.png |
| IF-0010 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":1,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":47}. 평가 5→6. |  | screenshots/IF-0010.png |
| IF-0011 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":2,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":48}. 평가 6→7. |  | screenshots/IF-0011.png |
| IF-0012 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":60,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":49}. 평가 7→8. |  | screenshots/IF-0012.png |
| IF-0013 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":90,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":50}. 평가 8→9. |  | screenshots/IF-0013.png |
| IF-0014 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":119,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":51}. 평가 9→10. |  | screenshots/IF-0014.png |
| IF-0015 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":120,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":52}. 평가 10→11. |  | screenshots/IF-0015.png |
| IF-0016 | 2026-10-30 | 통과 | 입력값 표시 「121」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. |  | screenshots/IF-0016.png |
| IF-0017 | 2026-10-30 | 통과 | 입력값 표시 「60.5」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. |  | screenshots/IF-0017.png |
| IF-0018 | 2026-10-30 | 통과 | 숫자 입력칸은 abc를 남기지 않아 표시값은 빈 문자열. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 변화 없음. |  | screenshots/IF-0018.png |
| IF-0019 | 2026-10-30 | 통과 | 입력값 표시 「」. alert 「연령은 1~120 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. |  | screenshots/IF-0019.png |
| IF-0020 | 2026-10-30 | 통과 | 입력값 표시 「-1」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. |  | screenshots/IF-0020.png |
| IF-0021 | 2026-10-30 | 통과 | 입력값 표시 「0」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 11→11. |  | screenshots/IF-0021.png |
| IF-0022 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":1,"jobId":1}. 응답 {"id":53}. 평가 11→12. |  | screenshots/IF-0022.png |
| IF-0023 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":7,"jobId":1}. 응답 {"id":54}. 평가 12→13. |  | screenshots/IF-0023.png |
| IF-0024 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":8,"jobId":1}. 응답 {"id":55}. 평가 13→14. |  | screenshots/IF-0024.png |
| IF-0025 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":23,"jobId":1}. 응답 {"id":56}. 평가 14→15. |  | screenshots/IF-0025.png |
| IF-0026 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload {"applicantName":"QA_CASE","age":72,"physicalLevel":3,"chronicDisease":false,"workHourLimit":24,"jobId":1}. 응답 {"id":57}. 평가 15→16. |  | screenshots/IF-0026.png |
| IF-0027 | 2026-10-30 | 통과 | 입력값 표시 「25」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 16→16. |  | screenshots/IF-0027.png |
| IF-0028 | 2026-10-30 | 통과 | 입력값 표시 「7.5」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 16→16. |  | screenshots/IF-0028.png |
| IF-0029 | 2026-10-30 | 통과 | 숫자 입력칸은 abc를 남기지 않아 표시값은 빈 문자열. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 변화 없음. |  | screenshots/IF-0029.png |
| IF-0030 | 2026-10-30 | 통과 | 입력값 표시 「」. alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」. POST 0건. 평가 건수 16→16. |  | screenshots/IF-0030.png |
| IF-0031 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload.physicalLevel=1. DB physical_level=1. 평가 16→17. |  | screenshots/IF-0031.png |
| IF-0032 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload.physicalLevel=2. DB physical_level=2. 평가 17→18. |  | screenshots/IF-0032.png |
| IF-0033 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload.physicalLevel=3. DB physical_level=3. 평가 18→19. |  | screenshots/IF-0033.png |
| IF-0034 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload.physicalLevel=4. DB physical_level=4. 평가 19→20. |  | screenshots/IF-0034.png |
| IF-0035 | 2026-10-30 | 통과 | POST 1건 HTTP 201. payload.physicalLevel=5. DB physical_level=5. 평가 20→21. |  | screenshots/IF-0035.png |
| IF-0036 | 2026-10-30 | 통과 | HTTP 201. payload.chronicDisease=false. DB chronic_disease_flag=false. |  | screenshots/IF-0036.png |
| IF-0037 | 2026-10-30 | 통과 | HTTP 201. payload.chronicDisease=true. DB chronic_disease_flag=true. |  | screenshots/IF-0037.png |
| IF-0038 | 2026-10-30 | 통과 | alert 「직무를 선택해주세요.」. POST 0건. |  | screenshots/IF-0038.png |
| IF-0039 | 2026-10-30 | 통과 | HTTP 201. payload.jobId=1. 결과 화면 「IF-0039 · 72세 · 아파트 야간 경비원」. 기대 직무명 아파트 야간 경비원. |  | screenshots/IF-0039.png |
| IF-0040 | 2026-10-30 | 통과 | HTTP 201. payload.jobId=2. 결과 화면 「IF-0040 · 72세 · 택배 배송 기사」. 기대 직무명 택배 배송 기사. |  | screenshots/IF-0040.png |
| IF-0041 | 2026-10-30 | 통과 | 응답 전 옵션 1개 「선택하세요」. 응답 후 9개. |  | screenshots/IF-0041.png |
| IF-0042 | 2026-10-30 | 통과 | alert 「직무 목록을 불러오지 못했습니다.」. 직무 옵션 1개. |  | screenshots/IF-0042.png |
| IF-0043 | 2026-10-30 | 실패 | 같은 차례 click() 2회 후 POST 2건. 버튼 「AI 분석 중...」 disabled=true. | BUG-IF-0043 | screenshots/IF-0043.png |
| IF-0044 | 2026-10-30 | 통과 | POST 1건. alert 「API 500: 서버 오류가 발생했습니다.」. 버튼 「위험도 분석 시작」 enabled=true. |  | screenshots/IF-0044.png |
| IF-0045 | 2026-10-30 | 통과 | 이동 주소 http://localhost/assessments/845/result. |  | screenshots/IF-0045.png |
| IF-0046 | 2026-10-30 | 통과 | 201 본문 {} 이면 id가 없어 주소는 http://localhost/assessments/undefined/result. alert 「API 500: 서버 오류가 발생했습니다.」. |  | screenshots/IF-0046.png |
| IF-0269 | 2026-10-30 | 통과 | 지연 중 「불러오는 중...」 표시=true. 응답 후 이름 표시. |  | screenshots/IF-0269.png |
| IF-0270 | 2026-10-30 | 통과 | alert 「API 404: 평가를 찾을 수 없습니다.」. |  | screenshots/IF-0270.png |
| IF-0271 | 2026-10-30 | 통과 | 문구 「아직 AI 분석 결과가 없습니다.」 표시. |  | screenshots/IF-0271.png |
| IF-0272 | 2026-10-30 | 통과 | 배지 「위험도 낮음」 표시. |  | screenshots/IF-0272.png |
| IF-0273 | 2026-10-30 | 통과 | 배지 「위험도 보통」 표시. |  | screenshots/IF-0273.png |
| IF-0274 | 2026-10-30 | 통과 | 배지 「위험도 높음」 표시. |  | screenshots/IF-0274.png |
| IF-0275 | 2026-10-30 | 통과 | 「기본 설명 (생성형 AI 미사용)」 표시. |  | screenshots/IF-0275.png |
| IF-0276 | 2026-10-30 | 통과 | 「생성형 AI(Gemini)가 작성」 표시. |  | screenshots/IF-0276.png |
| IF-0277 | 2026-10-30 | 통과 | 요인 0개. 점수 구성 카드 없음. |  | screenshots/IF-0277.png |
| IF-0278 | 2026-10-30 | 통과 | 요인 「연령」과 「10 / 20점」 표시. |  | screenshots/IF-0278.png |
| IF-0279 | 2026-10-30 | 통과 | 만점 0 막대 width=0%. |  | screenshots/IF-0279.png |
| IF-0280 | 2026-10-30 | 통과 | 태스크 0개. ML/DL 표 없음. |  | screenshots/IF-0280.png |
| IF-0281 | 2026-10-30 | 통과 | 표 칸 야간 / 12% / 0%. |  | screenshots/IF-0281.png |
| IF-0282 | 2026-10-30 | 통과 | 이동 주소 http://localhost/dashboard. |  | screenshots/IF-0282.png |
| IF-0283 | 2026-10-30 | 통과 | 목록 지연 중 「불러오는 중...」 표시=true. |  | screenshots/IF-0283.png |
| IF-0284 | 2026-10-30 | 통과 | 빈 content. 「아직 등록된 평가 기록이 없습니다.」 표시. |  | screenshots/IF-0284.png |
| IF-0285 | 2026-10-30 | 통과 | alert 「API 500: 목록 실패」. |  | screenshots/IF-0285.png |
| IF-0286 | 2026-10-30 | 통과 | summary null. 카드 0건, 0건, 0건. |  | screenshots/IF-0286.png |
| IF-0287 | 2026-10-30 | 통과 | 카드 3건, 1건, 2건. |  | screenshots/IF-0287.png |
| IF-0288 | 2026-10-30 | 통과 | 행 QA_CASE / 72세 / 아파트 야간 경비원 / - / 낮음 / 결과 보기삭제. |  | screenshots/IF-0288.png |
| IF-0289 | 2026-10-30 | 통과 | 등급 null. 「분석 전」 표시. |  | screenshots/IF-0289.png |
| IF-0290 | 2026-10-30 | 통과 | 첫 목록 요청 GET http://localhost/api/assessments?page=0&size=20. |  | screenshots/IF-0290.png |
| IF-0291 | 2026-10-30 | 통과 | page=1 요청 1건. GET http://localhost/api/assessments?page=1&size=20 |  | screenshots/IF-0291.png |
| IF-0292 | 2026-10-30 | 통과 | 첫 페이지 이전 버튼 disabled=true. |  | screenshots/IF-0292.png |
| IF-0293 | 2026-10-30 | 통과 | 마지막 페이지 다음 버튼 disabled=true. |  | screenshots/IF-0293.png |
| IF-0294 | 2026-10-30 | 통과 | confirm 취소. DELETE 0건. |  | screenshots/IF-0294.png |
| IF-0295 | 2026-10-30 | 통과 | confirm 승인. DELETE 1건. 목록 요청 2회. 화면에 갱신됨 표시. |  | screenshots/IF-0295.png |
| IF-0296 | 2026-10-30 | 통과 | alert 「API 500: 삭제 실패」. 행 유지=1. |  | screenshots/IF-0296.png |
| IF-0297 | 2026-10-30 | 통과 | 반환 {"ok":true,"n":7}. |  | results.json |
| IF-0298 | 2026-10-30 | 통과 | 204 반환 undefined. |  | results.json |
| IF-0299 | 2026-10-30 | 통과 | content-length 0 반환 undefined. |  | results.json |
| IF-0300 | 2026-10-30 | 통과 | 예외 「API 400: 실패」. |  | results.json |
| IF-0301 | 2026-10-30 | 통과 | 예외 「API 500: Error」. |  | results.json |
| IF-0302 | 2026-10-30 | 통과 | SyntaxError: Unexpected token 'o', "not-json" is not valid JSON |  | results.json |
| IF-0303 | 2026-10-30 | 통과 | TypeError: Failed to fetch |  | results.json |
| IF-0304 | 2026-10-30 | 통과 | 요청 Content-Type 「application/json」. |  | results.json |

## 환경

- 브라우저: Google Chrome headless, Playwright. 화면 언어 `ko-KR`.
- 화면은 `http://localhost`, API는 같은 주소의 `/api`.
- 검증은 브라우저 조작과 네트워크 기록이다. `client.ts` 8건은 그 파일의 `apiRequest` 본문을 브라우저에서 실행하고 `fetch`만 흉내 냈다.
- 정상 제출의 기본값은 나이 72, 건강 3, 만성질환 없음, 근무 8시간, 직무 1이다. 케이스에서 보는 칸만 바꿨다.
- 검증을 통과한 제출은 실제 `POST /api/assessments` 가 나갔고 AI 분석까지 끝나 201이 왔다. 만든 평가 id 43~66은 DELETE 204로 지웠다. 평가 삭제는 신청자와 건강 스냅샷을 남기므로, 이번 실행으로 생긴 신청자 43~66과 건강 행만 추가로 지웠다.
- 종료 건수: 평가 1(id 2), 신청자 21, 건강 스냅샷 21, AI 결과 1.

## 수행 순서

1. 입력 화면에서 이름, 연령, 근무시간을 시트 값으로 넣고 제출했다. POST 횟수, 본문, alert, 평가 건수를 남겼다.
2. 건강 상태 1~5와 만성질환 있음/없음은 제출 본문과 `health_snapshot` 컬럼을 비교했다.
3. 직무 1, 2는 제출 후 결과 화면의 직무명과 `GET /api/jobs` 의 이름을 비교했다.
4. 로딩, 조회 실패, 중복 클릭, 제출 500, 제출 201, 빈 JSON은 네트워크 응답을 바꿔 확인했다. 이 구간은 DB에 쓰지 않았다.
5. 결과 화면과 대시보드는 결과·목록·요약·삭제 응답을 바꿔 DOM을 확인했다.
6. `apiRequest` 는 200 JSON, 204, content-length 0, 400, 500 텍스트, 깨진 JSON, 네트워크 실패, POST Content-Type을 각각 호출했다.

1차 실행에서 IF-0297~0304는 타입 표기를 브라우저 함수로 넘기다 `SyntaxError` 가 났다. 제품 동작이 아니다. 같은 `client.ts` 본문에서 타입 표기만 지우고 다시 호출했고, 아래 결과는 재실행 값이다.

IF-0036, IF-0037도 1차 스크립트는 PostgreSQL 불리언을 `f`/`t`로 기대해 실패로 적었다. 실제 저장값은 `false`/`true` 로 본문과 같다. 시트 판정은 통과다.

## 실패

### IF-0043 중복 클릭 — 실패, BUG-IF-0043

- 절차: 정상 값을 채운 뒤, 버튼이 다시 그려지기 전에 `click()` 을 같은 차례에 두 번 호출했다. POST는 1.2초 지연 후 201을 주는 목이었다.
- 기대: `submitting=true` 로 버튼이 비활성이 되고, 같은 클릭의 중복 제출이 막힌다.
- 결과: POST 2건. 그 다음 그리기에서 버튼은 「AI 분석 중...」이고 disabled=true.
- 원인: `handleSubmit` 은 `setSubmitting(true)` 를 호출하지만, React가 버튼을 다시 그리기 전에 들어온 두 번째 클릭은 아직 `submitting === false` 를 본다. 한 번 그린 뒤의 추가 클릭은 막힌다.
- 캡처: `screenshots/IF-0043.png`

## 입력 검증

- IF-0001 빈 이름, IF-0002 공백만 있는 이름은 alert 「이름을 입력해주세요.」, POST 0, 평가 건수 유지. 통과.
- IF-0003 홍길동은 POST 1, HTTP 201, `applicantName` 은 홍길동. 통과.
- IF-0004 ` 홍길동 ` 은 본문에서 `홍길동` 으로 trim 된 뒤 201. DB `display_name` 도 홍길동. 통과.
- IF-0005 50자 `a` 는 201. 통과.
- IF-0006 51자 `a` 는 프론트가 길이를 막지 않아 POST 1. 응답 HTTP 400 `applicantName: 크기가 0에서 50 사이여야 합니다`. 화면 언어가 `ko-KR` 이라 검증 문장이 한글이다. 평가 건수는 늘지 않았다. 통과.
- IF-0007 `한글😀` 는 201, 본문 이름 일치. 통과.
- 연령 -1, 0, 121, 60.5, 빈 값(IF-0008, 0009, 0016, 0017, 0019)은 alert 「연령은 1~120 사이로 입력해주세요.」, POST 0. 통과.
- IF-0018 `abc` 는 `type=number` 칸이 글자를 남기지 않는다. 표시값은 빈 문자열이고 같은 연령 오류, POST 0. 통과.
- 연령 1, 2, 60, 90, 119, 120(IF-0010~0015)은 POST 1, HTTP 201, 본문 age가 그 정수. 통과.
- 근무시간 -1, 0, 25, 7.5, 빈 값(IF-0020, 0021, 0027, 0028, 0030)은 alert 「근무 가능 시간은 1~24 사이로 입력해주세요.」, POST 0. 통과.
- IF-0029 `abc` 도 숫자 칸이 글자를 버리고 같은 근무시간 오류, POST 0. 통과.
- 근무시간 1, 7, 8, 23, 24(IF-0022~0026)는 POST 1, HTTP 201, 본문 workHourLimit 일치. 통과.

## 필드 매핑과 직무

- IF-0031~0035 건강 1~5는 본문 `physicalLevel` 과 `health_snapshot.physical_level` 이 같은 숫자. HTTP 201. 통과. 서비스는 이 숫자를 AI 요청 `physical_level` 로 전달한다.
- IF-0036 없음은 본문 `chronicDisease=false`, DB `chronic_disease_flag=false`. IF-0037 있음은 `true`/`true`. HTTP 201. 통과.
- IF-0038 직무 미선택은 alert 「직무를 선택해주세요.」, POST 0. 통과.
- IF-0039 직무 1은 본문 jobId 1, 결과 화면 「아파트 야간 경비원」. IF-0040 직무 2는 jobId 2, 「택배 배송 기사」. 통과.

## 상태 분기

- IF-0041 `GET /api/jobs` 를 붙잡아 두면 옵션은 「선택하세요」 1개다. 놓으면 9개(안내 1개와 직무 8개)가 된다. 통과.
- IF-0042 직무 조회 500은 alert 「직무 목록을 불러오지 못했습니다.」. 옵션은 안내 1개. 통과.
- IF-0043 실패. 위 실패 절.
- IF-0044 POST 500 JSON은 alert 「API 500: 서버 오류가 발생했습니다.」. 버튼은 다시 「위험도 분석 시작」이고 활성이다. POST 1건. 통과.
- IF-0045 POST 201 `{"id":845}` 는 `/assessments/845/result` 로 이동. 통과.
- IF-0046 POST 201 본문 `{}` 는 id가 없어 `/assessments/undefined/result` 로 이동한다. 결과 조회가 이어지고 alert 「API 500: 서버 오류가 발생했습니다.」. 기대한 기록 항목이라 통과로 두었다. DB 기록은 없다.

## 결과 화면

주소 `/assessments/1/result` 의 GET을 바꿨다. DB는 변하지 않았다.

- IF-0269 응답을 붙잡으면 「불러오는 중...」. 놓으면 이름이 보인다. 통과.
- IF-0270 404는 alert 「API 404: 평가를 찾을 수 없습니다.」. 통과.
- IF-0271 `riskScore=null` 은 「아직 AI 분석 결과가 없습니다.」. 통과.
- IF-0272 LOW 「위험도 낮음」, IF-0273 MID 「위험도 보통」, IF-0274 HIGH 「위험도 높음」. 통과.
- IF-0275 `explanationSource=basic` 은 「기본 설명 (생성형 AI 미사용)」. IF-0276 gemini는 「생성형 AI(Gemini)가 작성」. 통과.
- IF-0277 요인 0개는 「점수 구성」 카드가 없다. IF-0278 한 건은 「연령」과 「10 / 20점」. IF-0279 만점 0은 막대 width 0%. 통과.
- IF-0280 태스크 0개는 ML/DL 표가 없다. IF-0281 `mlScore=0.123` 은 「12%」. 통과.
- IF-0282 「목록으로 돌아가기」는 `/dashboard`. 통과.

## 대시보드

목록, 요약, 삭제는 목 응답이다. 실제 DELETE는 나가지 않았다.

- IF-0283 목록을 붙잡으면 「불러오는 중...」. 통과.
- IF-0284 `content=[]` 는 「아직 등록된 평가 기록이 없습니다.」. 통과.
- IF-0285 목록 500은 alert 「API 500: 목록 실패」. 통과.
- IF-0286 요약 JSON `null` 은 카드 0건, 0건, 0건. 통과.
- IF-0287 요약 3, 1, 2는 카드 「3건」「1건」「2건」. 통과.
- IF-0288 점수 null은 「-」. IF-0289 등급 null은 「분석 전」. 통과.
- IF-0290 첫 요청은 `GET /api/assessments?page=0&size=20`. 통과.
- IF-0291 다음 클릭은 `page=1&size=20` 1건. 통과.
- IF-0292 첫 페이지 이전 버튼 disabled. IF-0293 마지막 페이지 다음 버튼 disabled. 통과.
- IF-0294 confirm 취소는 DELETE 0. IF-0295 승인은 DELETE 1과 목록 재조회, 화면 문구가 바뀐다. IF-0296 DELETE 500은 alert 「API 500: 삭제 실패」, 행은 남는다. 통과.

## apiRequest

`web-vite/src/shared/api/client.ts` 의 분기만 호출했다.

- IF-0297 200 JSON `{ok:true,n:7}` 를 그대로 반환. 통과.
- IF-0298 204는 `undefined`. IF-0299 200이면서 `content-length: 0` 도 `undefined`. 통과.
- IF-0300 400 `{message:"실패"}` 는 예외 `API 400: 실패`. 통과.
- IF-0301 500 본문 `Error` 는 예외 `API 500: Error`. 통과.
- IF-0302 200 `not-json` 은 `SyntaxError`. 통과.
- IF-0303 fetch 실패는 `TypeError: Failed to fetch` 가 그대로 전파. 통과.
- IF-0304 POST의 Content-Type은 `application/json`. 통과.

## 정리

제품 코드는 바꾸지 않았다. 이번 제출로 생긴 평가와 신청자, 건강 스냅샷은 삭제했다. 평가 id 2와 그 이전 신청자는 그대로다.

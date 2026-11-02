# [E2E] FAIL 및 미통과 상세 기록 (2026-10-30)

> **경로**: `qa/reports/e2e/2026-10-30/fail.md`  
> **기준 시간대**: `Asia/Seoul` (KST)  
> **원칙**: 코드 수정 전 반드시 본 문서에 먼저 기록하고 사용자에게 보고합니다. 도구 하나라도 실패 시 완료 처리하지 않습니다.

---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:54 KST)

- **실패/미통과 건수**: 1건 / 전체 2건

### [UI-023] 평가 제출 버튼 동일 이벤트 루프 연속 클릭(Double Click) 시 중복 POST 방지 검증 (IF-0043 공통) (`FAIL`) — `BUG-UI-023`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:32:53 KST`
- **테스트 종류**: `e2e`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `Frontend Source & State Race Inspector (AssessmentFormPage.tsx)` → **FAIL (useState setSubmitting 비동기 리렌더 전 동기 useRef 가드 미적용)**
- **도구 B 및 결과**: `Playwright E2E Trace & API Idempotency Inspector (TC_docs UI-023 / IF-0043)` → **FAIL (동일 틱 연속 click() 시 POST /api/assessments 2회 발생 확인)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `web-vite/src/pages/AssessmentFormPage.tsx` / 함수 `handleSubmit` / 줄 번호 `56-81, 143-150`
- **입력값 (Input)**: `유효 폼 입력 후 동일 이벤트 루프 내 button.click() 2회 연속 호출`
- **오류 메시지 / 응답**: `POST /api/assessments 요청이 1회가 아닌 2회 전송되어 중복 평가 레코드 생성됨`
- **예상 결과 (Expected)**: 연속 클릭 시에도 POST 요청 1건만 발생
- **실제 결과 (Actual)**: handleSubmit(56행)이 useState(submitting)만 사용하여 리렌더링 전 동일 차례 두 번째 click() 진입 시 POST 2건 발생
- **재현 방법 (Reproduction)**:
  ```zsh
  AssessmentFormPage에서 필수값 입력 후 제출 버튼에 대해 동기적 연속 click() 이벤트 발생
  ```
- **원인 분석 (Root Cause)**: React useState의 setSubmitting(true)(63행)는 다음 렌더 패스에서 disabled={submitting}(146행)을 반영하므로, 리렌더 전 동기 연속 클릭을 막지 못함 (useRef 기반 동기 락 부재).
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)
- **화면**: 같은 날짜 폴더의 `screenshots/UI-023.png` (한 번 클릭 후 비활성), `screenshots/UI-023-burst.png` (같은 차례 두 번 클릭)


## TC-20261030-1418 / UI-023
- RUN_ID: TC-20261030-1418
- TC_ID: UI-023
- timestamp: 2026-10-30T14:18:00+09:00
- feature: 중복 클릭
- test_type: e2e
- tool_a: 브라우저
- command_a: 분석 버튼 연속 클릭
- result_a: FAIL
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: AssessmentFormPage.tsx + 화면
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: BUG-UI-023
- RISK_ID: 
- evidence: 기대: 분석 중 버튼 비활성 및 중복 제출 방지 | 실제: 한 번 클릭 후 버튼은 "AI 분석 중..."이고 disabled, 추가 클릭은 거절되며 POST 1건. 버튼이 막히기 전 같은 차례의 연속 click()은 POST 2건 | 화면: screenshots/UI-023-burst.png, screenshots/UI-023.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1522 / IF-0043
- RUN_ID: TC-20261030-1522
- TC_ID: IF-0043
- timestamp: 2026-10-30T15:22:00+09:00
- feature: 중복 클릭
- test_type: e2e
- tool_a: Playwright + Network
- command_a: Network Mock 또는 전용 테스트 환경에서 시나리오 주입 → DOM/요청/라우팅 확인
- result_a: FAIL
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: FAIL
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: web-vite/src/pages/AssessmentFormPage.tsx
- function: 조회/제출 상태 분기
- line: UNKNOWN
- ISSUE_ID: BUG-IF-0043
- RISK_ID: 
- evidence: 기대: submitting=true로 버튼 비활성; 동일 클릭 중복 제출 방지 | 실제: 같은 차례 click() 2회 후 POST 2건. 버튼 「AI 분석 중...」 disabled=true. | 화면: screenshots/IF-0043.png | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

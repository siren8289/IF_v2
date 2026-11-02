# 개발 작업 로그 (`docs/DEV_LOG.md`)

## [2026-10-30] 바이브 코딩 QA·Security 자동화 지침 V2.5 시스템 구축

### 1. 작업 배경 및 목적
- 최초 개발부터 모든 기능 추가·수정·유지보수·버그 수정·리팩터링·배포 설정 변경까지 사용자가 매번 QA를 요청하지 않아도 상시 자동 적용되는 **QA·Security 자동화 시스템(V2.5)**을 구축함.

### 2. 구현 및 구성 산출물
1. **상시 적용 규칙 등록**:
   - [`AGENTS.md`](file:///Users/jeong-yelim/orca/IF_v2/AGENTS.md): 워크스페이스 전역 상시 로드 규칙 등록 (10단계 자동 실행 절차, 최소 2개 도구 교차 검증, FAIL/RISK 선기록·선보고 원칙).
   - [`qa-policy.md`](file:///Users/jeong-yelim/orca/IF_v2/qa-policy.md): ISTQB 및 OWASP ASVS/WSTG 기반 테스트 설계, 교차 검증 매트릭스, 공통 기록 스키마, PASS/FAIL/RISK 처리 지침 명세.
2. **에이전트 스킬 및 라이프사이클 훅 구성**:
   - [`.agents/skills/qa-security-v25/SKILL.md`](file:///Users/jeong-yelim/orca/IF_v2/.agents/skills/qa-security-v25/SKILL.md): QA·Security V2.5 표준 실행 런북 스킬.
   - [`.agents/hooks.json`](file:///Users/jeong-yelim/orca/IF_v2/.agents/hooks.json) 및 [`.agents/hooks/qa_lifecycle_hook.py`](file:///Users/jeong-yelim/orca/IF_v2/.agents/hooks/qa_lifecycle_hook.py): `SessionStart` 및 `PreInvocation` 시점 QA·Security V2.5 준수 알림 및 리포트 상태 주입 훅.
3. **실제 테스트 실행기 및 MD·TSV 기록 생성기**:
   - [`qa/recorder.py`](file:///Users/jeong-yelim/orca/IF_v2/qa/recorder.py): `Asia/Seoul` 기준 `qa/reports/{test-type}/{YYYY-MM-DD}/` 폴더 자동 생성(미실행 종류 폴더 생성 금지), `RUN_ID` 자동 채번 및 누적(Append) 보존, Excel 호환 UTF-8(BOM) `results.tsv` 및 `pass.md`, `fail.md`, `risk.md` 생성.
   - [`qa/run_qa.py`](file:///Users/jeong-yelim/orca/IF_v2/qa/run_qa.py): 7대 테스트 종류(`unit`, `api`, `integration`, `e2e`, `security`, `performance`, `regression`)를 최소 2개 서로 다른 도구(Tool A / Tool B)로 실제 교차 실행하고 DB 테스트 데이터를 자동 원복하는 실행기.
4. **GitHub Actions CI 필수 검사 게이트 연동**:
   - [`.github/workflows/githubactions.yml`](file:///Users/jeong-yelim/orca/IF_v2/.github/workflows/githubactions.yml): 기존 4개 잡(`backend-spring`, `web-vite`, `ai-fastapi`, `data-pipeline`) 보존 및 교차 검증 스텝 추가, `qa-security-gate` 잡(`--enforce-gate`) 추가.

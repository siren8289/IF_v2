---
name: qa-security-v25
description: >-
  바이브 코딩 QA·Security 자동화 지침 V2.5 실행 스킬. 코드 변경·기능 추가·버그 수정·리팩터링·배포 설정 변경 시
  ISTQB/OWASP ASVS 기반 TC 설계, 최소 2개 도구 교차 검증, qa/reports/{test-type}/{YYYY-MM-DD}/ 자동 기록,
  FAIL/RISK 선기록·선보고 및 회귀 테스트를 수행할 때 사용한다.
---

# QA·Security 자동화 V2.5 실행 런북 (Skill)

규칙의 본문은 `qa-policy.md`와 `AGENTS.md`에 있다. 공식 실행기는 `scripts/qa/run.py`다. `qa/run_qa.py`는 보존된 보조 구현이며 게이트로 실행하지 않는다. FAIL 또는 RISK는 제품 코드를 고치기 전에 기록하고 사용자에게 알린다. 실행하지 않은 E2E·성능 폴더는 만들지 않고 PASS로 적지 않는다.

## 1. 언제 사용하는가
- 최초 개발, 기능 추가, 기능 수정, 유지보수, 버그 수정, 리팩터링, 배포/인프라 설정 변경 등 **모든 작업마다 상시 활성화**한다.

## 2. 표준 실행 명령어 (`scripts/qa/run.py`)

```sh
# 전체 필수 검사와 회귀; E2E/성능은 미구축이므로 PASS로 표시하지 않는다.
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py
# 변경 직후 관련 검사; 수정 후 같은 명령을 재실행하면 새 RUN_ID로 누적된다.
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py --suite QA-AI --suite QA-REGRESSION
# 위험 선기록
python3 scripts/qa/run.py --risks-only
```

환경 설치·범위·한계는 qa-policy.md와 qa/suites.json을 따른다. CI와 Git pre-commit이 실제 게이트이며 아래 hook은 호스트 지원 시에만 안내를 주입한다.

## 3. 산출물 확인 체크리스트
1. `qa/reports/{test-type}/{YYYY-MM-DD}/` 하위에 `pass.md`, `fail.md`, `risk.md`, `results.tsv` 4개 파일이 생성되었는가?
2. 실행하지 않은 `{test-type}` 폴더가 불필요하게 생성되지 않았는가?
3. 각 TC마다 서로 다른 도구 2개(`TOOL_A`, `TOOL_B`)의 결과와 실제 확인된 파일(`TARGET_FILE`), 함수명(`FUNCTION_NAME`), 줄 번호(`LINE_NO`, 미확인 시 `UNKNOWN`), `GIT_COMMIT`이 기록되었는가?
4. `FAIL` 또는 `RISK` 발견 시 **코드 수정 전에** `fail.md` / `risk.md`에 먼저 기록하고 사용자에게 보고했는가?
5. 미해결 `HIGH` / `CRITICAL` 위험이 있을 때 완료/병합을 차단했는가?

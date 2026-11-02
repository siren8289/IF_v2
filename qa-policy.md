# QA·Security 자동화 정책 V2.5

## 적용과 실행

모든 개발·유지보수 작업에 AGENTS.md의 절차를 상시 적용한다. 흐름은 영향 분석 → TC 확인/추가 → 코드 변경 → 관련 검사 → 두 도구 교차 검증 → 분류/누적 기록 → 실패 보고/원인 분석/수정 → 두 도구 재검증 → 전체 회귀 → 최종 결과/위험 보고다.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r qa/requirements.txt -r ai/requirements-dev.txt -r data/requirements.txt
.venv/bin/python -m pip install torch
npm ci --prefix web-vite
# JDK 17, Node 22 이상, jq 및 actionlint 1.7.12 필요 (macOS: brew install actionlint)
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py
# 변경 직후 선택 검사, 완료 전에는 전체 검사 필수
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py --suite QA-WEB
# 사용자 정의 hooksPath가 없을 때 설치. 기존 훅이 있다면 삭제하지 않고 연결한다.
git config --local core.hooksPath .githooks
```

pre-commit 훅은 모든 suite를 실행하며 CI의 `QA gate`도 동일 실행기를 사용한다. CI는 필수 검사 실패 시 nonzero로 종료하고 always artifact로 기록을 보존한다. 기존 CI 작업도 유지한다. 로컬/CI 보고서는 서로 다른 실행 이력이며 CI artifact는 90일 보존한다. 장기 보존은 artifact를 별도 보관해야 한다. 커밋·푸시·배포는 이 구축 작업에서 실행하지 않는다.

원격 GitHub ruleset에 `QA gate`와 기존 CI 작업을 required status checks로 등록해야 서버에서 병합을 강제 차단할 수 있다. 저장소 파일만으로 원격 보호를 켰다고 주장하지 않는다. 수동/자동 배포 모두 main의 동일 SHA에 성공한 CI가 있어야 하며 검증한 SHA로 배포한다.

## 설계 근거와 TC 범위

- ISTQB 동등 분할·경계값·결정표·상태 전이: https://astqb.org/4-2-black-box-test-techniques/
- OWASP ASVS 요구사항: https://owasp.org/www-project-application-security-verification-standard/
- OWASP WSTG v4.2 인증·인가·입력 검증·업무 로직: https://wstg.owasp.org/stable/4-Web_Application_Security_Testing/
- 기술별 공식문서: https://docs.pytest.org/en/stable/ , https://docs.python.org/3/library/unittest.html , https://vitest.dev/guide/ , https://www.typescriptlang.org/docs/ , https://docs.gradle.org/current/userguide/java_testing.html , https://bandit.readthedocs.io/ , https://docs.astral.sh/ruff/ , https://docs.github.com/en/actions/tutorials/store-and-share-data

현재 구조는 React/Vite → Spring Boot/JPA → FastAPI ML/DL 및 PostgreSQL과 Python ETL이다. 기존 UI/API/logic 기록은 `qa/reports`의 2026-10-30 수동 행(`TC-20261030-`)에 있다. 실제 자동 실행 범위는 qa/suites.json에 있고 각 QA-* TC는 **검사 묶음의 계약**이다. 기존 개별 TC 결과는 그 수동 행과 원래 테스트 보고서를 근거로 확인한다. suite PASS를 미실행 개별 TC의 PASS로 확장하지 않는다.

기존 TC가 점수 40/41·60/61 경계, 정상/최악 입력, 잘못된 나이, RAG fallback, JSON/XML/중복, UI/API 클라이언트, Spring Controller/Service를 검증한다. 요구사항별 빈 값/NULL/상하한/중복/오류 응답/권한 항목은 변경 시 대조한다. 권한 명세가 없는 경우 임의로 요구사항을 만들지 않고 RISK-002에 연결한다. 두 엔진으로 같은 TC를 실행하는 것은 독립적인 기대값 검증이 아니다. TypeScript/Ruff/javac는 동작 검증과 범위가 다르므로 비교 내용을 기록한다.

현재 필수 종류는 unit/api/integration/security/regression이다. 자동 게이트는 E2E와 성능을 실행하지 않는다. 2026-10-30 폴더는 수동 UI 시트와 보조 실행 기록이 있어 지우지 않는다. 그 종류를 새로 실행하기 전에는 새 날짜 폴더를 만들지 않는다. 보안은 Bandit HIGH 정적 분석과 추적 파일의 제한적인 키 패턴 검사다. 의존성 CVE, 인증/인가 침투, 운영 환경 보안 전체를 검증한 것으로 해석하지 않는다.

## 기록 계약

`qa/reports/{test-type}/{YYYY-MM-DD}/` 아래 pass.md, fail.md, risk.md, results.tsv를 append-only로 관리한다. 날짜는 Asia/Seoul, RUN_ID는 시간+UUID이며 같은 날 재실행해도 기존 행/문단을 보존한다. TSV는 UTF-8 BOM(최초 1회)으로 Excel에서 한글을 읽을 수 있다. 동시 실행은 별도 작업 사본/CI job을 사용한다.

모든 행은 RUN_ID, TC_ID, 시각, 기능, 종류, 도구 A/B 및 명령·결과, 최종 상태, Git Commit, dirty 여부, 검사 대상 파일, 함수·줄, ISSUE_ID/RISK_ID, 증거 해시를 연결한다. 상태는 PASS/FAIL/BLOCKED/ERROR/NOT_RUN/SKIPPED이다. 명령 누락·타임아웃은 ERROR, 테스트 미발견은 NOT_RUN, 하나라도 필수 PASS가 아니면 실행은 실패한다. 스위트 수준 위치는 UNKNOWN이며 도구가 실제 식별한 위치만 상세 기록에 추가한다.

- PASS: 목적·기대/실제·도구·범위 비교·근거를 간결히 기록한다.
- FAIL: 실패 행과 MD를 수정 전에 먼저 남기고 사용자에게 보고한다. 담당자는 원본 로그를 확인해 입력·오류·재현·기대/실제·파일/함수/줄·원인·수정 위치·재검증 RUN_ID를 fail.md에 추가한다. 자동화는 원인과 수정 사실을 추측하지 않는다.
- RISK: qa/risks.json에 고유 ID·심각도·발생 가능성·영향·권장 조치·처리 상태·위치를 먼저 등록한 뒤 `python3 scripts/qa/run.py --risks-only`로 보고 이력을 남긴다. 코드 수정 전에 사용자에게 보고한다. 해결 시 근거를 추가해 RESOLVED로 변경하고 재실행한다. 과거 기록은 유지한다. HIGH/CRITICAL 미해결은 exit 1이다.

날짜 폴더에는 pass.md, fail.md, risk.md, results.tsv를 둔다. 화면이 필요한 UI·E2E 케이스는 화면 파일을 그 날짜 폴더의 screenshots/에 둔다. 원본 로그와 JUnit XML은 qa/.runtime 아래 로컬 저장하고 gitignore로 제외한다. 민감 입력과 비밀키를 로그에 출력하지 않는다. 추적 MD/TSV에는 로그 경로와 SHA256을 기록한다. Git SHA는 실행 시 HEAD이며 dirty 값이 true이면 미커밋 변경을 포함한다. 최종 결과 보고에 이 한계를 명시한다.

## 회귀 및 오류 주입

QA-REGRESSION은 실패 종료·도구 누락·시간 초과·테스트 0개·잘못된 상태·동일 날짜 누적·UTF-8 BOM·한글·미실행 종류 폴더 미생성을 unittest와 pytest로 검증한다. 실패 주입은 격리된 임시 폴더에서 수행한다. 전체 시스템 재실행은 과거 실제 FAIL과 이후 PASS를 함께 남긴다.


## 보존된 보조 구현

작업 도중 추가된 qa/run_qa.py와 qa/recorder.py는 삭제하지 않고 보존한다. 이 구현은 별도 형식의 보고서를 쓰고 실제 서버에 쓰기 요청도 포함하므로 현재 자동 실행 대상이 아니다. CI/스킬/훅의 공식 실행기는 scripts/qa/run.py 하나다. 두 기록기는 기존 TSV 헤더가 다르면 파일 수정 전에 실패한다. 보조 구현을 사용할 경우 격리 환경과 별도 기록 위치를 먼저 검토해야 한다. 보조 구현의 개별 시나리오는 이번 작업에서 실행/검증하지 않았다.

개별 실행 TC는 pytest/Vitest/Gradle JUnit XML에서 추출하여 TSV/MD에 누적한다. 오래된 Gradle XML은 실행 시작 시각으로 걸러 재사용하지 않는다. 원본 XML도 qa/.runtime에 복사하고 해시로 연결한다. QA-CONFIG는 actionlint/ShellCheck와 실제 배포 gate 셸에 대한 GitHub API 응답 오류 주입을 비교한다.

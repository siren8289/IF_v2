# qa 폴더

자동 검사의 계약, 위험 목록, 날짜별 기록이다. 손으로 돌린 UI·프론트·Spring API·로직 176건도 이 폴더의 `2026-10-30` 날짜 기록에 있다. RUN_ID가 `TC-20261030-`로 시작한다. 자동 묶음 PASS를 그 수동 행의 재실행으로 읽지 않는다.

공식 실행 명령은 이 폴더 밖이다.

```sh
PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py
```

규칙 본문은 저장소 루트의 `qa-policy.md`와 `AGENTS.md`다.

## 파일 역할

| 경로 | 역할 |
|---|---|
| `suites.json` | 공식 게이트가 돌리는 7개 묶음. QA-WEB, QA-DATA, QA-AI, QA-SPRING, QA-SECURITY, QA-REGRESSION, QA-CONFIG. 각 묶음은 도구 두 개의 명령과 범위 비교를 적는다. |
| `risks.json` | 위험 원장. 게이트는 여기의 미해결 HIGH/CRITICAL이 있으면 묶음이 통과해도 종료 코드 1이다. |
| `requirements.txt` | 게이트용 Python 패키지. pytest, httpx, ruff, bandit, PyYAML. |
| `reports/` | 날짜별 `pass.md`, `fail.md`, `risk.md`, `results.tsv`. 같은 날 실행은 RUN_ID로 이어 붙인다. 행을 지우거나 덮어쓰지 않는다. |
| `reports/last-run.json` | 마지막 공식 실행의 시각과 차단 여부. Stop 훅이 이 시각을 본다. |
| `reports/{종류}/{날짜}/` | `pass.md`, `fail.md`, `risk.md`, `results.tsv`. UI·E2E 화면은 그 안의 `screenshots/`에 둔다. |
| `../.runtime/` | 실행 로그와 JUnit XML. gitignore 대상이고, TSV에는 경로와 SHA256만 남긴다. |
| `archives/2026-10-30/` | 헤더를 맞추기 전 TSV 원본 7개의 SHA256 사본. |
| `run_qa.py` | 보존된 보조 실행기. 살아 있는 `:8080`에 요청을 보내고 `RUN-20261030-001` 형식의 행을 같은 보고서 폴더에 쓴다. 게이트로 실행하지 않는다. |
| `record.py` | `run_qa.py`가 쓰는 기록기. |
| `recorder.py` | 또 다른 기록기. 공식 TSV 헤더와 다르면 파일을 고치지 않고 실패하도록 막아 두었다. |
| `test_record.py` | `record.py`가 같은 날 두 RUN_ID를 지우지 않는지 보는 임시 디렉터리 스크립트. |
| `check_stop.py` | 제품 파일이 마지막 QA 실행보다 새로우면 세션 종료를 막는 훅. 테스트를 실행하지 않는다. |
| `IMPLEMENTATION.md` | `20261030T173746-09edf77edc` 한 건의 검증 메모. 최신 실행 기록이 아니다. |

공식 러너, 보안 패턴 검사, 러너 회귀 테스트는 `scripts/qa/`에 있다. `run.py`, `security.py`, `test_runner.py`, `test_workflows.py`, `test_history.py`, `normalize_history.py`.

## 마지막 공식 실행

`20261030T174647-e942dbd875`. 2026-10-30 17:46:47~17:47:29 KST. Git `9491fb1b`, 작업 사본 dirty. 종료 코드 1, `blocking: true`.

일곱 묶음은 모두 도구 두 개가 PASS다.

| 묶음 | 종류 | 도구 A | 도구 B |
|---|---|---|---|
| QA-WEB | unit | Vitest | TypeScript `tsc` |
| QA-DATA | unit | unittest | pytest |
| QA-AI | api | pytest | Ruff |
| QA-SPRING | integration | Gradle test | Gradle classes |
| QA-SECURITY | security | Bandit HIGH | 추적 파일 시크릿 패턴 |
| QA-REGRESSION | regression | unittest | pytest |
| QA-CONFIG | regression | actionlint / ShellCheck | 배포 셸에 심은 GitHub API 오류 |

Vitest와 tsc, pytest와 Ruff, Gradle test와 javac는 범위가 다르다. 묶음 PASS는 동작과 정적 검사가 각각 0으로 끝났다는 뜻이다. Bandit 통과는 CVE, 인증 침투, nginx 헤더, `npm audit`을 포함하지 않는다.

같은 실행이 위험 원장을 security 보고서에 다시 붙였다. 위험 행의 도구 결과는 UNKNOWN이다. 두 도구로 다시 시험한 결과가 아니다.

| ID | 심각도 | 상태 | 내용 |
|---|---|---|---|
| RISK-001 | HIGH | RESOLVED | 수동 배포가 CI를 지나치던 경로. 배포 셸 시험으로 닫음. |
| RISK-004 | HIGH | RESOLVED | MD5에 `usedforsecurity=False`. `ai/src/rag/embedder.py` 30행. |
| RISK-005 | MEDIUM | RESOLVED | 스킬이 없는 실행 경로를 가리키던 문제. |
| RISK-007 | HIGH | RESOLVED | 기록기 두 개가 다른 TSV 헤더로 같은 파일을 쓰던 문제. |
| RISK-002 | MEDIUM | OPEN | 권한 명세, E2E URL, 성능 기준이 없음. |
| RISK-003 | MEDIUM | OPEN | 로컬 훅은 우회되고, 원격 ruleset은 저장소 파일만으로 켜지지 않음. |
| RISK-006 | MEDIUM | OPEN | `data/etl/transform.py` `parse_data` 70행. ElementTree로 외부 XML. |
| RISK-SEC-001 | HIGH | OPEN | 평가 삭제에 인증이 없음. `AssessmentController.java` `delete` 67행. |
| RISK-LEGACY-FAILS | HIGH | OPEN | `docs/ERROR_LOG.md`의 제품 결함이 아직 수정되지 않음. |

게이트를 막은 것은 RISK-SEC-001과 RISK-LEGACY-FAILS다.

## 보고서에 섞인 다른 실행

`results.tsv`는 2026-10-30 하루에 실행을 이어 붙인 이력이다.

세 계열이 한 파일에 있다.

1. `20261030T시각-uuid`는 `scripts/qa/run.py`다. 17:24부터 17:46까지 여러 번 돌았고, 중간 실행에는 QA-AI, QA-SECURITY, QA-CONFIG, QA-REGRESSION 실패가 남아 있다. 이후 실행에서 그 묶음은 PASS다. 실패한 행은 지워지지 않았다.
2. `RUN-20261030-001`은 `qa/run_qa.py`가 살아 있는 서버에 보낸 한 차례다. 시각은 17:32 KST 전후다. performance 폴더의 행은 이 계열뿐이다. 공식 게이트는 e2e와 performance를 실행하지 않는다.
3. `TC-20261030-1418`은 브라우저 UI 29건, `TC-20261030-1522`는 프론트 82건, `TC-20261030-1459`는 Spring API 47건, `TC-20261030-1645`는 로직 18건이다. 화면 105장은 `qa/reports/e2e/2026-10-30/screenshots/`에 있다. 엑셀과 원본 JSON은 `qa/archives/`에 있다.

`RUN-20261030-001`에서 실패한 행과, 같은 파일의 `TC-20261030-` 수동 시트를 같이 보면 판정이 다르다.

| TC | 이 행의 결과 | 공식 시트 |
|---|---|---|
| IF-0052, 0059, 0060, 0067, 0072, 0079, 0087 | FAIL. Jackson 변환 201, text/plain 500 | 같은 실패. `docs/ERROR_LOG.md` |
| IF-0050 | FAIL. curl 502와 httpx 201이 갈렸고 DB가 2건 늘었다 | 통과. 이름 50자 201 한 건 |
| UI-023 | FAIL. 같은 차례 두 번 클릭 | 같은 실패 |
| LOG-006 | FAIL. 점수는 29로 같았고 DB 조회 문자열이 비었다 | 통과 |
| LOG-016 | FAIL. 삭제 후 신청자 행이 남았다 | 통과. 삭제는 평가와 AI 결과만 지우는 정책 |
| SEC-001, 002, 003 | PASS | 시트 176건 밖 |
| SEC-004, SEC-005 | FAIL. nginx 보안 헤더 없음, npm audit High 1건 | 시트 176건 밖. 아직 수정 안 함 |
| PERF-001 | FAIL. curl 2294ms, 동시 10건 P95 317ms. 합의된 기준 없음 | 공식 게이트 범위 밖 |
| PERF-002 | PASS. FastAPI 추론 1초 미만 | 공식 게이트 범위 밖 |
| REG-002 | FAIL. 요약 건수 2, 평가 id 2 상태가 빈 문자열 | 공식 시트에 없는 검사 |

개별 JUnit 이름(`QA-AI/tests.test_rag::...`, `QA-SPRING/TEST-...`)은 그 실행의 XML에서 뽑은 케이스다. 묶음이 PASS이면 그 케이스 행도 PASS로 붙어 있다.

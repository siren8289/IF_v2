# QA V2.5 구축 검증 결과

이 문서는 2026-10-30 17:37 실행 `20261030T173746-09edf77edc` 한 건의 스냅샷이다. 폴더 역할과 그 이후 실행은 `qa/README.md`를 본다. 마지막 공식 실행은 `qa/reports/last-run.json`의 `20261030T174647-e942dbd875`다.

- RUN_ID: 20261030T173746-09edf77edc
- Git Commit: 9491fb1b (작업 사본 dirty; 미커밋 변경 포함)
- 시각/시간대: 2026-10-30 Asia/Seoul
- 실행: `PATH="$PWD/.venv/bin:$PATH" python3 scripts/qa/run.py`
- 실제 결과: 7개 검사 묶음 / 14개 도구 검사 PASS; 구조화 XML 개별 TC 54개 PASS.
- 전체 exit: **1 / BLOCKED**. RISK-SEC-001 및 RISK-LEGACY-FAILS HIGH OPEN을 정상 차단했다. 검사 통과와 전체 게이트 승인은 별개다.
- E2E/성능/운영 AWS 배포: 이 최종 실행에서는 NOT_RUN. 기존 다른 실행기의 기록은 보존했으며 이번 실행 결과로 승계하지 않았다.
- GitHub Actions 구성은 actionlint/ShellCheck 및 배포 셸 오류 주입으로 검증했다. 원격 Actions 실행, push, 실제 배포, 원격 브랜치 보호 변경은 실행하지 않았다. main 미보호 상태는 RISK-003에 기록했다.
- 로컬 Git pre-commit 활성: `core.hooksPath=.githooks`. 현재 HIGH 위험이 남아 있으므로 이 훅도 커밋을 차단한다.
- MD/TSV 누적, BOM/한글, 실패·누락·시간 초과, HIGH→해결 상태 이력, JUnit 오류·실패·skip 구분, 두 writer 간 헤더 충돌 거부, 혼합/구형 보고서 정규화와 원본 보존을 unittest/pytest 양쪽으로 검증했다.
- `.agents` hook은 두 event의 JSON 출력까지 확인했다. 실제 호스트의 lifecycle hook 지원 여부는 검증하지 않았다. AGENTS.md와 Git/CI 게이트가 상시 적용의 기준이다.
- 혼합 기록 복구: qa/archives/2026-10-30의 원본 7개 SHA256을 검증했다. 기존 행을 삭제하지 않고 현재 results.tsv에 원래 상태·근거를 매핑했다. 과거 수동 기록의 잘못된 줄 위치 QA-CI-001: 변경 전 반복문은 113행이며, 기존 메모의 115행은 명령 옵션 위치다. 수정은 .github/workflows/deploy.yml:113.
- HISTORY-NORMALIZE-001 재검증: 20261030T173746-09edf77edc, QA-REGRESSION 두 엔진 PASS. 순수 legacy/혼합 형식 및 byte-for-byte 원본 보존 검증 완료.
- QA-AI 환경 문제 및 B324 수정 재검증: 20261030T173746-09edf77edc, QA-AI 및 QA-SECURITY 두 도구씩 PASS.

## 실제 검사 비교

|TC_ID|도구 A|도구 B|결과|
|---|---|---|---|
|QA-WEB|Vitest|TypeScript|PASS / PASS|
|QA-DATA|unittest|pytest|PASS / PASS|
|QA-SECURITY|Bandit|Secret-policy|PASS / PASS|
|QA-SPRING|JUnit/Gradle|javac/Gradle|PASS / PASS|
|QA-AI|pytest|Ruff|PASS / PASS|
|QA-REGRESSION|unittest|pytest|PASS / PASS|
|QA-CONFIG|actionlint/ShellCheck|unittest deployment simulation|PASS / PASS|

각 도구의 범위 차이와 명령, 개별 TC·증거 해시는 qa/reports의 날짜별 MD/TSV에서 확인한다. 잠재 위험의 최신 상태는 qa/risks.json을 기준으로 한다.

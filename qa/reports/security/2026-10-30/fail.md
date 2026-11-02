# FAIL

## 20261030T172455-160ef4c9a6 / QA-SECURITY
- RUN_ID: 20261030T172455-160ef4c9a6
- TC_ID: QA-SECURITY
- timestamp: 2026-10-30T17:24:55.062349+09:00
- feature: Python SAST 및 추적 파일 비밀키 패턴 검사
- test_type: security
- tool_a: Bandit
- command_a: ["python3", "-m", "bandit", "-r", "ai/src", "data/etl", "-lll", "-q"]
- result_a: FAIL
- tool_b: Secret-policy
- command_b: ["python3", "scripts/qa/security.py"]
- result_b: PASS
- status: FAIL
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src, data/etl
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/security/2026-10-30/20261030T172455-160ef4c9a6/QA-SECURITY-a.log sha256=d4efb21c8d1436c92c9629c3cdaee43e11c14f2f94d8a58fc625159628fb8b4d; qa/.runtime/evidence/security/2026-10-30/20261030T172455-160ef4c9a6/QA-SECURITY-b.log sha256=d49e8eeb796a1f4cdbc3f15128ccbd7c4c2cad046c77d6e8b8e5e719bb8516e7

Expected: both tools exit 0 with tests present where applicable. Actual: FAIL/PASS
Scope comparison: Bandit HIGH SAST 및 별도 추적 파일 private key/키 패턴 검사. 의존성 CVE/침투 테스트 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

### QA-SECURITY / 20261030T172455-160ef4c9a6 원인 분석 (수정 전)
- 오류: Bandit B324 HIGH. 입력: ai/src/rag/embedder.py의 단어 해시 호출.
- 기대: 비보안 용도의 임베딩 해시로 분류. 실제: 기본 MD5 보안 용도 플래그로 HIGH 검출.
- 위치: ai/src/rag/embedder.py:30, _local_fallback_embedding.
- RISK_ID: RISK-004. 변경 계획: usedforsecurity=False로 용도를 명시하고 기존 벡터 결과를 보존한다. 재현: manifest의 Bandit 명령.
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:33:06 KST)

- **실패/미통과 건수**: 2건 / 전체 5건

### [SEC-004] OWASP ASVS V14.4 / WSTG-CONF-07 HTTP 필수 보안 헤더(X-Content-Type-Options, X-Frame-Options) 적용 검증 (`FAIL`) — `BUG-SEC-004`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:32:54 KST`
- **테스트 종류**: `security`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl HTTP Header Inspector (GET http://127.0.0.1:80/)` → **FAIL (X-Content-Type-Options, X-Frame-Options 헤더 누락)**
- **도구 B 및 결과**: `SAST Nginx Configuration Analyzer (web-vite/nginx.conf)` → **FAIL (nginx.conf 내 add_header 보안 지시자 0건)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `web-vite/nginx.conf` / 함수 `server` / 줄 번호 `4-22`
- **입력값 (Input)**: `GET http://127.0.0.1:80/`
- **오류 메시지 / 응답**: `Missing X-Content-Type-Options, X-Frame-Options headers`
- **예상 결과 (Expected)**: 응답 헤더에 X-Content-Type-Options: nosniff 및 X-Frame-Options: DENY(또는 SAMEORIGIN) 포함
- **실제 결과 (Actual)**: 응답 헤더 내 보안 헤더 미존재 (현재 헤더 키: accept-ranges, connection, content-length, content-type, date, etag, last-modified, server)
- **재현 방법 (Reproduction)**:
  ```zsh
  curl -I http://127.0.0.1:80/
  ```
- **원인 분석 (Root Cause)**: web-vite/nginx.conf의 server 블록(4-22행)에 add_header X-Content-Type-Options "nosniff" 및 add_header X-Frame-Options "DENY" 설정이 누락되어 있음.
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)

### [SEC-005] OWASP ASVS V14.2 프론트엔드 서드파티 패키지 취약점(SCA) 검사 (`FAIL`) — `BUG-SEC-005`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:32:54 KST`
- **테스트 종류**: `security`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `npm audit CLI (npm audit --json)` → **FAIL (high/critical 취약점 1건: undici)**
- **도구 B 및 결과**: `package-lock.json Dependency Graph Inspector` → **FAIL (취약 의존성 트리 감지: undici)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `web-vite/package-lock.json` / 함수 `dependencies / devDependencies` / 줄 번호 `1-50`
- **입력값 (Input)**: `web-vite/package-lock.json`
- **오류 메시지 / 응답**: `npm audit detected 1 high/critical severity vulnerability (undici)`
- **예상 결과 (Expected)**: High/Critical 취약점 0건
- **실제 결과 (Actual)**: High/Critical 취약점 1건 검출 (undici)
- **재현 방법 (Reproduction)**:
  ```zsh
  cd /Users/jeong-yelim/orca/IF_v2/web-vite && npm audit
  ```
- **원인 분석 (Root Cause)**: web-vite/package-lock.json 내 하위 의존성(undici)에 보안 패치 이전 버전이 고정되어 있음.
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)


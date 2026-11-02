# RISK

## 20261030T172345-40bf1ccac6 / RISK-001
- RUN_ID: 20261030T172345-40bf1ccac6
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:23:45.050678+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "OPEN", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33}

## 20261030T172345-40bf1ccac6 / RISK-002
- RUN_ID: 20261030T172345-40bf1ccac6
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:23:45.050678+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172345-40bf1ccac6 / RISK-003
- RUN_ID: 20261030T172345-40bf1ccac6
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:23:45.050678+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172455-160ef4c9a6 / RISK-001
- RUN_ID: 20261030T172455-160ef4c9a6
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:24:55.062349+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "OPEN", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33}

## 20261030T172455-160ef4c9a6 / RISK-002
- RUN_ID: 20261030T172455-160ef4c9a6
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:24:55.062349+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172455-160ef4c9a6 / RISK-003
- RUN_ID: 20261030T172455-160ef4c9a6
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:24:55.062349+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172701-7dd10625a2 / RISK-001
- RUN_ID: 20261030T172701-7dd10625a2
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:27:01.262101+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "OPEN", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33}

## 20261030T172701-7dd10625a2 / RISK-002
- RUN_ID: 20261030T172701-7dd10625a2
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:27:01.262101+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172701-7dd10625a2 / RISK-003
- RUN_ID: 20261030T172701-7dd10625a2
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:27:01.262101+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172701-7dd10625a2 / RISK-004
- RUN_ID: 20261030T172701-7dd10625a2
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:27:01.262101+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "OPEN", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30}

## 20261030T172701-7dd10625a2 / RISK-005
- RUN_ID: 20261030T172701-7dd10625a2
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:27:01.262101+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "OPEN", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12}

## 20261030T172701-24c6ce0dc2 / RISK-001
- RUN_ID: 20261030T172701-24c6ce0dc2
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:27:01.356327+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "OPEN", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33}

## 20261030T172701-24c6ce0dc2 / RISK-002
- RUN_ID: 20261030T172701-24c6ce0dc2
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:27:01.356327+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172701-24c6ce0dc2 / RISK-003
- RUN_ID: 20261030T172701-24c6ce0dc2
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:27:01.356327+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172701-24c6ce0dc2 / RISK-004
- RUN_ID: 20261030T172701-24c6ce0dc2
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:27:01.356327+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "OPEN", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30}

## 20261030T172701-24c6ce0dc2 / RISK-005
- RUN_ID: 20261030T172701-24c6ce0dc2
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:27:01.356327+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "OPEN", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12}

## 20261030T172933-71ba9d567c / RISK-001
- RUN_ID: 20261030T172933-71ba9d567c
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:29:33.478316+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "OPEN", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33}

## 20261030T172933-71ba9d567c / RISK-002
- RUN_ID: 20261030T172933-71ba9d567c
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:29:33.478316+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172933-71ba9d567c / RISK-003
- RUN_ID: 20261030T172933-71ba9d567c
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:29:33.478316+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T172933-71ba9d567c / RISK-004
- RUN_ID: 20261030T172933-71ba9d567c
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:29:33.478316+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "OPEN", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30}

## 20261030T172933-71ba9d567c / RISK-005
- RUN_ID: 20261030T172933-71ba9d567c
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:29:33.478316+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T172933-71ba9d567c / RISK-006
- RUN_ID: 20261030T172933-71ba9d567c
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:29:33.478316+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173027-a0890b20ec / RISK-001
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T173027-a0890b20ec / RISK-002
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173027-a0890b20ec / RISK-003
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173027-a0890b20ec / RISK-004
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T173027-a0890b20ec / RISK-005
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T173027-a0890b20ec / RISK-006
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173203-e98ac2d793 / RISK-001
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T173203-e98ac2d793 / RISK-002
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173203-e98ac2d793 / RISK-003
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173203-e98ac2d793 / RISK-004
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T173203-e98ac2d793 / RISK-005
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T173203-e98ac2d793 / RISK-006
- RUN_ID: 20261030T173203-e98ac2d793
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:32:03.789306+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173302-2effc12f63 / RISK-001
- RUN_ID: 20261030T173302-2effc12f63
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:33:02.049682+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T173302-2effc12f63 / RISK-002
- RUN_ID: 20261030T173302-2effc12f63
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:33:02.049682+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173302-2effc12f63 / RISK-003
- RUN_ID: 20261030T173302-2effc12f63
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:33:02.049682+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173302-2effc12f63 / RISK-004
- RUN_ID: 20261030T173302-2effc12f63
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:33:02.049682+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T173302-2effc12f63 / RISK-005
- RUN_ID: 20261030T173302-2effc12f63
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:33:02.049682+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T173302-2effc12f63 / RISK-006
- RUN_ID: 20261030T173302-2effc12f63
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:33:02.049682+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173302-2effc12f63 / RISK-007
- RUN_ID: 20261030T173302-2effc12f63
- TC_ID: RISK-007
- timestamp: 2026-10-30T17:33:02.049682+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: qa/recorder.py
- function: write_test_type_reports
- line: 159
- ISSUE_ID: 
- RISK_ID: RISK-007
- evidence: UNKNOWN

{"id": "RISK-007", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 추가된 qa/run_qa.py 및 recorder.py가 현재 보고서와 다른 TSV 스키마로 동일 경로에 기록; CI가 서로 다른 게이트를 호출", "recommendation": "파일은 보존하고 CI/스킬을 단일 검증 실행기로 연결; 보조 실행기는 검토 전 공용 보고서 기록 금지", "status": "OPEN", "file": "qa/recorder.py", "function": "write_test_type_reports", "line": 159}
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:33:06 KST)

- **검출/추적 리스크 건수**: 1건

### [RISK-SEC-001] Spring API(/api/assessments/**) 인증·인가 및 요청 처리율 제한(Rate Limit) 부재 위험 (심각도: **HIGH**, 상태: **OPEN**)

- **RUN_ID**: `RUN-20261030-001`
- **관련 TC_ID**: `SEC-001, SEC-004`
- **실행 일시**: `2026-10-30 17:32:54 KST`
- **기능명 / 테스트 종류**: 평가 생성·조회·삭제 API 무인증 노출 및 Rate Limiting 부재 (`security`)
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `OWASP WSTG Authz Probe (curl DELETE without token)` → 인증 헤더 없이 DELETE 및 POST 호출 가능 확인
- **도구 B 및 결과**: `SAST Spring Security & Controller Inspector` → build.gradle 내 spring-boot-starter-security 미포함 및 AssessmentController 인증 어노테이션 부재 확인
- **대상 코드 위치**: 파일 `spring/src/main/demo/assessment/controller/AssessmentController.java` / 함수 `create, delete, result` / 줄 번호 `30-72`
- **심각도 (Severity)**: **HIGH**
- **발생 가능성 (Likelihood)**: **MEDIUM**
- **영향 (Impact)**: 인증 없이 누구나 DELETE /api/assessments/{id}로 타인의 평가 기록을 삭제하거나 POST /api/assessments를 대량 호출하여 Gemini API 쿼터 소진 가능
- **상세 내용**: 간소화 버전(PERSONAL_RISK.md) 설계에 따라 로그인 기능이 생략되어 있으나, 운영 배포 시 무인증 삭제(BOLA/IDOR) 및 AI 호출 비용 고갈 위험이 존재함.
- **권장 조치 (Recommendation)**: 운영 환경 전환 시 Spring Security 기반 인증/권한 검증 추가 및 Nginx limit_req_zone(Rate Limiting) 적용 권장
- **처리 상태 (Status)**: `OPEN`
- **보고 이력 (Report History)**: 2026-10-30 17:32:54 KST (RUN-20261030-001) risk.md 선기록 완료


## 20261030T173420-dd42c9f7f7 / RISK-001
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T173420-dd42c9f7f7 / RISK-002
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173420-dd42c9f7f7 / RISK-003
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173420-dd42c9f7f7 / RISK-004
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T173420-dd42c9f7f7 / RISK-005
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T173420-dd42c9f7f7 / RISK-006
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173420-dd42c9f7f7 / RISK-007
- RUN_ID: 20261030T173420-dd42c9f7f7
- TC_ID: RISK-007
- timestamp: 2026-10-30T17:34:20.980344+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: qa/recorder.py
- function: write_test_type_reports
- line: 159
- ISSUE_ID: 
- RISK_ID: RISK-007
- evidence: UNKNOWN

{"id": "RISK-007", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 추가된 qa/run_qa.py 및 recorder.py가 현재 보고서와 다른 TSV 스키마로 동일 경로에 기록; CI가 서로 다른 게이트를 호출", "recommendation": "파일은 보존하고 CI/스킬을 단일 검증 실행기로 연결; 보조 실행기는 검토 전 공용 보고서 기록 금지", "status": "OPEN", "file": "qa/recorder.py", "function": "write_test_type_reports", "line": 159}

## 20261030T173704-61738eab99 / RISK-001
- RUN_ID: 20261030T173704-61738eab99
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:37:04.716583+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T173704-61738eab99 / RISK-002
- RUN_ID: 20261030T173704-61738eab99
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:37:04.716583+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173704-61738eab99 / RISK-003
- RUN_ID: 20261030T173704-61738eab99
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:37:04.716583+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173704-61738eab99 / RISK-004
- RUN_ID: 20261030T173704-61738eab99
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:37:04.716583+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T173704-61738eab99 / RISK-005
- RUN_ID: 20261030T173704-61738eab99
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:37:04.716583+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T173704-61738eab99 / RISK-006
- RUN_ID: 20261030T173704-61738eab99
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:37:04.716583+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173704-61738eab99 / RISK-007
- RUN_ID: 20261030T173704-61738eab99
- TC_ID: RISK-007
- timestamp: 2026-10-30T17:37:04.716583+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: qa/recorder.py
- function: write_test_type_reports
- line: 159
- ISSUE_ID: 
- RISK_ID: RISK-007
- evidence: UNKNOWN

{"id": "RISK-007", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 추가된 qa/run_qa.py 및 recorder.py가 현재 보고서와 다른 TSV 스키마로 동일 경로에 기록; CI가 서로 다른 게이트를 호출", "recommendation": "파일은 보존하고 CI/스킬을 단일 검증 실행기로 연결; 보조 실행기는 검토 전 공용 보고서 기록 금지", "status": "RESOLVED", "file": "qa/recorder.py", "function": "write_test_type_reports", "line": 159, "resolution": "서로 다른 TSV writer 헤더 차단 테스트 PASS; CI 단일 실행기 연결. 혼합 이력은 원본 SHA256 보존 아카이브를 만든 뒤 열 정규화; qa/archives 참조"}

## 20261030T173704-61738eab99 / RISK-SEC-001
- RUN_ID: 20261030T173704-61738eab99
- TC_ID: RISK-SEC-001
- timestamp: 2026-10-30T17:37:04.716583+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: delete
- line: 67
- ISSUE_ID: 
- RISK_ID: RISK-SEC-001
- evidence: UNKNOWN

{"id": "RISK-SEC-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "평가 API에 인증/인가 설정 부재; 기존 동시 실행 보고서는 무인증 쓰기/삭제도 보고함", "recommendation": "사용자 접근 정책 확정 후 인증·인가 및 권한 TC 구현. 동적 삭제 재현은 이번 세션에서 실행하지 않음", "status": "OPEN", "file": "spring/src/main/demo/assessment/controller/AssessmentController.java", "function": "delete", "line": 67}

## 20261030T173704-61738eab99 / RISK-LEGACY-FAILS
- RUN_ID: 20261030T173704-61738eab99
- TC_ID: RISK-LEGACY-FAILS
- timestamp: 2026-10-30T17:37:04.716583+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: docs/ERROR_LOG.md
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-LEGACY-FAILS
- evidence: UNKNOWN

{"id": "RISK-LEGACY-FAILS", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 실행 RUN-20261030-001에서 기능 및 보안 FAIL 보고; 아직 수정·재검증되지 않음", "recommendation": "docs/ERROR_LOG.md와 날짜별 fail.md의 요구사항/실제 증거 대조 후 필수 TC 편입 및 수정·두 도구 재검증. 원본 결과 보존", "status": "OPEN", "file": "docs/ERROR_LOG.md", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173710-26efa742be / RISK-001
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T173710-26efa742be / RISK-002
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173710-26efa742be / RISK-003
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173710-26efa742be / RISK-004
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T173710-26efa742be / RISK-005
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T173710-26efa742be / RISK-006
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173710-26efa742be / RISK-007
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: RISK-007
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: qa/recorder.py
- function: write_test_type_reports
- line: 159
- ISSUE_ID: 
- RISK_ID: RISK-007
- evidence: UNKNOWN

{"id": "RISK-007", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 추가된 qa/run_qa.py 및 recorder.py가 현재 보고서와 다른 TSV 스키마로 동일 경로에 기록; CI가 서로 다른 게이트를 호출", "recommendation": "파일은 보존하고 CI/스킬을 단일 검증 실행기로 연결; 보조 실행기는 검토 전 공용 보고서 기록 금지", "status": "RESOLVED", "file": "qa/recorder.py", "function": "write_test_type_reports", "line": 159, "resolution": "서로 다른 TSV writer 헤더 차단 테스트 PASS; CI 단일 실행기 연결. 혼합 이력은 원본 SHA256 보존 아카이브를 만든 뒤 열 정규화; qa/archives 참조"}

## 20261030T173710-26efa742be / RISK-SEC-001
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: RISK-SEC-001
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: delete
- line: 67
- ISSUE_ID: 
- RISK_ID: RISK-SEC-001
- evidence: UNKNOWN

{"id": "RISK-SEC-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "평가 API에 인증/인가 설정 부재; 기존 동시 실행 보고서는 무인증 쓰기/삭제도 보고함", "recommendation": "사용자 접근 정책 확정 후 인증·인가 및 권한 TC 구현. 동적 삭제 재현은 이번 세션에서 실행하지 않음", "status": "OPEN", "file": "spring/src/main/demo/assessment/controller/AssessmentController.java", "function": "delete", "line": 67}

## 20261030T173710-26efa742be / RISK-LEGACY-FAILS
- RUN_ID: 20261030T173710-26efa742be
- TC_ID: RISK-LEGACY-FAILS
- timestamp: 2026-10-30T17:37:10.137081+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: docs/ERROR_LOG.md
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-LEGACY-FAILS
- evidence: UNKNOWN

{"id": "RISK-LEGACY-FAILS", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 실행 RUN-20261030-001에서 기능 및 보안 FAIL 보고; 아직 수정·재검증되지 않음", "recommendation": "docs/ERROR_LOG.md와 날짜별 fail.md의 요구사항/실제 증거 대조 후 필수 TC 편입 및 수정·두 도구 재검증. 원본 결과 보존", "status": "OPEN", "file": "docs/ERROR_LOG.md", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173728-084ab85c8a / RISK-001
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T173728-084ab85c8a / RISK-002
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173728-084ab85c8a / RISK-003
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173728-084ab85c8a / RISK-004
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T173728-084ab85c8a / RISK-005
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T173728-084ab85c8a / RISK-006
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173728-084ab85c8a / RISK-007
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: RISK-007
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: qa/recorder.py
- function: write_test_type_reports
- line: 159
- ISSUE_ID: 
- RISK_ID: RISK-007
- evidence: UNKNOWN

{"id": "RISK-007", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 추가된 qa/run_qa.py 및 recorder.py가 현재 보고서와 다른 TSV 스키마로 동일 경로에 기록; CI가 서로 다른 게이트를 호출", "recommendation": "파일은 보존하고 CI/스킬을 단일 검증 실행기로 연결; 보조 실행기는 검토 전 공용 보고서 기록 금지", "status": "RESOLVED", "file": "qa/recorder.py", "function": "write_test_type_reports", "line": 159, "resolution": "서로 다른 TSV writer 헤더 차단 테스트 PASS; CI 단일 실행기 연결. 혼합 이력은 원본 SHA256 보존 아카이브를 만든 뒤 열 정규화; qa/archives 참조"}

## 20261030T173728-084ab85c8a / RISK-SEC-001
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: RISK-SEC-001
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: delete
- line: 67
- ISSUE_ID: 
- RISK_ID: RISK-SEC-001
- evidence: UNKNOWN

{"id": "RISK-SEC-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "평가 API에 인증/인가 설정 부재; 기존 동시 실행 보고서는 무인증 쓰기/삭제도 보고함", "recommendation": "사용자 접근 정책 확정 후 인증·인가 및 권한 TC 구현. 동적 삭제 재현은 이번 세션에서 실행하지 않음", "status": "OPEN", "file": "spring/src/main/demo/assessment/controller/AssessmentController.java", "function": "delete", "line": 67}

## 20261030T173728-084ab85c8a / RISK-LEGACY-FAILS
- RUN_ID: 20261030T173728-084ab85c8a
- TC_ID: RISK-LEGACY-FAILS
- timestamp: 2026-10-30T17:37:28.576232+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: docs/ERROR_LOG.md
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-LEGACY-FAILS
- evidence: UNKNOWN

{"id": "RISK-LEGACY-FAILS", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 실행 RUN-20261030-001에서 기능 및 보안 FAIL 보고; 아직 수정·재검증되지 않음", "recommendation": "docs/ERROR_LOG.md와 날짜별 fail.md의 요구사항/실제 증거 대조 후 필수 TC 편입 및 수정·두 도구 재검증. 원본 결과 보존", "status": "OPEN", "file": "docs/ERROR_LOG.md", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173746-09edf77edc / RISK-001
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T173746-09edf77edc / RISK-002
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173746-09edf77edc / RISK-003
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173746-09edf77edc / RISK-004
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T173746-09edf77edc / RISK-005
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T173746-09edf77edc / RISK-006
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173746-09edf77edc / RISK-007
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: RISK-007
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: qa/recorder.py
- function: write_test_type_reports
- line: 159
- ISSUE_ID: 
- RISK_ID: RISK-007
- evidence: UNKNOWN

{"id": "RISK-007", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 추가된 qa/run_qa.py 및 recorder.py가 현재 보고서와 다른 TSV 스키마로 동일 경로에 기록; CI가 서로 다른 게이트를 호출", "recommendation": "파일은 보존하고 CI/스킬을 단일 검증 실행기로 연결; 보조 실행기는 검토 전 공용 보고서 기록 금지", "status": "RESOLVED", "file": "qa/recorder.py", "function": "write_test_type_reports", "line": 159, "resolution": "서로 다른 TSV writer 헤더 차단 테스트 PASS; CI 단일 실행기 연결. 혼합 이력은 원본 SHA256 보존 아카이브를 만든 뒤 열 정규화; qa/archives 참조"}

## 20261030T173746-09edf77edc / RISK-SEC-001
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: RISK-SEC-001
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: delete
- line: 67
- ISSUE_ID: 
- RISK_ID: RISK-SEC-001
- evidence: UNKNOWN

{"id": "RISK-SEC-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "평가 API에 인증/인가 설정 부재; 기존 동시 실행 보고서는 무인증 쓰기/삭제도 보고함", "recommendation": "사용자 접근 정책 확정 후 인증·인가 및 권한 TC 구현. 동적 삭제 재현은 이번 세션에서 실행하지 않음", "status": "OPEN", "file": "spring/src/main/demo/assessment/controller/AssessmentController.java", "function": "delete", "line": 67}

## 20261030T173746-09edf77edc / RISK-LEGACY-FAILS
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: RISK-LEGACY-FAILS
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: docs/ERROR_LOG.md
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-LEGACY-FAILS
- evidence: UNKNOWN

{"id": "RISK-LEGACY-FAILS", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 실행 RUN-20261030-001에서 기능 및 보안 FAIL 보고; 아직 수정·재검증되지 않음", "recommendation": "docs/ERROR_LOG.md와 날짜별 fail.md의 요구사항/실제 증거 대조 후 필수 TC 편입 및 수정·두 도구 재검증. 원본 결과 보존", "status": "OPEN", "file": "docs/ERROR_LOG.md", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173817-5b5ab53906 / RISK-001
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T173817-5b5ab53906 / RISK-002
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173817-5b5ab53906 / RISK-003
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T173817-5b5ab53906 / RISK-004
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T173817-5b5ab53906 / RISK-005
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T173817-5b5ab53906 / RISK-006
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T173817-5b5ab53906 / RISK-007
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: RISK-007
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: qa/recorder.py
- function: write_test_type_reports
- line: 159
- ISSUE_ID: 
- RISK_ID: RISK-007
- evidence: UNKNOWN

{"id": "RISK-007", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 추가된 qa/run_qa.py 및 recorder.py가 현재 보고서와 다른 TSV 스키마로 동일 경로에 기록; CI가 서로 다른 게이트를 호출", "recommendation": "파일은 보존하고 CI/스킬을 단일 검증 실행기로 연결; 보조 실행기는 검토 전 공용 보고서 기록 금지", "status": "RESOLVED", "file": "qa/recorder.py", "function": "write_test_type_reports", "line": 159, "resolution": "서로 다른 TSV writer 헤더 차단 테스트 PASS; CI 단일 실행기 연결. 혼합 이력은 원본 SHA256 보존 아카이브를 만든 뒤 열 정규화; qa/archives 참조"}

## 20261030T173817-5b5ab53906 / RISK-SEC-001
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: RISK-SEC-001
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: delete
- line: 67
- ISSUE_ID: 
- RISK_ID: RISK-SEC-001
- evidence: UNKNOWN

{"id": "RISK-SEC-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "평가 API에 인증/인가 설정 부재; 기존 동시 실행 보고서는 무인증 쓰기/삭제도 보고함", "recommendation": "사용자 접근 정책 확정 후 인증·인가 및 권한 TC 구현. 동적 삭제 재현은 이번 세션에서 실행하지 않음", "status": "OPEN", "file": "spring/src/main/demo/assessment/controller/AssessmentController.java", "function": "delete", "line": 67}

## 20261030T173817-5b5ab53906 / RISK-LEGACY-FAILS
- RUN_ID: 20261030T173817-5b5ab53906
- TC_ID: RISK-LEGACY-FAILS
- timestamp: 2026-10-30T17:38:17.175568+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: docs/ERROR_LOG.md
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-LEGACY-FAILS
- evidence: UNKNOWN

{"id": "RISK-LEGACY-FAILS", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 실행 RUN-20261030-001에서 기능 및 보안 FAIL 보고; 아직 수정·재검증되지 않음", "recommendation": "docs/ERROR_LOG.md와 날짜별 fail.md의 요구사항/실제 증거 대조 후 필수 TC 편입 및 수정·두 도구 재검증. 원본 결과 보존", "status": "OPEN", "file": "docs/ERROR_LOG.md", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T174647-e942dbd875 / RISK-001
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: RISK-001
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .github/workflows/deploy.yml
- function: jobs.deploy.if
- line: 33
- ISSUE_ID: 
- RISK_ID: RISK-001
- evidence: UNKNOWN

{"id": "RISK-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "수동 배포가 필수 CI 검사를 우회할 수 있음", "recommendation": "수동 실행에서도 동일 SHA의 성공한 CI 확인", "status": "RESOLVED", "file": ".github/workflows/deploy.yml", "function": "jobs.deploy.if", "line": 33, "resolution": "실제 배포 셸의 실패/다른 SHA/다른 브랜치/PR 차단 및 성공 조건 테스트 PASS; actionlint 재검증 예정"}

## 20261030T174647-e942dbd875 / RISK-002
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: RISK-002
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-002
- evidence: UNKNOWN

{"id": "RISK-002", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "권한 요구사항 및 실제 배포 환경 E2E/성능 기준이 확정되지 않아 전체 보안 보증 불가", "recommendation": "역할별 권한 명세, 테스트 환경 URL, 부하 및 지연 기준 확정 후 TC 추가", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T174647-e942dbd875 / RISK-003
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: RISK-003
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-003
- evidence: UNKNOWN

{"id": "RISK-003", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "로컬 훅은 우회 가능하고 원격 브랜치 보호 설정은 저장소 파일만으로 강제할 수 없음", "recommendation": "GitHub ruleset에서 CI / QA gate 필수 및 관리자 우회 제한 설정", "status": "OPEN", "file": "UNKNOWN", "function": "UNKNOWN", "line": "UNKNOWN"}

## 20261030T174647-e942dbd875 / RISK-004
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: RISK-004
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/src/rag/embedder.py
- function: _local_fallback_embedding
- line: 30
- ISSUE_ID: 
- RISK_ID: RISK-004
- evidence: UNKNOWN

{"id": "RISK-004", "severity": "HIGH", "likelihood": "LOW", "impact": "Bandit B324: MD5 사용 목적이 비보안 임베딩임을 코드에서 명시하지 않음", "recommendation": "usedforsecurity=False를 명시해 기존 임베딩 호환 유지; 정적 검사와 RAG 회귀 재실행", "status": "RESOLVED", "file": "ai/src/rag/embedder.py", "function": "_local_fallback_embedding", "line": 30, "resolution": "ai/src/rag/embedder.py:30 usedforsecurity=False; QA-AI pytest/Ruff 및 QA-SECURITY Bandit/Secret-policy 재검증 20261030T172701-24c6ce0dc2 모두 PASS"}

## 20261030T174647-e942dbd875 / RISK-005
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: RISK-005
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: .agents/skills/qa-security-v25/SKILL.md
- function: UNKNOWN
- line: 12
- ISSUE_ID: 
- RISK_ID: RISK-005
- evidence: UNKNOWN

{"id": "RISK-005", "severity": "MEDIUM", "likelihood": "HIGH", "impact": "기존 .agents 스킬이 존재하지 않는 qa/run_qa.py를 참조하고 hook 명령 경로도 실제 파일과 다름", "recommendation": "기존 파일을 보존하며 실제 실행기로 연결; host가 이 hook 계약을 지원하는지는 별도 확인", "status": "RESOLVED", "file": ".agents/skills/qa-security-v25/SKILL.md", "function": "UNKNOWN", "line": 12, "resolution": "기존 스킬 및 hooks.json을 실제 경로로 연결; host hook 지원 자체는 검증 범위 제외"}

## 20261030T174647-e942dbd875 / RISK-006
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: RISK-006
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: NOT_RUN
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: data/etl/transform.py
- function: parse_data
- line: 70
- ISSUE_ID: 
- RISK_ID: RISK-006
- evidence: UNKNOWN

{"id": "RISK-006", "severity": "MEDIUM", "likelihood": "MEDIUM", "impact": "Bandit B314/B405: 외부 XML을 표준 ElementTree로 파싱", "recommendation": "defusedxml 전환 및 엔티티 확장/대형 XML 거절 TC 추가", "status": "OPEN", "file": "data/etl/transform.py", "function": "parse_data", "line": 70}

## 20261030T174647-e942dbd875 / RISK-007
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: RISK-007
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: qa/recorder.py
- function: write_test_type_reports
- line: 159
- ISSUE_ID: 
- RISK_ID: RISK-007
- evidence: UNKNOWN

{"id": "RISK-007", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 추가된 qa/run_qa.py 및 recorder.py가 현재 보고서와 다른 TSV 스키마로 동일 경로에 기록; CI가 서로 다른 게이트를 호출", "recommendation": "파일은 보존하고 CI/스킬을 단일 검증 실행기로 연결; 보조 실행기는 검토 전 공용 보고서 기록 금지", "status": "RESOLVED", "file": "qa/recorder.py", "function": "write_test_type_reports", "line": 159, "resolution": "서로 다른 TSV writer 헤더 차단 테스트 PASS; CI 단일 실행기 연결. 혼합 이력은 원본 SHA256 보존 아카이브를 만든 뒤 열 정규화; qa/archives 참조"}

## 20261030T174647-e942dbd875 / RISK-SEC-001
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: RISK-SEC-001
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: delete
- line: 67
- ISSUE_ID: 
- RISK_ID: RISK-SEC-001
- evidence: UNKNOWN

{"id": "RISK-SEC-001", "severity": "HIGH", "likelihood": "MEDIUM", "impact": "평가 API에 인증/인가 설정 부재; 기존 동시 실행 보고서는 무인증 쓰기/삭제도 보고함", "recommendation": "사용자 접근 정책 확정 후 인증·인가 및 권한 TC 구현. 동적 삭제 재현은 이번 세션에서 실행하지 않음", "status": "OPEN", "file": "spring/src/main/demo/assessment/controller/AssessmentController.java", "function": "delete", "line": 67}

## 20261030T174647-e942dbd875 / RISK-LEGACY-FAILS
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: RISK-LEGACY-FAILS
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: QA V2.5
- test_type: security
- tool_a: UNKNOWN
- command_a: UNKNOWN
- result_a: UNKNOWN
- tool_b: UNKNOWN
- command_b: UNKNOWN
- result_b: UNKNOWN
- status: BLOCKED
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: docs/ERROR_LOG.md
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: RISK-LEGACY-FAILS
- evidence: UNKNOWN

{"id": "RISK-LEGACY-FAILS", "severity": "HIGH", "likelihood": "HIGH", "impact": "병행 실행 RUN-20261030-001에서 기능 및 보안 FAIL 보고; 아직 수정·재검증되지 않음", "recommendation": "docs/ERROR_LOG.md와 날짜별 fail.md의 요구사항/실제 증거 대조 후 필수 TC 편입 및 수정·두 도구 재검증. 원본 결과 보존", "status": "OPEN", "file": "docs/ERROR_LOG.md", "function": "UNKNOWN", "line": "UNKNOWN"}

# PASS

## 20261103T023235-7994cf0a4f / TC-SEC-SAST-001
- RUN_ID: 20261103T023235-7994cf0a4f
- TC_ID: TC-SEC-SAST-001
- FEATURE_ID: FEAT-SEC-SAST
- timestamp_start: 2026-11-03T02:33:40+09:00
- timestamp_end: 2026-11-03T02:35:02+09:00
- area: 03_security_quality
- section: sast
- scenario: Semgrep과 CodeQL/비밀키 교차
- tool_a: Semgrep
- command_a: python3 scripts/qa/probes/semgrep_run.py
- result_a: PASS
- expected_a: PASS
- actual_a: exit 0
- tool_b: CodeQL_or_secret_policy
- command_b: python3 scripts/qa/probes/codeql_or_fallback.py
- result_b: PASS
- expected_b: PASS
- actual_b: NOT_RUN/local: CodeQL CLI absent; running secret-policy fallback secret-policy PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T023235-7994cf0a4f/Semgrep.log#84958162b8d607b3;qa/.runtime/20261103T023235-7994cf0a4f/CodeQL_or_secret_policy.log#0d891df3214b2ffa

시나리오: Semgrep과 CodeQL/비밀키 교차
비교: Semgrep + CodeQL(가능 시)/비밀키 패턴 폴백. CodeQL 로컬 미설치 시 CI CodeQL과 RISK-V30-002.
1차: Semgrep 기대=PASS 실제=PASS
2차: CodeQL_or_secret_policy 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T034221-c3386f4577 / TC-SEC-SAST-001
- RUN_ID: 20261103T034221-c3386f4577
- TC_ID: TC-SEC-SAST-001
- FEATURE_ID: FEAT-SEC-SAST
- timestamp_start: 2026-11-03T04:04:15+09:00
- timestamp_end: 2026-11-03T04:05:12+09:00
- area: 03_security_quality
- section: sast
- scenario: Semgrep + CodeQL(가능 시)/비밀키 패턴 폴백. CodeQL 로컬 미설치 시 CI CodeQL과 RISK-V30-002.
- tool_a: Semgrep
- command_a: python3 scripts/qa/probes/semgrep_run.py
- result_a: PASS
- expected_a: PASS
- actual_a: exit 0
- tool_b: CodeQL_or_secret_policy
- command_b: python3 scripts/qa/probes/codeql_or_fallback.py
- result_b: PASS
- expected_b: PASS
- actual_b: NOT_RUN/local: CodeQL CLI absent; running secret-policy fallback secret-policy PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034221-c3386f4577/Semgrep.log#84958162b8d607b3;qa/.runtime/20261103T034221-c3386f4577/CodeQL_or_secret_policy.log#0d891df3214b2ffa

시나리오: Semgrep + CodeQL(가능 시)/비밀키 패턴 폴백. CodeQL 로컬 미설치 시 CI CodeQL과 RISK-V30-002.
비교: Semgrep + CodeQL(가능 시)/비밀키 패턴 폴백. CodeQL 로컬 미설치 시 CI CodeQL과 RISK-V30-002.
1차: Semgrep 기대=PASS 실제=PASS
2차: CodeQL_or_secret_policy 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

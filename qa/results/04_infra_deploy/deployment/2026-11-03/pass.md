# PASS

## 20261103T023235-7994cf0a4f / TC-INFRA-COMPOSE-001
- RUN_ID: 20261103T023235-7994cf0a4f
- TC_ID: TC-INFRA-COMPOSE-001
- FEATURE_ID: FEAT-COMPOSE
- timestamp_start: 2026-11-03T02:32:42+09:00
- timestamp_end: 2026-11-03T02:32:58+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Compose 설정과 HTTP 스모크
- tool_a: compose_config
- command_a: python3 scripts/qa/probes/compose_ready.py
- result_a: PASS
- expected_a: PASS
- actual_a: OK compose config; postgres healthcheck present
- tool_b: curl_smoke
- command_b: python3 scripts/qa/probes/http_blackbox.py --base http://127.0.0.1:8000 --path /docs --allow-blocked
- result_b: PASS
- expected_b: PASS
- actual_b: OK 200 http://127.0.0.1:8000/docs bytes=200
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: compose.yaml
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T023235-7994cf0a4f/compose_config.log#0b36de23f1313960;qa/.runtime/20261103T023235-7994cf0a4f/curl_smoke.log#edb22dffb2e58a9d

시나리오: Compose 설정과 HTTP 스모크
비교: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
1차: compose_config 기대=PASS 실제=PASS
2차: curl_smoke 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T034221-c3386f4577 / TC-INFRA-COMPOSE-001
- RUN_ID: 20261103T034221-c3386f4577
- TC_ID: TC-INFRA-COMPOSE-001
- FEATURE_ID: FEAT-COMPOSE
- timestamp_start: 2026-11-03T04:05:13+09:00
- timestamp_end: 2026-11-03T04:05:27+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
- tool_a: compose_config
- command_a: python3 scripts/qa/probes/compose_ready.py
- result_a: PASS
- expected_a: PASS
- actual_a: OK compose config; postgres healthcheck present
- tool_b: curl_smoke
- command_b: python3 scripts/qa/probes/http_blackbox.py --base http://127.0.0.1:8000 --path /docs --allow-blocked
- result_b: PASS
- expected_b: PASS
- actual_b: OK 200 http://127.0.0.1:8000/docs bytes=200
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034221-c3386f4577/compose_config.log#0b36de23f1313960;qa/.runtime/20261103T034221-c3386f4577/curl_smoke.log#edb22dffb2e58a9d

시나리오: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
비교: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
1차: compose_config 기대=PASS 실제=PASS
2차: curl_smoke 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T041121-74509b288b / TC-INFRA-COMPOSE-001
- RUN_ID: 20261103T041121-74509b288b
- TC_ID: TC-INFRA-COMPOSE-001
- FEATURE_ID: FEAT-COMPOSE
- timestamp_start: 2026-11-03T04:11:25+09:00
- timestamp_end: 2026-11-03T04:11:49+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
- tool_a: compose_config
- command_a: python3 scripts/qa/probes/compose_ready.py
- result_a: PASS
- expected_a: PASS
- actual_a: OK compose config; postgres healthcheck present
- tool_b: curl_smoke
- command_b: python3 scripts/qa/probes/http_blackbox.py --base http://127.0.0.1:8000 --path /docs --allow-blocked
- result_b: PASS
- expected_b: PASS
- actual_b: OK 200 http://127.0.0.1:8000/docs bytes=200
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T041121-74509b288b/compose_config.log#0b36de23f1313960;qa/.runtime/20261103T041121-74509b288b/curl_smoke.log#edb22dffb2e58a9d

시나리오: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
비교: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
1차: compose_config 기대=PASS 실제=PASS
2차: curl_smoke 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

## 20261103T040956-523c5ec792 / TC-INFRA-COMPOSE-001
- RUN_ID: 20261103T040956-523c5ec792
- TC_ID: TC-INFRA-COMPOSE-001
- FEATURE_ID: FEAT-COMPOSE
- timestamp_start: 2026-11-03T04:16:14+09:00
- timestamp_end: 2026-11-03T04:16:16+09:00
- area: 04_infra_deploy
- section: deployment
- scenario: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
- tool_a: compose_config
- command_a: python3 scripts/qa/probes/compose_ready.py
- result_a: PASS
- expected_a: PASS
- actual_a: OK compose config; postgres healthcheck present
- tool_b: curl_smoke
- command_b: python3 scripts/qa/probes/http_blackbox.py --base http://127.0.0.1:8000 --path /docs --allow-blocked
- result_b: PASS
- expected_b: PASS
- actual_b: OK 200 http://127.0.0.1:8000/docs bytes=200
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: UNKNOWN
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T040956-523c5ec792/compose_config.log#0b36de23f1313960;qa/.runtime/20261103T040956-523c5ec792/curl_smoke.log#edb22dffb2e58a9d

시나리오: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
비교: Compose 설정/health 계약 + curl HTTP 스모크(스택 미기동 시 BLOCKED, PASS 아님).
1차: compose_config 기대=PASS 실제=PASS
2차: curl_smoke 기대=PASS 실제=PASS
최종=PASS. 미실행을 PASS로 처리하지 않음.

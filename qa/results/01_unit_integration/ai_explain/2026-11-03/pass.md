# PASS

## 20261103T033035-526c702671 / IF-0247
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0247
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:05+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: API 키 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: API 키 없음
기대: source=basic; 한국어 기본 설명
1차=PASS 2차=PASS 최종=PASS
입력: GEMINI_API_KEY 비우기

## 20261103T033035-526c702671 / IF-0248
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0248
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:05+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: Gemini 정상
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Gemini 정상
기대: source=gemini; trim 적용
1차=PASS 2차=PASS 최종=PASS
입력: 응답 텍스트가 있는 mock

## 20261103T033035-526c702671 / IF-0249
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0249
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:05+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: Gemini 빈 텍스트
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Gemini 빈 텍스트
기대: source=basic
1차=PASS 2차=PASS 최종=PASS
입력: response.text=None mock

## 20261103T033035-526c702671 / IF-0250
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0250
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:05+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: Gemini 예외
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: Gemini 예외
기대: source=basic
1차=PASS 2차=PASS 최종=PASS
입력: generate_content 예외 mock

## 20261103T033035-526c702671 / IF-0251
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0251
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:05+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 최대 요인 동률
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 최대 요인 동률
기대: max는 첫 번째 동률 항목 선택
1차=PASS 2차=PASS 최종=PASS
입력: factors points 동률

## 20261103T033035-526c702671 / IF-0252
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0252
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:05+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 점수 등급 LOW
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 점수 등급 LOW
기대: 기본 설명에 낮음 포함
1차=PASS 2차=PASS 최종=PASS
입력: LOW result

## 20261103T033035-526c702671 / IF-0253
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0253
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 점수 등급 MID
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 점수 등급 MID
기대: 보통 포함
1차=PASS 2차=PASS 최종=PASS
입력: MID result

## 20261103T033035-526c702671 / IF-0254
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0254
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 점수 등급 HIGH
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 점수 등급 HIGH
기대: 높음 포함
1차=PASS 2차=PASS 최종=PASS
입력: HIGH result

## 20261103T033035-526c702671 / IF-0255
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0255
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 경고 문구
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: 경고 문구
기대: 사고 확률 단정하지 않는 문장 포함
1차=PASS 2차=PASS 최종=PASS
입력: 점수 모델 출력

## 20261103T034653-861cf08d61 / IF-0247
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0247
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:45+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: API 키 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: API 키 없음
기대: source=basic; 한국어 기본 설명
1차=PASS 2차=PASS 최종=PASS
입력: GEMINI_API_KEY 비우기

## 20261103T034653-861cf08d61 / IF-0248
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0248
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:45+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: Gemini 정상
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Gemini 정상
기대: source=gemini; trim 적용
1차=PASS 2차=PASS 최종=PASS
입력: 응답 텍스트가 있는 mock

## 20261103T034653-861cf08d61 / IF-0249
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0249
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:45+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: Gemini 빈 텍스트
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Gemini 빈 텍스트
기대: source=basic
1차=PASS 2차=PASS 최종=PASS
입력: response.text=None mock

## 20261103T034653-861cf08d61 / IF-0250
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0250
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: Gemini 예외
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: Gemini 예외
기대: source=basic
1차=PASS 2차=PASS 최종=PASS
입력: generate_content 예외 mock

## 20261103T034653-861cf08d61 / IF-0251
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0251
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 최대 요인 동률
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 최대 요인 동률
기대: max는 첫 번째 동률 항목 선택
1차=PASS 2차=PASS 최종=PASS
입력: factors points 동률

## 20261103T034653-861cf08d61 / IF-0252
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0252
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 점수 등급 LOW
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 점수 등급 LOW
기대: 기본 설명에 낮음 포함
1차=PASS 2차=PASS 최종=PASS
입력: LOW result

## 20261103T034653-861cf08d61 / IF-0253
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0253
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 점수 등급 MID
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 점수 등급 MID
기대: 보통 포함
1차=PASS 2차=PASS 최종=PASS
입력: MID result

## 20261103T034653-861cf08d61 / IF-0254
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0254
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 점수 등급 HIGH
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 점수 등급 HIGH
기대: 높음 포함
1차=PASS 2차=PASS 최종=PASS
입력: HIGH result

## 20261103T034653-861cf08d61 / IF-0255
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0255
- FEATURE_ID: FEAT-AI 설명
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_explain
- scenario: 경고 문구
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: PASS
- expected_a: PASS
- actual_a: mapped suite result=PASS
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: PASS
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ai_explain.py
- function: explain → 기본 문구/LLM 분기
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: 경고 문구
기대: 사고 확률 단정하지 않는 문장 포함
1차=PASS 2차=PASS 최종=PASS
입력: 점수 모델 출력

# PASS

## 20261103T033035-526c702671 / IF-0256
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0256
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: ML 최초 로드
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
- code_file: ai/src/ml_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: ML 최초 로드
기대: joblib 모델을 한 번 로드
1차=PASS 2차=PASS 최종=PASS
입력: _models=None

## 20261103T033035-526c702671 / IF-0257
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0257
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: ML 재호출
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
- code_file: ai/src/ml_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: ML 재호출
기대: 재로딩 없이 캐시 사용
1차=PASS 2차=PASS 최종=PASS
입력: _models 존재

## 20261103T033035-526c702671 / IF-0258
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0258
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: ML 정상 범위
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
- code_file: ai/src/ml_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: ML 정상 범위
기대: 라벨별 확률 0~1
1차=PASS 2차=PASS 최종=PASS
입력: 직무명=운전기사

## 20261103T033035-526c702671 / IF-0260
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0260
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 0글자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DL 0글자
기대: padding 100자리
1차=PASS 2차=PASS 최종=PASS
입력: title=""

## 20261103T033035-526c702671 / IF-0261
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0261
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 1글자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DL 1글자
기대: 1개 토큰+99개 패딩
1차=PASS 2차=PASS 최종=PASS
입력: title="가"

## 20261103T033035-526c702671 / IF-0262
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0262
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 100글자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DL 100글자
기대: 길이 100 유지
1차=PASS 2차=PASS 최종=PASS
입력: 100자 제목

## 20261103T033035-526c702671 / IF-0263
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0263
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 101글자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DL 101글자
기대: 101번째 자르기
1차=PASS 2차=PASS 최종=PASS
입력: 101자 제목

## 20261103T033035-526c702671 / IF-0264
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0264
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 미등록 문자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DL 미등록 문자
기대: ID=1
1차=PASS 2차=PASS 최종=PASS
입력: vocab에 없는 글자

## 20261103T033035-526c702671 / IF-0265
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0265
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 첫 로드
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DL 첫 로드
기대: torch.load 1회 후 eval
1차=PASS 2차=PASS 최종=PASS
입력: _model=None

## 20261103T033035-526c702671 / IF-0266
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0266
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 재호출
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DL 재호출
기대: 모델 캐시 유지
1차=PASS 2차=PASS 최종=PASS
입력: _model 존재

## 20261103T033035-526c702671 / IF-0267
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0267
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 값 범위
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DL 값 범위
기대: sigmoid 결과 0~1
1차=PASS 2차=PASS 최종=PASS
입력: 직무명=운전기사

## 20261103T034653-861cf08d61 / IF-0256
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0256
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: ML 최초 로드
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
- code_file: ai/src/ml_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: ML 최초 로드
기대: joblib 모델을 한 번 로드
1차=PASS 2차=PASS 최종=PASS
입력: _models=None

## 20261103T034653-861cf08d61 / IF-0257
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0257
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: ML 재호출
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
- code_file: ai/src/ml_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: ML 재호출
기대: 재로딩 없이 캐시 사용
1차=PASS 2차=PASS 최종=PASS
입력: _models 존재

## 20261103T034653-861cf08d61 / IF-0258
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0258
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: ML 정상 범위
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
- code_file: ai/src/ml_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: ML 정상 범위
기대: 라벨별 확률 0~1
1차=PASS 2차=PASS 최종=PASS
입력: 직무명=운전기사

## 20261103T034653-861cf08d61 / IF-0260
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0260
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 0글자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DL 0글자
기대: padding 100자리
1차=PASS 2차=PASS 최종=PASS
입력: title=""

## 20261103T034653-861cf08d61 / IF-0261
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0261
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 1글자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DL 1글자
기대: 1개 토큰+99개 패딩
1차=PASS 2차=PASS 최종=PASS
입력: title="가"

## 20261103T034653-861cf08d61 / IF-0262
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0262
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 100글자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DL 100글자
기대: 길이 100 유지
1차=PASS 2차=PASS 최종=PASS
입력: 100자 제목

## 20261103T034653-861cf08d61 / IF-0263
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0263
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 101글자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DL 101글자
기대: 101번째 자르기
1차=PASS 2차=PASS 최종=PASS
입력: 101자 제목

## 20261103T034653-861cf08d61 / IF-0264
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0264
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 미등록 문자
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DL 미등록 문자
기대: ID=1
1차=PASS 2차=PASS 최종=PASS
입력: vocab에 없는 글자

## 20261103T034653-861cf08d61 / IF-0265
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0265
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 첫 로드
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DL 첫 로드
기대: torch.load 1회 후 eval
1차=PASS 2차=PASS 최종=PASS
입력: _model=None

## 20261103T034653-861cf08d61 / IF-0266
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0266
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 재호출
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DL 재호출
기대: 모델 캐시 유지
1차=PASS 2차=PASS 최종=PASS
입력: _model 존재

## 20261103T034653-861cf08d61 / IF-0267
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0267
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:47+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 값 범위
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
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DL 값 범위
기대: sigmoid 결과 0~1
1차=PASS 2차=PASS 최종=PASS
입력: 직무명=운전기사

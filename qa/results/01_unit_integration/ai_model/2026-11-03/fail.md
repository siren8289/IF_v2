# FAIL

## 20261103T033035-526c702671 / IF-0259
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0259
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: ML 모델 파일 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ml_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: ML 모델 파일 없음
기대: 오류와 로그 확인
1차=FAIL 2차=PASS 최종=FAIL
입력: task_ml.joblib 누락 모킹

## 20261103T033035-526c702671 / IF-0268
- RUN_ID: 20261103T033035-526c702671
- TC_ID: IF-0268
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T03:41:40+09:00
- timestamp_end: 2026-11-03T03:42:06+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 모델 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T033035-526c702671/ai.xml#b53be1dd39a6f9f9;qa/.runtime/20261103T033035-526c702671/web.xml#e61a375ed2b8c84c;qa/.runtime/20261103T033035-526c702671/data.xml#eae001a504e6b8d8

시트 시나리오: DL 모델 없음
기대: 서버 오류 기록
1차=FAIL 2차=PASS 최종=FAIL
입력: task_cnn.pt 누락 모킹

## 20261103T034653-861cf08d61 / IF-0259
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0259
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:46+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: ML 모델 파일 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/ml_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: ML 모델 파일 없음
기대: 오류와 로그 확인
1차=FAIL 2차=PASS 최종=FAIL
입력: task_ml.joblib 누락 모킹

## 20261103T034653-861cf08d61 / IF-0268
- RUN_ID: 20261103T034653-861cf08d61
- TC_ID: IF-0268
- FEATURE_ID: FEAT-AI 모델
- timestamp_start: 2026-11-03T04:09:13+09:00
- timestamp_end: 2026-11-03T04:09:47+09:00
- area: 01_unit_integration
- section: ai_model
- scenario: DL 모델 없음
- tool_a: automated_junit_or_pytest
- command_a: parsed from suite XML
- result_a: FAIL
- expected_a: PASS
- actual_a: mapped suite result=FAIL
- tool_b: Ruff
- command_b: ruff check
- result_b: PASS
- expected_b: PASS
- actual_b: cross=PASS
- status: FAIL
- git_commit: aad712788755
- dirty: true
- code_file: ai/src/dl_model.py
- function: 모델 로드/토큰 인코딩/예측
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261103T034653-861cf08d61/ai.xml#f49abe259694447c;qa/.runtime/20261103T034653-861cf08d61/web.xml#841979877a3e16ec;qa/.runtime/20261103T034653-861cf08d61/data.xml#7a8bbb0f95e656b8

시트 시나리오: DL 모델 없음
기대: 서버 오류 기록
1차=FAIL 2차=PASS 최종=FAIL
입력: task_cnn.pt 누락 모킹

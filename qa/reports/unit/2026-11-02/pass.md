# PASS

## RUN-20261102-001 / QA-UNIT-AI-SCORE
- RUN_ID: RUN-20261102-001
- TC_ID: QA-UNIT-AI-SCORE
- timestamp: 2026-11-02T11:57:51+09:00
- feature: 위험 점수 등급 경계
- test_type: unit
- tool_a: python
- command_a: import ai/src/risk_score.py grade_of/calculate_score
- result_a: PASS
- tool_b: unittest
- command_b: temp test_grade_gate.py
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a9
- dirty: true
- files: ai/src/risk_score.py
- function: grade_of
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: python=ok unittest=. ---------------------------------------------------------------------- Ran 1 test in 0.000s OK

검증 목적: 40/41, 60/61 경계와 0점, 100점 규칙을 두 실행기로 확인한다.
이 검사는 FastAPI, torch, pytest를 불러오지 않는다. 공식 파일 ai/tests/test_risk_score.py 는 다음 TC다.
기대: LOW/MID/HIGH와 0/100. 실제 A=PASS B=PASS.
A출력: ok

B출력: .
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

## RUN-20261102-001 / QA-UNIT-AI-PYTEST
- RUN_ID: RUN-20261102-001
- TC_ID: QA-UNIT-AI-PYTEST
- timestamp: 2026-11-02T11:57:51+09:00
- feature: 공식 FastAPI 점수 테스트 파일
- test_type: unit
- tool_a: pytest
- command_a: python3 -m pytest tests/test_risk_score.py -q
- result_a: PASS
- tool_b: python
- command_b: assert test function names exist in ai/tests/test_risk_score.py
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a9
- dirty: true
- files: ai/tests/test_risk_score.py
- function: test_grade_boundaries
- line: 11
- ISSUE_ID: 
- RISK_ID: 
- evidence: ..... [100%] =============================== warnings summary =============================== ../.venv/lib/python3.11/site-packages/fastapi/testclient.py:1 /Users/jeong-yelim/orca/IF_v2/.venv/lib/python3.11/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starl

검증 목적: ai/tests/test_risk_score.py 를 수집해 실행한다.
이 파일은 src.main 을 불러 torch, scikit-learn, fastapi가 필요하다. 의존성이 없으면 ERROR이며 PASS로 올리지 않는다. test_rag.py 는 이번 명령에 없다.
기대: pytest 종료 0. 실제 A=PASS B=PASS code=0.
출력:
.....                                                                    [100%]
=============================== warnings summary ===============================
../.venv/lib/python3.11/site-packages/fastapi/testclient.py:1
  /Users/jeong-yelim/orca/IF_v2/.venv/lib/python3.11/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
5 passed, 1 warning in 4.22s

## RUN-20261102-001 / QA-UNIT-DATA
- RUN_ID: RUN-20261102-001
- TC_ID: QA-UNIT-DATA
- timestamp: 2026-11-02T11:57:51+09:00
- feature: ETL 변환 단위 테스트
- test_type: unit
- tool_a: unittest
- command_a: python3 -m unittest discover -s data/tests -v
- result_a: PASS
- tool_b: python
- command_b: parse_data XML fixture
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a9
- dirty: true
- files: data/tests/test_transform.py
- function: test_parse_xml
- line: 8
- ISSUE_ID: 
- RISK_ID: 
- evidence: unittest=test_duplicate_removed (test_transform.TestTransform.test_duplicate_removed) ... ok test_json_parsing (test_transform.TestTransform.test_json_parsing) ... ok te direct=ok

검증 목적: data/tests의 기존 3건과 XML 한 건의 직접 호출이 맞는지 본다.
직접 호출은 unittest 전체의 대체 실행이 아니라 같은 parse_data 경로의 두 번째 도구다.
기대: 둘 다 성공. 실제 A=PASS B=PASS.
test_duplicate_removed (test_transform.TestTransform.test_duplicate_removed) ... ok
test_json_parsing (test_transform.TestTransform.test_json_parsing) ... ok
test_parse_xml (test_transform.TestTransform.test_parse_xml) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

ok

## RUN-20261102-001 / QA-UNIT-WEB
- RUN_ID: RUN-20261102-001
- TC_ID: QA-UNIT-WEB
- timestamp: 2026-11-02T11:57:51+09:00
- feature: 프론트 단위 테스트와 타입 검사
- test_type: unit
- tool_a: Vitest
- command_a: npm test
- result_a: PASS
- tool_b: tsc
- command_b: npm run typecheck
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a9
- dirty: true
- files: web-vite/src/pages/pages.test.tsx
- function: UNKNOWN
- line: 24
- ISSUE_ID: 
- RISK_ID: 
- evidence: vitest=> if-web-vite@0.2.0 test > vitest run RUN v5.0.3 /Users/jeong-yelim/orca/IF_v2/web-vite ✓ src/shared/api/client.test.ts (4 tests) 7ms ✓ src/pages/pages.test.tsx tsc=> if-web-vite@0.2.0 typecheck > tsc --noEmit

검증 목적: 기존 Vitest와 tsc --noEmit을 각각 실행한다.
둘은 범위가 다르다. Vitest는 동작, tsc는 타입이다. 한쪽만 성공하면 PASS가 아니다.
기대: 둘 다 종료 0. 실제 A=PASS B=PASS.

> if-web-vite@0.2.0 test
> vitest run


 RUN  v5.0.3 /Users/jeong-yelim/orca/IF_v2/web-vite

 ✓ src/shared/api/client.test.ts (4 tests) 7ms
 ✓ src/pages/pages.test.tsx (3 tests) 174ms

 Test Files  2 passed (2)
      Tests  7 passed (7)
   Start at  11:58:08
   Duration  1.11s (environment 65%, setup 13%, tests 10%, transform 7%, import 4%)

npm notice
npm notice New major version of npm available! 11.16.0 -> 12.2.1
npm notice Changelog: https://github.com/npm/cli/releases/tag/v12.2.1
npm notice To update run: npm install -g npm@12.2.1
npm notice


> if-web-vite@0.2.0 typecheck
> tsc --noEmit
## 20261102T130018-a7c3e91b04 / IF-0178
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0178
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(0)=0.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0.00000000. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0179
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0179
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(1)=0.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0.00000000. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0180
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0180
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(59)=0.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0.00000000. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0181
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0181
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(60)=0.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0.00000000. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0182
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0182
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(61)=0.66666667
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0.66666667. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0183
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0183
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(72)=8.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 8.00000000. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0184
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0184
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(89)=19.33333333
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 19.33333333. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0185
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0185
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(90)=20.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 20.00000000. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0186
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0186
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(91)=20.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 20.00000000. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0187
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0187
- timestamp: 2026-11-02T13:00:18+09:00
- feature: age_points(120)=20.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: age_points
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 20.00000000. pytest 소수 8자리 비교 통과. 소스 39-44행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0188
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0188
- timestamp: 2026-11-02T13:00:18+09:00
- feature: health_points(1)=0.0
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: health_points
- line: 47
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0.0. pytest 소수 8자리 비교 통과. 소스 52행 (level-1)*25/4 와 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0189
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0189
- timestamp: 2026-11-02T13:00:18+09:00
- feature: health_points(2)=6.25
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: health_points
- line: 47
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 6.25. pytest 소수 8자리 비교 통과. 소스 52행 (level-1)*25/4 와 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0190
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0190
- timestamp: 2026-11-02T13:00:18+09:00
- feature: health_points(3)=12.5
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: health_points
- line: 47
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 12.5. pytest 소수 8자리 비교 통과. 소스 52행 (level-1)*25/4 와 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0191
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0191
- timestamp: 2026-11-02T13:00:18+09:00
- feature: health_points(4)=18.75
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: health_points
- line: 47
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 18.75. pytest 소수 8자리 비교 통과. 소스 52행 (level-1)*25/4 와 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0192
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0192
- timestamp: 2026-11-02T13:00:18+09:00
- feature: health_points(5)=25.0
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: health_points
- line: 47
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 25.0. pytest 소수 8자리 비교 통과. 소스 52행 (level-1)*25/4 와 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0193
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0193
- timestamp: 2026-11-02T13:00:18+09:00
- feature: chronic_points(False)=0
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: chronic_points
- line: 55
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0. pytest 통과. 소스 57행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0194
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0194
- timestamp: 2026-11-02T13:00:18+09:00
- feature: chronic_points(True)=15
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: chronic_points
- line: 55
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 15. pytest 통과. 소스 57행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0195
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0195
- timestamp: 2026-11-02T13:00:18+09:00
- feature: work_hour_points(1)=10.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: work_hour_points
- line: 60
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 10.00000000. pytest 소수 8자리 비교 통과. 소스 66-68행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0196
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0196
- timestamp: 2026-11-02T13:00:18+09:00
- feature: work_hour_points(2)=8.57142857
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: work_hour_points
- line: 60
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 8.57142857. pytest 소수 8자리 비교 통과. 소스 66-68행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0197
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0197
- timestamp: 2026-11-02T13:00:18+09:00
- feature: work_hour_points(6)=2.85714286
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: work_hour_points
- line: 60
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 2.85714286. pytest 소수 8자리 비교 통과. 소스 66-68행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0198
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0198
- timestamp: 2026-11-02T13:00:18+09:00
- feature: work_hour_points(7)=1.42857143
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: work_hour_points
- line: 60
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 1.42857143. pytest 소수 8자리 비교 통과. 소스 66-68행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0199
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0199
- timestamp: 2026-11-02T13:00:18+09:00
- feature: work_hour_points(8)=0.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: work_hour_points
- line: 60
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0.00000000. pytest 소수 8자리 비교 통과. 소스 66-68행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0200
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0200
- timestamp: 2026-11-02T13:00:18+09:00
- feature: work_hour_points(9)=0.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: work_hour_points
- line: 60
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0.00000000. pytest 소수 8자리 비교 통과. 소스 66-68행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0201
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0201
- timestamp: 2026-11-02T13:00:18+09:00
- feature: work_hour_points(24)=0.00000000
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: work_hour_points
- line: 60
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 0.00000000. pytest 소수 8자리 비교 통과. 소스 66-68행 식과 같다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0202
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0202
- timestamp: 2026-11-02T13:00:18+09:00
- feature: DRIVING ML=0 DL=0 points=0.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 0.00, 나머지 라벨 0, 전체 합도 0.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0203
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0203
- timestamp: 2026-11-02T13:00:18+09:00
- feature: DRIVING ML=1 DL=0 points=5.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 5.00, 나머지 라벨 0, 전체 합도 5.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0204
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0204
- timestamp: 2026-11-02T13:00:18+09:00
- feature: DRIVING ML=0 DL=1 points=5.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 5.00, 나머지 라벨 0, 전체 합도 5.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0205
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0205
- timestamp: 2026-11-02T13:00:18+09:00
- feature: DRIVING ML=0.2 DL=0.8 points=5.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 5.00, 나머지 라벨 0, 전체 합도 5.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0206
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0206
- timestamp: 2026-11-02T13:00:18+09:00
- feature: DRIVING ML=1 DL=1 points=10.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 10.00, 나머지 라벨 0, 전체 합도 10.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0207
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0207
- timestamp: 2026-11-02T13:00:18+09:00
- feature: NIGHT_SHIFT ML=0 DL=0 points=0.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 0.00, 나머지 라벨 0, 전체 합도 0.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0208
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0208
- timestamp: 2026-11-02T13:00:18+09:00
- feature: NIGHT_SHIFT ML=1 DL=0 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0209
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0209
- timestamp: 2026-11-02T13:00:18+09:00
- feature: NIGHT_SHIFT ML=0 DL=1 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0210
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0210
- timestamp: 2026-11-02T13:00:18+09:00
- feature: NIGHT_SHIFT ML=0.2 DL=0.8 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0211
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0211
- timestamp: 2026-11-02T13:00:18+09:00
- feature: NIGHT_SHIFT ML=1 DL=1 points=8.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 8.00, 나머지 라벨 0, 전체 합도 8.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0212
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0212
- timestamp: 2026-11-02T13:00:18+09:00
- feature: WALKING ML=0 DL=0 points=0.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 0.00, 나머지 라벨 0, 전체 합도 0.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0213
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0213
- timestamp: 2026-11-02T13:00:18+09:00
- feature: WALKING ML=1 DL=0 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0214
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0214
- timestamp: 2026-11-02T13:00:18+09:00
- feature: WALKING ML=0 DL=1 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0215
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0215
- timestamp: 2026-11-02T13:00:18+09:00
- feature: WALKING ML=0.2 DL=0.8 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0216
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0216
- timestamp: 2026-11-02T13:00:18+09:00
- feature: WALKING ML=1 DL=1 points=8.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 8.00, 나머지 라벨 0, 전체 합도 8.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0217
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0217
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CLEANING_TASK ML=0 DL=0 points=0.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 0.00, 나머지 라벨 0, 전체 합도 0.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0218
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0218
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CLEANING_TASK ML=1 DL=0 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0219
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0219
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CLEANING_TASK ML=0 DL=1 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0220
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0220
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CLEANING_TASK ML=0.2 DL=0.8 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0221
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0221
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CLEANING_TASK ML=1 DL=1 points=8.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 8.00, 나머지 라벨 0, 전체 합도 8.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0222
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0222
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CARE_TASK ML=0 DL=0 points=0.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 0.00, 나머지 라벨 0, 전체 합도 0.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0223
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0223
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CARE_TASK ML=1 DL=0 points=3.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 3.00, 나머지 라벨 0, 전체 합도 3.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0224
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0224
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CARE_TASK ML=0 DL=1 points=3.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 3.00, 나머지 라벨 0, 전체 합도 3.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0225
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0225
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CARE_TASK ML=0.2 DL=0.8 points=3.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 3.00, 나머지 라벨 0, 전체 합도 3.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0226
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0226
- timestamp: 2026-11-02T13:00:18+09:00
- feature: CARE_TASK ML=1 DL=1 points=6.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 6.00, 나머지 라벨 0, 전체 합도 6.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0227
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0227
- timestamp: 2026-11-02T13:00:18+09:00
- feature: FACILITY_MAINTENANCE ML=0 DL=0 points=0.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 0.00, 나머지 라벨 0, 전체 합도 0.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0228
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0228
- timestamp: 2026-11-02T13:00:18+09:00
- feature: FACILITY_MAINTENANCE ML=1 DL=0 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0229
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0229
- timestamp: 2026-11-02T13:00:18+09:00
- feature: FACILITY_MAINTENANCE ML=0 DL=1 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0230
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0230
- timestamp: 2026-11-02T13:00:18+09:00
- feature: FACILITY_MAINTENANCE ML=0.2 DL=0.8 points=4.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 4.00, 나머지 라벨 0, 전체 합도 4.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0231
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0231
- timestamp: 2026-11-02T13:00:18+09:00
- feature: FACILITY_MAINTENANCE ML=1 DL=1 points=8.00
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: task_points
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 라벨 8.00, 나머지 라벨 0, 전체 합도 8.00이며 30 미만. pytest 통과. 소스 78-94행. 단일 라벨은 30 상한에 걸리지 않는다. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0232
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0232
- timestamp: 2026-11-02T13:00:18+09:00
- feature: grade_of(0)=LOW
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: grade_of
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 LOW. pytest 통과. 소스 99-103행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0233
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0233
- timestamp: 2026-11-02T13:00:18+09:00
- feature: grade_of(39)=LOW
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: grade_of
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 LOW. pytest 통과. 소스 99-103행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0234
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0234
- timestamp: 2026-11-02T13:00:18+09:00
- feature: grade_of(40)=LOW
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: grade_of
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 LOW. pytest 통과. 소스 99-103행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0235
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0235
- timestamp: 2026-11-02T13:00:18+09:00
- feature: grade_of(41)=MID
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: grade_of
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 MID. pytest 통과. 소스 99-103행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0236
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0236
- timestamp: 2026-11-02T13:00:18+09:00
- feature: grade_of(59)=MID
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: grade_of
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 MID. pytest 통과. 소스 99-103행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0237
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0237
- timestamp: 2026-11-02T13:00:18+09:00
- feature: grade_of(60)=MID
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: grade_of
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 MID. pytest 통과. 소스 99-103행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0238
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0238
- timestamp: 2026-11-02T13:00:18+09:00
- feature: grade_of(61)=HIGH
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: grade_of
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 HIGH. pytest 통과. 소스 99-103행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0239
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0239
- timestamp: 2026-11-02T13:00:18+09:00
- feature: grade_of(100)=HIGH
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: grade_of
- line: 97
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 기대 HIGH. pytest 통과. 소스 99-103행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0240
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0240
- timestamp: 2026-11-02T13:00:18+09:00
- feature: 전부 0
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: calculate_score
- line: 106
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: factors 0, 0, 0, 0, 0. score 0. LOW. pytest 통과. 소스 112-124행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0241
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0241
- timestamp: 2026-11-02T13:00:18+09:00
- feature: 건강 12.5만
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: calculate_score
- line: 106
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: factors 0, 12.5, 0, 0, 0. 합 12.5를 Python round하면 12. score 12. LOW. 건강 칸은 12.5로 남는다. pytest 통과. 소스 112-124행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0242
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0242
- timestamp: 2026-11-02T13:00:18+09:00
- feature: 만성질환만
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: calculate_score
- line: 106
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: factors 0, 0, 15, 0, 0. score 15. LOW. pytest 통과. 소스 112-124행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0243
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0243
- timestamp: 2026-11-02T13:00:18+09:00
- feature: 나이 90
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: calculate_score
- line: 106
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: factors 20, 0, 0, 0, 0. score 20. LOW. pytest 통과. 소스 112-124행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0244
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0244
- timestamp: 2026-11-02T13:00:18+09:00
- feature: 개인 요인 최댓값
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: calculate_score
- line: 106
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: factors 20, 25, 15, 10, 0. score 70. HIGH. pytest 통과. 소스 112-124행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0245
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0245
- timestamp: 2026-11-02T13:00:18+09:00
- feature: 작업 라벨 전부 1
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: calculate_score
- line: 106
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: 라벨 행 합은 48이고 factor는 min(48, 30)=30. factors 0, 0, 0, 0, 30. score 30. LOW. pytest 통과. 소스 112-124행. DB 변화 없음.

## 20261102T130018-a7c3e91b04 / IF-0246
- RUN_ID: 20261102T130018-a7c3e91b04
- TC_ID: IF-0246
- timestamp: 2026-11-02T13:00:18+09:00
- feature: 모든 요인 최댓값
- test_type: unit
- tool_a: pytest
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_risk_score_if0178.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/risk_score.py"]
- result_b: PASS
- status: PASS
- git_commit: 69f74c49c8a90b6eed679ebceac75175c196e5b7
- dirty: True
- files: ai/src/risk_score.py, ai/tests/test_risk_score_if0178.py
- function: calculate_score
- line: 106
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T130018-a7c3e91b04/if0178-junit.xml sha256=ee513738f31beff392b68cd6220144e19a42ba89af15e33c2c31d00ffd45e625; qa/.runtime/20261102T130018-a7c3e91b04/source-review.txt sha256=995353333bde94c657eca877b5def52dd7be3134b8e824dd8bb8500e2f21a6f8; qa/.runtime/20261102T130018-a7c3e91b04/pytest-summary.txt sha256=68ac9be2c9308e752fb077695484a1cf6325ac407c4b4d2f938a70de4f8b9027

Expected/Actual: factors 20, 25, 15, 10, 30. 작업 원합 48은 factor에서 30으로 잘린다. score 100. HIGH. pytest 통과. 소스 112-124행. DB 변화 없음.
## 20261102T131137-c6d14f0a82 / IF-0247
- RUN_ID: 20261102T131137-c6d14f0a82
- TC_ID: IF-0247
- timestamp: 2026-11-02T13:11:37+09:00
- feature: API 키 없음
- test_type: unit
- tool_a: pytest monkeypatch
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_ai_explain_if0247.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ai_explain.py"]
- result_b: PASS
- status: PASS
- git_commit: 005e2044a275ac0e2cb454dbe2d6139a657a2823
- dirty: True
- files: ai/src/ai_explain.py, ai/tests/test_ai_explain_if0247.py
- function: explain
- line: 51
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131137-c6d14f0a82/if0247-junit.xml sha256=08b10eefad4911f649aeb82de7d2909d5c2f09dc7e3ac5cffdc7cc35450df114; qa/.runtime/20261102T131137-c6d14f0a82/source-review.txt sha256=8d877ca429b53ad1e8f31fecdaf509609aea6d556ff03634a00182b649d57a24; qa/.runtime/20261102T131137-c6d14f0a82/pytest-summary.txt sha256=79f7ac18f530aaaff8744079c41615097c250f84dfce5ad0841e1b1dfe8fe635

Expected/Actual: source=basic. 한국어 기본 설명에 참고 지수와 낮음이 있다. pytest 통과. 소스 51-53행, 21-25행. DB 없음. Gemini 실호출 없음.

## 20261102T131137-c6d14f0a82 / IF-0248
- RUN_ID: 20261102T131137-c6d14f0a82
- TC_ID: IF-0248
- timestamp: 2026-11-02T13:11:37+09:00
- feature: Gemini 정상 trim
- test_type: unit
- tool_a: pytest monkeypatch
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_ai_explain_if0247.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ai_explain.py"]
- result_b: PASS
- status: PASS
- git_commit: 005e2044a275ac0e2cb454dbe2d6139a657a2823
- dirty: True
- files: ai/src/ai_explain.py, ai/tests/test_ai_explain_if0247.py
- function: explain
- line: 72
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131137-c6d14f0a82/if0247-junit.xml sha256=08b10eefad4911f649aeb82de7d2909d5c2f09dc7e3ac5cffdc7cc35450df114; qa/.runtime/20261102T131137-c6d14f0a82/source-review.txt sha256=8d877ca429b53ad1e8f31fecdaf509609aea6d556ff03634a00182b649d57a24; qa/.runtime/20261102T131137-c6d14f0a82/pytest-summary.txt sha256=79f7ac18f530aaaff8744079c41615097c250f84dfce5ad0841e1b1dfe8fe635

Expected/Actual: source=gemini. mock 텍스트의 앞뒤 공백이 strip된다. pytest 통과. 소스 71-72행. DB 없음. Gemini 실호출 없음.

## 20261102T131137-c6d14f0a82 / IF-0249
- RUN_ID: 20261102T131137-c6d14f0a82
- TC_ID: IF-0249
- timestamp: 2026-11-02T13:11:37+09:00
- feature: Gemini 빈 텍스트
- test_type: unit
- tool_a: pytest monkeypatch
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_ai_explain_if0247.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ai_explain.py"]
- result_b: PASS
- status: PASS
- git_commit: 005e2044a275ac0e2cb454dbe2d6139a657a2823
- dirty: True
- files: ai/src/ai_explain.py, ai/tests/test_ai_explain_if0247.py
- function: explain
- line: 71
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131137-c6d14f0a82/if0247-junit.xml sha256=08b10eefad4911f649aeb82de7d2909d5c2f09dc7e3ac5cffdc7cc35450df114; qa/.runtime/20261102T131137-c6d14f0a82/source-review.txt sha256=8d877ca429b53ad1e8f31fecdaf509609aea6d556ff03634a00182b649d57a24; qa/.runtime/20261102T131137-c6d14f0a82/pytest-summary.txt sha256=79f7ac18f530aaaff8744079c41615097c250f84dfce5ad0841e1b1dfe8fe635

Expected/Actual: response.text=None이면 source=basic. mock 호출은 확인했다. pytest 통과. 소스 71행, 78행. DB 없음. Gemini 실호출 없음.

## 20261102T131137-c6d14f0a82 / IF-0250
- RUN_ID: 20261102T131137-c6d14f0a82
- TC_ID: IF-0250
- timestamp: 2026-11-02T13:11:37+09:00
- feature: Gemini 예외
- test_type: unit
- tool_a: pytest monkeypatch
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_ai_explain_if0247.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ai_explain.py"]
- result_b: PASS
- status: PASS
- git_commit: 005e2044a275ac0e2cb454dbe2d6139a657a2823
- dirty: True
- files: ai/src/ai_explain.py, ai/tests/test_ai_explain_if0247.py
- function: explain
- line: 73
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131137-c6d14f0a82/if0247-junit.xml sha256=08b10eefad4911f649aeb82de7d2909d5c2f09dc7e3ac5cffdc7cc35450df114; qa/.runtime/20261102T131137-c6d14f0a82/source-review.txt sha256=8d877ca429b53ad1e8f31fecdaf509609aea6d556ff03634a00182b649d57a24; qa/.runtime/20261102T131137-c6d14f0a82/pytest-summary.txt sha256=79f7ac18f530aaaff8744079c41615097c250f84dfce5ad0841e1b1dfe8fe635

Expected/Actual: generate_content 예외면 source=basic. mock 호출은 확인했다. pytest 통과. 소스 73-78행. DB 없음. Gemini 실호출 없음.

## 20261102T131137-c6d14f0a82 / IF-0251
- RUN_ID: 20261102T131137-c6d14f0a82
- TC_ID: IF-0251
- timestamp: 2026-11-02T13:11:37+09:00
- feature: 최대 요인 동률
- test_type: unit
- tool_a: pytest monkeypatch
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_ai_explain_if0247.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ai_explain.py"]
- result_b: PASS
- status: PASS
- git_commit: 005e2044a275ac0e2cb454dbe2d6139a657a2823
- dirty: True
- files: ai/src/ai_explain.py, ai/tests/test_ai_explain_if0247.py
- function: basic_explanation
- line: 20
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131137-c6d14f0a82/if0247-junit.xml sha256=08b10eefad4911f649aeb82de7d2909d5c2f09dc7e3ac5cffdc7cc35450df114; qa/.runtime/20261102T131137-c6d14f0a82/source-review.txt sha256=8d877ca429b53ad1e8f31fecdaf509609aea6d556ff03634a00182b649d57a24; qa/.runtime/20261102T131137-c6d14f0a82/pytest-summary.txt sha256=79f7ac18f530aaaff8744079c41615097c250f84dfce5ad0841e1b1dfe8fe635

Expected/Actual: points가 같은 첫 항목 나이를 고른다. pytest 통과. 소스 20행 max. DB 없음. Gemini 실호출 없음.

## 20261102T131137-c6d14f0a82 / IF-0252
- RUN_ID: 20261102T131137-c6d14f0a82
- TC_ID: IF-0252
- timestamp: 2026-11-02T13:11:37+09:00
- feature: 등급 LOW
- test_type: unit
- tool_a: pytest monkeypatch
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_ai_explain_if0247.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ai_explain.py"]
- result_b: PASS
- status: PASS
- git_commit: 005e2044a275ac0e2cb454dbe2d6139a657a2823
- dirty: True
- files: ai/src/ai_explain.py, ai/tests/test_ai_explain_if0247.py
- function: basic_explanation
- line: 18
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131137-c6d14f0a82/if0247-junit.xml sha256=08b10eefad4911f649aeb82de7d2909d5c2f09dc7e3ac5cffdc7cc35450df114; qa/.runtime/20261102T131137-c6d14f0a82/source-review.txt sha256=8d877ca429b53ad1e8f31fecdaf509609aea6d556ff03634a00182b649d57a24; qa/.runtime/20261102T131137-c6d14f0a82/pytest-summary.txt sha256=79f7ac18f530aaaff8744079c41615097c250f84dfce5ad0841e1b1dfe8fe635

Expected/Actual: 기본 설명에 낮음이 있다. pytest 통과. 소스 9행, 18행. DB 없음. Gemini 실호출 없음.

## 20261102T131137-c6d14f0a82 / IF-0253
- RUN_ID: 20261102T131137-c6d14f0a82
- TC_ID: IF-0253
- timestamp: 2026-11-02T13:11:37+09:00
- feature: 등급 MID
- test_type: unit
- tool_a: pytest monkeypatch
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_ai_explain_if0247.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ai_explain.py"]
- result_b: PASS
- status: PASS
- git_commit: 005e2044a275ac0e2cb454dbe2d6139a657a2823
- dirty: True
- files: ai/src/ai_explain.py, ai/tests/test_ai_explain_if0247.py
- function: basic_explanation
- line: 18
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131137-c6d14f0a82/if0247-junit.xml sha256=08b10eefad4911f649aeb82de7d2909d5c2f09dc7e3ac5cffdc7cc35450df114; qa/.runtime/20261102T131137-c6d14f0a82/source-review.txt sha256=8d877ca429b53ad1e8f31fecdaf509609aea6d556ff03634a00182b649d57a24; qa/.runtime/20261102T131137-c6d14f0a82/pytest-summary.txt sha256=79f7ac18f530aaaff8744079c41615097c250f84dfce5ad0841e1b1dfe8fe635

Expected/Actual: 기본 설명에 보통이 있다. pytest 통과. 소스 9행, 18행. DB 없음. Gemini 실호출 없음.

## 20261102T131137-c6d14f0a82 / IF-0254
- RUN_ID: 20261102T131137-c6d14f0a82
- TC_ID: IF-0254
- timestamp: 2026-11-02T13:11:37+09:00
- feature: 등급 HIGH
- test_type: unit
- tool_a: pytest monkeypatch
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_ai_explain_if0247.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ai_explain.py"]
- result_b: PASS
- status: PASS
- git_commit: 005e2044a275ac0e2cb454dbe2d6139a657a2823
- dirty: True
- files: ai/src/ai_explain.py, ai/tests/test_ai_explain_if0247.py
- function: basic_explanation
- line: 18
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131137-c6d14f0a82/if0247-junit.xml sha256=08b10eefad4911f649aeb82de7d2909d5c2f09dc7e3ac5cffdc7cc35450df114; qa/.runtime/20261102T131137-c6d14f0a82/source-review.txt sha256=8d877ca429b53ad1e8f31fecdaf509609aea6d556ff03634a00182b649d57a24; qa/.runtime/20261102T131137-c6d14f0a82/pytest-summary.txt sha256=79f7ac18f530aaaff8744079c41615097c250f84dfce5ad0841e1b1dfe8fe635

Expected/Actual: 기본 설명에 높음이 있다. pytest 통과. 소스 9행, 18행. DB 없음. Gemini 실호출 없음.

## 20261102T131137-c6d14f0a82 / IF-0255
- RUN_ID: 20261102T131137-c6d14f0a82
- TC_ID: IF-0255
- timestamp: 2026-11-02T13:11:37+09:00
- feature: 사고 확률 경고
- test_type: unit
- tool_a: pytest monkeypatch
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_ai_explain_if0247.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ai_explain.py"]
- result_b: PASS
- status: PASS
- git_commit: 005e2044a275ac0e2cb454dbe2d6139a657a2823
- dirty: True
- files: ai/src/ai_explain.py, ai/tests/test_ai_explain_if0247.py
- function: basic_explanation
- line: 24
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131137-c6d14f0a82/if0247-junit.xml sha256=08b10eefad4911f649aeb82de7d2909d5c2f09dc7e3ac5cffdc7cc35450df114; qa/.runtime/20261102T131137-c6d14f0a82/source-review.txt sha256=8d877ca429b53ad1e8f31fecdaf509609aea6d556ff03634a00182b649d57a24; qa/.runtime/20261102T131137-c6d14f0a82/pytest-summary.txt sha256=79f7ac18f530aaaff8744079c41615097c250f84dfce5ad0841e1b1dfe8fe635

Expected/Actual: 문장에 '이 점수는 사고 확률이 아니므로'가 있다. pytest 통과. 소스 24행. DB 없음. Gemini 실호출 없음.
## 20261102T131746-e5a91c7b20 / IF-0256
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0256
- timestamp: 2026-11-02T13:17:46+09:00
- feature: ML 최초 로드
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/ml_model.py, ai/tests/test_model_if0256.py
- function: load_ml_models
- line: 22
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: joblib.load 1회. 반환 딕셔너리가 _models와 같다. pytest 통과. 소스 25-29행. 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0257
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0257
- timestamp: 2026-11-02T13:17:46+09:00
- feature: ML 재호출 캐시
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/ml_model.py, ai/tests/test_model_if0256.py
- function: load_ml_models
- line: 25
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: 두 번째 호출은 같은 객체이고 joblib.load는 여전히 1회다. pytest 통과. 소스 25행. 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0258
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0258
- timestamp: 2026-11-02T13:17:46+09:00
- feature: ML 확률 0~1
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/ml_model.py, ai/tests/test_model_if0256.py
- function: predict_ml
- line: 32
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: 제목 운전기사. 라벨 점수 0.75와 0.0으로 0~1 안이다. pytest 통과. 소스 42-44행. 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0260
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0260
- timestamp: 2026-11-02T13:17:46+09:00
- feature: DL 빈 제목 패딩
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/dl_model.py, ai/tests/test_model_if0256.py
- function: encode_title
- line: 54
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: 빈 문자열은 0이 100개다. pytest 통과. 소스 59-60행. 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0261
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0261
- timestamp: 2026-11-02T13:17:46+09:00
- feature: DL 1글자
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/dl_model.py, ai/tests/test_model_if0256.py
- function: encode_title
- line: 54
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: 토큰 1개와 패딩 99개. 길이 100. pytest 통과. 소스 59-60행. 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0262
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0262
- timestamp: 2026-11-02T13:17:46+09:00
- feature: DL 100글자
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/dl_model.py, ai/tests/test_model_if0256.py
- function: encode_title
- line: 54
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: 길이 100이 유지된다. pytest 통과. 소스 59행 title[:100]. 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0263
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0263
- timestamp: 2026-11-02T13:17:46+09:00
- feature: DL 101글자
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/dl_model.py, ai/tests/test_model_if0256.py
- function: encode_title
- line: 54
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: 101번째 글자는 잘리고 길이는 100이다. pytest 통과. 소스 59행. 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0264
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0264
- timestamp: 2026-11-02T13:17:46+09:00
- feature: DL 미등록 문자
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/dl_model.py, ai/tests/test_model_if0256.py
- function: encode_title
- line: 59
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: 사전에 없는 글자는 ID 1이다. pytest 통과. 소스 59행 vocab.get(char, 1). 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0265
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0265
- timestamp: 2026-11-02T13:17:46+09:00
- feature: DL 최초 로드
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/dl_model.py, ai/tests/test_model_if0256.py
- function: load_dl_model
- line: 70
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: torch.load 1회, map_location=cpu, weights_only=True, 이어서 eval. pytest 통과. 소스 76행, 83행. 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0266
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0266
- timestamp: 2026-11-02T13:17:46+09:00
- feature: DL 재호출 캐시
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/dl_model.py, ai/tests/test_model_if0256.py
- function: load_dl_model
- line: 73
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: 두 번째 호출은 같은 모델, 사전, 라벨이고 torch.load는 1회다. pytest 통과. 소스 73행. 실제 모델 파일은 열지 않음. DB 없음.

## 20261102T131746-e5a91c7b20 / IF-0267
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0267
- timestamp: 2026-11-02T13:17:46+09:00
- feature: DL sigmoid 0~1
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: PASS
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: PASS
- status: PASS
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/dl_model.py, ai/tests/test_model_if0256.py
- function: predict_dl
- line: 87
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected/Actual: 제목 운전기사. sigmoid 후 소수 넷째 자리가 0~1 안이다. pytest 통과. 소스 98행, 102행. 실제 모델 파일은 열지 않음. DB 없음.

# FAIL

## RUN-20261102-001 / QA-UNIT-SPRING
- RUN_ID: RUN-20261102-001
- TC_ID: QA-UNIT-SPRING
- timestamp: 2026-11-02T11:57:51+09:00
- feature: Spring 평가 컨트롤러/서비스 단위 테스트
- test_type: unit
- tool_a: Gradle JUnit
- command_a: ./gradlew test --rerun-tasks
- result_a: FAIL
- tool_b: JUnit XML
- command_b: spring/build/test-results/test/TEST-*.xml
- result_b: FAIL
- status: FAIL
- git_commit: 69f74c49c8a9
- dirty: true
- files: spring/src/test/java/com/example/demo/assessment/AssessmentControllerTest.java
- function: 나이가_범위를_벗어나면_400
- line: 33
- ISSUE_ID: 
- RISK_ID: 
- evidence: gradle=FAIL xml tests=65 failures=1 errors=0 files=TEST-com.example.demo.assessment.AssessmentControllerTest.xml,TEST-com.example.demo.assessment.AssessmentPipelineIf0094Test.xml,TEST-com.example.demo.assessment.AssessmentServiceTest.xml

검증 목적: 기존 AssessmentControllerTest, AssessmentServiceTest가 통과하는지 확인한다.
도구 A는 Gradle 테스트 프로세스다. 도구 B는 그 실행이 남긴 JUnit XML을 따로 읽는다. XML은 두 번째 실행이 아니라 같은 실행의 독립 판독이다.
기대: 두 판독 모두 실패 0, 테스트 1건 이상. 실제: A=FAIL B=FAIL tests=65 failures=1 errors=0.
범위: H2와 Mock AI. 운영 PostgreSQL과 살아있는 FastAPI는 포함하지 않는다.
로그 끝:
11-02T11:58:01.793+09:00  INFO 76243 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-2 - Shutdown initiated...
2026-11-02T11:58:01.794+09:00  INFO 76243 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-2 - Shutdown completed.
2026-11-02T11:58:01.795+09:00  INFO 76243 --- [ionShutdownHook] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default'
2026-11-02T11:58:01.795+09:00  INFO 76243 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-3 - Shutdown initiated...
2026-11-02T11:58:01.796+09:00  INFO 76243 --- [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-3 - Shutdown completed.

> Task :test FAILED

65 tests completed, 1 failed

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':test'.
> There were failing tests. See the report at: file:///Users/jeong-yelim/orca/IF_v2/spring/build/reports/tests/test/index.html

* Try:
> Run with --scan to get full insights.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.9/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD FAILED in 9s
5 actionable tasks: 5 executed
## 20261102T131746-e5a91c7b20 / IF-0259
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0259
- timestamp: 2026-11-02T13:17:46+09:00
- feature: ML 모델 파일 없음
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: FAIL
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: FAIL
- status: FAIL
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/ml_model.py, ai/tests/test_model_if0256.py
- function: load_ml_models
- line: 27
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected: 없는 task_ml.joblib에서 오류가 나고 로그가 남는다.
Actual: FileNotFoundError는 났다. caplog.records는 0건이다. _models는 None으로 남았다.
Input: MODEL_PATH=/tmp/if-v2-if0259-task_ml.joblib, 파일 없음, _models=None.
Error: AssertionError caplog.records == []. 그 앞의 pytest.raises(FileNotFoundError)는 통과했다.
Repro: cd ai && ../.venv/bin/python -m pytest tests/test_model_if0256.py::test_IF_0259_missing_ml_file -q
Cause: load_ml_models 27행 joblib.load가 예외를 그대로 올린다. logging 호출이 없다.
Location: ai/src/ml_model.py load_ml_models 27. 수정하지 않음. 재검증 RUN_ID 없음.

## 20261102T131746-e5a91c7b20 / IF-0268
- RUN_ID: 20261102T131746-e5a91c7b20
- TC_ID: IF-0268
- timestamp: 2026-11-02T13:17:46+09:00
- feature: DL 모델 파일 없음
- test_type: unit
- tool_a: pytest mock
- command_a: ["../.venv/bin/python", "-m", "pytest", "tests/test_model_if0256.py", "-q"]
- result_a: FAIL
- tool_b: 소스 대조
- command_b: ["read", "ai/src/ml_model.py", "ai/src/dl_model.py"]
- result_b: FAIL
- status: FAIL
- git_commit: 82d6829e9232acd1ca77ffde59be3b5a0f06419d
- dirty: True
- files: ai/src/dl_model.py, ai/tests/test_model_if0256.py
- function: load_dl_model
- line: 76
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/20261102T131746-e5a91c7b20/if0256-junit.xml sha256=c78151b88ea48b5ec220c1786bfbf0407b06d8a7d6be5d73d8a25560aabdd874; qa/.runtime/20261102T131746-e5a91c7b20/source-review.txt sha256=61605d25b4198547bdbd6b7b90798fc356c5c4704cb3d9cd72fd8ebe9ca0e555; qa/.runtime/20261102T131746-e5a91c7b20/pytest-summary.txt sha256=fb5474fc786f8b81f119cad990c701038529b66033227d17b6224efefebdc2c9

Expected: 없는 task_cnn.pt에서 서버 오류가 기록된다.
Actual: FileNotFoundError는 났다. caplog.records는 0건이다. _model은 None으로 남았다. HTTP 예외나 logger 기록은 없다.
Input: MODEL_PATH=/tmp/if-v2-if0268-task_cnn.pt, 파일 없음, _model=None.
Error: AssertionError caplog.records == []. 그 앞의 pytest.raises(FileNotFoundError)는 통과했다.
Repro: cd ai && ../.venv/bin/python -m pytest tests/test_model_if0256.py::test_IF_0268_missing_dl_file -q
Cause: load_dl_model 76행 torch.load가 예외를 그대로 올린다. 서버 오류를 기록하는 코드가 없다.
Location: ai/src/dl_model.py load_dl_model 76. 수정하지 않음. 재검증 RUN_ID 없음.

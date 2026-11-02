# PASS

## 20261030T172701-24c6ce0dc2 / QA-AI
- RUN_ID: 20261030T172701-24c6ce0dc2
- TC_ID: QA-AI
- timestamp: 2026-10-30T17:27:01.356327+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T172701-24c6ce0dc2/QA-AI-a.log sha256=a73c43c334fb7b11082132a2b356da186d7abc30794acae86fdfdde9f4792c7f; qa/.runtime/evidence/api/2026-10-30/20261030T172701-24c6ce0dc2/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_pdf_reader_default_guidelines
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_pdf_reader_default_guidelines
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_pdf_reader_file_not_found
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_pdf_reader_file_not_found
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_chunking_splits_and_overlaps
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_chunking_splits_and_overlaps
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_chunk_documents_preserves_metadata
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_chunk_documents_preserves_metadata
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_embedding_dimension_and_consistency
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_embedding_dimension_and_consistency
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_cosine_similarity_difference
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_cosine_similarity_difference
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_vector_store_add_and_search
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_vector_store_add_and_search
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_pgvector_sql_schema
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_pgvector_sql_schema
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_reranker_promotes_relevant_and_high_risk_chunks
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_reranker_promotes_relevant_and_high_risk_chunks
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_abstain_when_chunks_empty
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_abstain_when_chunks_empty
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_abstain_when_similarity_is_too_low
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_abstain_when_similarity_is_too_low
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_evidence_explanation_and_citations
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_evidence_explanation_and_citations
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_langgraph_workflow_generate_path
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_langgraph_workflow_generate_path
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_langgraph_workflow_abstain_path
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_langgraph_workflow_abstain_path
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_harness_validation_rejects_empty_title
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_harness_validation_rejects_empty_title
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_harness_validation_rejects_invalid_score
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_harness_validation_rejects_invalid_score
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_harness_retry_success_after_failure
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_harness_retry_success_after_failure
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_harness_error_handling_fallback
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_harness_error_handling_fallback
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_full_pipeline_end_to_end
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_full_pipeline_end_to_end
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_rag_api_health_endpoint
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_rag_api_health_endpoint
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_rag_api_search_endpoint
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_rag_api_search_endpoint
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_rag_api_explain_endpoint_success
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_rag_api_explain_endpoint_success
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_rag::test_rag_api_explain_rejects_empty_title
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_rag::test_rag_api_explain_rejects_empty_title
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_risk_score::test_grade_boundaries
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_risk_score::test_grade_boundaries
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_risk_score::test_young_healthy_person_gets_zero_without_task_points
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_risk_score::test_young_healthy_person_gets_zero_without_task_points
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_risk_score::test_worst_inputs_reach_100
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_risk_score::test_worst_inputs_reach_100
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_risk_score::test_analyze_api_uses_ml_dl_and_explanation
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_risk_score::test_analyze_api_uses_ml_dl_and_explanation
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173027-a0890b20ec / QA-AI/tests.test_risk_score::test_analyze_api_rejects_bad_age
- RUN_ID: 20261030T173027-a0890b20ec
- TC_ID: QA-AI/tests.test_risk_score::test_analyze_api_rejects_bad_age
- timestamp: 2026-10-30T17:30:27.147518+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173027-a0890b20ec/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-a.log sha256=5542af839b97c0e9bafb61c00f6403ae8a0c28a7a5a32e07497af3a02832e4db; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-QA-AI.xml sha256=6397395a44a01bd445fa2f7954085b1790d47ab7390316cad25f04b52c598700; qa/.runtime/evidence/api/2026-10-30/20261030T173027-a0890b20ec/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:26 KST)

- **통과 건수**: 14건 / 전체 22건

| RUN_ID | TC_ID | 실행 일시 (KST) | 기능명 | 도구 A (결과) | 도구 B (결과) | 최종 상태 | Git Commit | 대상 파일 | 함수명 | 줄 번호 | 관련 ID | 검증 목적 및 근거 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `RUN-20261030-001` | `IF-0047` | 2026-10-30 17:31:03 KST | 이름(applicantName) 필드 누락 시 400 VALIDATION_ERROR 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 400)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 400, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | `AssessmentCreateRequest` | `15` | `-` | **목적**: 이름(applicantName) 필드 누락 시 400 VALIDATION_ERROR 검증<br>**기대**: HTTP 400 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 400 ({"success":false,"data":null,"message":"applicantName: must not be blank","error), Tool B: HTTP 400, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0049` | 2026-10-30 17:31:03 KST | 이름(applicantName) 공백 문자열(' ') 전송 시 @NotBlank 400 거절 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 400)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 400, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | `AssessmentCreateRequest` | `15` | `-` | **목적**: 이름(applicantName) 공백 문자열(' ') 전송 시 @NotBlank 400 거절 검증<br>**기대**: HTTP 400 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 400 ({"success":false,"data":null,"message":"applicantName: must not be blank","error), Tool B: HTTP 400, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0051` | 2026-10-30 17:31:03 KST | 이름(applicantName) 최대 경계 초과(51자) 시 @Size(max=50) 400 거절 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 400)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 400, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | `AssessmentCreateRequest` | `15` | `-` | **목적**: 이름(applicantName) 최대 경계 초과(51자) 시 @Size(max=50) 400 거절 검증<br>**기대**: HTTP 400 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 400 ({"success":false,"data":null,"message":"applicantName: size must be between 0 an), Tool B: HTTP 400, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0055` | 2026-10-30 17:31:03 KST | 나이(age) 최소 경계 미만(0) 전송 시 @Min(1) 400 거절 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 400)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 400, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | `AssessmentCreateRequest` | `16` | `-` | **목적**: 나이(age) 최소 경계 미만(0) 전송 시 @Min(1) 400 거절 검증<br>**기대**: HTTP 400 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 400 ({"success":false,"data":null,"message":"age: must be greater than or equal to 1"), Tool B: HTTP 400, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0056` | 2026-10-30 17:31:03 KST | 나이(age) 최소 경계값(1) 정상 등록(201) 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 201)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 201, assessment_delta=+1)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | `AssessmentCreateRequest` | `16` | `-` | **목적**: 나이(age) 최소 경계값(1) 정상 등록(201) 검증<br>**기대**: HTTP 201 및 DB 증감 +1<br>**실제/근거**: Tool A: HTTP 201 ({"id":90}), Tool B: HTTP 201, DB assessment 증감=+1 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0057` | 2026-10-30 17:31:03 KST | 나이(age) 최대 경계값(120) 정상 등록(201) 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 201)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 201, assessment_delta=+1)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | `AssessmentCreateRequest` | `16` | `-` | **목적**: 나이(age) 최대 경계값(120) 정상 등록(201) 검증<br>**기대**: HTTP 201 및 DB 증감 +1<br>**실제/근거**: Tool A: HTTP 201 ({"id":92}), Tool B: HTTP 201, DB assessment 증감=+1 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0058` | 2026-10-30 17:31:03 KST | 나이(age) 최대 경계 초과(121) 전송 시 @Max(120) 400 거절 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 400)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 400, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | `AssessmentCreateRequest` | `16` | `-` | **목적**: 나이(age) 최대 경계 초과(121) 전송 시 @Max(120) 400 거절 검증<br>**기대**: HTTP 400 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 400 ({"success":false,"data":null,"message":"age: must be less than or equal to 120",), Tool B: HTTP 400, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0066` | 2026-10-30 17:31:03 KST | 건강 상태(physicalLevel) 최대 경계 초과(6) 시 @Max(5) 400 거절 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 400)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 400, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | `AssessmentCreateRequest` | `17` | `-` | **목적**: 건강 상태(physicalLevel) 최대 경계 초과(6) 시 @Max(5) 400 거절 검증<br>**기대**: HTTP 400 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 400 ({"success":false,"data":null,"message":"physicalLevel: must be less than or equa), Tool B: HTTP 400, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0071` | 2026-10-30 17:31:03 KST | 만성질환(chronicDisease)에 허용되지 않는 문자열("yes") 전송 시 400 INVALID_JSON 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 400)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 400, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/global/exception/GlobalExceptionHandler.java` | `handleInvalidJson` | `43-46` | `-` | **목적**: 만성질환(chronicDisease)에 허용되지 않는 문자열("yes") 전송 시 400 INVALID_JSON 검증<br>**기대**: HTTP 400 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 400 ({"success":false,"data":null,"message":"요청 JSON 형식이 올바르지 않습니다.","errorCode":"INV), Tool B: HTTP 400, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0078` | 2026-10-30 17:31:03 KST | 근무시간(workHourLimit) 최대 경계 초과(25) 시 @Max(24) 400 거절 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 400)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 400, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | `AssessmentCreateRequest` | `19` | `-` | **목적**: 근무시간(workHourLimit) 최대 경계 초과(25) 시 @Max(24) 400 거절 검증<br>**기대**: HTTP 400 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 400 ({"success":false,"data":null,"message":"workHourLimit: must be less than or equa), Tool B: HTTP 400, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0083` | 2026-10-30 17:31:03 KST | 존재하지 않는 직무(jobId=999999) 전송 시 DB 저장 전 404 NOT_FOUND 거절 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 404)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 404, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/assessment/service/AssessmentService.java` | `createAndAnalyze` | `81-82` | `-` | **목적**: 존재하지 않는 직무(jobId=999999) 전송 시 DB 저장 전 404 NOT_FOUND 거절 검증<br>**기대**: HTTP 404 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 404 ({"success":false,"data":null,"message":"직무를 찾을 수 없습니다: 999999","errorCode":"NOT_), Tool B: HTTP 404, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `IF-0086` | 2026-10-30 17:31:03 KST | 깨진 JSON 본문('{"age":') 전송 시 400 INVALID_JSON 방어 검증 | `curl CLI (POST /api/assessments)` (PASS (HTTP 400)) | `Python urllib + psql 4-Table Delta Verifier` (PASS (HTTP 400, assessment_delta=+0)) | **PASS** | `9491fb1b` | `spring/src/main/demo/global/exception/GlobalExceptionHandler.java` | `handleInvalidJson` | `43-46` | `-` | **목적**: 깨진 JSON 본문('{"age":') 전송 시 400 INVALID_JSON 방어 검증<br>**기대**: HTTP 400 및 DB 증감 0<br>**실제/근거**: Tool A: HTTP 400 ({"success":false,"data":null,"message":"요청 JSON 형식이 올바르지 않습니다.","errorCode":"INV), Tool B: HTTP 400, DB assessment 증감=+0 (POST http://127.0.0.1:8080/api/assessments (Content-Type: application/json)) |
| `RUN-20261030-001` | `API-AI-001` | 2026-10-30 17:31:03 KST | FastAPI POST /api/v1/risk/analyze 정상 추론 및 응답 스키마 검증 | `curl CLI (POST /api/v1/risk/analyze)` (PASS (HTTP 200)) | `Python HTTP Client + JSON Schema Validator` (PASS (HTTP 200, score=48, grade=MID)) | **PASS** | `9491fb1b` | `ai/src/main.py` | `analyze` | `50-81` | `-` | **목적**: FastAPI 분석 엔드포인트가 ML+DL+규칙 점수와 설명을 정상 반환하는지 검증<br>**기대**: HTTP 200, risk_score 0~100, risk_grade LOW/MID/HIGH, task_scores 6개<br>**실제/근거**: HTTP 200, score=48, grade=MID, tasks=6 (POST http://127.0.0.1:8000/api/v1/risk/analyze) |
| `RUN-20261030-001` | `API-AI-002` | 2026-10-30 17:31:03 KST | FastAPI POST /api/v1/risk/analyze 공백 직무명('   ') 입력 시 422 거절 검증 | `curl CLI (POST /api/v1/risk/analyze)` (PASS (HTTP 422)) | `Python HTTP Client` (PASS (HTTP 422)) | **PASS** | `9491fb1b` | `ai/src/main.py` | `analyze` | `54-58` | `-` | **목적**: 공백만 있는 직무 제목 전송 시 strip() 후 HTTP 422로 거절하는지 검증<br>**기대**: HTTP 422 Unprocessable Entity ('직무 제목을 입력하세요.')<br>**실제/근거**: Tool A: HTTP 422, Tool B: HTTP 422 ({"detail":"직무 제목을 입력하세요."}) (POST http://127.0.0.1:8000/api/v1/risk/analyze) |


## 20261030T173746-09edf77edc / QA-AI
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_pdf_reader_default_guidelines
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_pdf_reader_default_guidelines
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_pdf_reader_file_not_found
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_pdf_reader_file_not_found
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_chunking_splits_and_overlaps
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_chunking_splits_and_overlaps
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_chunk_documents_preserves_metadata
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_chunk_documents_preserves_metadata
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_embedding_dimension_and_consistency
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_embedding_dimension_and_consistency
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_cosine_similarity_difference
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_cosine_similarity_difference
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_vector_store_add_and_search
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_vector_store_add_and_search
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_pgvector_sql_schema
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_pgvector_sql_schema
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_reranker_promotes_relevant_and_high_risk_chunks
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_reranker_promotes_relevant_and_high_risk_chunks
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_abstain_when_chunks_empty
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_abstain_when_chunks_empty
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_abstain_when_similarity_is_too_low
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_abstain_when_similarity_is_too_low
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_evidence_explanation_and_citations
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_evidence_explanation_and_citations
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_langgraph_workflow_generate_path
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_langgraph_workflow_generate_path
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_langgraph_workflow_abstain_path
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_langgraph_workflow_abstain_path
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_harness_validation_rejects_empty_title
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_harness_validation_rejects_empty_title
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_harness_validation_rejects_invalid_score
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_harness_validation_rejects_invalid_score
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_harness_retry_success_after_failure
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_harness_retry_success_after_failure
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_harness_error_handling_fallback
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_harness_error_handling_fallback
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_full_pipeline_end_to_end
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_full_pipeline_end_to_end
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_rag_api_health_endpoint
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_rag_api_health_endpoint
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_rag_api_search_endpoint
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_rag_api_search_endpoint
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_rag_api_explain_endpoint_success
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_rag_api_explain_endpoint_success
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_rag::test_rag_api_explain_rejects_empty_title
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_rag::test_rag_api_explain_rejects_empty_title
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_risk_score::test_grade_boundaries
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_risk_score::test_grade_boundaries
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_risk_score::test_young_healthy_person_gets_zero_without_task_points
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_risk_score::test_young_healthy_person_gets_zero_without_task_points
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_risk_score::test_worst_inputs_reach_100
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_risk_score::test_worst_inputs_reach_100
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_risk_score::test_analyze_api_uses_ml_dl_and_explanation
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_risk_score::test_analyze_api_uses_ml_dl_and_explanation
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T173746-09edf77edc / QA-AI/tests.test_risk_score::test_analyze_api_rejects_bad_age
- RUN_ID: 20261030T173746-09edf77edc
- TC_ID: QA-AI/tests.test_risk_score::test_analyze_api_rejects_bad_age
- timestamp: 2026-10-30T17:37:46.299025+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T173746-09edf77edc/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-a.log sha256=ce4a57ec4d7b7b14f45688f14c434e2ea34fb55ab7e5c5d3144ea9c823f5abf2; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-QA-AI.xml sha256=6fc4d60dc0d07a923fc7ec37053e92fd31023d69c194b3c0c3b78ecd7d52c16d; qa/.runtime/evidence/api/2026-10-30/20261030T173746-09edf77edc/QA-AI-b.log sha256=82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_pdf_reader_default_guidelines
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_pdf_reader_default_guidelines
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_pdf_reader_file_not_found
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_pdf_reader_file_not_found
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_chunking_splits_and_overlaps
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_chunking_splits_and_overlaps
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_chunk_documents_preserves_metadata
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_chunk_documents_preserves_metadata
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_embedding_dimension_and_consistency
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_embedding_dimension_and_consistency
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_cosine_similarity_difference
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_cosine_similarity_difference
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_vector_store_add_and_search
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_vector_store_add_and_search
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_pgvector_sql_schema
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_pgvector_sql_schema
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_reranker_promotes_relevant_and_high_risk_chunks
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_reranker_promotes_relevant_and_high_risk_chunks
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_abstain_when_chunks_empty
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_abstain_when_chunks_empty
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_abstain_when_similarity_is_too_low
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_abstain_when_similarity_is_too_low
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_evidence_explanation_and_citations
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_evidence_explanation_and_citations
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_langgraph_workflow_generate_path
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_langgraph_workflow_generate_path
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_langgraph_workflow_abstain_path
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_langgraph_workflow_abstain_path
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_harness_validation_rejects_empty_title
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_harness_validation_rejects_empty_title
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_harness_validation_rejects_invalid_score
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_harness_validation_rejects_invalid_score
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_harness_retry_success_after_failure
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_harness_retry_success_after_failure
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_harness_error_handling_fallback
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_harness_error_handling_fallback
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_full_pipeline_end_to_end
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_full_pipeline_end_to_end
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_rag_api_health_endpoint
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_rag_api_health_endpoint
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_rag_api_search_endpoint
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_rag_api_search_endpoint
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_rag_api_explain_endpoint_success
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_rag_api_explain_endpoint_success
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_rag::test_rag_api_explain_rejects_empty_title
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_rag::test_rag_api_explain_rejects_empty_title
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_risk_score::test_grade_boundaries
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_risk_score::test_grade_boundaries
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_risk_score::test_young_healthy_person_gets_zero_without_task_points
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_risk_score::test_young_healthy_person_gets_zero_without_task_points
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_risk_score::test_worst_inputs_reach_100
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_risk_score::test_worst_inputs_reach_100
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_risk_score::test_analyze_api_uses_ml_dl_and_explanation
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_risk_score::test_analyze_api_uses_ml_dl_and_explanation
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## 20261030T174647-e942dbd875 / QA-AI/tests.test_risk_score::test_analyze_api_rejects_bad_age
- RUN_ID: 20261030T174647-e942dbd875
- TC_ID: QA-AI/tests.test_risk_score::test_analyze_api_rejects_bad_age
- timestamp: 2026-10-30T17:46:47.844925+09:00
- feature: 위험 점수 경계 및 FastAPI/RAG 회귀
- test_type: api
- tool_a: pytest
- command_a: ["python3", "-m", "pytest", "tests", "-q", "--junitxml=../qa/.runtime/20261030T174647-e942dbd875/QA-AI.xml"]
- result_a: PASS
- tool_b: Ruff
- command_b: ["python3", "-m", "ruff", "check", "src", "tests", "--select", "E9,F63,F7,F82"]
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: True
- files: ai/tests/test_risk_score.py, ai/tests/test_rag.py
- function: UNKNOWN
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-a.log sha256=1c1174b57296b924e9d5d2afa84b8fbc3f0ebf2ddec798b03da063ec43bd83e2; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-QA-AI.xml sha256=e0d6f2cc297219e7e2ff9d1e223108f98ba91ad379d30557a44f47953392d5cd; qa/.runtime/evidence/api/2026-10-30/20261030T174647-e942dbd875/QA-AI-b.log sha256=5b196eb3a6acb50d3fa398d04ca284985cc1ffec870e940264b00780bfd2c971

Observed JUnit XML case status: PASS
Expected: both tools exit 0 with tests present where applicable. Actual: PASS/PASS
Scope comparison: pytest 동작 및 Ruff의 문법/미정의 이름 분석. 외부 모델/운영 API 보안 보증 제외.
Input/reproduction: run the recorded argv in its manifest cwd.
On failure: evidence is recorded before repair; report to user, diagnose log, append cause/fix locations and rerun both tools plus regression. Unknown source locations remain UNKNOWN.

## TC-20261030-1459 / IF-0047
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0047
- timestamp: 2026-10-30T14:59:00+09:00
- feature: applicantName 필드 누락
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 이름 필드 없음. HTTP 400 VALIDATION_ERROR applicantName: must not be blank. 네 테이블 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0048
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0048
- timestamp: 2026-10-30T14:59:00+09:00
- feature: applicantName ''
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 이름 빈 문자열. HTTP 400 applicantName: must not be blank. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0049
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0049
- timestamp: 2026-10-30T14:59:00+09:00
- feature: applicantName ' '
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 이름 공백 한 칸. HTTP 400 applicantName: must not be blank. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0050
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0050
- timestamp: 2026-10-30T14:59:00+09:00
- feature: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 이름 50자. HTTP 201 {"id":22}. 평가·신청자·건강·AI 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0051
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0051
- timestamp: 2026-10-30T14:59:00+09:00
- feature: applicantName 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → applicantName 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 이름 51자. HTTP 400 applicantName: size must be between 0 and 50. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0053
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0053
- timestamp: 2026-10-30T14:59:00+09:00
- feature: age 필드 누락
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 나이 필드 없음. HTTP 400 age: must not be null. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0054
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0054
- timestamp: 2026-10-30T14:59:00+09:00
- feature: age -1
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 나이 -1. HTTP 400 age: must be greater than or equal to 1. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0055
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0055
- timestamp: 2026-10-30T14:59:00+09:00
- feature: age 0
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 나이 0. HTTP 400 age: must be greater than or equal to 1. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0056
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0056
- timestamp: 2026-10-30T14:59:00+09:00
- feature: age 1
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 나이 1. HTTP 201 {"id":24}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0057
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0057
- timestamp: 2026-10-30T14:59:00+09:00
- feature: age 120
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 나이 120. HTTP 201 {"id":25}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0058
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0058
- timestamp: 2026-10-30T14:59:00+09:00
- feature: age 121
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → age 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 나이 121. HTTP 400 age: must be less than or equal to 120. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0061
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0061
- timestamp: 2026-10-30T14:59:00+09:00
- feature: physicalLevel 필드 누락
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 건강 상태 없음. HTTP 400 physicalLevel: must not be null. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0062
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0062
- timestamp: 2026-10-30T14:59:00+09:00
- feature: physicalLevel 0
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 건강 상태 0. HTTP 400 physicalLevel: must be greater than or equal to 1. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0063
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0063
- timestamp: 2026-10-30T14:59:00+09:00
- feature: physicalLevel 1
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 건강 상태 1. HTTP 201 {"id":28}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0064
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0064
- timestamp: 2026-10-30T14:59:00+09:00
- feature: physicalLevel 3
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 건강 상태 3. HTTP 201 {"id":29}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0065
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0065
- timestamp: 2026-10-30T14:59:00+09:00
- feature: physicalLevel 5
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 건강 상태 5. HTTP 201 {"id":30}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0066
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0066
- timestamp: 2026-10-30T14:59:00+09:00
- feature: physicalLevel 6
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → physicalLevel 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 건강 상태 6. HTTP 400 physicalLevel: must be less than or equal to 5. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0068
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0068
- timestamp: 2026-10-30T14:59:00+09:00
- feature: chronicDisease 필드 누락
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 만성질환 없음. HTTP 400 chronicDisease: must not be null. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0069
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0069
- timestamp: 2026-10-30T14:59:00+09:00
- feature: chronicDisease True
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 만성질환 true. HTTP 201 {"id":32}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0070
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0070
- timestamp: 2026-10-30T14:59:00+09:00
- feature: chronicDisease False
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 만성질환 false. HTTP 201 {"id":33}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0071
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0071
- timestamp: 2026-10-30T14:59:00+09:00
- feature: chronicDisease 'yes'
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → chronicDisease 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 만성질환 yes. HTTP 400 INVALID_JSON. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0073
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0073
- timestamp: 2026-10-30T14:59:00+09:00
- feature: workHourLimit 필드 누락
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 근무시간 없음. HTTP 400 workHourLimit: must not be null. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0074
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0074
- timestamp: 2026-10-30T14:59:00+09:00
- feature: workHourLimit 0
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 근무시간 0. HTTP 400 workHourLimit: must be greater than or equal to 1. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0075
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0075
- timestamp: 2026-10-30T14:59:00+09:00
- feature: workHourLimit 1
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 근무시간 1. HTTP 201 {"id":35}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0076
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0076
- timestamp: 2026-10-30T14:59:00+09:00
- feature: workHourLimit 8
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 근무시간 8. HTTP 201 {"id":36}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0077
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0077
- timestamp: 2026-10-30T14:59:00+09:00
- feature: workHourLimit 24
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 근무시간 24. HTTP 201 {"id":37}. 각 +1. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0078
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0078
- timestamp: 2026-10-30T14:59:00+09:00
- feature: workHourLimit 25
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → workHourLimit 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 근무시간 25. HTTP 400 workHourLimit: must be less than or equal to 24. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0080
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0080
- timestamp: 2026-10-30T14:59:00+09:00
- feature: jobId 필드 누락
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 직무 없음. HTTP 400 jobId: must not be null. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0081
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0081
- timestamp: 2026-10-30T14:59:00+09:00
- feature: jobId 1
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 직무 1. HTTP 201 {"id":39}. 각 +1. 목록에서 아파트 야간 경비원, 29점 LOW. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0082
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0082
- timestamp: 2026-10-30T14:59:00+09:00
- feature: jobId 2
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 직무 2. HTTP 201 {"id":40}. 각 +1. 목록에서 택배 배송 기사, 31점 LOW. DELETE 204 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0083
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0083
- timestamp: 2026-10-30T14:59:00+09:00
- feature: jobId 999999
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 직무 999999. HTTP 404 NOT_FOUND 직무를 찾을 수 없습니다: 999999. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0084
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0084
- timestamp: 2026-10-30T14:59:00+09:00
- feature: jobId -1
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 직무 -1. HTTP 404 직무를 찾을 수 없습니다: -1. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0085
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0085
- timestamp: 2026-10-30T14:59:00+09:00
- feature: jobId 'abc'
- test_type: api
- tool_a: Postman/MockMvc/SQL
- command_a: 1. POST /api/assessments 준비 2. 대상 필드만 변경 3. Status/Response 확인 4. DB 신규 데이터 존재 여부 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
- function: @Valid DTO → jobId 필드
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: @NotNull/@NotBlank/@Size/@Min/@Max 위반은 4xx; 유효 값은 AI 상태에 따라 201/AI 오류; 타입 에러는 4xx | 실제: 직무 abc. HTTP 400 INVALID_JSON. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0086
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0086
- timestamp: 2026-10-30T14:59:00+09:00
- feature: malformed body: {"age":
- test_type: api
- tool_a: Postman/MockMvc
- command_a: HTTP 요청 직접 전송 → 상태/응답 및 서버 로그 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치 | 실제: 본문 {"age": . HTTP 400 INVALID_JSON. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0088
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0088
- timestamp: 2026-10-30T14:59:00+09:00
- feature: POST body = []
- test_type: api
- tool_a: Postman/MockMvc
- command_a: HTTP 요청 직접 전송 → 상태/응답 및 서버 로그 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치 | 실제: 본문 []. HTTP 400 INVALID_JSON. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0089
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0089
- timestamp: 2026-10-30T14:59:00+09:00
- feature: POST body=null
- test_type: api
- tool_a: Postman/MockMvc
- command_a: HTTP 요청 직접 전송 → 상태/응답 및 서버 로그 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치 | 실제: 빈 본문, Content-Type application/json. HTTP 400 INVALID_JSON. 두 번 모두 400, 증가 0. JSON null도 400 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0090
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0090
- timestamp: 2026-10-30T14:59:00+09:00
- feature: GET /api/assessments with page=-1
- test_type: api
- tool_a: Postman/MockMvc
- command_a: HTTP 요청 직접 전송 → 상태/응답 및 서버 로그 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치 | 실제: page=-1&size=20. HTTP 200. 페이지가 0으로 보정되어 첫 페이지. 실행 당시 첫 행 id 40. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0091
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0091
- timestamp: 2026-10-30T14:59:00+09:00
- feature: GET /api/assessments with size=0
- test_type: api
- tool_a: Postman/MockMvc
- command_a: HTTP 요청 직접 전송 → 상태/응답 및 서버 로그 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치 | 실제: page=0&size=0. HTTP 200. size 0이 기본 20으로 바뀌어 첫 페이지. 실행 당시 첫 행 id 40. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0092
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0092
- timestamp: 2026-10-30T14:59:00+09:00
- feature: GET /api/assessments with size=20
- test_type: api
- tool_a: Postman/MockMvc
- command_a: HTTP 요청 직접 전송 → 상태/응답 및 서버 로그 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치 | 실제: page=0&size=20. HTTP 200, size 20, 첫 페이지. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.

## TC-20261030-1459 / IF-0093
- RUN_ID: TC-20261030-1459
- TC_ID: IF-0093
- timestamp: 2026-10-30T14:59:00+09:00
- feature: GET /api/assessments with page=9999
- test_type: api
- tool_a: Postman/MockMvc
- command_a: HTTP 요청 직접 전송 → 상태/응답 및 서버 로그 확인
- result_a: PASS
- tool_b: 시트 기록
- command_b: 한 번의 수동 실행. 두 번째 도구 재실행 아님
- result_b: PASS
- status: PASS
- git_commit: 9491fb1b8644049541e4933d83f7b6e8205a5d09
- dirty: false
- files: spring/src/main/demo/assessment/controller/AssessmentController.java
- function: HTTP body 또는 Pageable 변환
- line: UNKNOWN
- ISSUE_ID: 
- RISK_ID: 
- evidence: 기대: 잘못된 본문은 서버 예외가 아닌 4xx; 페이지 반환은 Spring Pageable 동작과 일치 | 실제: page=9999&size=20. HTTP 200, content 빈 배열, pageNumber 9999, totalElements 20, numberOfElements 0. 증가 0 | 수동 시트 한 번 실행. 두 번째 도구로 다시 돌린 기록이 아니다.


# 수동 시트 원문 TC-20261030-1459

# IF-0047 ~ IF-0093 Spring API 테스트 결과

실행일: 2026-10-30 14:59~15:06 (KST)  
대상: 이미 떠 있던 Docker 스택의 Spring `http://localhost:8080`  
판정: **40건 통과, 7건 실패**

기계가 받은 원본 응답은 같은 폴더의 `results.json` 이다. 같은 판정을 엑셀로 넣은 파일은 `IF-0047-0093-결과.xlsx` 다. 탭으로 구분한 표는 `IF-0047-0093-결과표.tsv` 다. 실패 7건은 두 표의 `에러 파일`, `에러 위치`, `에러 난 코드`, `에러 원인` 칸에 소스 위치를 적었다. 통과 건은 그 칸이 비어 있다.

`results.json` 의 `status` 는 실행 스크립트가 매긴 값이다. 타입 변환이 201로 끝나면 통과로 두었고, `page=-1` 과 `size=0` 은 4xx가 아니면 실패로 두었다. 이 문서의 실행 상태는 시트에 적힌 기대 문장으로 다시 판정한 값이다. 타입 오류는 4xx, 페이지 동작은 Spring Pageable과 같아야 한다.

실패 7건은 이슈 트래커에 올리지 않았다. 번호는 이 문서 안에서만 쓴다.

| 버그 ID | 케이스 | 파일과 위치 | 한 줄 |
|---|---|---|---|
| BUG-IF-0052 | IF-0052 | `AssessmentCreateRequest.java` 15행 `applicantName` | JSON 숫자 17이 문자열 `"17"`로 바뀐 뒤 201 |
| BUG-IF-0059 | IF-0059 | `AssessmentCreateRequest.java` 16행 `age` | 60.5가 60으로 잘린 뒤 201 |
| BUG-IF-0060 | IF-0060 | `AssessmentCreateRequest.java` 16행 `age` | `"70"`이 정수 70으로 바뀐 뒤 201 |
| BUG-IF-0067 | IF-0067 | `AssessmentCreateRequest.java` 17행 `physicalLevel` | `"3"`이 정수 3으로 바뀐 뒤 201 |
| BUG-IF-0072 | IF-0072 | `AssessmentCreateRequest.java` 18행 `chronicDisease` | 숫자 1이 true로 바뀐 뒤 201 |
| BUG-IF-0079 | IF-0079 | `AssessmentCreateRequest.java` 19행 `workHourLimit` | 2.5가 2로 잘린 뒤 201 |
| BUG-IF-0087 | IF-0087 | `GlobalExceptionHandler.java` 48–51행 `handleUnexpected` | `text/plain`이 500으로 떨어짐 |

여섯 개 타입 버그는 원인이 같다. Jackson 기본 변환이 잘못된 JSON 타입을 필드 타입으로 바꾼 뒤 `@Valid` 까지 통과한다. 프로젝트에 변환을 막는 설정은 없다.

## 육하원칙

이 절은 케이스 목록을 왜 이렇게 실행했는지에 대한 답이다.

### 누가

시트 IF-0047~IF-0093을 로컬 Docker 스택에 그대로 실행했다. 제품 코드를 고치는 사람은 없고, 떠 있는 Spring과 PostgreSQL에 요청을 보내고 응답과 행 수를 기록했다.

### 언제

2026-10-30이다. 본 실행에서 마지막으로 만들어진 평가의 시각은 `2026-10-30T05:59:47Z`(한국 시간 14:59)이다. `text/plain` 500 로그는 같은 날 `05:59:51Z`다. 소수와 문자 타입이 어떤 정수로 저장됐는지는 그 직후 확인용 요청으로 다시 읽었다.

### 어디서

요청 주소는 `http://localhost:8080` 이다. 프로세스는 컨테이너 `if-app-stack-spring-1`, 데이터베이스는 `if-app-stack-postgres-1` 의 `if_spring` 이다. 판정 근거는 `AssessmentCreateRequest` 의 제약, `AssessmentController` 의 `@Valid` 와 `Pageable`, `GlobalExceptionHandler` 의 400/500 분기, `AssessmentService` 가 직무를 저장보다 먼저 찾는 순서다.

### 무엇을

`POST /api/assessments` 한 건의 입력만 봤다. 이름, 나이, 건강 상태, 만성질환, 근무시간, 직무에 대해 누락, 빈 값, 공백, 최소, 최대, 그 바로 밖, 그리고 JSON 타입이 다른 값을 보냈다. 이어서 깨진 본문, `text/plain`, 배열, 빈 본문, `page=-1`, `size=0`, `size=20`, `page=9999` 를 봤다. 케이스 수는 47이다.

### 어떻게

정상 JSON을 하나 고정하고, 케이스마다 대상 칸만 바꿨다. 기본값은 이름 `기준이름`, 나이 70, 건강 3, 만성질환 false, 근무 8시간, 직무 1이다. 이름 케이스를 제외하면 이름을 케이스 ID로 바꿔 나중에 만든 행을 구분했다.

요청 전후에 `assessment`, `applicant`, `health_snapshot`, `ai_risk_result` 건수를 세었다. 상태 코드와 본문을 남기고, 201로 생긴 평가는 확인 후 삭제했다. 평가 삭제는 신청자와 건강 스냅샷을 지우지 않아서, 이번 실행으로 남은 그 행만 따로 지웠다. 기존 평가 id 2는 건드리지 않았다.

타입 변환 케이스는 본 실행에서 행을 지운 뒤에야 컬럼을 보려 해서, 같은 조합을 한 번 더 보내고 SQL로 읽은 뒤 지웠다. 나이 60.5는 60, 근무 2.5는 2, 나이 `"70"` 은 70, 건강 `"3"` 은 3, 만성질환 1은 true, 이름 숫자 17은 `"17"` 이었다.

### 왜 이렇게 했는가

한 칸만 바꾼 이유는 거절 이유가 그 필드인지 분리하기 위해서다. 나머지 값이 같이 틀리면 400이 나도 어느 제약이 막았는지 알 수 없다.

경계값을 고른 이유는 `@Min`, `@Max`, `@Size` 가 범위 안에서는 통과하고 한 계단 밖에서 거절하기 때문이다. 나이 1과 120, 0과 121, 이름 50자와 51자, 건강 1·5와 0·6, 근무 1·24와 0·25가 그 계단이다. 누락과 빈 문자열, 공백 한 칸은 `@NotNull` 과 `@NotBlank` 가 막는 자리다.

타입을 일부러 어긋나게 보낸 이유는 Jackson이 먼저 값을 바꾼 뒤 `@Valid` 가 보기 때문이다. 소수 잘림, 숫자 문자열, 숫자 1을 불리언으로 받는 변환은 검증 어노테이션에 닿기 전에 끝난다. 시트는 `타입 에러는 4xx` 라고 적혀 있으므로, 변환되어 201로 저장된 여섯 건은 실패다. `"yes"` 와 `"abc"` 처럼 변환이 안 되는 값은 400이라 통과다.

직무 999999와 -1을 검증 400이 아니라 404로 본 이유는 `jobId` 에 최소·최대가 없기 때문이다. 없는 직무는 서비스가 신청자를 저장하기 전에 404를 낸다. 시트 문장 가운데 `유효한 값은 서비스 후속 로직 검사` 에 해당하고, 행이 늘지 않으면 통과다.

건수를 센 이유는 4xx만으로는 저장 뒤 되돌려졌는지 알 수 없기 때문이다. 저장과 AI 호출은 한 트랜잭션이 아니다. 거절은 네 테이블이 그대로여야 하고, 통과한 생성은 네 테이블이 각 1건이어야 한다.

MockMvc 대신 떠 있는 서버에 보낸 이유는 시트 도구가 Postman, MockMvc, SQL을 허용하지만, 사용자가 맞는 것은 컨테이너 안의 Jackson, 검증 메시지, 페이지 보정이기 때문이다. HTTP와 SQL이 그 셋을 한 번에 보여 준다.

만든 행을 지운 이유는 201이 공유 데이터베이스에 평가를 남기기 때문이다. 테스트가 끝난 뒤 건수가 시작 전과 같아야 다음 확인이 섞이지 않는다.

`page=-1` 과 `size=0` 을 실패로 두지 않은 이유는 시트 문장이 둘로 나뉘기 때문이다. 잘못된 본문은 4xx이고, 페이지 반환은 Spring Pageable과 같으면 된다. Spring Data는 음수 페이지를 0으로, 0 이하 크기를 기본 20으로 바꾼 뒤 200을 준다. 그 보정이 나왔으므로 통과다. `page=9999` 는 빈 페이지 200이라 범위 밖 페이지의 Pageable 동작과 같다.

`text/plain` 을 실패로 둔 이유는 잘못된 본문이 서버 예외 500이 되면 안 되기 때문이다. `HttpMediaTypeNotSupportedException` 을 다루는 핸들러가 없어 공통 `Exception` 처리가 500 `INTERNAL_ERROR` 를 냈다. 행은 늘지 않았지만 상태 코드가 기대와 다르다.

## 비어 있던 칸

실행 상태는 모두 `미실행`이었다. 실제 결과, 증거 링크, 버그 ID가 비어 있었다. 아래가 이번 실행으로 채운 값이다. 각 행의 실행일은 2026-10-30이다. 통과 건의 버그 ID는 없다. 실패 건만 오른쪽 네 칸에 파일, 줄, 그 줄의 코드, 원인을 적는다.

| TC ID | 실행일 | 실행 상태 | 실제 결과 | 버그 ID | 증거 링크 | 에러 파일 | 에러 위치 | 에러 난 코드 | 에러 원인 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IF-0047 | 2026-10-30 | 통과 | 이름 필드 없음. HTTP 400 VALIDATION_ERROR `applicantName: must not be blank`. 네 테이블 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0048 | 2026-10-30 | 통과 | 이름 `""`. HTTP 400 `applicantName: must not be blank`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0049 | 2026-10-30 | 통과 | 이름 `" "`. HTTP 400 `applicantName: must not be blank`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0050 | 2026-10-30 | 통과 | 이름 50자 `a`. HTTP 201 `{"id":22}`. 평가·신청자·건강·AI 각 +1. 확인 후 DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0051 | 2026-10-30 | 통과 | 이름 51자 `a`. HTTP 400 `applicantName: size must be between 0 and 50`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0052 | 2026-10-30 | 실패 | 이름 JSON 숫자 17. HTTP 201 `{"id":23}`. `applicant.display_name` 은 `"17"`. 타입 오류인데 4xx가 아님 | BUG-IF-0052 | http://localhost:8080/api/assessments | spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java | 15행 applicantName. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록 | `@NotBlank @Size(max = 50) String applicantName` | JSON 숫자 17이 문자열 "17"이 된 뒤 빈 값이 아니고 50자 안이라 통과. HTTP 201, id 23, display_name은 17 |
| IF-0053 | 2026-10-30 | 통과 | 나이 필드 없음. HTTP 400 `age: must not be null`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0054 | 2026-10-30 | 통과 | 나이 -1. HTTP 400 `age: must be greater than or equal to 1`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0055 | 2026-10-30 | 통과 | 나이 0. HTTP 400 `age: must be greater than or equal to 1`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0056 | 2026-10-30 | 통과 | 나이 1. HTTP 201 `{"id":24}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0057 | 2026-10-30 | 통과 | 나이 120. HTTP 201 `{"id":25}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0058 | 2026-10-30 | 통과 | 나이 121. HTTP 400 `age: must be less than or equal to 120`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0059 | 2026-10-30 | 실패 | 나이 60.5. HTTP 201 `{"id":26}`. 추가 확인에서 저장된 age는 60. 타입 오류인데 4xx가 아님 | BUG-IF-0059 | http://localhost:8080/api/assessments | spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java | 16행 age. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록 | `@NotNull @Min(1) @Max(120) Integer age` | 60.5가 정수 60으로 잘린 뒤 1~120 안이라 통과. HTTP 201, id 26. 저장 age는 60 |
| IF-0060 | 2026-10-30 | 실패 | 나이 `"70"`. HTTP 201 `{"id":27}`. 추가 확인에서 저장된 age는 70. 타입 오류인데 4xx가 아님 | BUG-IF-0060 | http://localhost:8080/api/assessments | spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java | 16행 age. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록 | `@NotNull @Min(1) @Max(120) Integer age` | 문자열 "70"이 정수 70이 된 뒤 범위 안이라 통과. HTTP 201, id 27. 저장 age는 70 |
| IF-0061 | 2026-10-30 | 통과 | 건강 상태 없음. HTTP 400 `physicalLevel: must not be null`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0062 | 2026-10-30 | 통과 | 건강 상태 0. HTTP 400 `physicalLevel: must be greater than or equal to 1`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0063 | 2026-10-30 | 통과 | 건강 상태 1. HTTP 201 `{"id":28}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0064 | 2026-10-30 | 통과 | 건강 상태 3. HTTP 201 `{"id":29}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0065 | 2026-10-30 | 통과 | 건강 상태 5. HTTP 201 `{"id":30}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0066 | 2026-10-30 | 통과 | 건강 상태 6. HTTP 400 `physicalLevel: must be less than or equal to 5`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0067 | 2026-10-30 | 실패 | 건강 상태 `"3"`. HTTP 201 `{"id":31}`. 추가 확인에서 physical_level은 3. 타입 오류인데 4xx가 아님 | BUG-IF-0067 | http://localhost:8080/api/assessments | spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java | 17행 physicalLevel. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록 | `@NotNull @Min(1) @Max(5) Integer physicalLevel` | 문자열 "3"이 정수 3이 된 뒤 1~5 안이라 통과. HTTP 201, id 31. 저장 physical_level은 3 |
| IF-0068 | 2026-10-30 | 통과 | 만성질환 없음. HTTP 400 `chronicDisease: must not be null`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0069 | 2026-10-30 | 통과 | 만성질환 true. HTTP 201 `{"id":32}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0070 | 2026-10-30 | 통과 | 만성질환 false. HTTP 201 `{"id":33}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0071 | 2026-10-30 | 통과 | 만성질환 `"yes"`. HTTP 400 INVALID_JSON `요청 JSON 형식이 올바르지 않습니다.`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0072 | 2026-10-30 | 실패 | 만성질환 숫자 1. HTTP 201 `{"id":34}`. 추가 확인에서 chronic_disease_flag는 true. 타입 오류인데 4xx가 아님 | BUG-IF-0072 | http://localhost:8080/api/assessments | spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java | 18행 chronicDisease. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록 | `@NotNull Boolean chronicDisease` | 숫자 1이 true가 된 뒤 @NotNull만 통과. HTTP 201, id 34. 저장 chronic_disease_flag는 true |
| IF-0073 | 2026-10-30 | 통과 | 근무시간 없음. HTTP 400 `workHourLimit: must not be null`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0074 | 2026-10-30 | 통과 | 근무시간 0. HTTP 400 `workHourLimit: must be greater than or equal to 1`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0075 | 2026-10-30 | 통과 | 근무시간 1. HTTP 201 `{"id":35}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0076 | 2026-10-30 | 통과 | 근무시간 8. HTTP 201 `{"id":36}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0077 | 2026-10-30 | 통과 | 근무시간 24. HTTP 201 `{"id":37}`. 각 +1. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0078 | 2026-10-30 | 통과 | 근무시간 25. HTTP 400 `workHourLimit: must be less than or equal to 24`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0079 | 2026-10-30 | 실패 | 근무시간 2.5. HTTP 201 `{"id":38}`. 추가 확인에서 work_hour_limit은 2. 타입 오류인데 4xx가 아님 | BUG-IF-0079 | http://localhost:8080/api/assessments | spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java | 19행 workHourLimit. 변환은 AssessmentController.java 56행 @RequestBody. 이 줄의 @Valid는 변환된 값만 본다. GlobalExceptionHandler.java 35–40행 handleValidation은 호출되지 않음. AppConfig.java 18–24행은 RestTemplate만 등록 | `@NotNull @Min(1) @Max(24) Integer workHourLimit` | 2.5가 정수 2로 잘린 뒤 1~24 안이라 통과. HTTP 201, id 38. 저장 work_hour_limit은 2 |
| IF-0080 | 2026-10-30 | 통과 | 직무 없음. HTTP 400 `jobId: must not be null`. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0081 | 2026-10-30 | 통과 | 직무 1. HTTP 201 `{"id":39}`. 각 +1. 목록에서 아파트 야간 경비원, 29점 LOW. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0082 | 2026-10-30 | 통과 | 직무 2. HTTP 201 `{"id":40}`. 각 +1. 목록에서 택배 배송 기사, 31점 LOW. DELETE 204 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0083 | 2026-10-30 | 통과 | 직무 999999. HTTP 404 NOT_FOUND `직무를 찾을 수 없습니다: 999999`. 저장 전 차단, 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0084 | 2026-10-30 | 통과 | 직무 -1. HTTP 404 `직무를 찾을 수 없습니다: -1`. 저장 전 차단, 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0085 | 2026-10-30 | 통과 | 직무 `"abc"`. HTTP 400 INVALID_JSON. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0086 | 2026-10-30 | 통과 | 본문 `{"age":`. HTTP 400 INVALID_JSON. 증가 0. 서버 예외 응답 아님 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0087 | 2026-10-30 | 실패 | 정상 JSON을 `Content-Type: text/plain` 으로 전송. HTTP 500 INTERNAL_ERROR `서버 오류가 발생했습니다.`. 증가 0. 로그는 HttpMediaTypeNotSupportedException | BUG-IF-0087 | http://localhost:8080/api/assessments | spring/src/main/demo/global/exception/GlobalExceptionHandler.java | 51행 handleUnexpected의 return. 메서드는 48–51행. 예외는 스프링 AbstractMessageConverterMethodArgumentResolver.readWithMessageConverters 213행 HttpMediaTypeNotSupportedException. 그 호출은 AssessmentController.java 56행 @RequestBody | `return error(HttpStatus.INTERNAL_SERVER_ERROR, "INTERNAL_ERROR", "서버 오류가 발생했습니다.");` | Content-Type text/plain;charset=UTF-8 를 AssessmentCreateRequest로 읽는 컨버터가 없음. 43–46행 handleInvalidJson은 HttpMessageNotReadableException만 400. 500은 51행에서 확정. DB 증가 0. 로그 2026-10-30T05:59:51.359Z |
| IF-0088 | 2026-10-30 | 통과 | 본문 `[]`. HTTP 400 INVALID_JSON. 증가 0 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0089 | 2026-10-30 | 통과 | 본문 비움, Content-Type은 application/json. HTTP 400 INVALID_JSON. 같은 요청을 스크립트가 한 번 더 보냈고 둘 다 400, 증가 0. JSON 토큰 `null` 도 추가 확인에서 400 |  | http://localhost:8080/api/assessments |  |  |  |  |
| IF-0090 | 2026-10-30 | 통과 | `GET /api/assessments?page=-1&size=20`. HTTP 200. Spring이 페이지를 0으로 보정하고 첫 페이지를 반환. 실행 당시 첫 행은 id 40. 증가 0 |  | http://localhost:8080/api/assessments?page=-1&size=20 |  |  |  |  |
| IF-0091 | 2026-10-30 | 통과 | `GET /api/assessments?page=0&size=0`. HTTP 200. size 0은 기본값 20으로 바뀌고 첫 페이지를 반환. 실행 당시 첫 행은 id 40. 증가 0 |  | http://localhost:8080/api/assessments?page=0&size=0 |  |  |  |  |
| IF-0092 | 2026-10-30 | 통과 | `GET /api/assessments?page=0&size=20`. HTTP 200, size 20, 첫 페이지. 증가 0 |  | http://localhost:8080/api/assessments?page=0&size=20 |  |  |  |  |
| IF-0093 | 2026-10-30 | 통과 | `GET /api/assessments?page=9999&size=20`. HTTP 200, content [], pageNumber 9999, size 20, totalElements 20, totalPages 1, numberOfElements 0. 증가 0 |  | http://localhost:8080/api/assessments?page=9999&size=20 |  |  |  |  |

## 환경

- API: `if-app-stack-spring-1`, `http://localhost:8080`. spring-webmvc 6.1.6.
- DB: `if-app-stack-postgres-1`, 사용자 `if_user`, DB `if_spring`. 건수는 컨테이너 안에서 `psql`로 세었다.
- 검증은 Postman이나 MockMvc가 아니다. HTTP 요청과 SQL 건수 비교다.
- 시작 전 평가는 1건이었다. assessment id 2. 신청자 21명, 건강 스냅샷 21건, AI 결과 1건. id 2와 그 전에 있던 신청자는 지우지 않았다.
- 정상 생성 19건은 평가 id 22~40이다. 목록 시각 `2026-10-30T05:59:47Z` 까지 만들어졌고, AI까지 끝나 `AI_COMPLETED` 였다. `text/plain` 500 로그 시각은 `2026-10-30T05:59:51Z` 다.
- 끝난 뒤 평가 id 22~40은 `DELETE /api/assessments/{id}` 가 모두 204였다. 평가 삭제는 신청자와 건강 스냅샷을 지우지 않는다. 그래서 이름 `"17"` 신청자(id 23)가 남아 있었고, 그 행과 연결이 끊긴 건강 스냅샷만 삭제했다.

종료 건수: 평가 1, 신청자 21, 건강 스냅샷 21, AI 결과 1. 평가 id는 2만 남았다.

## 수행 순서

1. `AssessmentCreateRequest` 제약을 코드에서 확인했다. 이름 `@NotBlank @Size(max=50)`, 나이 `@NotNull @Min(1) @Max(120)`, 건강 `@NotNull @Min(1) @Max(5)`, 만성질환 `@NotNull Boolean`, 근무시간 `@NotNull @Min(1) @Max(24)`, 직무 `@NotNull Long`. 직무에는 최소·최대가 없다.
2. 케이스마다 `assessment`, `applicant`, `health_snapshot`, `ai_risk_result` 건수를 요청 전후로 비교했다.
3. 기본 JSON은 이름 `기준이름`, 나이 70, 건강 3, 만성질환 false, 근무 8시간, 직무 1이다. 이름 케이스는 그 값에서 이름만 바꿨다. 나머지 DTO 케이스는 이름을 케이스 ID로 바꾸고 대상 필드만 바꿨다.
4. 201로 생긴 평가는 응답의 id를 모았다가 전부 삭제했다.
5. 타입 변환으로 저장된 값은 본 실행에서 삭제 전에 읽지 못했다. 그래서 같은 서버에 확인용 POST를 두 번 더 보내고, SQL로 컬럼을 읽은 뒤 지웠다.
   - id 41: 나이 60.5, 건강 `"3"`, 만성질환 1, 근무 2.5. 저장값은 age 60, physical_level 3, chronic_disease_flag true, work_hour_limit 2.
   - id 42: 나이 `"70"`. 저장값은 age 70.
   - 둘 다 DELETE 204 후 신청자·건강 행을 삭제했다.
6. 페이지 파라미터의 `pageNumber`/`pageSize` 는 본 실행 응답이 500자로 잘려 있었다. 정리 후 같은 GET을 다시 호출해 보정값을 확인했다. 그때 평가는 id 2만 있었다.

`@Valid` 실패는 `GlobalExceptionHandler` 가 400 `VALIDATION_ERROR` 로 바꾼다. 메시지는 `필드: 기본 메시지` 다. JSON을 읽지 못하면 400 `INVALID_JSON`, 문장 `요청 JSON 형식이 올바르지 않습니다.` 다. 그 밖 예외는 500 `INTERNAL_ERROR`, 문장 `서버 오류가 발생했습니다.` 다.

서비스는 직무를 먼저 찾고, 없을 때 저장 전에 404를 낸다. 저장과 AI 호출은 한 트랜잭션이 아니다. 이번 유효 값 19건은 AI가 성공해 201이었다.

## 실패가 난 파일과 위치

같은 위치는 위 결과표와 `IF-0047-0093-결과.xlsx`, `IF-0047-0093-결과표.tsv` 의 `에러 파일`, `에러 위치`, `에러 난 코드`, `에러 원인` 칸에 다시 적혀 있다. 일곱 건 모두 예외가 DTO 한 줄에서 던져지지는 않는다. 요청은 `AssessmentController.create` 의 `@RequestBody` 에서 JSON으로 바뀌고, 그 다음 `@Valid` 가 돈다. 타입 여섯 건은 변환이 먼저 성공해서 검증이 통과한다. `text/plain` 한 건은 변환 단계에서 예외가 나고, 그 예외를 400으로 바꾸는 핸들러가 없어 500이 된다.

진입점은 같다.

```54:58:spring/src/main/demo/assessment/controller/AssessmentController.java
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Map<String, Long> create(@Valid @RequestBody AssessmentCreateRequest request) {
        Long id = assessmentService.createAndAnalyze(request);
        return Map.of("id", id);
```

56행 `@RequestBody` 가 Jackson 변환이다. `@Valid` 는 변환이 끝난 자바 값만 본다. 프로젝트에 Jackson 변환을 막는 설정은 없다. `AppConfig.java` 18–24행은 `RestTemplate` 빈만 등록한다.

### 타입 변환 6건

시트 기대는 `타입 에러는 4xx` 이고, 잘못된 값은 저장 전에 막혀야 한다. 아래 필드는 타입이 달라도 Jackson 기본 변환이 끝난 값이 `@NotNull`, `@Min`, `@Max`, `@Size` 를 통과한다. `GlobalExceptionHandler.handleValidation` 35–40행은 호출되지 않는다.

```14:20:spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java
public record AssessmentCreateRequest(
        @NotBlank @Size(max = 50) String applicantName,
        @NotNull @Min(1) @Max(120) Integer age,
        @NotNull @Min(1) @Max(5) Integer physicalLevel,   // 1=좋음 ~ 5=나쁨
        @NotNull Boolean chronicDisease,
        @NotNull @Min(1) @Max(24) Integer workHourLimit,
        @NotNull Long jobId
```

| 케이스 | 파일 | 위치 | 그 줄의 코드 | 그 줄에서 일어난 일 |
|---|---|---|---|---|
| IF-0052 | `spring/src/main/demo/assessment/dto/AssessmentCreateRequest.java` | 15행 `applicantName` | `@NotBlank @Size(max = 50) String applicantName` | JSON 숫자 17이 문자열 `"17"`이 된 뒤 빈 값도 아니고 50자 안이라 통과. HTTP 201, id 23 |
| IF-0059 | 같은 파일 | 16행 `age` | `@NotNull @Min(1) @Max(120) Integer age` | 60.5가 정수 60으로 잘린 뒤 1~120 안이라 통과. HTTP 201, id 26. 저장 age=60 |
| IF-0060 | 같은 파일 | 16행 `age` | `@NotNull @Min(1) @Max(120) Integer age` | 문자열 `"70"`이 정수 70이 된 뒤 범위 안이라 통과. HTTP 201, id 27. 저장 age=70 |
| IF-0067 | 같은 파일 | 17행 `physicalLevel` | `@NotNull @Min(1) @Max(5) Integer physicalLevel` | 문자열 `"3"`이 정수 3이 된 뒤 1~5 안이라 통과. HTTP 201, id 31. 저장 physical_level=3 |
| IF-0072 | 같은 파일 | 18행 `chronicDisease` | `@NotNull Boolean chronicDisease` | 숫자 1이 true가 된 뒤 `@NotNull` 만 통과. HTTP 201, id 34. 저장 chronic_disease_flag=true |
| IF-0079 | 같은 파일 | 19행 `workHourLimit` | `@NotNull @Min(1) @Max(24) Integer workHourLimit` | 2.5가 정수 2로 잘린 뒤 1~24 안이라 통과. HTTP 201, id 38. 저장 work_hour_limit=2 |

Spring Boot 3.2.5의 Jackson은 이 변환을 기본으로 켠다. 소수→정수 잘림, 숫자 문자열→정수, 정수→문자열, 정수 1→true가 여기에 해당한다. 이 레코드 필드에는 변환을 거절하는 설정이 없다.

같은 종류의 다른 입력은 거절됐다. 만성질환 `"yes"` (IF-0071)와 직무 `"abc"` (IF-0085)는 Jackson이 변환하지 못해 `HttpMessageNotReadableException` 이 나고, `GlobalExceptionHandler.java` 43–46행 `handleInvalidJson` 이 400 `INVALID_JSON` 을 준다. 증가 0이다.

### IF-0087 text/plain — BUG-IF-0087

정상 JSON을 `Content-Type: text/plain` 으로 보냈다. 응답은 HTTP 500이다.

```json
{"success":false,"data":null,"message":"서버 오류가 발생했습니다.","errorCode":"INTERNAL_ERROR"}
```

DB 증가는 0이다. 예외가 난 순서다.

1. `AssessmentController.java` 56행 `@RequestBody` 가 본문 컨버터를 고른다. `text/plain` 을 `AssessmentCreateRequest` 로 읽는 컨버터가 없다.
2. 스프링 프레임워크 `AbstractMessageConverterMethodArgumentResolver.readWithMessageConverters` 213행에서 `HttpMediaTypeNotSupportedException` 이 난다. 로그 `2026-10-30T05:59:51.359Z`, 문장 `Content-Type 'text/plain;charset=UTF-8' is not supported`.
3. 그 예외를 400으로 바꾸는 메서드가 이 프로젝트에 없다. `GlobalExceptionHandler.java` 43–46행은 `HttpMessageNotReadableException` 만 처리한다. 48–51행 `handleUnexpected` 가 나머지 `Exception` 을 받아 500 `INTERNAL_ERROR` 를 만든다.

```43:51:spring/src/main/demo/global/exception/GlobalExceptionHandler.java
    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<ApiResponse<Void>> handleInvalidJson(HttpMessageNotReadableException e) {
        return error(HttpStatus.BAD_REQUEST, "INVALID_JSON", "요청 JSON 형식이 올바르지 않습니다.");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiResponse<Void>> handleUnexpected(Exception e) {
        log.error("Unhandled exception", e);
        return error(HttpStatus.INTERNAL_SERVER_ERROR, "INTERNAL_ERROR", "서버 오류가 발생했습니다.");
```

500이 확정되는 줄은 51행 `return error(HttpStatus.INTERNAL_SERVER_ERROR, ...)` 이다. 깨진 JSON(IF-0086), 배열 본문(IF-0088), 빈 본문(IF-0089)은 2번이 아니라 `HttpMessageNotReadableException` 이라 43행에서 400이 된다.

추가로, Content-Type을 빼고 빈 본문을 보내면 서버가 `application/x-www-form-urlencoded` 로 보고 같은 500을 냈다. 시각 `2026-10-30T06:06:52.142Z`. 평가 건수는 1에서 변하지 않았다. 이 호출은 47개 케이스 밖이다.

## 필드별 결과

### applicantName

- IF-0047 누락, IF-0048 `""`, IF-0049 `" "` 은 400 `must not be blank`, 증가 0. 통과.
- IF-0050 50자 `a` 는 201 id 22, 각 +1. `@Size(max=50)` 경계 안. 통과.
- IF-0051 51자 `a` 는 400 `size must be between 0 and 50`, 증가 0. 통과.
- IF-0052 숫자 17은 201. 실패. BUG-IF-0052. 파일 `AssessmentCreateRequest.java` 15행 `applicantName`.

### age

- IF-0053 누락은 400 `must not be null`. IF-0054 -1, IF-0055 0은 400 `must be greater than or equal to 1`. IF-0058 121은 400 `must be less than or equal to 120`. 모두 증가 0. 통과.
- IF-0056 나이 1은 201 id 24. IF-0057 나이 120은 201 id 25. 통과.
- IF-0059 60.5는 60으로 저장되고 201. 실패. BUG-IF-0059. 파일 `AssessmentCreateRequest.java` 16행 `age`.
- IF-0060 `"70"` 은 70으로 저장되고 201. 실패. BUG-IF-0060. 파일 `AssessmentCreateRequest.java` 16행 `age`.

### physicalLevel

- IF-0061 누락은 400 `must not be null`. IF-0062 0은 400 `must be greater than or equal to 1`. IF-0066 6은 400 `must be less than or equal to 5`. 증가 0. 통과.
- IF-0063 1은 201 id 28. IF-0064 3은 201 id 29. IF-0065 5는 201 id 30. 통과.
- IF-0067 `"3"` 은 3으로 저장되고 201. 실패. BUG-IF-0067. 파일 `AssessmentCreateRequest.java` 17행 `physicalLevel`.

### chronicDisease

- IF-0068 누락은 400 `must not be null`. 증가 0. 통과.
- IF-0069 true는 201 id 32. IF-0070 false는 201 id 33. 통과.
- IF-0071 `"yes"` 는 400 INVALID_JSON. 증가 0. 통과.
- IF-0072 숫자 1은 true로 저장되고 201. 실패. BUG-IF-0072. 파일 `AssessmentCreateRequest.java` 18행 `chronicDisease`.

### workHourLimit

- IF-0073 누락은 400 `must not be null`. IF-0074 0은 400 `must be greater than or equal to 1`. IF-0078 25는 400 `must be less than or equal to 24`. 증가 0. 통과.
- IF-0075 1은 201 id 35. IF-0076 8은 201 id 36. IF-0077 24는 201 id 37. 통과.
- IF-0079 2.5는 2로 저장되고 201. 실패. BUG-IF-0079. 파일 `AssessmentCreateRequest.java` 19행 `workHourLimit`.

### jobId

- IF-0080 누락은 400 `must not be null`. 증가 0. 통과.
- IF-0081 직무 1은 201 id 39. 목록 응답에서 아파트 야간 경비원, 점수 29, 등급 LOW. 통과.
- IF-0082 직무 2는 201 id 40. 택배 배송 기사, 점수 31, 등급 LOW. 통과.
- IF-0083 999999는 404 `직무를 찾을 수 없습니다: 999999`. IF-0084 -1은 404 `직무를 찾을 수 없습니다: -1`. 직무 필드에는 `@Min` 이 없고, 서비스가 조회 실패를 저장 전에 반환한다. 증가 0. 통과.
- IF-0085 `"abc"` 는 400 INVALID_JSON. 증가 0. 통과.

### HTTP 본문

- IF-0086 본문 `{"age":` 는 400 INVALID_JSON. 증가 0. 통과.
- IF-0087 text/plain 은 500. 실패. BUG-IF-0087. 500이 확정되는 줄은 `GlobalExceptionHandler.java` 51행 `handleUnexpected`. 예외는 컨트롤러 56행 `@RequestBody`에서 시작.
- IF-0088 본문 `[]` 는 400 INVALID_JSON. 증가 0. 통과.
- IF-0089 빈 본문, Content-Type `application/json` 은 400 INVALID_JSON. 스크립트가 빈 본문을 두 번 보냈고 둘 다 400, 증가 0. 추가 확인으로 JSON `null` 도 400 INVALID_JSON, 평가 건수 1 유지. 통과.

### 페이징

컨트롤러는 `@PageableDefault(size = 20, sort = {"assessedAt", "id"}, direction = DESC)` 이다. 기대 문장의 페이지 절은 Spring Pageable 동작과 같으면 된다. 네 건 모두 읽기이고 DB 증가는 0이다.

- IF-0090 `page=-1&size=20` 은 HTTP 200이다. 실행 중에는 방금 만든 평가가 남아 첫 행이 id 40(IF-0082, 31점 LOW)이었다. 정리 후 다시 호출하면 `pageNumber` 0, `pageSize` 20, content는 id 2 한 건이다. 음수 페이지가 0으로 보정된다. 통과.
- IF-0091 `page=0&size=0` 은 HTTP 200이다. 실행 중 응답 앞부분은 IF-0090과 같은 첫 페이지였다. 정리 후 다시 호출하면 `pageSize` 20, `number` 0, content는 id 2다. size 0은 기본 20으로 바뀐다. 통과.
- IF-0092 `page=0&size=20` 은 HTTP 200, size 20, 첫 페이지. 통과.
- IF-0093 `page=9999&size=20` 은 HTTP 200이다. 본 실행 응답은 content [], pageNumber 9999, pageSize 20, offset 199980, totalElements 20, totalPages 1, numberOfElements 0, empty true. totalElements 20은 원래 평가 1건에 이번 201 평가 19건이 아직 있던 시점이다. 정리 후 같은 주소는 content [] , totalElements 1, number 9999다. 통과.

## 정리

제품 코드는 바꾸지 않았다. 이번 실행으로 만든 평가 22~40과 확인용 41, 42는 삭제했다. 신청자 `"17"`, `IF-PROBE`, `IF-PROBE70` 과 그에 붙은 건강 스냅샷만 추가로 지웠다. 평가 id 2와 그 이전 신청자는 그대로다.

# FAIL
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:53 KST)

- **실패/미통과 건수**: 2건 / 전체 2건

### [LOG-006] Spring -> FastAPI -> PostgreSQL 통합 분석 파이프라인 및 이름 trim(LOG-004) 정합성 검증 (`FAIL`) — `-`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:32:39 KST`
- **테스트 종류**: `integration`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `Python HTTP Client (POST /api/assessments -> GET /result)` → **PASS (id=104, name='LOG004_QA', status=AI_COMPLETED, score=29)**
- **도구 B 및 결과**: `psql DB Join Query + FastAPI Direct Inference Comparator` → **FAIL (DB='', FastAPI_direct_score=29)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/service/AssessmentService.java` / 함수 `createAndAnalyze, getResult` / 줄 번호 `79-129, 167-209`
- **입력값 (Input)**: `Spring이 신청자 이름을 trim하여 저장하고 FastAPI 분석 결과를 받아 ai_risk_result에 정확히 적재하는지 교차 검증`
- **오류 메시지 / 응답**: `API score=29, FastAPI score=29, DB=''`
- **예상 결과 (Expected)**: display_name='LOG004_QA', status='AI_COMPLETED', Spring 저장 점수 == FastAPI 직접 추론 점수
- **실제 결과 (Actual)**: API score=29, FastAPI score=29, DB=''
- **재현 방법 (Reproduction)**:
  ```zsh
  AssessmentService.java:86-128
  ```
- **원인 분석 (Root Cause)**: 
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)

### [LOG-016] 평가 삭제(DELETE /api/assessments/{id}) 시 양방향 FK 해제 및 테이블 삭제 범위 검증 (`FAIL`) — `RISK-INT-001`

- **RUN_ID**: `RUN-20261030-001`
- **실행 일시**: `2026-10-30 17:32:39 KST`
- **테스트 종류**: `integration`
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (POST -> DELETE /api/assessments/{id})` → **PASS (HTTP 204)**
- **도구 B 및 결과**: `psql 4-Table Row Count Inspector` → **FAIL (assessment/ai_risk_result 삭제 확인, applicant/health_snapshot 잔류+1 확인 후 정리 완료)**
- **최종 상태**: **FAIL**
- **오류 코드 위치**: 파일 `spring/src/main/demo/assessment/service/AssessmentService.java` / 함수 `delete` / 줄 번호 `216-227`
- **입력값 (Input)**: `삭제 API가 양방향 참조(assessment <-> ai_risk_result)를 끊고 정상 삭제(204)하는지 검증`
- **오류 메시지 / 응답**: `HTTP 204, 삭제 직후 applicant 잔류 +1건 (정리 후 원복 완료)`
- **예상 결과 (Expected)**: HTTP 204 및 assessment, ai_risk_result 행 삭제
- **실제 결과 (Actual)**: HTTP 204, 삭제 직후 applicant 잔류 +1건 (정리 후 원복 완료)
- **재현 방법 (Reproduction)**:
  ```zsh
  AssessmentService.java:216-227
  ```
- **원인 분석 (Root Cause)**: 
- **수정 코드 위치 (Fix Location)**: PENDING_USER_APPROVAL (선기록·선보고 원칙에 따라 수정 대기)
- **재검증 내역 (Re-verification)**: 최초 검출 (코드 수정 후 Tool A/B 재검증 예정)


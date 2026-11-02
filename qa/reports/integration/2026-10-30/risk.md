# RISK
---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:53 KST)

- **검출/추적 리스크 건수**: 1건

### [RISK-INT-001] AssessmentService.delete() 수행 시 Applicant 및 HealthSnapshot 미삭제(Orphan Row) 위험 (심각도: **MEDIUM**, 상태: **OPEN**)

- **RUN_ID**: `RUN-20261030-001`
- **관련 TC_ID**: `LOG-016`
- **실행 일시**: `2026-10-30 17:32:39 KST`
- **기능명 / 테스트 종류**: 평가 삭제 시 신청자(applicant) 및 건강 스냅샷(health_snapshot) 고아 행 잔류 (`integration`)
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `curl CLI (DELETE /api/assessments/{id})` → HTTP 204 정상 응답
- **도구 B 및 결과**: `psql DB Count Verifier` → 삭제 직후 applicant 및 health_snapshot 행이 +1씩 남아 있음을 SQL로 실증 확인
- **대상 코드 위치**: 파일 `spring/src/main/demo/assessment/service/AssessmentService.java` / 함수 `delete` / 줄 번호 `216-227`
- **심각도 (Severity)**: **MEDIUM**
- **발생 가능성 (Likelihood)**: **HIGH**
- **영향 (Impact)**: 평가를 삭제해도 신청자 이름·나이와 건강 상태가 DB에 영구히 남아 개인정보 파기 누락 및 스토리지 누적 발생
- **상세 내용**: AssessmentService.delete()(216-227행)가 assessment와 ai_risk_result만 삭제하고 applicantRepository, healthRepository는 삭제하지 않음.
- **권장 조치 (Recommendation)**: delete() 메서드에서 다른 Assessment가 참조하지 않는 healthSnapshot과 applicant도 함께 삭제하도록 개선 권장
- **처리 상태 (Status)**: `OPEN`
- **보고 이력 (Report History)**: 2026-10-30 17:32:39 KST (RUN-20261030-001) risk.md 선기록 완료


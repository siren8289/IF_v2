# [E2E] 잠재 위험 및 보안/설계 리스크 기록 (2026-10-30)

> **경로**: `qa/reports/e2e/2026-10-30/risk.md`  
> **기준 시간대**: `Asia/Seoul` (KST)  
> **원칙**: 테스트 통과 여부와 별도로 예외 처리 누락, 잠재 취약점, 설계 위험, 불명확 요구사항을 기록합니다. 미해결 HIGH/CRITICAL 위험은 완료·병합을 차단합니다.

---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:32:54 KST)

- **검출/추적 리스크 건수**: 1건

### [RISK-E2E-001] AssessmentFormPage.tsx 생성 응답 id 유효성 미검증 후 라우팅 위험 (심각도: **LOW**, 상태: **OPEN**)

- **RUN_ID**: `RUN-20261030-001`
- **관련 TC_ID**: `IF-0046`
- **실행 일시**: `2026-10-30 17:32:53 KST`
- **기능명 / 테스트 종류**: 평가 생성 응답에 id가 없을 때 잘못된 결과 주소 이동 (`e2e`)
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `Frontend Source Inspector` → id undefined 방어 조건문 미존재 확인
- **도구 B 및 결과**: `E2E Trace Verifier (IF-0046)` → /assessments/undefined/result 이동 확인
- **대상 코드 위치**: 파일 `web-vite/src/pages/AssessmentFormPage.tsx` / 함수 `handleSubmit` / 줄 번호 `66-75`
- **심각도 (Severity)**: **LOW**
- **발생 가능성 (Likelihood)**: **LOW**
- **영향 (Impact)**: 서버가 201 응답 본문에 id 없이 {}를 반환할 경우 /assessments/undefined/result로 이동하여 500/400 에러 알림이 표시됨
- **상세 내용**: AssessmentFormPage.tsx 66-75행에서 createAssessment() 반환값 id가 유정의 정수인지 확인하지 않고 navigate(`/assessments/${id}/result`)를 호출함.
- **권장 조치 (Recommendation)**: createAssessment() 응답 id가 유효한 숫자가 아니면 오류 배너를 띄우고 페이지 이동을 중단하도록 방어 로직 추가 권장
- **처리 상태 (Status)**: `OPEN`
- **보고 이력 (Report History)**: 2026-10-30 17:32:53 KST (RUN-20261030-001) risk.md 선기록 완료


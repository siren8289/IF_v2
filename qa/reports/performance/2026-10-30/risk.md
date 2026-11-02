# [PERFORMANCE] 잠재 위험 및 보안/설계 리스크 기록 (2026-10-30)

> **경로**: `qa/reports/performance/2026-10-30/risk.md`  
> **기준 시간대**: `Asia/Seoul` (KST)  
> **원칙**: 테스트 통과 여부와 별도로 예외 처리 누락, 잠재 취약점, 설계 위험, 불명확 요구사항을 기록합니다. 미해결 HIGH/CRITICAL 위험은 완료·병합을 차단합니다.

---

## 실행 이력: `RUN-20261030-001` (정규 실행 (Standard Run) — 2026-10-30 17:33:10 KST)

- **검출/추적 리스크 건수**: 1건

### [RISK-PERF-001] AssessmentService.createAndAnalyze 동기 RestTemplate(40s 타임아웃) 스레드 점유 위험 (심각도: **MEDIUM**, 상태: **OPEN**)

- **RUN_ID**: `RUN-20261030-001`
- **관련 TC_ID**: `PERF-001, PERF-002`
- **실행 일시**: `2026-10-30 17:33:06 KST`
- **기능명 / 테스트 종류**: Spring RestTemplate 동기 블로킹 호출(ReadTimeout 40초)에 따른 스레드 풀 고갈 위험 (`performance`)
- **Git Commit**: `9491fb1b`
- **도구 A 및 결과**: `Static Config Inspector (AppConfig.java)` → connectTimeout=3s, readTimeout=40s 확인
- **도구 B 및 결과**: `Runtime Concurrency & Timeout Analyzer (LOG-012)` → AI 지연 시 40.099초 동안 요청 스레드 블로킹 확인
- **대상 코드 위치**: 파일 `spring/src/main/demo/global/config/AppConfig.java` / 함수 `restTemplate` / 줄 번호 `18-24`
- **심각도 (Severity)**: **MEDIUM**
- **발생 가능성 (Likelihood)**: **MEDIUM**
- **영향 (Impact)**: FastAPI(Gemini 외부 호출 포함)가 지연될 때 요청당 최대 40초 동안 Tomcat 워커 스레드를 점유하여 동시 평가 요청 집중 시 전체 API 응답 지연 발생 가능
- **상세 내용**: AppConfig.java(22행)의 RestTemplate ReadTimeout이 40초로 설정되어 있고 동기식으로 호출됨.
- **권장 조치 (Recommendation)**: 향후 트래픽 증가 시 AI 분석 요청을 비동기 큐(@Async / 메시지 큐)로 분리하거나 Bulkhead(동시 호출 제한) 적용 권장
- **처리 상태 (Status)**: `OPEN`
- **보고 이력 (Report History)**: 2026-10-30 17:33:06 KST (RUN-20261030-001) risk.md 선기록 완료


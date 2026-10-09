# IF_v2 개인 참고 위험 지수 (Mac 로컬)

기존 F-001~F-003 API와 모델/통계/설명 기능은 유지한다. 새 F-004는 `POST /api/v1/risk/personal-score`로 제공한다. 사고 확률을 추정하거나 검증된 개인 사고 예측 모델을 제공하는 기능이 아니다. `risk_probability`는 항상 `null`이고 `score_type`은 `REFERENCE_INDEX`다. AWS 배포/접속/설정 변경은 수행하지 않는다.

## 산출 정책 PERSONAL_INDEX_V1

다음 기여 점수를 합한 뒤 가장 가까운 정수로 반올림(0.5 올림)하고 0~100으로 제한한다. **가중치와 등급 경계는 실증 검증 전 정책값이다.** 개인 사고 결과를 학습한 가중치나 의학적 기준으로 해석하면 안 된다.

| 요소 | 계산 | 최대 점수 |
|---|---|---:|
| 연령 | `clamp((age-60)*20/30, 0, 20)` | 20 |
| 건강 상태 입력 | `(physical_level-1)*25/4`, 1=좋음·5=나쁨 | 25 |
| 자기보고 만성질환 | 있음 15, 없음 0 | 15 |
| 근무 가능 시간 제약 | `max(0,8-work_hour_limit)*10/7` | 10 |
| ML/DL 작업 특성 | 라벨별 ML/DL 모델 점수 평균 × 정책 가중치 합계, 상한 30 | 30 |

작업 가중치: DRIVING=10, NIGHT_SHIFT=8, WALKING=8, CLEANING_TASK=8, CARE_TASK=6, FACILITY_MAINTENANCE=8. OFFICE_TASK는 가산하지 않는다. 양 모델의 필수 라벨이 없거나 점수가 유한한 0~1 값이 아니면 계산을 실패시킨다. 모델 점수는 작업 특성/사고 발생 확률이 아니다.

등급: LOW=0~40, MID=41~60, HIGH=61~100. 낮은 점수도 안전 보장을 뜻하지 않는다. 근무 가능 시간은 실제 근무시간과 다르며 현재 정책에서는 자기보고 입력 제약으로만 사용한다.

F-002/F-003을 재사용해 산업·연령 통계와 설명을 결과에 첨부한다. 미검수 산업 매핑과 노출인구 분모 부재로 재해 건수는 가산하지 않는다. 공고 ID가 없거나 통계가 없으면 `evidence_status=UNAVAILABLE`과 사유를 표시한다. 통계가 있어도 `REFERENCE_ONLY`다. 독립 검수 데이터·개인 사고 결과에 대한 보정/타당성 검증은 후속 과제다. 담당자 검토 없이 채용·배제·진단·안전 판정에 사용하지 않는다.

## API와 저장

```bash
curl http://127.0.0.1:18000/api/v1/risk/personal-score \
  -H 'Content-Type: application/json' \
  -d '{"job_id":"KJ21062610080016","title":"야간 배송기사 모집","age":70,"physical_level":3,"chronic_disease":true,"work_hour_limit":6}'
```

필수 입력은 title, age(1~120 정수), physical_level(1~5 정수), chronic_disease(boolean), work_hour_limit(1~24 정수)다. job_id는 선택 항목이다. 누락한 건강 정보를 정상값으로 대체하지 않는다. 응답에 입력, ML/DL 원본 분석, 요인별 기여, 작업별 모델 점수/가중치, 통계, F-003 설명, 한계, 정책 버전을 제공한다.

Spring의 기존 `POST /api/assessments/{id}/compute-risk`가 DB의 개인/건강/직무 입력을 FastAPI에 보내고 유효한 정수 점수·등급·지수 타입·입력 일치·버전을 검증한다. 성공 시 한 트랜잭션에서 `ai_risk_result`에 점수/등급/원본 JSON/버전을 저장하고 `PENDING_AI → AI_COMPLETED`로 변경한다. 확정(FINALIZED) 결과는 덮어쓰지 않는다. 외부 추론은 DB 트랜잭션 밖에서 수행하며 저장 시 평가 행 잠금과 입력 재확인으로 동시 요청/입력 변경을 처리한다. 재계산 실패 시 이전 결과는 유지한다.

기존 `total_risk_percent` 컬럼은 호환성을 위해 유지하되 PERSONAL_INDEX_V1에서는 **퍼센트가 아닌 정수 지수**를 저장한다. 신규 스키마 마이그레이션은 필요하지 않다. 이전 EVIDENCE_ONLY 결과의 조회와 null 점수는 유지한다. React는 null을 “미산출”로, 실제 0점을 “0점”으로 표시하고 계산/조회 오류를 알린다. 등급별 안전 보장 문구를 제거하고 산출 근거와 한계를 표시한다.

## 로컬 실행 및 E2E 재현

아래 명령은 저장소 루트에서 실행한다. Python은 프로젝트 `.venv` 인터프리터를 사용한다. 필요한 경우 `.venv/bin/python -m pip install -r ai/requirements.txt`, `cd web-vite && npm ci`로 의존성을 설치한다. Mac에 Chrome과 Java 17, Docker가 필요하다.

테스트는 기존 PostgreSQL과 분리한 **일회용 DB**를 사용한다. `create-drop`은 아래 임시 DB에만 적용한다.

```bash
docker run --rm -d --name if-personal-risk-test-db \
  -p 127.0.0.1:15432:5432 \
  -e POSTGRES_DB=if_personal_test -e POSTGRES_USER=if_test \
  -e POSTGRES_PASSWORD=if_test_local_only postgres:16-alpine
```

터미널 1 (FastAPI):

```bash
cd ai
../.venv/bin/python -m uvicorn src.api.main:app --host 127.0.0.1 --port 18000
```

터미널 2 (Spring; DB 준비 후 실행):

```bash
cd spring
./gradlew test bootJar
java -jar build/libs/spring-0.0.1-SNAPSHOT.jar \
  --server.address=127.0.0.1 --server.port=18080 \
  --spring.datasource.url=jdbc:postgresql://localhost:15432/if_personal_test \
  --spring.datasource.username=if_test \
  --spring.datasource.password=if_test_local_only \
  --spring.jpa.hibernate.ddl-auto=create-drop \
  --app.ai.base-url=http://127.0.0.1:18000
```

`/actuator/health`가 UP인 것을 확인한 후 루트의 터미널 3:

```bash
docker exec if-personal-risk-test-db psql -U if_test -d if_personal_test \
  -c "INSERT INTO job(job_title,external_job_id,created_at) VALUES ('야간 배송기사 모집','KJ21062610080016',NOW());"
cd web-vite
npm test
npm run build
npm run test:e2e
```

E2E는 Vite를 자동으로 localhost:3000에 실행하고 실제 입력→ML/DL 추론→PostgreSQL 저장→점수/한계 표시→새로고침→대시보드를 검증한다. 실행 중인 Vite가 있으면 종료해 포트를 비워둔다. `E2E_API_URL`로 로컬 Spring 주소를 지정할 수 있고 이미 띄운 프런트엔드에는 `E2E_BASE_URL`도 지정한다. 외부 호스트는 테스트 설정에서 차단한다. Chrome 대신 Playwright Chromium을 쓰려면 `npx playwright install chromium` 후 `E2E_BROWSER=chromium npm run test:e2e`를 사용한다. E2E는 평가 결과를 삭제하지만 신청자/건강 스냅샷은 임시 DB 삭제 시 정리된다.

Spring AI 읽기 제한 기본값은 30초다(첫 ML/DL 모델 로딩 포함). `APP_AI_READ_TIMEOUT_MS` 또는 `--app.ai.read-timeout-ms=30000`으로 조정할 수 있다. 연결 제한은 3초다. 계산 실패는 성공 상태로 저장되지 않는다.

검증 후 FastAPI/Spring을 Ctrl+C로 종료하고 임시 DB만 삭제한다:

```bash
docker stop if-personal-risk-test-db
```

pytest (루트):

```bash
PYTHONPATH="$PWD/ai" .venv/bin/python -m pytest ai/src/features data/tests --import-mode=importlib -q
```

## 변경 파일

- FastAPI: `ai/src/api/routes.py`, `ai/src/features/f004_personal_risk/__init__.py`, `service.py`, `tests/test_personal_risk.py`. `ai/requirements.txt`의 중복 항목 정리(기존 의존성 유지).
- Spring: `ai/client/AIClient.java`, `ai/service/AIRiskService.java`, `ai/entity/AIRiskResult.java`, `assessment/dto/AssessmentRiskDetailResponse.java`, `assessment/repository/AssessmentRepository.java`, `applicant/dto/ApplicantDto.java`, `global/config/AppConfig.java` (모두 `spring/src/main/demo/` 기준). `spring/src/test/java/demo/ai/PersonalRiskPersistenceTest.java` 추가.
- React: `src/features/assessment/{service.ts,service.test.ts,components/AssessmentForm.tsx}`, `src/features/dashboard/{mappers.ts,mappers.test.ts,components/AssessmentTable.tsx}`, `src/features/risk/{useRiskDetail.ts,useComputeRisk.ts,useComputeRisk.test.tsx,riskLevel.ts,RiskResultCard.test.tsx,components/RiskResultCard.tsx}`, `src/pages/{RiskAnalysisPage.tsx,RiskResultPage.tsx}`, `src/shared/{api/types.ts,model/assessment.ts,model/assessment.test.ts}` (`web-vite/` 기준).
- E2E 구성: `web-vite/{package.json,package-lock.json,vite.config.ts,playwright.config.ts,e2e/personal-risk.spec.ts}`, `.gitignore`, 이 문서.
- 기존 F-001~F-003 추론/통계/설명 구현, AWS 구성, 기존 로컬 DB 데이터는 변경하지 않는다.

## 검증 결과

2026-10-10 Mac 로컬에서 pytest 92개, JUnit 46개, React/Vitest 20개 통과. TypeScript/Vite 빌드와 실제 PostgreSQL 기반 Playwright E2E도 통과했다. JUnit은 H2 테스트 프로필로 저장/롤백/상태 전이/잘못된 AI 응답/입력 변경/확정 결과 보호/이전 EVIDENCE_ONLY 조회를 검증했다. 별도 임시 PostgreSQL에서 실제 ML/DL HTTP 연동으로 55점·MID·AI_COMPLETED·PERSONAL_INDEX_V1 저장 행을 직접 조회했다. 이는 구현 검증이며 개인 사고 예측 정확도 검증이 아니다.

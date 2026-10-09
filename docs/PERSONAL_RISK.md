# IF_v2 고령자 위험도 판단 (간소화 버전)

기능은 2개만 남겼다.

1. **평가 입력 → 위험도 결과**: 신청자 정보를 입력하면 AI가 0~100점 참고 지수와 설명을 만든다.
2. **대시보드**: 저장된 평가 목록, 요약(전체/고위험/분석 완료), 결과 보기, 삭제.

점수는 사고 확률이나 진단이 아니라 정해 둔 규칙으로 더한 참고 지수다.

## 구조

```
React (web-vite)  →  Spring (spring)  →  FastAPI (ai)
                         │                  ├─ ML: scikit-learn 다중 라벨 분류 (models/task_ml.joblib)
                         │                  ├─ DL: PyTorch 문자 CNN       (models/task_cnn.pt)
                         │                  └─ 생성형 AI: Gemini 설명 (키가 없으면 기본 설명)
                         └─ PostgreSQL
```

## API

| 서버 | 메서드 | 경로 | 설명 |
|---|---|---|---|
| FastAPI | POST | `/api/v1/risk/analyze` | ML + DL + 점수 계산 + 설명 |
| FastAPI | GET | `/health` | 상태 확인 |
| Spring | GET | `/api/jobs` | 직무 목록 |
| Spring | GET | `/api/assessments` | 대시보드 목록 (20개씩) |
| Spring | GET | `/api/assessments/summary` | 요약 카드 |
| Spring | POST | `/api/assessments` | 평가 등록 + AI 분석, `{ "id": 1 }` 반환 |
| Spring | GET | `/api/assessments/{id}/result` | 결과 화면 데이터 |
| Spring | DELETE | `/api/assessments/{id}` | 삭제 |

AI 호출이 실패하면 평가는 `PENDING_AI` 상태로 남고 화면에 오류가 표시된다.

## 점수 규칙 (`ai/src/risk_score.py`)

| 요소 | 계산 | 최대 |
|---|---|---:|
| 나이 | 60세 이하 0점, 90세 이상 20점, 사이는 비례 | 20 |
| 건강 상태 | `(physical_level-1)*25/4`, 1=좋음·5=나쁨 | 25 |
| 만성질환 | 있음 15, 없음 0 | 15 |
| 근무 가능 시간 | 8시간 이상 0점, `(8-시간)*10/7` | 10 |
| 직무 특성 | (ML 점수 + DL 점수)/2 × 가중치 합, 최대 30 | 30 |

가중치: 운전 10, 야간 근무 8, 장시간 보행 8, 청소 8, 돌봄 6, 시설 관리 8. 사무(OFFICE_TASK)는 더하지 않는다.
등급: LOW 0~40, MID 41~60, HIGH 61~100.

## 생성형 AI 설정

`GEMINI_API_KEY`가 있으면 Gemini가 설명을 쓰고, 없거나 실패하면 규칙 기반 기본 설명을 쓴다.
서버에서는 `/home/ubuntu/IF_v2/.env`에 `GEMINI_API_KEY=...`를 넣으면 compose가 FastAPI에 전달한다.

## 로컬 실행

```bash
# FastAPI
cd ai
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install torch --index-url https://download.pytorch.org/whl/cpu
.venv/bin/python -m uvicorn src.main:app --port 8000

# Spring (PostgreSQL 필요)
cd spring
./gradlew bootRun

# React
cd web-vite
npm ci
npm run dev   # http://localhost:3000
```

## 테스트

```bash
cd ai && .venv/bin/python -m pytest tests -q      # AI
cd spring && ./gradlew build                       # Spring (H2 사용)
cd web-vite && npm test && npm run build           # React
```

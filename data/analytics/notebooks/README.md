# Notebooks (공공데이터 EDA 및 품질 검증)

프로젝트에 등록된 공공데이터 API 및 데이터셋별 EDA·품질 검증 노트북 목록입니다.

## 1. 개별 API EDA 및 품질 검증 노트북

| 번호 | 노트북 파일 | 데이터 소스 / API | 저장되는 Raw CSV |
| :--- | :--- | :--- | :--- |
| **01** | [`01_job_posting_eda.ipynb`](01_job_posting_eda.ipynb) | 한국노인인력개발원 자립형 노인일자리 사업모집공고 (`JobBsnInfoService`) | `data/raw/job_bsn_recruit_raw.csv` |
| **02** | [`02_job_posting_quality.ipynb`](02_job_posting_quality.ipynb) | 자립형 노인일자리 공고 데이터 품질(DQ) 검증 규칙 점검 | `data/raw/job_bsn_recruit_raw.csv` 참조 |
| **03** | [`03_senuri_job_eda.ipynb`](03_senuri_job_eda.ipynb) | 한국노인인력개발원 노인 구인정보 (`SenuriService`) | `data/raw/senuri_job_raw.csv` |
| **04** | [`04_senior_activity_code_eda.ipynb`](04_senior_activity_code_eda.ipynb) | 한국노인인력개발원 노인사회활동 시스템 지역/코드 (`OdsnCodeInquiryService2`) | `data/raw/senior_activity_code_raw.csv` |
| **05** | [`05_ltc_statistics_eda.ipynb`](05_ltc_statistics_eda.ipynb) | 국민건강보험공단 노인장기요양보험 시도별 판정(15072696) 및 인정현황(3051420) | `data/raw/ltc_grade_judgement_raw.csv`<br>`data/raw/ltc_recognition_status_raw.csv` |
| **06** | [`06_industrial_accident_eda.ipynb`](06_industrial_accident_eda.ipynb) | 한국산업안전보건공단 산업재해 4종 (규모별/지청별/사고별/연령별) | `data/raw/accident_by_scale_raw.csv`<br>`data/raw/accident_by_branch_raw.csv`<br>`data/raw/accident_by_industry_raw.csv`<br>`data/raw/accident_by_age_raw.csv` |
| **07** | [`07_ltc_institution_eda.ipynb`](07_ltc_institution_eda.ipynb) | 국민건강보험공단 장기요양기관 검색 (`searchLtcInsttService02`) | `data/raw/ltc_institution_raw.csv` |

## 2. 전체 API 스키마 비교 Summary 노트북

| 번호 | 노트북 파일 | 설명 |
| :--- | :--- | :--- |
| **08** | [`08_public_api_summary.ipynb`](08_public_api_summary.ipynb) | 전체 API/데이터셋의 전체 컬럼, 데이터타입, 결측률, 공통 식별자(PK/JOIN 후보) 종합 비교 |

## 3. 원칙
- **원형 보존**: EDA 단계에서는 컬럼 삭제, 전처리, JOIN, DB 적재를 수행하지 않고 원본 데이터 그대로 보존합니다.
- **API Key**: `../../.env`의 `PUBLIC_DATA_API_KEY` 환경변수를 공통 사용합니다.
- **Raw 데이터**: 모든 API의 수집 원본은 `data/raw/*.csv`에 UTF-8-SIG 인코딩으로 저장됩니다.

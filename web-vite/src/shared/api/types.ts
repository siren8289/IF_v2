/** Backend API DTOs (align with openapi.yml / Spring DTOs) */

/** 신청자 등록 응답 */
export interface ApplicantResponse {
  id: number;
  displayName: string;
  age: number;
  createdAt: string;
}

/** POST /api/applicants 요청 본문 */
export interface ApplicantCreateRequest {
  displayName: string;
  age: number;
}

/** POST /api/applicants/{id}/health-snapshots 요청 본문 */
export interface HealthSnapshotCreateRequest {
  physicalLevel: number;
  chronicDiseaseFlag: boolean;
  workHourLimit: number;
}

/** 건강 스냅샷 등록 응답. id를 평가 생성(healthId)에 사용한다. */
export interface HealthSnapshotResponse {
  id: number;
  applicantId: number;
  physicalLevel: number;
  chronicDiseaseFlag: boolean;
  workHourLimit: number;
  createdAt: string;
}

/** 평가 생성 응답. id로 분석/결과 화면 URL을 만든다. */
export interface AssessmentResponse {
  id: number;
  applicantId: number;
  status: string;
  assessedAt: string;
}

/** POST /api/applicants/{id}/assessments 요청 본문 */
export interface AssessmentCreateRequest {
  jobId: number;
  healthId: number;
}

/** GET /api/jobs 항목 (평가 대상 직무) */
export interface JobResponse {
  id: number;
  jobTitle: string;
  workplace: string;
  workHours: string;
  description: string;
  createdAt: string;
}

/** GET /api/assessments/{id}/risk-detail: FastAPI 점수/설명을 Spring이 합쳐 내려준 결과 */
export interface AssessmentRiskDetailResponse {
  scoreType?: string | null;
  reviewRequired?: boolean | null;
  modelVersion?: string | null;
  dataStatus?: string | null;
  limitations?: string[];
  calculation?: {
    evidence_status: string;
    evidence?: { job: { industry_candidate: string | null; evidence_year: number | null; industry_accident_count: number | null }; age_reference: { statistic_year: number } } | null;
    explanation?: { summary?: string } | null;
    task_basis: { label: string; ml_score: number; dl_score: number; weight: number; weighted_points: number }[];
  } | null;
  riskScore: number | null;
  riskBand: string | null;
  riskGrade: string | null;
  summary: string;
  factorSummaries: string[];
  guidance: string;
  disclaimer: string;
}

/** GET /api/assessments 목록 항목 (대시보드). fetch join으로 한 번에 조회됨. */
export interface AssessmentRecordResponse {
  id: number;
  applicantName: string;
  age: number;
  jobTitle: string;
  physicalLevel: string | null;
  status: string;
  riskScore: number | null;
  riskGrade: "LOW" | "MID" | "HIGH" | null;
  assessedAt: string;
}

/** GET /api/assessments/summary. 목록과 별도로 서버에서 COUNT 집계한 값. */
export interface AssessmentSummaryResponse {
  totalCount: number;
  highRiskCount: number;
  finalizedCount: number;
}

/** Spring Data Page<T> 직렬화 형태 (일부 필드만 사용) */
export interface PageResponse<T> {
  content: T[];
  totalElements: number;
  totalPages: number;
  number: number;
  size: number;
}

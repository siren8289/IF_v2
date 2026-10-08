import { apiRequest } from "./client";
import type {
  AssessmentCreateRequest,
  AssessmentRecordResponse,
  AssessmentResponse,
  AssessmentRiskDetailResponse,
  AssessmentSummaryResponse,
  PageResponse,
} from "./types";

/** 대시보드 목록: join 쿼리 1회로 조회 (신청자별 N+1 호출 방지). */
export function listAssessmentRecords(
  page = 0,
  size = 50
): Promise<PageResponse<AssessmentRecordResponse>> {
  return apiRequest<PageResponse<AssessmentRecordResponse>>(
    `/api/assessments?page=${page}&size=${size}&sort=assessedAt,desc`
  );
}

/** 요약 카드용 집계. 목록 페이지 길이로 계산하면 페이지 크기를 넘는 순간 틀어지므로 서버 COUNT를 쓴다. */
export function getAssessmentSummary(): Promise<AssessmentSummaryResponse> {
  return apiRequest<AssessmentSummaryResponse>("/api/assessments/summary");
}

export function createAssessment(
  applicantId: number,
  body: AssessmentCreateRequest
): Promise<AssessmentResponse> {
  return apiRequest<AssessmentResponse>(
    `/api/applicants/${applicantId}/assessments`,
    { method: "POST", body: JSON.stringify(body) }
  );
}

export async function deleteAssessment(assessmentId: number): Promise<void> {
  await apiRequest<void>(`/api/assessments/${assessmentId}`, {
    method: "DELETE",
  });
}

/** 상태만 수정: PENDING_AI | AI_COMPLETED | FINALIZED */
export async function updateAssessment(
  assessmentId: number,
  body: { status?: string }
): Promise<void> {
  await apiRequest<void>(`/api/assessments/${assessmentId}`, {
    method: "PATCH",
    body: JSON.stringify(body),
  });
}

/** AI 위험도 계산 트리거 */
export async function computeRisk(assessmentId: number): Promise<void> {
  await apiRequest<void>(`/api/assessments/${assessmentId}/compute-risk`, {
    method: "POST",
  });
}

export function getRiskDetail(
  assessmentId: number
): Promise<AssessmentRiskDetailResponse> {
  return apiRequest<AssessmentRiskDetailResponse>(
    `/api/assessments/${assessmentId}/risk-detail`
  );
}

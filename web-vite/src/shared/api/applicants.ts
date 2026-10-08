// API Client 계층: 신청자/건강 스냅샷 등록 엔드포인트 (평가 입력 1~2단계).
import { apiRequest } from "./client";
import type {
  ApplicantCreateRequest,
  ApplicantResponse,
  HealthSnapshotCreateRequest,
  HealthSnapshotResponse,
} from "./types";

/** POST /api/applicants */
export function createApplicant(
  body: ApplicantCreateRequest
): Promise<ApplicantResponse> {
  return apiRequest<ApplicantResponse>("/api/applicants", {
    method: "POST",
    body: JSON.stringify(body),
  });
}

/** POST /api/applicants/{applicantId}/health-snapshots */
export function createHealthSnapshot(
  applicantId: number,
  body: HealthSnapshotCreateRequest
): Promise<HealthSnapshotResponse> {
  return apiRequest<HealthSnapshotResponse>(
    `/api/applicants/${applicantId}/health-snapshots`,
    { method: "POST", body: JSON.stringify(body) }
  );
}

import { apiRequest } from "./client";
import type {
  ApplicantCreateRequest,
  ApplicantResponse,
  HealthSnapshotCreateRequest,
  HealthSnapshotResponse,
} from "./types";

export function createApplicant(
  body: ApplicantCreateRequest
): Promise<ApplicantResponse> {
  return apiRequest<ApplicantResponse>("/api/applicants", {
    method: "POST",
    body: JSON.stringify(body),
  });
}

export function createHealthSnapshot(
  applicantId: number,
  body: HealthSnapshotCreateRequest
): Promise<HealthSnapshotResponse> {
  return apiRequest<HealthSnapshotResponse>(
    `/api/applicants/${applicantId}/health-snapshots`,
    { method: "POST", body: JSON.stringify(body) }
  );
}

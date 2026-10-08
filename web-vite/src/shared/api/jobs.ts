// API Client 계층: 직무 목록 엔드포인트.
import { apiRequest } from "./client";
import type { JobResponse } from "./types";

/** GET /api/jobs: 평가 입력 폼의 직무 선택지 */
export function listJobs(): Promise<JobResponse[]> {
  return apiRequest<JobResponse[]>("/api/jobs");
}

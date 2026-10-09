// API Client 계층: 직무 목록 엔드포인트.
import { apiRequest } from "./client";
import type { JobResponse, PageResponse } from "./types";

/** GET /api/jobs: 평가 입력 폼의 직무 선택지 */
export async function listJobs(): Promise<JobResponse[]> {
  const page = await apiRequest<PageResponse<JobResponse>>("/api/jobs");
  return page.content;
}

import { apiRequest } from "./client";
import type { JobResponse } from "./types";

export function listJobs(): Promise<JobResponse[]> {
  return apiRequest<JobResponse[]>("/api/jobs");
}

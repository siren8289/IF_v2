import { useEffect, useState } from "react";
import { listJobs } from "@/shared/api/jobs";
import type { JobResponse } from "@/shared/api/types";

/** 마운트 시 직무 목록을 한 번 불러온다. 실패하면 빈 목록(폼에서 안내 문구 표시). */
export function useJobs(): JobResponse[] {
  const [jobs, setJobs] = useState<JobResponse[]>([]);

  useEffect(() => {
    listJobs().then(setJobs).catch(() => setJobs([]));
  }, []);

  return jobs;
}

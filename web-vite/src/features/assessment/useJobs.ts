import { useEffect, useState } from "react";
import { listJobs } from "@/shared/api/jobs";
import type { JobResponse } from "@/shared/api/types";

export function useJobs(): JobResponse[] {
  const [jobs, setJobs] = useState<JobResponse[]>([]);

  useEffect(() => {
    listJobs().then(setJobs).catch(() => setJobs([]));
  }, []);

  return jobs;
}

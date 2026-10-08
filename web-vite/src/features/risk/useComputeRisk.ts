import { useEffect, useRef } from "react";
import { computeRisk } from "@/shared/api/assessments";

/** 평가 ID당 한 번만 위험도 계산을 요청하고, 성공/실패와 무관하게 완료 시 onSettled를 호출한다. */
export function useComputeRisk(assessmentId: number | null, onSettled: () => void): void {
  const startedRef = useRef(false);
  const onSettledRef = useRef(onSettled);
  onSettledRef.current = onSettled;

  useEffect(() => {
    if (assessmentId === null || startedRef.current) return;
    startedRef.current = true;
    computeRisk(assessmentId)
      .catch(() => {})
      .finally(() => onSettledRef.current());
  }, [assessmentId]);
}

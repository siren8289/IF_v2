import { useEffect, useRef } from "react";
import { computeRisk } from "@/shared/api/assessments";

/** 평가 ID당 한 번만 위험도 계산을 요청하고, 성공/실패와 무관하게 완료 시 onSettled를 호출한다. */
export function useComputeRisk(assessmentId: number | null, onSettled: (error: string | null) => void): void {
  // StrictMode에서 effect가 두 번 실행되어도 계산 요청(POST)이 중복되지 않게 한다.
  const startedRef = useRef<{ id: number; promise: Promise<void> } | null>(null);
  const onSettledRef = useRef(onSettled);
  onSettledRef.current = onSettled;

  useEffect(() => {
    if (assessmentId === null) return;
    if (startedRef.current?.id !== assessmentId) {
      startedRef.current = { id: assessmentId, promise: computeRisk(assessmentId) };
    }
    let cancelled = false;
    startedRef.current.promise
      .then(() => { if (!cancelled) onSettledRef.current(null); })
      .catch((error) => {
        if (!cancelled) onSettledRef.current(error instanceof Error ? error.message : "계산에 실패했습니다.");
      });
    return () => { cancelled = true; };
  }, [assessmentId]);
}

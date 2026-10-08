import { useEffect, useState } from "react";
import { getRiskDetail } from "@/shared/api/assessments";
import {
  riskGradeToLevel,
  type Assessment,
  type RiskLevel,
} from "@/shared/model/assessment";

/** 결과 화면이 그리는 값 묶음 (점수/등급/요인/요약/가이드/면책) */
export interface RiskView {
  score: number;
  level: RiskLevel;
  factors: string[];
  summary: string | null;
  guidance: string | null;
  disclaimer: string | null;
}

/** 상세 조회 결과를 보여주되, 실패하면 대시보드에서 넘겨받은 값(fallback)을 유지한다. */
export function useRiskDetail(
  assessmentId: number | null,
  fallback?: Partial<Assessment>
): RiskView {
  const [view, setView] = useState<RiskView>({
    score: fallback?.riskScore || 0,
    level: fallback?.riskLevel || "Low",
    factors: fallback?.riskFactors || [],
    summary: null,
    guidance: null,
    disclaimer: null,
  });

  useEffect(() => {
    if (assessmentId === null) return;
    // 언마운트/ID 변경 후 늦게 도착한 응답이 상태를 덮어쓰지 않게 한다.
    let cancelled = false;

    getRiskDetail(assessmentId)
      .then((detail) => {
        if (cancelled) return;
        setView({
          score: detail.riskScore ?? 0,
          level: riskGradeToLevel(detail.riskGrade),
          factors: detail.factorSummaries || [],
          summary: detail.summary || null,
          guidance: detail.guidance || null,
          disclaimer: detail.disclaimer || null,
        });
      })
      .catch(() => {});

    return () => {
      cancelled = true;
    };
  }, [assessmentId]);

  return view;
}

import { useEffect, useState } from "react";
import { getRiskDetail } from "@/shared/api/assessments";
import { riskGradeToLevel, type Assessment, type RiskLevel } from "@/shared/model/assessment";

export interface RiskView {
  score: number | null;
  level: RiskLevel;
  factors: string[];
  summary: string | null;
  guidance: string | null;
  disclaimer: string | null;
  loading?: boolean;
  error?: string | null;
  modelVersion?: string | null;
  evidenceSummary?: string | null;
}

export function useRiskDetail(assessmentId: number | null, fallback?: Partial<Assessment>): RiskView {
  const initial: RiskView = {
    score: fallback?.riskScore ?? null, level: fallback?.riskScore == null ? "Unknown" : fallback.riskLevel ?? "Unknown",
    factors: fallback?.riskFactors ?? [], summary: null, guidance: null, disclaimer: null,
    loading: assessmentId !== null, error: null,
  };
  const [view, setView] = useState<RiskView>(initial);
  useEffect(() => {
    setView(initial);
    if (assessmentId === null) return;
    let cancelled = false;
    getRiskDetail(assessmentId).then(detail => {
      if (cancelled) return;
      const score = detail.riskScore;
      const validScore = typeof score === "number" && Number.isFinite(score) && score >= 0 && score <= 100;
      setView({
        score: validScore ? score : null,
        level: validScore ? riskGradeToLevel(detail.riskGrade) : "Unknown",
        factors: [
          ...(detail.factorSummaries ?? []),
          ...(detail.calculation?.task_basis ?? []).map(task =>
            `${task.label}: ML ${task.ml_score}, DL ${task.dl_score}, 가중치 ${task.weight}, 기여 ${task.weighted_points}점 (작업 모델 점수, 사고 확률 아님)`),
        ],
        summary: detail.summary || null, guidance: detail.guidance || null,
        disclaimer: detail.limitations?.length ? detail.limitations.join("\n") : detail.disclaimer || null,
        modelVersion: detail.modelVersion, loading: false, error: null,
        evidenceSummary: detail.calculation?.evidence
          ? `산업 후보: ${detail.calculation.evidence.job.industry_candidate ?? "없음"} (매핑 검토 필요), 산업 통계 연도: ${detail.calculation.evidence.job.evidence_year ?? "없음"}, 재해자수: ${detail.calculation.evidence.job.industry_accident_count ?? "없음"}, 연령 통계 연도: ${detail.calculation.evidence.age_reference.statistic_year}. 재해 건수는 지수에 가산하지 않습니다. ${detail.calculation.explanation?.summary ?? ""}`
          : detail.calculation ? "해당 공고의 통계 참고 근거를 제공할 수 없습니다. 통계는 점수에 반영하지 않았습니다." : null,
      });
    }).catch(error => {
      if (!cancelled) setView(previous => ({ ...previous, loading: false,
        error: `결과를 조회하지 못했습니다: ${error instanceof Error ? error.message : "서버 오류"}` }));
    });
    return () => { cancelled = true; };
  }, [assessmentId]);
  return view;
}

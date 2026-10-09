import type { RiskLevel } from "@/shared/model/assessment";

// 등급별 색상/라벨 (Tailwind 클래스 + 게이지 SVG stroke 색)
export const RISK_LEVEL_STYLE: Record<
  RiskLevel,
  { color: string; bg: string; border: string; text: string; stroke: string }
> = {
  Unknown: { color: "text-gray-500", bg: "bg-gray-50", border: "border-gray-200", text: "미산출", stroke: "#9ca3af" },
  High: { color: "text-red-500", bg: "bg-red-50", border: "border-red-200", text: "참고 지수 높음", stroke: "#ef4444" },
  Medium: { color: "text-amber-500", bg: "bg-amber-50", border: "border-amber-200", text: "참고 지수 보통", stroke: "#f59e0b" },
  Low: { color: "text-green-500", bg: "bg-green-50", border: "border-green-200", text: "참고 지수 낮음", stroke: "#22c55e" },
};

/** 서버 요약이 없을 때 등급별로 보여줄 기본 문구 */
export const DEFAULT_SUMMARY: Record<RiskLevel, string> = {
  Unknown: "아직 점수가 산출되지 않았습니다.",
  High: "참고 지수가 높은 구간입니다. 담당자의 작업 조건과 입력 검토가 필요합니다.",
  Medium: "참고 지수가 중간 구간입니다. 실제 사고 확률을 뜻하지 않습니다.",
  Low: "참고 지수가 낮은 구간입니다. 안전을 보장하는 결과는 아닙니다.",
};

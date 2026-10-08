import type { RiskLevel } from "@/shared/model/assessment";

// 등급별 색상/라벨 (Tailwind 클래스 + 게이지 SVG stroke 색)
export const RISK_LEVEL_STYLE: Record<
  RiskLevel,
  { color: string; bg: string; border: string; text: string; stroke: string }
> = {
  High: { color: "text-red-500", bg: "bg-red-50", border: "border-red-200", text: "고위험", stroke: "#ef4444" },
  Medium: { color: "text-amber-500", bg: "bg-amber-50", border: "border-amber-200", text: "중위험", stroke: "#f59e0b" },
  Low: { color: "text-green-500", bg: "bg-green-50", border: "border-green-200", text: "저위험", stroke: "#22c55e" },
};

/** 서버 요약이 없을 때 등급별로 보여줄 기본 문구 */
export const DEFAULT_SUMMARY: Record<RiskLevel, string> = {
  High: "즉각적인 안전 조치가 필요한 고위험군입니다. 야외 활동 및 고강도 노동을 제한해야 합니다.",
  Medium: "일부 환경에서 위험이 예상됩니다. 주기적인 모니터링과 적절한 휴식이 권장됩니다.",
  Low: "일상적인 활동에 큰 제약이 없는 안전한 상태입니다.",
};

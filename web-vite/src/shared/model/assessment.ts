export type RiskLevel = "Low" | "Medium" | "High";
export type AssessmentStatus = "Draft" | "Analyzed" | "Completed";
export type HealthStatus = "good" | "average" | "bad";

/** 화면에서 쓰는 평가 모델 (API DTO와 분리). */
export interface Assessment {
  id: string;
  date: string;
  applicantName: string;
  age: number;
  healthStatus: string;
  riskScore: number;
  riskLevel: RiskLevel;
  riskFactors: string[];
  status: AssessmentStatus;
}

export const STATUS_OPTIONS: { value: string; label: string }[] = [
  { value: "PENDING_AI", label: "AI 대기" },
  { value: "AI_COMPLETED", label: "분석 완료" },
  { value: "FINALIZED", label: "확정" },
];

const STATUS_FROM_API: Record<string, AssessmentStatus> = {
  PENDING_AI: "Draft",
  AI_COMPLETED: "Analyzed",
  FINALIZED: "Completed",
};

export function statusFromApi(status: string): AssessmentStatus {
  return STATUS_FROM_API[status] ?? "Draft";
}

export function statusToApi(status: AssessmentStatus): string {
  if (status === "Draft") return "PENDING_AI";
  if (status === "Analyzed") return "AI_COMPLETED";
  return "FINALIZED";
}

/** 서버 등급(LOW/MID/HIGH)을 화면 등급으로 변환. 값이 없으면 Medium. */
export function riskGradeToLevel(grade: string | null | undefined): RiskLevel {
  if (grade === "HIGH") return "High";
  if (grade === "LOW") return "Low";
  return "Medium";
}

/** 입력 폼의 건강 상태를 서버 physicalLevel(1~5)로 변환. */
export function healthStatusToPhysicalLevel(status: HealthStatus): number {
  if (status === "good") return 1;
  if (status === "average") return 3;
  return 5;
}

/** 서버 physicalLevel(1~5 문자열)을 표시용 한글 라벨로 변환. */
export function physicalLevelToLabel(physicalLevel: string | null): string {
  if (!physicalLevel) return "정보 없음";
  const level = Number(physicalLevel);
  if (level <= 2) return "좋음";
  if (level >= 4) return "나쁨";
  return "보통";
}

/** URL 파라미터를 평가 ID로 변환. 유효하지 않으면 null. */
export function parseAssessmentId(raw: string | undefined): number | null {
  if (!raw) return null;
  const id = Number(raw);
  return Number.isInteger(id) && id > 0 ? id : null;
}

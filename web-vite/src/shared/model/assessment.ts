// 화면 도메인 모델과 서버 값 <-> 화면 값 변환 규칙. 여러 기능(대시보드/평가/위험도)이 공유한다.
export type RiskLevel = "Low" | "Medium" | "High" | "Unknown";
export type AssessmentStatus = "Draft" | "Analyzed" | "Completed";
export type HealthStatus = "good" | "average" | "bad";

/** 화면에서 쓰는 평가 모델 (API DTO와 분리). */
export interface Assessment {
  id: string;
  date: string;
  applicantName: string;
  age: number;
  healthStatus: string;
  riskScore: number | null;
  riskLevel: RiskLevel;
  riskFactors: string[];
  status: AssessmentStatus;
}

/** 상태 수정 모달의 선택지 (value는 서버 상태 값). */
export const STATUS_OPTIONS: { value: string; label: string }[] = [
  { value: "PENDING_AI", label: "AI 대기" },
  { value: "AI_COMPLETED", label: "분석 완료" },
  { value: "FINALIZED", label: "확정" },
];

// 서버 상태 -> 화면 상태 매핑 테이블
const STATUS_FROM_API: Record<string, AssessmentStatus> = {
  PENDING_AI: "Draft",
  AI_COMPLETED: "Analyzed",
  FINALIZED: "Completed",
};

/** 서버 상태를 화면 상태로 변환. 알 수 없는 값은 Draft. */
export function statusFromApi(status: string): AssessmentStatus {
  return STATUS_FROM_API[status] ?? "Draft";
}

/** 화면 상태를 서버 상태로 변환 (상태 수정 모달 초기값용). */
export function statusToApi(status: AssessmentStatus): string {
  if (status === "Draft") return "PENDING_AI";
  if (status === "Analyzed") return "AI_COMPLETED";
  return "FINALIZED";
}

/** 서버 등급(LOW/MID/HIGH)을 화면 등급으로 변환. 값이 없으면 Unknown. */
export function riskGradeToLevel(grade: string | null | undefined): RiskLevel {
  if (grade === "HIGH") return "High";
  if (grade === "LOW") return "Low";
  if (grade === "MID") return "Medium";
  return "Unknown";
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

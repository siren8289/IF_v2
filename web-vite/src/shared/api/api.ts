// 화면이 Spring을 부르는 함수와, 그 응답의 모양(타입).
// 타입 이름은 달라도, 칸 이름은 Java DTO의 JSON 이름과 같아야 한다.
import { apiRequest } from "./client";

// ---------- 타입 (Spring 응답과 같은 모양) ----------

export interface Job {
  id: number;
  jobTitle: string;
  workplace: string | null;
}

export interface AssessmentRecord {
  id: number;
  applicantName: string;
  age: number;
  jobTitle: string;
  physicalLevel: number;
  status: string;
  riskScore: number | null;
  riskGrade: string | null;
  assessedAt: string | null;
}

/** Spring 페이지 응답. content가 이번 페이지의 행, number는 0부터 시작하는 페이지 번호. */
export interface Page<T> {
  content: T[];
  totalElements: number;
  totalPages: number;
  number: number;
}

export interface Summary {
  totalCount: number;
  highRiskCount: number;
  analyzedCount: number;
}

export interface CreateAssessmentRequest {
  applicantName: string;
  age: number;
  physicalLevel: number;
  chronicDisease: boolean;
  workHourLimit: number;
  jobId: number;
}

export interface AssessmentResult {
  id: number;
  applicantName: string;
  age: number;
  jobTitle: string;
  status: string;
  riskScore: number | null;
  riskGrade: string | null;
  explanation: string | null;
  explanationSource: string | null;
  factors: { name: string; points: number; max: number }[];
  taskScores: { name: string; mlScore: number; dlScore: number }[];
}

// ---------- API 함수 ----------

/** 평가 입력 화면의 직무 선택 목록. */
export function getJobs() {
  return apiRequest<Job[]>("/api/jobs");
}

/** 대시보드 표. page는 0부터. 한 페이지에 20건. */
export function getAssessments(page: number) {
  return apiRequest<Page<AssessmentRecord>>(`/api/assessments?page=${page}&size=20`);
}

/** 대시보드 위쪽 카드 세 개. */
export function getSummary() {
  return apiRequest<Summary>("/api/assessments/summary");
}

/** 평가 등록 + AI 분석. 만들어진 평가 id를 돌려준다. */
export async function createAssessment(body: CreateAssessmentRequest) {
  const res = await apiRequest<{ id: number }>("/api/assessments", {
    method: "POST",
    body: JSON.stringify(body),
  });
  return res.id;
}

/** 결과 화면. id는 주소의 평가 번호. */
export function getResult(id: number) {
  return apiRequest<AssessmentResult>(`/api/assessments/${id}/result`);
}

/** 평가 한 건 삭제. Spring은 본문 없이 204를 돌려준다. */
export function deleteAssessment(id: number) {
  return apiRequest<void>(`/api/assessments/${id}`, { method: "DELETE" });
}

// ---------- 화면 표시용 ----------
// 서버는 LOW/MID/HIGH 코드만 준다. 한글과 색은 화면에서만 붙인다.

export const GRADE_TEXT: Record<string, string> = {
  LOW: "낮음",
  MID: "보통",
  HIGH: "높음",
};

export const GRADE_COLOR: Record<string, string> = {
  LOW: "bg-green-100 text-green-700",
  MID: "bg-yellow-100 text-yellow-700",
  HIGH: "bg-red-100 text-red-700",
};

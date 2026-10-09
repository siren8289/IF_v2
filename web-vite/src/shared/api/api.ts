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

export function getJobs() {
  return apiRequest<Job[]>("/api/jobs");
}

export function getAssessments(page: number) {
  return apiRequest<Page<AssessmentRecord>>(`/api/assessments?page=${page}&size=20`);
}

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

export function getResult(id: number) {
  return apiRequest<AssessmentResult>(`/api/assessments/${id}/result`);
}

export function deleteAssessment(id: number) {
  return apiRequest<void>(`/api/assessments/${id}`, { method: "DELETE" });
}

// ---------- 화면 표시용 ----------

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

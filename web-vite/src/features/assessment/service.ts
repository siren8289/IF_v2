import { createApplicant, createHealthSnapshot } from "@/shared/api/applicants";
import { createAssessment } from "@/shared/api/assessments";
import {
  healthStatusToPhysicalLevel,
  type HealthStatus,
} from "@/shared/model/assessment";

export interface NewAssessmentInput {
  applicantName: string;
  age: number;
  healthStatus: HealthStatus;
  jobId: number;
}

/** 신청자 -> 건강 스냅샷 -> 평가 순으로 등록하고 생성된 평가 ID를 반환한다. */
export async function registerAssessment(input: NewAssessmentInput): Promise<number> {
  const applicant = await createApplicant({
    displayName: input.applicantName,
    age: input.age,
  });
  const health = await createHealthSnapshot(applicant.id, {
    physicalLevel: healthStatusToPhysicalLevel(input.healthStatus),
    chronicDiseaseFlag: false,
    workHourLimit: 8,
  });
  const created = await createAssessment(applicant.id, {
    jobId: input.jobId,
    healthId: health.id,
  });
  return created.id;
}

export interface AssessmentFormValues {
  applicantName: string;
  age: string;
  healthStatus: HealthStatus;
  jobId: number | "";
}

export function validateAssessmentForm(values: AssessmentFormValues): Record<string, string> {
  const errors: Record<string, string> = {};
  if (!values.applicantName) errors.applicantName = "이름을 입력해주세요";
  if (!values.age || isNaN(Number(values.age))) errors.age = "유효한 연령을 입력해주세요";
  if (!values.jobId) errors.job = "직무를 선택해주세요";
  return errors;
}

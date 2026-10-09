import { createApplicant, createHealthSnapshot } from "@/shared/api/applicants";
import { createAssessment } from "@/shared/api/assessments";
import {
  healthStatusToPhysicalLevel,
  type HealthStatus,
} from "@/shared/model/assessment";

/** 등록 요청에 필요한 값(검증 완료 후 형태). */
export interface NewAssessmentInput {
  applicantName: string;
  age: number;
  healthStatus: HealthStatus;
  jobId: number;
  chronicDiseaseFlag: boolean;
  workHourLimit: number;
}

/** 신청자 -> 건강 스냅샷 -> 평가 순으로 등록하고 생성된 평가 ID를 반환한다. */
export async function registerAssessment(input: NewAssessmentInput): Promise<number> {
  // 단일 트랜잭션 API가 아니므로 앞 단계의 id를 다음 단계 요청에 이어서 쓴다.
  const applicant = await createApplicant({
    displayName: input.applicantName,
    age: input.age,
  });
  const health = await createHealthSnapshot(applicant.id, {
    physicalLevel: healthStatusToPhysicalLevel(input.healthStatus),
    chronicDiseaseFlag: input.chronicDiseaseFlag,
    workHourLimit: input.workHourLimit,
  });
  const created = await createAssessment(applicant.id, {
    jobId: input.jobId,
    healthId: health.id,
  });
  return created.id;
}

/** 폼 입력값(문자열 위주). 등록 요청 전 검증 대상이다. */
export interface AssessmentFormValues {
  applicantName: string;
  age: string;
  healthStatus: HealthStatus;
  jobId: number | "";
  chronicDisease: "" | "yes" | "no";
  workHourLimit: string;
}

export function validateAssessmentForm(values: AssessmentFormValues): Record<string, string> {
  const errors: Record<string, string> = {};
  if (!values.applicantName) errors.applicantName = "이름을 입력해주세요";
  if (!Number.isInteger(Number(values.age)) || Number(values.age) < 1 || Number(values.age) > 120) errors.age = "유효한 연령을 입력해주세요";
  if (!values.jobId) errors.job = "직무를 선택해주세요";
  if (!values.chronicDisease) errors.chronicDisease = "만성질환 여부를 선택해주세요";
  if (!Number.isInteger(Number(values.workHourLimit)) || Number(values.workHourLimit) < 1 || Number(values.workHourLimit) > 24) errors.workHourLimit = "근무 가능 시간을 1~24의 정수로 입력해주세요";
  return errors;
}

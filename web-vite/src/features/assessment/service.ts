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
    // 만성질환/근무시간 입력 UI가 없어 기존 동작과 같은 고정값을 보낸다.
    chronicDiseaseFlag: false,
    workHourLimit: 8,
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
}

export function validateAssessmentForm(values: AssessmentFormValues): Record<string, string> {
  const errors: Record<string, string> = {};
  if (!values.applicantName) errors.applicantName = "이름을 입력해주세요";
  if (!values.age || isNaN(Number(values.age))) errors.age = "유효한 연령을 입력해주세요";
  if (!values.jobId) errors.job = "직무를 선택해주세요";
  return errors;
}

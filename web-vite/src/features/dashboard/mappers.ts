import type { AssessmentRecordResponse } from "@/shared/api/types";
import {
  physicalLevelToLabel,
  riskGradeToLevel,
  statusFromApi,
  type Assessment,
} from "@/shared/model/assessment";

/** GET /api/assessments 항목(API DTO)을 화면 모델로 변환한다. */
export function mapRecordToAssessment(record: AssessmentRecordResponse): Assessment {
  return {
    id: String(record.id),
    date: record.assessedAt,
    applicantName: record.applicantName,
    age: record.age,
    healthStatus: physicalLevelToLabel(record.physicalLevel),
    riskScore: record.riskScore ?? null,
    riskLevel: riskGradeToLevel(record.riskGrade),
    riskFactors: [],
    status: statusFromApi(record.status),
  };
}

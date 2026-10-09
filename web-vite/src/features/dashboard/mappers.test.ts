import { mapRecordToAssessment } from "./mappers";

// 대시보드 목록: API 레코드 -> 화면 모델 변환 확인한다.
describe("mapRecordToAssessment", () => {
  it("API 레코드를 화면 모델로 변환한다", () => {
    expect(
      mapRecordToAssessment({
        id: 7,
        applicantName: "홍길동",
        age: 70,
        jobTitle: "경비",
        physicalLevel: "5",
        status: "AI_COMPLETED",
        riskScore: 81,
        riskGrade: "HIGH",
        assessedAt: "2026-01-02T00:00:00",
      })
    ).toEqual({
      id: "7",
      date: "2026-01-02T00:00:00",
      applicantName: "홍길동",
      age: 70,
      healthStatus: "나쁨",
      riskScore: 81,
      riskLevel: "High",
      riskFactors: [],
      status: "Analyzed",
    });
  });

  it("점수/등급이 없으면 미산출로 표시한다", () => {
    const result = mapRecordToAssessment({
      id: 1,
      applicantName: "김",
      age: 66,
      jobTitle: "x",
      physicalLevel: null,
      status: "PENDING_AI",
      riskScore: null,
      riskGrade: null,
      assessedAt: "2026-01-02T00:00:00",
    });
    expect(result).toMatchObject({ riskScore: null, riskLevel: "Unknown", healthStatus: "정보 없음", status: "Draft" });
  });
});

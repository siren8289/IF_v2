import {
  healthStatusToPhysicalLevel,
  parseAssessmentId,
  physicalLevelToLabel,
  riskGradeToLevel,
  statusFromApi,
  statusToApi,
} from "./assessment";

describe("assessment model", () => {
  it("서버 등급을 화면 등급으로 변환하고 값이 없으면 Medium", () => {
    expect(riskGradeToLevel("HIGH")).toBe("High");
    expect(riskGradeToLevel("MID")).toBe("Medium");
    expect(riskGradeToLevel("LOW")).toBe("Low");
    expect(riskGradeToLevel(null)).toBe("Medium");
  });

  it("상태를 서버 값과 상호 변환", () => {
    expect(statusFromApi("PENDING_AI")).toBe("Draft");
    expect(statusFromApi("AI_COMPLETED")).toBe("Analyzed");
    expect(statusFromApi("FINALIZED")).toBe("Completed");
    expect(statusFromApi("UNKNOWN")).toBe("Draft");
    expect(statusToApi("Draft")).toBe("PENDING_AI");
    expect(statusToApi("Analyzed")).toBe("AI_COMPLETED");
    expect(statusToApi("Completed")).toBe("FINALIZED");
  });

  it("건강 상태를 physicalLevel 1/3/5로 변환", () => {
    expect(healthStatusToPhysicalLevel("good")).toBe(1);
    expect(healthStatusToPhysicalLevel("average")).toBe(3);
    expect(healthStatusToPhysicalLevel("bad")).toBe(5);
  });

  it("physicalLevel을 한글 라벨로 변환", () => {
    expect(physicalLevelToLabel(null)).toBe("정보 없음");
    expect(physicalLevelToLabel("1")).toBe("좋음");
    expect(physicalLevelToLabel("3")).toBe("보통");
    expect(physicalLevelToLabel("5")).toBe("나쁨");
  });

  it("URL 파라미터에서 유효한 ID만 추출", () => {
    expect(parseAssessmentId("12")).toBe(12);
    expect(parseAssessmentId("abc")).toBeNull();
    expect(parseAssessmentId("0")).toBeNull();
    expect(parseAssessmentId(undefined)).toBeNull();
  });
});

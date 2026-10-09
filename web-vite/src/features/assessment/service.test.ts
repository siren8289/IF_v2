import { registerAssessment, validateAssessmentForm } from "./service";
import { callsTo, mockApi } from "@/test/mockApi";

afterEach(() => vi.unstubAllGlobals());

// 평가 등록이 신청자 -> 건강 스냅샷 -> 평가 순서로, 앞 단계 ID를 이어서 쓰는지 확인한다.
describe("registerAssessment", () => {
  it("신청자 -> 건강 스냅샷 -> 평가 순으로 호출하고 평가 ID를 반환한다", async () => {
    const fetchMock = mockApi({
      "POST /api/applicants": { json: { id: 10 } },
      "POST /api/applicants/10/health-snapshots": { json: { id: 20 } },
      "POST /api/applicants/10/assessments": { json: { id: 30 } },
    });

    const id = await registerAssessment({ applicantName: "홍길동", age: 68, healthStatus: "bad", jobId: 4, chronicDiseaseFlag: true, workHourLimit: 6 });

    expect(id).toBe(30);
    expect(fetchMock.mock.calls.map(([url]) => new URL(String(url)).pathname)).toEqual([
      "/api/applicants",
      "/api/applicants/10/health-snapshots",
      "/api/applicants/10/assessments",
    ]);
    expect(JSON.parse(String(callsTo(fetchMock, "POST /api/applicants")[0][1]?.body))).toEqual({
      displayName: "홍길동",
      age: 68,
    });
    expect(JSON.parse(String(fetchMock.mock.calls[1][1]?.body))).toEqual({
      physicalLevel: 5,
      chronicDiseaseFlag: true,
      workHourLimit: 6,
    });
    expect(JSON.parse(String(fetchMock.mock.calls[2][1]?.body))).toEqual({ jobId: 4, healthId: 20 });
  });
});

describe("validateAssessmentForm", () => {
  it("필수 값이 비어 있으면 오류를 반환한다", () => {
    expect(validateAssessmentForm({ applicantName: "", age: "", healthStatus: "average", jobId: "", chronicDisease: "", workHourLimit: "" })).toEqual({
      applicantName: "이름을 입력해주세요",
      age: "유효한 연령을 입력해주세요",
      job: "직무를 선택해주세요",
      chronicDisease: "만성질환 여부를 선택해주세요",
      workHourLimit: "근무 가능 시간을 1~24의 정수로 입력해주세요",
    });
  });

  it("모두 입력하면 오류가 없다", () => {
    expect(validateAssessmentForm({ applicantName: "홍", age: "65", healthStatus: "good", jobId: 1, chronicDisease: "no", workHourLimit: "8" })).toEqual({});
  });
});

import { apiRequest } from "./client";
import { createAssessment, deleteAssessment } from "./api";
import { mockApi, callsTo } from "@/test/mockApi";

afterEach(() => vi.unstubAllGlobals());

describe("apiRequest", () => {
  it("기본 주소(localhost:8080)로 JSON 요청을 보낸다", async () => {
    const fetchMock = mockApi({ "GET /api/jobs": { json: [{ id: 1 }] } });
    await expect(apiRequest("/api/jobs")).resolves.toEqual([{ id: 1 }]);
    expect(String(fetchMock.mock.calls[0][0])).toBe("http://localhost:8080/api/jobs");
  });

  it("실패 응답은 서버 메시지가 포함된 Error로 던진다", async () => {
    mockApi({ "GET /api/jobs": { status: 502, json: { message: "AI 서버 호출에 실패했습니다." } } });
    await expect(apiRequest("/api/jobs")).rejects.toThrow("API 502: AI 서버 호출에 실패했습니다.");
  });

  it("204 응답은 undefined를 반환한다", async () => {
    mockApi({ "DELETE /api/assessments/3": { status: 204 } });
    await expect(deleteAssessment(3)).resolves.toBeUndefined();
  });

  it("평가 등록은 POST 한 번으로 id를 받는다", async () => {
    const fetchMock = mockApi({ "POST /api/assessments": { status: 201, json: { id: 7 } } });
    const id = await createAssessment({
      applicantName: "홍길동", age: 70, physicalLevel: 3,
      chronicDisease: true, workHourLimit: 6, jobId: 1,
    });
    expect(id).toBe(7);
    expect(callsTo(fetchMock, "POST /api/assessments")).toHaveLength(1);
  });
});

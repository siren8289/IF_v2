import { apiRequest } from "./client";
import { listAssessmentRecords, updateAssessment } from "./assessments";
import { mockApi } from "@/test/mockApi";

// fetch를 목으로 바꿔 API Client의 요청 형식과 오류 처리를 확인한다.
afterEach(() => vi.unstubAllGlobals());

describe("apiRequest", () => {
  it("기본 주소(localhost:8080)로 JSON 요청을 보낸다", async () => {
    const fetchMock = mockApi({ "GET /api/jobs": { json: [{ id: 1 }] } });
    await expect(apiRequest("/api/jobs")).resolves.toEqual([{ id: 1 }]);
    expect(String(fetchMock.mock.calls[0][0])).toBe("http://localhost:8080/api/jobs");
    expect(fetchMock.mock.calls[0][1]?.headers).toMatchObject({ "Content-Type": "application/json" });
  });

  it("실패 응답은 상태 코드가 포함된 Error로 던진다", async () => {
    mockApi({ "GET /api/jobs": { status: 500 } });
    await expect(apiRequest("/api/jobs")).rejects.toThrow("API 500");
  });

  it("204 응답은 undefined를 반환한다", async () => {
    mockApi({ "PATCH /api/assessments/3": { status: 204 } });
    await expect(updateAssessment(3, { status: "FINALIZED" })).resolves.toBeUndefined();
  });
});

// Spring API 계약(엔드포인트 형식)이 바뀌지 않았는지 확인한다.
describe("assessments API 계약", () => {
  it("목록은 page/size/sort 쿼리를 유지한다", async () => {
    const fetchMock = mockApi({
      "GET /api/assessments": { json: { content: [], totalElements: 0, totalPages: 0, number: 0, size: 20 } },
    });
    await listAssessmentRecords(2, 20);
    expect(String(fetchMock.mock.calls[0][0])).toContain("?page=2&size=20&sort=assessedAt,desc");
  });
});

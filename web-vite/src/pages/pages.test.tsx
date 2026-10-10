import { screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { renderApp } from "@/test/renderApp";
import { callsTo, mockApi } from "@/test/mockApi";

afterEach(() => vi.unstubAllGlobals());

const RESULT = {
  id: 7,
  applicantName: "홍길동",
  age: 70,
  jobTitle: "야간 경비원",
  status: "AI_COMPLETED",
  riskScore: 65,
  riskGrade: "HIGH",
  explanation: "야간 근무 특성이 강합니다.",
  explanationSource: "basic",
  factors: [{ name: "나이", points: 6.67, max: 20 }],
  taskScores: [{ name: "야간 근무", mlScore: 0.99, dlScore: 0.98 }],
};

describe("화면", () => {
  it("처음 주소는 대시보드로 이동하고 요약과 목록을 보여준다", async () => {
    mockApi({
      "GET /api/assessments": {
        json: {
          content: [{ id: 7, applicantName: "홍길동", age: 70, jobTitle: "야간 경비원", physicalLevel: 3,
            status: "AI_COMPLETED", riskScore: 65, riskGrade: "HIGH", assessedAt: null }],
          totalElements: 1, totalPages: 1, number: 0,
        },
      },
      "GET /api/assessments/summary": { json: { totalCount: 1, highRiskCount: 1, analyzedCount: 1 } },
    });

    const router = renderApp("/");

    expect(await screen.findByText("홍길동")).toBeInTheDocument();
    expect(router.state.location.pathname).toBe("/dashboard");
    expect(screen.getByText("65점")).toBeInTheDocument();
  });

  it("평가 입력 후 POST 한 번 하고 결과 화면으로 이동한다", async () => {
    const fetchMock = mockApi({
      "GET /api/jobs": { json: [{ id: 1, jobTitle: "야간 경비원", workplace: "서울" }] },
      "POST /api/assessments": { status: 201, json: { id: 7 } },
      "GET /api/assessments/7/result": { json: RESULT },
    });
    const user = userEvent.setup();
    const router = renderApp("/assessments/new");

    await user.type(screen.getByLabelText("이름"), "홍길동");
    await user.type(screen.getByLabelText("연령"), "70");
    await user.selectOptions(screen.getByLabelText("만성질환"), "yes");
    await screen.findByRole("option", { name: "야간 경비원 (서울)" });
    await user.selectOptions(screen.getByLabelText("직무"), "1");
    await user.click(screen.getByRole("button", { name: "위험도 분석 시작" }));

    await waitFor(() => expect(router.state.location.pathname).toBe("/assessments/7/result"));
    const [, init] = callsTo(fetchMock, "POST /api/assessments")[0];
    expect(JSON.parse(String(init?.body))).toEqual({
      applicantName: "홍길동", age: 70, physicalLevel: 3,
      chronicDisease: true, workHourLimit: 8, jobId: 1,
    });
    expect(await screen.findByText("65점")).toBeInTheDocument();
    expect(screen.getByText("야간 근무 특성이 강합니다.")).toBeInTheDocument();
  });

  it("입력값이 잘못되면 API를 호출하지 않는다", async () => {
    const fetchMock = mockApi({ "GET /api/jobs": { json: [] } });
    const user = userEvent.setup();
    renderApp("/assessments/new");

    await user.click(screen.getByRole("button", { name: "위험도 분석 시작" }));

    expect(await screen.findByRole("alert")).toHaveTextContent("이름을 입력해주세요.");
    expect(callsTo(fetchMock, "POST /api/assessments")).toHaveLength(0);
  });
});

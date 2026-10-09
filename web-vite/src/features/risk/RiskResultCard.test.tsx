import { render, screen, waitFor } from "@testing-library/react";
import { RiskResultCard } from "./components/RiskResultCard";
import { useRiskDetail } from "./useRiskDetail";
import { mockApi } from "@/test/mockApi";

afterEach(() => vi.unstubAllGlobals());

function Result({ id = 1 }: { id?: number }) { return <RiskResultCard view={useRiskDetail(id)} />; }

it("null을 0점으로 바꾸지 않고 미산출로 표시한다", async () => {
  mockApi({ "GET /api/assessments/1/risk-detail": { json: { riskScore: null, riskGrade: null } } });
  render(<Result />);
  await waitFor(() => expect(screen.queryByRole("status")).not.toBeInTheDocument());
  expect(screen.getAllByText("미산출").length).toBeGreaterThan(0);
  expect(screen.queryByText("0점")).not.toBeInTheDocument();
});

it("실제 0점과 산출 근거를 표시한다", async () => {
  mockApi({ "GET /api/assessments/1/risk-detail": { json: {
    riskScore: 0, riskGrade: "LOW", summary: "참고 지수", factorSummaries: ["연령 정책: 0점"],
    limitations: ["사고 확률이 아닙니다."], modelVersion: "PERSONAL_INDEX_V1",
  } } });
  render(<Result />);
  expect(await screen.findByText("0점")).toBeInTheDocument();
  expect(screen.getByText("연령 정책: 0점")).toBeInTheDocument();
  expect(screen.getByText("사고 확률이 아닙니다.")).toBeInTheDocument();
});

it("조회 실패를 알리고 임의 점수를 표시하지 않는다", async () => {
  mockApi({ "GET /api/assessments/1/risk-detail": { status: 502 } });
  render(<Result />);
  expect(await screen.findByRole("alert")).toHaveTextContent("결과를 조회하지 못했습니다");
  expect(screen.queryByText("0점")).not.toBeInTheDocument();
});

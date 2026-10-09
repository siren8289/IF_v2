import { StrictMode, type ReactNode } from "react";
import { renderHook, waitFor } from "@testing-library/react";
import { useComputeRisk } from "./useComputeRisk";
import { mockApi } from "@/test/mockApi";

afterEach(() => vi.unstubAllGlobals());

it("StrictMode에서도 계산 요청은 한 번만 하고 성공을 알린다", async () => {
  const fetchMock = mockApi({ "POST /api/assessments/1/compute-risk": { status: 204 } });
  const settled = vi.fn();
  renderHook(() => useComputeRisk(1, settled), {
    wrapper: ({ children }: { children: ReactNode }) => <StrictMode>{children}</StrictMode>,
  });
  await waitFor(() => expect(settled).toHaveBeenCalledWith(null));
  expect(fetchMock).toHaveBeenCalledTimes(1);
  expect(settled).toHaveBeenCalledTimes(1);
});

it("실패를 성공처럼 숨기지 않고 전달한다", async () => {
  mockApi({ "POST /api/assessments/1/compute-risk": { status: 502 } });
  const settled = vi.fn();
  renderHook(() => useComputeRisk(1, settled));
  await waitFor(() => expect(settled).toHaveBeenCalledWith(expect.stringContaining("API 502")));
});

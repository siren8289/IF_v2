import { test, expect } from "@playwright/test";

const apiURL = process.env.E2E_API_URL || "http://127.0.0.1:18080";

test("개인 입력 → 실제 ML/DL 지수 → 저장 결과 → 대시보드", async ({ page, request }, testInfo) => {
  let assessmentId: number | undefined;
  try {
    await page.goto("/login");
    await page.getByRole("button", { name: "로그인", exact: true }).click();
    await expect(page).toHaveURL(/\/dashboard$/);
    await page.getByRole("button", { name: "새로운 평가 시작" }).click();
    await page.getByLabel("이름", { exact: true }).fill("개인 지수 E2E 테스트");
    await page.getByLabel("연령", { exact: true }).fill("70");
    await page.getByRole("button", { name: "보통", exact: true }).click();
    await page.getByLabel("만성질환 여부 (자기보고)").selectOption("yes");
    await page.getByLabel("하루 근무 가능 시간").fill("6");
    await expect(page.getByLabel("검토 대상 직무").locator("option").nth(1)).toBeAttached();
    await page.getByLabel("검토 대상 직무").selectOption({ index: 1 });
    const computed = page.waitForResponse(response => /\/compute-risk$/.test(response.url()) && response.request().method() === "POST");
    await page.getByRole("button", { name: "위험도 분석 시작" }).click();
    const computeResponse = await computed;
    assessmentId = Number(computeResponse.url().match(/assessments\/(\d+)/)?.[1]);
    expect(computeResponse.ok(), `compute-risk HTTP ${computeResponse.status()}`).toBeTruthy();
    await expect(page).toHaveURL(new RegExp(`/assessments/${assessmentId}/result$`));
    const detailResponse = await request.get(`${apiURL}/api/assessments/${assessmentId}/risk-detail`);
    expect(detailResponse.ok()).toBeTruthy();
    const detail = await detailResponse.json();
    expect(detail.riskScore).toBeGreaterThanOrEqual(0);
    expect(detail.riskScore).toBeLessThanOrEqual(100);
    expect(detail.scoreType).toBe("REFERENCE_INDEX");
    expect(detail.calculation.risk_probability).toBeNull();
    expect(detail.calculation.inputs.chronic_disease).toBe(true);
    expect(detail.calculation.inputs.work_hour_limit).toBe(6);
    await expect(page.getByText(`${detail.riskScore}점`, { exact: true })).toBeVisible();
    await expect(page.getByText(/산출 버전: PERSONAL_INDEX_V1/)).toBeVisible();
    await expect(page.getByText(/가중치와 등급 경계는 실증 검증 전/)).toBeVisible();
    await expect(page.getByText("산업·연령 통계 참고 근거 (점수 가산 없음)")).toBeVisible();
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.screenshot({ path: testInfo.outputPath("personal-risk.png"), fullPage: true });
    await page.reload();
    await expect(page.getByText(`${detail.riskScore}점`, { exact: true })).toBeVisible();
    const records = await (await request.get(`${apiURL}/api/assessments?size=100`)).json();
    const saved = records.content.find((item: { id: number }) => item.id === assessmentId);
    expect(saved.status).toBe("AI_COMPLETED");
    expect(saved.riskScore).toBe(detail.riskScore);
    expect(saved.riskGrade).toBe(detail.riskGrade);
    await page.getByRole("button", { name: "목록으로 돌아가기" }).click();
    await expect(page.getByText("개인 지수 E2E 테스트", { exact: true })).toBeVisible();
  } finally {
    if (assessmentId) {
      const deleted = await request.delete(`${apiURL}/api/assessments/${assessmentId}`);
      expect(deleted.ok()).toBeTruthy();
    }
  }
});

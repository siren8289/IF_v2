import { test, expect } from "@playwright/test";

const apiURL = process.env.E2E_API_URL || "http://127.0.0.1:18080";

test("평가 입력 → AI 분석 결과 → 대시보드", async ({ page, request }) => {
  let assessmentId: number | undefined;
  try {
    await page.goto("/");
    await expect(page).toHaveURL(/\/dashboard$/);
    await page.getByRole("button", { name: "새로운 평가 시작" }).click();

    await page.getByLabel("이름").fill("E2E 테스트");
    await page.getByLabel("연령").fill("70");
    await page.getByLabel("만성질환").selectOption("yes");
    await page.getByLabel("하루 근무 가능 시간").fill("6");
    await expect(page.getByLabel("직무").locator("option").nth(1)).toBeAttached();
    await page.getByLabel("직무").selectOption({ index: 1 });

    const created = page.waitForResponse(
      (res) => res.url().endsWith("/api/assessments") && res.request().method() === "POST"
    );
    await page.getByRole("button", { name: "위험도 분석 시작" }).click();
    const createResponse = await created;
    expect(createResponse.status()).toBe(201);
    assessmentId = (await createResponse.json()).id;

    await expect(page).toHaveURL(new RegExp(`/assessments/${assessmentId}/result$`));
    const result = await (await request.get(`${apiURL}/api/assessments/${assessmentId}/result`)).json();
    expect(result.riskScore).toBeGreaterThanOrEqual(0);
    expect(result.riskScore).toBeLessThanOrEqual(100);
    expect(result.taskScores.length).toBeGreaterThan(0);
    await expect(page.getByText(`${result.riskScore}점`, { exact: true })).toBeVisible();

    await page.getByRole("button", { name: "목록으로 돌아가기" }).click();
    await expect(page.getByText("E2E 테스트", { exact: true })).toBeVisible();
  } finally {
    if (assessmentId) {
      const deleted = await request.delete(`${apiURL}/api/assessments/${assessmentId}`);
      expect(deleted.ok()).toBeTruthy();
    }
  }
});

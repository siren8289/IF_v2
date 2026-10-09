import { defineConfig } from "@playwright/test";

const baseURL = process.env.E2E_BASE_URL || "http://localhost:3000";
const apiURL = process.env.E2E_API_URL || "http://127.0.0.1:18080";
for (const url of [baseURL, apiURL]) {
  if (!["localhost", "127.0.0.1"].includes(new URL(url).hostname)) {
    throw new Error("E2E는 로컬 테스트 서버에서만 실행할 수 있습니다.");
  }
}

export default defineConfig({
  testDir: "./e2e", workers: 1, timeout: 60000,
  reporter: [["list"], ["html", { open: "never" }]],
  use: { baseURL, channel: process.env.E2E_BROWSER || "chrome", trace: "retain-on-failure" },
  webServer: process.env.E2E_BASE_URL ? undefined : {
    command: "npm run dev -- --host 127.0.0.1", url: baseURL, reuseExistingServer: false,
    env: { VITE_API_URL: apiURL },
  },
});

// 개발 서버, 경로 별칭, 테스트 설정.
// "@" 로 시작하는 import는 src 폴더를 가리킨다. 예: import x from "@/pages/..."
// 개발 서버는 3000번. strictPort라서 3000이 이미 쓰이면 다른 번호로 바꾸지 않고 실패한다.
import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: { "@": fileURLToPath(new URL("./src", import.meta.url)) },
  },
  server: { port: 3000, strictPort: true },
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["./src/test/setup.ts"],
    css: false,
  },
});

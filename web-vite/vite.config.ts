import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: { "@": fileURLToPath(new URL("./src", import.meta.url)) },
  },
  // Spring CORS가 localhost:3000만 허용하므로 기존 Next.js와 같은 포트를 유지한다.
  server: { port: 3000, strictPort: true },
  preview: { port: 3000, strictPort: true },
  // vitest는 jsdom 환경에서 실행하고 CSS는 처리하지 않는다.
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["./src/test/setup.ts"],
    css: false,
  },
});

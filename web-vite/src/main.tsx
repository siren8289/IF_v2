import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import { Providers } from "@/app/providers";
import { router } from "@/app/router";
import "@/styles/index.css";

// 앱 진입점: Next의 layout.tsx/page.tsx를 대체한다. Provider -> Router -> Page 순으로 감싼다.
createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Providers>
      <RouterProvider router={router} />
    </Providers>
  </StrictMode>
);

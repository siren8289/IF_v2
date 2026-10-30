// 브라우저가 이 파일을 가장 먼저 실행한다.
// index.html 안의 <div id="root"> 를 찾아 React 화면을 그 안에 붙인다.
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import { router } from "@/app/router";
import "@/styles/index.css";

// StrictMode는 개발 중에 문제를 더 일찍 보여 주려고 렌더를 한 번 더 한다.
// RouterProvider는 주소(URL)에 따라 어떤 페이지를 그릴지 결정한다.
createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);

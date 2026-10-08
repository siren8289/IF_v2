import { render } from "@testing-library/react";
import { RouterProvider, createMemoryRouter } from "react-router-dom";
import { Providers } from "@/app/providers";
import { routes } from "@/app/routes";

// 실제 라우트 정의를 메모리 라우터로 렌더링한다. loggedIn이면 로그인된 세션으로 시작한다.
export function renderApp(path: string, { loggedIn = false } = {}) {
  if (loggedIn) sessionStorage.setItem("if_session", "1");
  const router = createMemoryRouter(routes, { initialEntries: [path] });
  render(
    <Providers>
      <RouterProvider router={router} />
    </Providers>
  );
  return router;
}

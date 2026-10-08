import { render } from "@testing-library/react";
import { RouterProvider, createMemoryRouter } from "react-router-dom";
import { Providers } from "@/app/providers";
import { routes } from "@/app/routes";

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

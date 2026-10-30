// 주소창의 경로와 화면 컴포넌트를 연결하는 라우터.
// 실제 경로 목록은 routes.tsx에 있다. 이 파일은 그 목록으로 라우터 객체를 만든다.
import { createBrowserRouter } from "react-router-dom";
import { routes } from "./routes";

export const router = createBrowserRouter(routes);

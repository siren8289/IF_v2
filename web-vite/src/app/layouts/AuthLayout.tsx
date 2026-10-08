import { Outlet } from "react-router-dom";
import { PageFrame } from "./PageFrame";

/** 로그인/회원가입: 헤더 없음 */
export function AuthLayout() {
  return (
    <PageFrame>
      <Outlet />
    </PageFrame>
  );
}

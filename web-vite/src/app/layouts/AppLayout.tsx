// 모든 페이지가 공유하는 겉틀. 위에는 제목 링크, 아래에는 그 주소의 페이지.
import { Link, Outlet } from "react-router-dom";
import { PageFrame } from "./PageFrame";

export function AppLayout() {
  // 로고를 누르면 항상 대시보드로 돌아간다.
  const header = (
    <header className="bg-white border-b border-gray-200 h-16 flex items-center px-6 sticky top-0 z-20 shadow-sm">
      <div className="w-full max-w-7xl mx-auto flex items-center">
        <Link to="/dashboard" className="font-bold text-xl text-[#2F8F6B]">
          If - 고령자 위험도 판단 시스템
        </Link>
      </div>
    </header>
  );

  return (
    <PageFrame header={header}>
      {/* Outlet: routes.tsx에서 고른 자식 페이지가 이 자리에 들어온다. */}
      <Outlet />
    </PageFrame>
  );
}

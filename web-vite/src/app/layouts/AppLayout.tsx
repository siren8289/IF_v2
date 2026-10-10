import { Link, Outlet } from "react-router-dom";
import { PageFrame } from "./PageFrame";

export function AppLayout() {
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
      <Outlet />
    </PageFrame>
  );
}

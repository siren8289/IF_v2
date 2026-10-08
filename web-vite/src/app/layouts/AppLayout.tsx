import { Outlet, useLocation, useNavigate } from "react-router-dom";
import { ArrowLeft, LogOut } from "lucide-react";
import { useAuth } from "@/features/auth/AuthContext";
import { PageFrame } from "./PageFrame";

const TITLE = "If - 고령자 위험도 판단 시스템";

/** 로그인 이후 화면: 상단 헤더(대시보드는 로그아웃, 그 외는 뒤로가기) + 본문 */
export function AppLayout() {
  const { logout } = useAuth();
  const navigate = useNavigate();
  const isDashboard = useLocation().pathname === "/dashboard";

  const handleBack = () => {
    if (isDashboard) {
      logout();
      navigate("/login");
    } else {
      navigate("/dashboard");
    }
  };

  const header = (
    <header className="bg-white border-b border-gray-200 h-16 flex items-center px-6 sticky top-0 z-20 shadow-sm">
      <div className="w-full max-w-7xl mx-auto flex items-center">
        <button
          type="button"
          onClick={handleBack}
          className="p-2 -ml-2 rounded-full hover:bg-gray-100 transition-colors text-slate-600 mr-4"
          aria-label={isDashboard ? "Logout" : "Go back"}
        >
          {isDashboard ? <LogOut size={20} /> : <ArrowLeft size={20} />}
        </button>
        <h1 className="font-bold text-xl text-[#2F8F6B]">{TITLE}</h1>
      </div>
    </header>
  );

  return (
    <PageFrame header={header}>
      <Outlet />
    </PageFrame>
  );
}

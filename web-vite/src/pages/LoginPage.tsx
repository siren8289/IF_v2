import { useNavigate } from "react-router-dom";
import { LoginForm } from "@/features/auth/components/LoginForm";

// 라우트 /login: 로그인 성공 시 대시보드로 이동한다. 화면/로직은 features/auth에 있다.
export default function LoginPage() {
  const navigate = useNavigate();
  return <LoginForm onSuccess={() => navigate("/dashboard")} />;
}

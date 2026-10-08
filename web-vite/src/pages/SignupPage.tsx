import { useNavigate } from "react-router-dom";
import { SignupForm } from "@/features/auth/components/SignupForm";

// 라우트 /signup: 가입 완료 후 로그인 화면으로 이동한다.
export default function SignupPage() {
  const navigate = useNavigate();
  return <SignupForm onSuccess={() => navigate("/login")} />;
}

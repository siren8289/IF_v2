import { useNavigate } from "react-router-dom";
import { LoginForm } from "@/features/auth/components/LoginForm";

export default function LoginPage() {
  const navigate = useNavigate();
  return <LoginForm onSuccess={() => navigate("/dashboard")} />;
}

import { useNavigate } from "react-router-dom";
import { SignupForm } from "@/features/auth/components/SignupForm";

export default function SignupPage() {
  const navigate = useNavigate();
  return <SignupForm onSuccess={() => navigate("/login")} />;
}

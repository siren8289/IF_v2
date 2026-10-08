import { useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { ArrowLeft, ShieldCheck } from "lucide-react";
import { toast } from "sonner";
import { registerUser } from "../authStorage";
import { validateSignup, type SignupFormValues } from "../validateSignup";
import { AuthShell } from "./AuthShell";

interface SignupFormProps {
  onSuccess: () => void;
}

const inputClass = (hasError: boolean) =>
  `w-full px-5 py-3.5 bg-gray-50 border rounded-xl focus:outline-none focus:ring-2 focus:ring-[#2F8F6B] transition-all ${hasError ? "border-red-500" : "border-gray-200"}`;

export function SignupForm({ onSuccess }: SignupFormProps) {
  const [values, setValues] = useState<SignupFormValues>({
    id: "",
    password: "",
    confirmPassword: "",
    name: "",
    department: "",
  });
  const [errors, setErrors] = useState<Record<string, string>>({});

  const set = (key: keyof SignupFormValues) => (e: React.ChangeEvent<HTMLInputElement>) =>
    setValues({ ...values, [key]: e.target.value });

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    const nextErrors = validateSignup(values);
    setErrors(nextErrors);
    if (Object.keys(nextErrors).length > 0) return;

    const result = registerUser({
      id: values.id,
      password: values.password,
      name: values.name,
      department: values.department,
    });
    if (result === "duplicate") {
      setErrors({ id: "이미 존재하는 아이디입니다" });
      return;
    }
    toast.success("회원가입이 완료되었습니다.");
    onSuccess();
  };

  return (
    <AuthShell
      heightClass="md:h-[750px]"
      enterFrom={{ x: 20 }}
      panelClassName="w-full md:w-1/2 p-8 md:p-12 flex flex-col justify-center relative"
      title={<h2 className="text-4xl font-bold mb-6">관리자 계정 생성</h2>}
      description={
        <p className="text-white/90 text-lg leading-relaxed">
          If 시스템의 관리자가 되어<br />
          고령자 안전 관리에 동참해주세요.
        </p>
      }
      badges={
        <div className="flex items-center gap-2 bg-white/10 px-4 py-2 rounded-lg backdrop-blur-sm">
          <ShieldCheck size={20} />
          <span className="text-sm font-medium">안전성 평가</span>
        </div>
      }
    >
      <Link
        to="/login"
        className="absolute top-8 left-8 flex items-center text-gray-400 hover:text-gray-800 transition-colors group"
      >
        <ArrowLeft size={20} className="mr-1 group-hover:-translate-x-1 transition-transform" />
        로그인으로 돌아가기
      </Link>

      <div className="max-w-md mx-auto w-full mt-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">회원가입</h1>
          <p className="text-gray-500">새로운 관리자 정보를 입력해주세요.</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="signup-id" className="block text-sm font-bold text-gray-700 mb-2">아이디</label>
            <input id="signup-id" type="text" value={values.id} onChange={set("id")} className={inputClass(!!errors.id)} placeholder="아이디를 입력하세요" />
            {errors.id && <p className="text-red-500 text-xs mt-1">{errors.id}</p>}
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label htmlFor="signup-name" className="block text-sm font-bold text-gray-700 mb-2">이름</label>
              <input id="signup-name" type="text" value={values.name} onChange={set("name")} className={inputClass(!!errors.name)} placeholder="홍길동" />
              {errors.name && <p className="text-red-500 text-xs mt-1">{errors.name}</p>}
            </div>
            <div>
              <label htmlFor="signup-department" className="block text-sm font-bold text-gray-700 mb-2">부서 (선택)</label>
              <input id="signup-department" type="text" value={values.department} onChange={set("department")} className={inputClass(false)} placeholder="복지팀" />
            </div>
          </div>

          <div>
            <label htmlFor="signup-password" className="block text-sm font-bold text-gray-700 mb-2">비밀번호</label>
            <input id="signup-password" type="password" value={values.password} onChange={set("password")} className={inputClass(!!errors.password)} placeholder="비밀번호" />
            {errors.password && <p className="text-red-500 text-xs mt-1">{errors.password}</p>}
          </div>

          <div>
            <label htmlFor="signup-confirm" className="block text-sm font-bold text-gray-700 mb-2">비밀번호 확인</label>
            <input id="signup-confirm" type="password" value={values.confirmPassword} onChange={set("confirmPassword")} className={inputClass(!!errors.confirmPassword)} placeholder="비밀번호 확인" />
            {errors.confirmPassword && <p className="text-red-500 text-xs mt-1">{errors.confirmPassword}</p>}
          </div>

          <button
            type="submit"
            className="w-full bg-[#2F8F6B] hover:bg-[#257A5A] text-white font-bold py-4 rounded-xl shadow-lg shadow-[#2F8F6B]/30 transition-all transform active:scale-[0.99] mt-6"
          >
            가입하기
          </button>
        </form>
      </div>
    </AuthShell>
  );
}

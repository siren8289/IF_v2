export interface SignupFormValues {
  id: string;
  password: string;
  confirmPassword: string;
  name: string;
  department: string;
}

/** 가입 폼 검증. 필드명 -> 오류 문구 맵을 반환하며 빈 객체면 통과. */
export function validateSignup(values: SignupFormValues): Record<string, string> {
  const errors: Record<string, string> = {};
  if (!values.id) errors.id = "아이디를 입력해주세요";
  if (!values.password) errors.password = "비밀번호를 입력해주세요";
  if (values.password !== values.confirmPassword)
    errors.confirmPassword = "비밀번호가 일치하지 않습니다";
  if (!values.name) errors.name = "이름을 입력해주세요";
  return errors;
}

/** 가입 시 localStorage에 저장되는 계정 정보 */
export interface StoredUser {
  id: string;
  password: string;
  name: string;
  department: string;
}

/** 로그인 성공 종류: 기본 관리자 또는 가입한 사용자(환영 메시지에 이름 사용) */
export type LoginResult = { kind: "admin" } | { kind: "user"; name: string };

// 백엔드 인증이 없는 데모용: 계정은 localStorage(평문), 로그인 상태는 sessionStorage에 둔다.
const USERS_KEY = "if_users";
const SESSION_KEY = "if_session";
const ADMIN = { id: "admin", password: "1234" };

// 저장소 값이 깨졌을 때 화면이 죽지 않도록 빈 목록으로 취급한다.
function readUsers(): StoredUser[] {
  try {
    const parsed = JSON.parse(localStorage.getItem(USERS_KEY) || "[]");
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

/** 아이디/비밀번호 검사. 기본 관리자 -> 가입 사용자 순으로 확인한다. */
export function authenticate(id: string, password: string): LoginResult | null {
  if (id === ADMIN.id && password === ADMIN.password) return { kind: "admin" };
  const user = readUsers().find((u) => u.id === id && u.password === password);
  return user ? { kind: "user", name: user.name } : null;
}

/** 계정 저장. 이미 같은 아이디가 있으면 저장하지 않고 'duplicate'를 반환한다. */
export function registerUser(user: StoredUser): "ok" | "duplicate" {
  const users = readUsers();
  if (users.some((u) => u.id === user.id)) return "duplicate";
  localStorage.setItem(USERS_KEY, JSON.stringify([...users, user]));
  return "ok";
}

/** 탭 닫으면 로그아웃되도록 sessionStorage로 로그인 여부를 관리한다. */
export function hasSession(): boolean {
  return sessionStorage.getItem(SESSION_KEY) === "1";
}

export function setSession(active: boolean): void {
  if (active) sessionStorage.setItem(SESSION_KEY, "1");
  else sessionStorage.removeItem(SESSION_KEY);
}

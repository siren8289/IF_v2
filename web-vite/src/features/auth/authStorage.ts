export interface StoredUser {
  id: string;
  password: string;
  name: string;
  department: string;
}

export type LoginResult = { kind: "admin" } | { kind: "user"; name: string };

// 백엔드 인증이 없는 데모용: 계정은 localStorage(평문), 로그인 상태는 sessionStorage에 둔다.
const USERS_KEY = "if_users";
const SESSION_KEY = "if_session";
const ADMIN = { id: "admin", password: "1234" };

function readUsers(): StoredUser[] {
  try {
    const parsed = JSON.parse(localStorage.getItem(USERS_KEY) || "[]");
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

export function authenticate(id: string, password: string): LoginResult | null {
  if (id === ADMIN.id && password === ADMIN.password) return { kind: "admin" };
  const user = readUsers().find((u) => u.id === id && u.password === password);
  return user ? { kind: "user", name: user.name } : null;
}

export function registerUser(user: StoredUser): "ok" | "duplicate" {
  const users = readUsers();
  if (users.some((u) => u.id === user.id)) return "duplicate";
  localStorage.setItem(USERS_KEY, JSON.stringify([...users, user]));
  return "ok";
}

export function hasSession(): boolean {
  return sessionStorage.getItem(SESSION_KEY) === "1";
}

export function setSession(active: boolean): void {
  if (active) sessionStorage.setItem(SESSION_KEY, "1");
  else sessionStorage.removeItem(SESSION_KEY);
}

import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  useState,
  type ReactNode,
} from "react";
import {
  authenticate,
  hasSession,
  setSession,
  type LoginResult,
} from "./authStorage";

interface AuthContextValue {
  isAuthenticated: boolean;
  login: (id: string, password: string) => LoginResult | null;
  logout: () => void;
}

// 인증 상태(전역 상태): 페이지 이동과 무관하게 RequireAuth/헤더(로그아웃)가 공유한다.
const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  // 새로고침해도 로그인이 유지되도록 초기값을 sessionStorage에서 읽는다.
  const [isAuthenticated, setIsAuthenticated] = useState(hasSession);

  const login = useCallback((id: string, password: string) => {
    const result = authenticate(id, password);
    if (result) {
      setSession(true);
      setIsAuthenticated(true);
    }
    return result;
  }, []);

  const logout = useCallback(() => {
    setSession(false);
    setIsAuthenticated(false);
  }, []);

  const value = useMemo(
    () => ({ isAuthenticated, login, logout }),
    [isAuthenticated, login, logout]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

/** Provider 밖에서 호출하면 바로 알 수 있도록 오류를 던진다. */
export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}

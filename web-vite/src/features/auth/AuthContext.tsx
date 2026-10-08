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

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
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

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}

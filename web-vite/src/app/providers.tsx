import type { ReactNode } from "react";
import { AuthProvider } from "@/features/auth/AuthContext";
import { Toaster } from "@/shared/ui/Toaster";

// 앱 전역 Provider: 인증 상태와 토스트. (기존 Next의 app/providers.tsx 역할)
export function Providers({ children }: { children: ReactNode }) {
  return (
    <AuthProvider>
      {children}
      <Toaster />
    </AuthProvider>
  );
}

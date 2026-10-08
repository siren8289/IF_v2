import type { ReactNode } from "react";
import { AuthProvider } from "@/features/auth/AuthContext";
import { Toaster } from "@/shared/ui/Toaster";

export function Providers({ children }: { children: ReactNode }) {
  return (
    <AuthProvider>
      {children}
      <Toaster />
    </AuthProvider>
  );
}

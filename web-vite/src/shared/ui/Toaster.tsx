import type { CSSProperties } from "react";
import { Toaster as Sonner, type ToasterProps } from "sonner";

// 토스트 컨테이너. next-themes 없이 시스템 테마를 따르고, 색상은 theme.css 변수를 쓴다.

export function Toaster(props: ToasterProps) {
  return (
    <Sonner
      theme="system"
      className="toaster group"
      style={
        {
          "--normal-bg": "var(--popover)",
          "--normal-text": "var(--popover-foreground)",
          "--normal-border": "var(--border)",
        } as CSSProperties
      }
      {...props}
    />
  );
}

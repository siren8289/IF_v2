import type { ReactNode } from "react";
import { motion } from "motion/react";

interface AuthShellProps {
  // 좌측 브랜딩 패널 내용(제목/설명/뱃지)은 화면별로 다르므로 슬롯으로 받는다.
  title: ReactNode;
  description: ReactNode;
  badges: ReactNode;
  heightClass: string;
  enterFrom: { x?: number; y?: number };
  panelClassName: string;
  children: ReactNode;
}

/** 로그인/회원가입 공통: 좌측 브랜딩 패널 + 우측 폼 영역 */
export function AuthShell({
  title,
  description,
  badges,
  heightClass,
  enterFrom,
  panelClassName,
  children,
}: AuthShellProps) {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <motion.div
        initial={{ opacity: 0, ...enterFrom }}
        animate={{ opacity: 1, x: 0, y: 0 }}
        transition={{ duration: 0.5 }}
        className={`bg-white w-full max-w-5xl rounded-2xl shadow-2xl overflow-hidden flex h-auto ${heightClass}`}
      >
        <div className="hidden md:flex w-1/2 relative bg-gradient-to-br from-[#2F8F6B] to-[#1e6b4e] items-center justify-center overflow-hidden">
          <div className="absolute top-[-20%] left-[-20%] w-[80%] h-[80%] rounded-full border-[2px] border-white/10" />
          <div className="absolute bottom-[-10%] right-[-10%] w-[60%] h-[60%] rounded-full bg-white/5" />

          <div className="relative z-20 text-white p-12">
            <div className="w-20 h-20 bg-white/20 backdrop-blur-sm rounded-2xl mb-8 flex items-center justify-center border border-white/30 shadow-lg">
              <span className="text-white text-4xl font-bold">If</span>
            </div>
            {title}
            {description}
            <div className="mt-12 flex gap-4">{badges}</div>
          </div>
        </div>

        <div className={panelClassName}>{children}</div>
      </motion.div>
    </div>
  );
}

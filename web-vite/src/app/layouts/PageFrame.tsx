import type { ReactNode } from "react";

/** 모든 화면 공통 배경/컨테이너. header가 있으면 상단 바를 함께 렌더링한다. */
export function PageFrame({ header, children }: { header?: ReactNode; children: ReactNode }) {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col font-sans text-slate-800">
      {header}
      <main className="flex-1 w-full max-w-7xl mx-auto p-4 md:p-8 relative">{children}</main>
    </div>
  );
}

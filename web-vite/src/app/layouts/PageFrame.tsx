import type { ReactNode } from "react";

// 기존 Layout.tsx의 배경과 본문 영역만 분리했다.
// 헤더를 넣을지는 이 컴포넌트를 부르는 쪽(AppLayout)이 정한다.

/** 모든 화면 공통 배경. header가 있으면 상단 바를 함께 그린다. */
export function PageFrame({ header, children }: { header?: ReactNode; children: ReactNode }) {
  return (
    // min-h-screen: 내용이 적어도 화면 높이만큼 배경을 칠한다.
    // flex-col: 헤더를 위에, 본문을 그 아래에 쌓는다.
    <div className="min-h-screen bg-gray-50 flex flex-col font-sans text-slate-800">
      {header}
      <main className="flex-1 w-full max-w-7xl mx-auto p-4 md:p-8 relative">{children}</main>
    </div>
  );
}

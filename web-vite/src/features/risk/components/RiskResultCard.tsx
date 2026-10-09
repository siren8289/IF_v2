import { motion } from "motion/react";
import { AlertTriangle, Info } from "lucide-react";
import type { RiskView } from "../useRiskDetail";
import { DEFAULT_SUMMARY, RISK_LEVEL_STYLE } from "../riskLevel";

// 위험도 결과 카드(표시 전용): 좌측 점수 게이지, 우측 AI 요약과 주요 기여 요인.
export function RiskResultCard({ view }: { view: RiskView }) {
  const { score, level, factors, summary, guidance, disclaimer } = view;
  const style = RISK_LEVEL_STYLE[level];

  return (
    <div className="bg-white p-10 rounded-3xl shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-100 grid grid-cols-1 md:grid-cols-2 gap-10">
      <div className="flex flex-col items-center justify-start md:pt-4 border-b md:border-b-0 md:border-r border-gray-100 pb-8 md:pb-0 md:pr-8">
        <div className="relative w-64 h-64 flex items-center justify-center mb-6">
          <svg className="w-full h-full transform -rotate-90">
            <circle cx="128" cy="128" r="110" stroke="#f3f4f6" strokeWidth="20" fill="transparent" />
            <motion.circle
              initial={{ pathLength: 0 }}
              animate={{ pathLength: (score ?? 0) / 100 }}
              transition={{ duration: 1, ease: "easeOut" }}
              cx="128"
              cy="128"
              r="110"
              stroke={style.stroke}
              strokeWidth="20"
              fill="transparent"
              strokeLinecap="round"
              className="drop-shadow-sm"
            />
          </svg>
          <div className="absolute flex flex-col items-center">
            <span className="text-5xl font-bold text-gray-800">{score === null ? "미산출" : `${score}점`}</span>
            <span className={`text-2xl font-bold ${style.color} mt-2`}>{style.text}</span>
          </div>
        </div>
        <p className="text-gray-400 text-sm text-center">
          0~100점 정책 참고 지수입니다.<br />사고 확률(%)이 아니며 담당자 검토가 필요합니다.
        </p>
      </div>

      <div className="flex flex-col justify-center space-y-8">
        <div className={`p-6 rounded-2xl border ${style.bg} ${style.border}`}>
          <div className="flex items-start gap-4">
            <Info className={`${style.color} shrink-0 mt-1`} size={24} />
            <div>
              {view.loading && <p role="status">결과 조회 중…</p>}
              {view.error && <p role="alert" className="text-red-700">{view.error}</p>}
              {view.modelVersion && <p className="text-xs text-gray-500">산출 버전: {view.modelVersion} · 검토 필요</p>}
              <h3 className={`font-bold ${style.color} mb-2 text-lg`}>AI 해석 요약</h3>
              <p className="text-gray-700 leading-relaxed text-sm md:text-base whitespace-pre-line">
                {/* 서버 요약이 없으면 등급별 기본 문구를 보여준다. */}
                {summary || DEFAULT_SUMMARY[level]}
              </p>
              {guidance && (
                <p className="text-gray-600 text-xs md:text-sm mt-3 whitespace-pre-line">{guidance}</p>
              )}
              {disclaimer && (
                <p className="text-gray-400 text-xs mt-3 whitespace-pre-line">{disclaimer}</p>
              )}
            </div>
          </div>
        </div>

        <div>
          {view.evidenceSummary && (
            <details className="mb-6 bg-gray-50 p-4 rounded-xl text-sm text-gray-600">
              <summary className="cursor-pointer font-bold">산업·연령 통계 참고 근거 (점수 가산 없음)</summary>
              <p className="mt-3 leading-relaxed">{view.evidenceSummary}</p>
            </details>
          )}
          <h3 className="font-bold text-gray-800 mb-4 flex items-center gap-2 text-lg">
            <AlertTriangle size={20} className="text-gray-400" />
            주요 기여 요인
          </h3>
          <div className="space-y-3">
            {factors.length > 0 ? (
              factors.map((factor, idx) => (
                <div key={idx} className="bg-gray-50 px-5 py-4 rounded-xl border border-gray-100 flex items-center justify-between">
                  <span className="text-gray-700 font-medium">{factor}</span>
                  <span className="text-xs text-gray-500 font-bold bg-white border border-gray-200 px-2 py-1 rounded-md shadow-sm shrink-0 whitespace-nowrap ml-3">산출 근거</span>
                </div>
              ))
            ) : (
              <div className="bg-gray-50 px-5 py-4 rounded-xl border border-gray-100 text-gray-500 text-center py-6">
                <p className="font-medium">요인별 설명이 없습니다.</p>
                <p className="text-xs mt-1">결과를 산출한 뒤 근거를 확인할 수 있습니다.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

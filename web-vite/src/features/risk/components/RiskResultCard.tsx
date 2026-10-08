import { motion } from "motion/react";
import { AlertTriangle, Info } from "lucide-react";
import type { RiskView } from "../useRiskDetail";
import { DEFAULT_SUMMARY, RISK_LEVEL_STYLE } from "../riskLevel";

export function RiskResultCard({ view }: { view: RiskView }) {
  const { score, level, factors, summary, guidance, disclaimer } = view;
  const style = RISK_LEVEL_STYLE[level];

  return (
    <div className="bg-white p-10 rounded-3xl shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-100 grid grid-cols-1 md:grid-cols-2 gap-10">
      <div className="flex flex-col items-center justify-center border-b md:border-b-0 md:border-r border-gray-100 pb-8 md:pb-0 md:pr-8">
        <div className="relative w-64 h-64 flex items-center justify-center mb-6">
          <svg className="w-full h-full transform -rotate-90">
            <circle cx="128" cy="128" r="110" stroke="#f3f4f6" strokeWidth="20" fill="transparent" />
            <motion.circle
              initial={{ pathLength: 0 }}
              animate={{ pathLength: score / 100 }}
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
            <span className="text-7xl font-bold text-gray-800">{score}</span>
            <span className={`text-2xl font-bold ${style.color} mt-2`}>{style.text}</span>
          </div>
        </div>
        <p className="text-gray-400 text-sm text-center">
          종합적인 데이터를 기반으로<br />산출된 결과입니다.
        </p>
      </div>

      <div className="flex flex-col justify-center space-y-8">
        <div className={`p-6 rounded-2xl border ${style.bg} ${style.border}`}>
          <div className="flex items-start gap-4">
            <Info className={`${style.color} shrink-0 mt-1`} size={24} />
            <div>
              <h3 className={`font-bold ${style.color} mb-2 text-lg`}>AI 해석 요약</h3>
              <p className="text-gray-700 leading-relaxed text-sm md:text-base whitespace-pre-line">
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
          <h3 className="font-bold text-gray-800 mb-4 flex items-center gap-2 text-lg">
            <AlertTriangle size={20} className="text-gray-400" />
            주요 기여 요인
          </h3>
          <div className="space-y-3">
            {factors.length > 0 ? (
              factors.map((factor, idx) => (
                <div key={idx} className="bg-gray-50 px-5 py-4 rounded-xl border border-gray-100 flex items-center justify-between">
                  <span className="text-gray-700 font-medium">{factor}</span>
                  <span className="text-xs text-red-500 font-bold bg-white border border-red-100 px-2 py-1 rounded-md shadow-sm">+ 위험요인</span>
                </div>
              ))
            ) : (
              <div className="bg-gray-50 px-5 py-4 rounded-xl border border-gray-100 text-gray-500 text-center py-6">
                <p className="font-medium">요인별 설명이 없습니다.</p>
                <p className="text-xs mt-1">AI 설명이 생성되지 않았거나, 위험도 계산 시 설명 API가 호출되지 않았을 수 있습니다. (Gemini API 키·FastAPI 서버 확인)</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

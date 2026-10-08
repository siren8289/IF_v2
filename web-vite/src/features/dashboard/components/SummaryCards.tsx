import { AlertTriangle, CheckCircle, FileText } from "lucide-react";
import type { AssessmentSummaryResponse } from "@/shared/api/types";

const CARD =
  "bg-white p-8 rounded-3xl shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-100";

export function SummaryCards({ summary }: { summary: AssessmentSummaryResponse | null }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <div className={CARD}>
        <div className="flex items-center gap-5">
          <div className="p-4 bg-blue-50 text-blue-600 rounded-2xl"><FileText size={28} /></div>
          <div>
            <p className="text-sm font-medium text-gray-500 mb-1">총 평가 건수</p>
            <p className="text-3xl font-bold text-gray-800">{summary?.totalCount ?? 0}건</p>
          </div>
        </div>
      </div>
      <div className={CARD}>
        <div className="flex items-center gap-5">
          <div className="p-4 bg-red-50 text-red-600 rounded-2xl"><AlertTriangle size={28} /></div>
          <div>
            <p className="text-sm font-medium text-gray-500 mb-1">고위험군 발견</p>
            <p className="text-3xl font-bold text-gray-800">{summary?.highRiskCount ?? 0}건</p>
          </div>
        </div>
      </div>
      <div className={CARD}>
        <div className="flex items-center gap-5">
          <div className="p-4 bg-green-50 text-green-600 rounded-2xl"><CheckCircle size={28} /></div>
          <div>
            <p className="text-sm font-medium text-gray-500 mb-1">평가 완료</p>
            <p className="text-3xl font-bold text-gray-800">{summary?.finalizedCount ?? 0}건</p>
          </div>
        </div>
      </div>
    </div>
  );
}

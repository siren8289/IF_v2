import { Navigate, useLocation, useNavigate, useParams } from "react-router-dom";
import { RiskResultCard } from "@/features/risk/components/RiskResultCard";
import { useRiskDetail } from "@/features/risk/useRiskDetail";
import { parseAssessmentId, type Assessment } from "@/shared/model/assessment";

// 라우트 /assessments/:id/result: risk-detail 조회 결과를 카드로 보여주고 목록으로 돌아간다.
export default function RiskResultPage() {
  const navigate = useNavigate();
  const { id } = useParams();
  const location = useLocation();
  const assessmentId = parseAssessmentId(id);
  // 대시보드에서 넘긴 값은 risk-detail 조회가 실패했을 때만 표시용으로 쓴다.
  const fallback = (location.state as { assessment?: Assessment } | null)?.assessment;
  const view = useRiskDetail(assessmentId, fallback);

  if (assessmentId === null) return <Navigate to="/dashboard" replace />;

  return (
    <div className="max-w-4xl mx-auto pb-24 pt-8">
      <div className="mb-10 text-center">
        <h2 className="text-xl font-medium text-slate-600">
          AI가 분석한 신청자의 안전 위험도입니다.
        </h2>
      </div>

      <RiskResultCard view={view} />

      <div className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 p-4 z-10">
        <div className="max-w-4xl mx-auto flex gap-4">
          <button
            type="button"
            onClick={() => navigate("/dashboard")}
            className="flex-1 bg-[#2F8F6B] hover:bg-[#257A5A] text-white font-bold py-4 rounded-xl shadow-lg shadow-[#2F8F6B]/20 transition-all"
          >
            목록으로 돌아가기
          </button>
        </div>
      </div>

      <div className="h-20"></div>
    </div>
  );
}

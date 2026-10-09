import { Navigate, useNavigate, useParams } from "react-router-dom";
import { RiskAnalyzing } from "@/features/risk/components/RiskAnalyzing";
import { useComputeRisk } from "@/features/risk/useComputeRisk";
import { parseAssessmentId } from "@/shared/model/assessment";

// 라우트 /assessments/:id/analysis: compute-risk(Spring -> FastAPI) 요청 중 대기 화면을 보여준다.
export default function RiskAnalysisPage() {
  const navigate = useNavigate();
  const { id } = useParams();
  const assessmentId = parseAssessmentId(id);

  // 계산이 끝나면(실패 포함) 결과 화면으로 replace 이동해, 뒤로가기로 재계산되지 않게 한다.
  useComputeRisk(assessmentId, (error) =>
    navigate(`/assessments/${assessmentId}/result`, { replace: true, state: { computationError: error } })
  );

  if (assessmentId === null) return <Navigate to="/dashboard" replace />;
  return <RiskAnalyzing />;
}

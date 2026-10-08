import { useNavigate } from "react-router-dom";
import { AssessmentForm } from "@/features/assessment/components/AssessmentForm";

// 라우트 /assessments/new: 등록이 끝나면 생성된 ID로 분석 화면(/assessments/:id/analysis)으로 이동한다.
export default function AssessmentFormPage() {
  const navigate = useNavigate();
  return (
    <AssessmentForm
      onCreated={(id) => navigate(`/assessments/${id}/analysis`)}
    />
  );
}

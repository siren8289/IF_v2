import { useNavigate } from "react-router-dom";
import { AssessmentForm } from "@/features/assessment/components/AssessmentForm";

export default function AssessmentFormPage() {
  const navigate = useNavigate();
  return (
    <AssessmentForm
      onCreated={(id) => navigate(`/assessments/${id}/analysis`)}
    />
  );
}

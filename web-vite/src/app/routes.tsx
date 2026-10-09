import { Navigate, type RouteObject } from "react-router-dom";
import AssessmentFormPage from "@/pages/AssessmentFormPage";
import DashboardPage from "@/pages/DashboardPage";
import RiskResultPage from "@/pages/RiskResultPage";
import { AppLayout } from "./layouts/AppLayout";

// 화면은 3개: 대시보드 → 평가 입력 → 결과
export const routes: RouteObject[] = [
  {
    element: <AppLayout />,
    children: [
      { path: "/dashboard", element: <DashboardPage /> },
      { path: "/assessments/new", element: <AssessmentFormPage /> },
      { path: "/assessments/:id/result", element: <RiskResultPage /> },
    ],
  },
  { path: "*", element: <Navigate to="/dashboard" replace /> },
];

import { Navigate, type RouteObject } from "react-router-dom";
import AssessmentFormPage from "@/pages/AssessmentFormPage";
import DashboardPage from "@/pages/DashboardPage";
import LoginPage from "@/pages/LoginPage";
import RiskAnalysisPage from "@/pages/RiskAnalysisPage";
import RiskResultPage from "@/pages/RiskResultPage";
import SignupPage from "@/pages/SignupPage";
import { AppLayout } from "./layouts/AppLayout";
import { AuthLayout } from "./layouts/AuthLayout";
import { RequireAuth } from "./RequireAuth";

// 브라우저 라우터와 테스트(메모리 라우터)가 같은 정의를 쓰도록 라우터 생성과 분리했다.
export const routes: RouteObject[] = [
  { path: "/", element: <Navigate to="/login" replace /> },
  {
    element: <AuthLayout />,
    children: [
      { path: "/login", element: <LoginPage /> },
      { path: "/signup", element: <SignupPage /> },
    ],
  },
  // 평가 ID는 전역 state 대신 URL로 전달한다 (새로고침/직접 접근 가능).
  {
    element: <RequireAuth />,
    children: [
      {
        element: <AppLayout />,
        children: [
          { path: "/dashboard", element: <DashboardPage /> },
          { path: "/assessments/new", element: <AssessmentFormPage /> },
          { path: "/assessments/:id/analysis", element: <RiskAnalysisPage /> },
          { path: "/assessments/:id/result", element: <RiskResultPage /> },
        ],
      },
    ],
  },
  { path: "*", element: <Navigate to="/login" replace /> },
];

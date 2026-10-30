// 화면은 3개다. 대시보드 → 평가 입력 → 결과.
// 세 화면 모두 AppLayout(상단 바 + 본문) 안에 들어간다.
// 모르는 주소는 대시보드로 보낸다.
import { Navigate, type RouteObject } from "react-router-dom";
import AssessmentFormPage from "@/pages/AssessmentFormPage";
import DashboardPage from "@/pages/DashboardPage";
import RiskResultPage from "@/pages/RiskResultPage";
import { AppLayout } from "./layouts/AppLayout";

export const routes: RouteObject[] = [
  {
    // 공통 틀. 자식 경로는 이 틀의 <Outlet /> 자리에 그려진다.
    element: <AppLayout />,
    children: [
      { path: "/dashboard", element: <DashboardPage /> },
      { path: "/assessments/new", element: <AssessmentFormPage /> },
      // :id 는 평가 번호다. 결과 페이지가 useParams()로 읽는다.
      { path: "/assessments/:id/result", element: <RiskResultPage /> },
    ],
  },
  // * 는 위 경로에 안 맞는 모든 주소. replace라서 뒤로 가기를 눌러도 잘못된 주소로 돌아가지 않는다.
  { path: "*", element: <Navigate to="/dashboard" replace /> },
];

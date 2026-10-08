import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { FileText, Plus } from "lucide-react";
import { AssessmentTable } from "@/features/dashboard/components/AssessmentTable";
import { StatusEditModal } from "@/features/dashboard/components/StatusEditModal";
import { SummaryCards } from "@/features/dashboard/components/SummaryCards";
import { useAssessmentRecords } from "@/features/dashboard/useAssessmentRecords";
import { statusToApi, type Assessment } from "@/shared/model/assessment";

// 라우트 /dashboard: 목록·요약 조회(useAssessmentRecords)와 화면 이동/모달 상태를 조합한다.
export default function DashboardPage() {
  const navigate = useNavigate();
  const {
    assessments,
    summary,
    pageIndex,
    totalPages,
    loading,
    error,
    reload,
    goToPage,
    remove,
    changeStatus,
  } = useAssessmentRecords();
  // 펼친 행과 수정 대상은 화면 전용 상태라 훅이 아닌 페이지에서 관리한다.
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [editing, setEditing] = useState<Assessment | null>(null);

  const startNew = () => navigate("/assessments/new");

  const handleDelete = async (item: Assessment) => {
    if (!window.confirm(`「${item.applicantName}」 평가 기록을 삭제하시겠습니까?`)) return;
    setExpandedId((id) => (id === item.id ? null : id));
    await remove(item.id);
  };

  // 저장 시 모달을 먼저 닫고 PATCH -> 목록·요약 재조회를 한다.
  const handleSaveStatus = async (status: string) => {
    if (!editing) return;
    const id = editing.id;
    setEditing(null);
    await changeStatus(id, status);
  };

  return (
    <div className="max-w-7xl mx-auto pb-12">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 gap-4">
        <div>
          <h2 className="text-2xl font-bold text-gray-800">안녕하세요, 관리자님</h2>
          <p className="text-gray-500 mt-1">오늘의 위험도 판단 업무 현황입니다.</p>
        </div>
        <button
          type="button"
          onClick={startNew}
          className="flex items-center gap-2 bg-[#2F8F6B] hover:bg-[#257A5A] text-white px-6 py-3 rounded-xl font-bold shadow-lg shadow-[#2F8F6B]/20 transition-all active:scale-[0.98]"
        >
          <Plus size={20} />
          <span>새로운 평가 시작</span>
        </button>
      </div>

      {error && (
        <div role="alert" className="mb-6 p-4 bg-red-50 border border-red-200 rounded-xl text-red-700">
          {error}
          <button type="button" onClick={reload} className="ml-2 underline">다시 시도</button>
        </div>
      )}
      {loading && <div className="mb-8 text-center py-12 text-gray-500">불러오는 중...</div>}

      {!loading && (
        <>
          <SummaryCards summary={summary} />

          <div className="bg-white rounded-3xl shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-100 overflow-hidden">
            <div className="p-8 border-b border-gray-100 flex justify-between items-center">
              <h3 className="font-bold text-xl text-gray-800">최근 평가 기록</h3>
              <span className="text-sm font-medium text-gray-500 bg-gray-100 px-3 py-1 rounded-full">
                총 {summary?.totalCount ?? 0}건
              </span>
            </div>

            {assessments.length === 0 ? (
              <div className="text-center py-24">
                <div className="w-20 h-20 bg-gray-50 rounded-full flex items-center justify-center mx-auto mb-6 text-gray-300">
                  <FileText size={40} />
                </div>
                <p className="text-lg text-gray-500 font-medium">아직 등록된 평가 기록이 없습니다.</p>
                <p className="text-gray-400 mt-2 mb-8">새로운 신청자의 위험도를 평가해보세요.</p>
                <button type="button" onClick={startNew} className="text-[#2F8F6B] font-bold hover:underline">
                  평가 시작하기
                </button>
              </div>
            ) : (
              <AssessmentTable
                items={assessments}
                expandedId={expandedId}
                onToggle={(item) => setExpandedId((id) => (id === item.id ? null : item.id))}
                // 목록에서 이미 가진 값을 router state로 넘겨 결과 화면의 fallback으로 쓴다.
                onViewReport={(item) =>
                  navigate(`/assessments/${item.id}/result`, { state: { assessment: item } })
                }
                onEdit={setEditing}
                onDelete={handleDelete}
              />
            )}

            {totalPages > 1 && (
              <div className="flex items-center justify-between px-8 py-5 border-t border-gray-100">
                <span className="text-sm text-gray-500">{pageIndex + 1} / {totalPages} 페이지</span>
                <div className="flex gap-2">
                  <button
                    type="button"
                    disabled={pageIndex === 0}
                    onClick={() => goToPage(pageIndex - 1)}
                    className="px-4 py-2 rounded-lg border border-gray-200 text-sm font-bold text-gray-600 disabled:opacity-40 disabled:cursor-not-allowed hover:bg-gray-50"
                  >
                    이전
                  </button>
                  <button
                    type="button"
                    disabled={pageIndex + 1 >= totalPages}
                    onClick={() => goToPage(pageIndex + 1)}
                    className="px-4 py-2 rounded-lg border border-gray-200 text-sm font-bold text-gray-600 disabled:opacity-40 disabled:cursor-not-allowed hover:bg-gray-50"
                  >
                    다음
                  </button>
                </div>
              </div>
            )}
          </div>
        </>
      )}

      {editing && (
        <StatusEditModal
          initialStatus={statusToApi(editing.status)}
          onSave={handleSaveStatus}
          onClose={() => setEditing(null)}
        />
      )}
    </div>
  );
}

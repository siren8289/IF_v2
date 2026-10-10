import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
  deleteAssessment,
  getAssessments,
  getSummary,
  GRADE_COLOR,
  GRADE_TEXT,
  type AssessmentRecord,
  type Summary,
} from "@/shared/api/api";

const CARD = "bg-white p-6 rounded-2xl shadow-sm border border-gray-100";

export default function DashboardPage() {
  const navigate = useNavigate();
  const [records, setRecords] = useState<AssessmentRecord[]>([]);
  const [summary, setSummary] = useState<Summary | null>(null);
  const [page, setPage] = useState(0);
  const [totalPages, setTotalPages] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function load(pageNumber: number) {
    setLoading(true);
    setError(null);
    try {
      const list = await getAssessments(pageNumber);
      const sum = await getSummary();
      setRecords(list.content);
      setTotalPages(list.totalPages);
      setSummary(sum);
    } catch (e) {
      setError(e instanceof Error ? e.message : "목록을 불러오지 못했습니다.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load(page);
  }, [page]);

  async function handleDelete(item: AssessmentRecord) {
    if (!window.confirm(`「${item.applicantName}」 평가 기록을 삭제할까요?`)) return;
    try {
      await deleteAssessment(item.id);
      load(page);
    } catch (e) {
      setError(e instanceof Error ? e.message : "삭제하지 못했습니다.");
    }
  }

  return (
    <div className="max-w-7xl mx-auto pb-12">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h2 className="text-2xl font-bold text-gray-800">평가 대시보드</h2>
          <p className="text-gray-500 mt-1">등록된 평가와 위험도 결과입니다.</p>
        </div>
        <button
          type="button"
          onClick={() => navigate("/assessments/new")}
          className="bg-[#2F8F6B] hover:bg-[#257A5A] text-white px-6 py-3 rounded-xl font-bold"
        >
          새로운 평가 시작
        </button>
      </div>

      {error && (
        <div role="alert" className="mb-6 p-4 bg-red-50 border border-red-200 rounded-xl text-red-700">
          {error}
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className={CARD}>
          <p className="text-sm text-gray-500">총 평가 건수</p>
          <p className="text-3xl font-bold">{summary?.totalCount ?? 0}건</p>
        </div>
        <div className={CARD}>
          <p className="text-sm text-gray-500">고위험</p>
          <p className="text-3xl font-bold text-red-600">{summary?.highRiskCount ?? 0}건</p>
        </div>
        <div className={CARD}>
          <p className="text-sm text-gray-500">AI 분석 완료</p>
          <p className="text-3xl font-bold text-[#2F8F6B]">{summary?.analyzedCount ?? 0}건</p>
        </div>
      </div>

      <div className={CARD}>
        <h3 className="font-bold text-lg mb-4">최근 평가 기록</h3>

        {loading && <p className="text-gray-500 py-8 text-center">불러오는 중...</p>}

        {!loading && records.length === 0 && (
          <p className="text-gray-500 py-8 text-center">아직 등록된 평가 기록이 없습니다.</p>
        )}

        {!loading && records.length > 0 && (
          <table className="w-full text-left">
            <thead>
              <tr className="border-b text-sm text-gray-500">
                <th className="py-3">이름</th>
                <th>나이</th>
                <th>직무</th>
                <th>점수</th>
                <th>등급</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {records.map((item) => (
                <tr key={item.id} className="border-b last:border-0">
                  <td className="py-3 font-medium">{item.applicantName}</td>
                  <td>{item.age}세</td>
                  <td>{item.jobTitle}</td>
                  <td>{item.riskScore === null ? "-" : `${item.riskScore}점`}</td>
                  <td>
                    {item.riskGrade ? (
                      <span className={`px-2 py-1 rounded-full text-xs font-bold ${GRADE_COLOR[item.riskGrade]}`}>
                        {GRADE_TEXT[item.riskGrade] ?? item.riskGrade}
                      </span>
                    ) : (
                      <span className="text-gray-400 text-sm">분석 전</span>
                    )}
                  </td>
                  <td className="text-right space-x-3">
                    <Link to={`/assessments/${item.id}/result`} className="text-[#2F8F6B] font-bold text-sm">
                      결과 보기
                    </Link>
                    <button
                      type="button"
                      onClick={() => handleDelete(item)}
                      className="text-red-500 text-sm"
                    >
                      삭제
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}

        {totalPages > 1 && (
          <div className="flex justify-end gap-2 mt-4">
            <button type="button" disabled={page === 0} onClick={() => setPage(page - 1)}
              className="px-3 py-1 border rounded disabled:opacity-40">이전</button>
            <span className="px-2 py-1 text-sm text-gray-500">{page + 1} / {totalPages}</span>
            <button type="button" disabled={page + 1 >= totalPages} onClick={() => setPage(page + 1)}
              className="px-3 py-1 border rounded disabled:opacity-40">다음</button>
          </div>
        )}
      </div>
    </div>
  );
}

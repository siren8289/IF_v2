import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getResult, GRADE_COLOR, GRADE_TEXT, type AssessmentResult } from "@/shared/api/api";

const CARD = "bg-white p-6 rounded-2xl shadow-sm border border-gray-100";

export default function RiskResultPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [result, setResult] = useState<AssessmentResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getResult(Number(id))
      .then(setResult)
      .catch((e) => setError(e instanceof Error ? e.message : "결과를 불러오지 못했습니다."));
  }, [id]);

  if (error) {
    return <div role="alert" className="p-4 bg-red-50 border border-red-200 rounded-xl text-red-700">{error}</div>;
  }
  if (!result) {
    return <p className="text-gray-500 text-center py-12">불러오는 중...</p>;
  }

  return (
    <div className="max-w-3xl mx-auto pb-12 pt-6 space-y-6">
      <div className={CARD}>
        <p className="text-sm text-gray-500">
          {result.applicantName} · {result.age}세 · {result.jobTitle}
        </p>

        {result.riskScore === null ? (
          <p className="mt-4 text-gray-600">아직 AI 분석 결과가 없습니다.</p>
        ) : (
          <div className="mt-4 flex items-center gap-4">
            <span className="text-5xl font-bold text-gray-800">{result.riskScore}점</span>
            {result.riskGrade && (
              <span className={`px-3 py-1 rounded-full text-sm font-bold ${GRADE_COLOR[result.riskGrade]}`}>
                위험도 {GRADE_TEXT[result.riskGrade] ?? result.riskGrade}
              </span>
            )}
          </div>
        )}
      </div>

      {result.explanation && (
        <div className={CARD}>
          <h3 className="font-bold mb-2">AI 설명</h3>
          <p className="text-gray-700 whitespace-pre-line">{result.explanation}</p>
          <p className="text-xs text-gray-400 mt-2">
            {result.explanationSource === "gemini" ? "생성형 AI(Gemini)가 작성" : "기본 설명 (생성형 AI 미사용)"}
          </p>
        </div>
      )}

      {result.factors.length > 0 && (
        <div className={CARD}>
          <h3 className="font-bold mb-4">점수 구성</h3>
          <ul className="space-y-3">
            {result.factors.map((factor) => (
              <li key={factor.name}>
                <div className="flex justify-between text-sm">
                  <span>{factor.name}</span>
                  <span>{factor.points} / {factor.max}점</span>
                </div>
                <div className="h-2 bg-gray-100 rounded-full mt-1">
                  <div
                    className="h-2 bg-[#2F8F6B] rounded-full"
                    style={{ width: `${factor.max > 0 ? (factor.points / factor.max) * 100 : 0}%` }}
                  />
                </div>
              </li>
            ))}
          </ul>
        </div>
      )}

      {result.taskScores.length > 0 && (
        <div className={CARD}>
          <h3 className="font-bold mb-4">직무 특성 분석 (ML / DL)</h3>
          <table className="w-full text-sm">
            <thead>
              <tr className="text-gray-500 border-b">
                <th className="text-left py-2">특성</th>
                <th className="text-right">ML</th>
                <th className="text-right">DL</th>
              </tr>
            </thead>
            <tbody>
              {result.taskScores.map((task) => (
                <tr key={task.name} className="border-b last:border-0">
                  <td className="py-2">{task.name}</td>
                  <td className="text-right">{Math.round(task.mlScore * 100)}%</td>
                  <td className="text-right">{Math.round(task.dlScore * 100)}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <button
        type="button"
        onClick={() => navigate("/dashboard")}
        className="w-full border border-gray-200 bg-white py-3 rounded-xl font-bold text-gray-600"
      >
        목록으로 돌아가기
      </button>
    </div>
  );
}

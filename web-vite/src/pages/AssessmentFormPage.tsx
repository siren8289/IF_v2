import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { createAssessment, getJobs, type Job } from "@/shared/api/api";

const INPUT = "w-full px-4 py-3 bg-white border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#2F8F6B]";

const HEALTH_OPTIONS = [
  { value: 1, label: "1 - 매우 좋음" },
  { value: 2, label: "2 - 좋음" },
  { value: 3, label: "3 - 보통" },
  { value: 4, label: "4 - 나쁨" },
  { value: 5, label: "5 - 매우 나쁨" },
];

export default function AssessmentFormPage() {
  const navigate = useNavigate();
  const [jobs, setJobs] = useState<Job[]>([]);

  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [physicalLevel, setPhysicalLevel] = useState(3);
  const [chronicDisease, setChronicDisease] = useState("no");
  const [workHourLimit, setWorkHourLimit] = useState("8");
  const [jobId, setJobId] = useState("");

  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    getJobs()
      .then(setJobs)
      .catch(() => setError("직무 목록을 불러오지 못했습니다."));
  }, []);

  // 입력값 확인. 문제가 있으면 오류 문장을, 없으면 null을 돌려준다.
  function validate() {
    if (name.trim() === "") return "이름을 입력해주세요.";
    const ageNumber = Number(age);
    if (!Number.isInteger(ageNumber) || ageNumber < 1 || ageNumber > 120) return "연령은 1~120 사이로 입력해주세요.";
    const hours = Number(workHourLimit);
    if (!Number.isInteger(hours) || hours < 1 || hours > 24) return "근무 가능 시간은 1~24 사이로 입력해주세요.";
    if (jobId === "") return "직무를 선택해주세요.";
    return null;
  }

  async function handleSubmit() {
    const message = validate();
    if (message) {
      setError(message);
      return;
    }

    setSubmitting(true);
    setError(null);
    try {
      const id = await createAssessment({
        applicantName: name.trim(),
        age: Number(age),
        physicalLevel,
        chronicDisease: chronicDisease === "yes",
        workHourLimit: Number(workHourLimit),
        jobId: Number(jobId),
      });
      navigate(`/assessments/${id}/result`);
    } catch (e) {
      setError(e instanceof Error ? e.message : "분석에 실패했습니다.");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="max-w-2xl mx-auto pb-12 pt-6">
      <h2 className="text-2xl font-bold text-gray-800 mb-6">새로운 평가</h2>

      <div className="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 space-y-6">
        <div>
          <label htmlFor="name" className="block text-sm font-bold mb-2">이름</label>
          <input id="name" className={INPUT} value={name} placeholder="홍길동"
            onChange={(e) => setName(e.target.value)} />
        </div>

        <div>
          <label htmlFor="age" className="block text-sm font-bold mb-2">연령</label>
          <input id="age" type="number" className={INPUT} value={age} placeholder="65"
            onChange={(e) => setAge(e.target.value)} />
        </div>

        <div>
          <label htmlFor="health" className="block text-sm font-bold mb-2">건강 상태</label>
          <select id="health" className={INPUT} value={physicalLevel}
            onChange={(e) => setPhysicalLevel(Number(e.target.value))}>
            {HEALTH_OPTIONS.map((option) => (
              <option key={option.value} value={option.value}>{option.label}</option>
            ))}
          </select>
        </div>

        <div>
          <label htmlFor="chronic" className="block text-sm font-bold mb-2">만성질환</label>
          <select id="chronic" className={INPUT} value={chronicDisease}
            onChange={(e) => setChronicDisease(e.target.value)}>
            <option value="no">없음</option>
            <option value="yes">있음</option>
          </select>
        </div>

        <div>
          <label htmlFor="hours" className="block text-sm font-bold mb-2">하루 근무 가능 시간</label>
          <input id="hours" type="number" className={INPUT} value={workHourLimit}
            onChange={(e) => setWorkHourLimit(e.target.value)} />
        </div>

        <div>
          <label htmlFor="job" className="block text-sm font-bold mb-2">직무</label>
          <select id="job" className={INPUT} value={jobId} onChange={(e) => setJobId(e.target.value)}>
            <option value="">선택하세요</option>
            {jobs.map((job) => (
              <option key={job.id} value={job.id}>
                {job.jobTitle}{job.workplace ? ` (${job.workplace})` : ""}
              </option>
            ))}
          </select>
        </div>

        {error && (
          <div role="alert" className="p-4 bg-red-50 border border-red-200 rounded-xl text-red-700 text-sm">
            {error}
          </div>
        )}

        <button
          type="button"
          onClick={handleSubmit}
          disabled={submitting}
          className="w-full bg-[#2F8F6B] hover:bg-[#257A5A] disabled:opacity-60 text-white font-bold py-4 rounded-xl"
        >
          {submitting ? "AI 분석 중..." : "위험도 분석 시작"}
        </button>

        <p className="text-xs text-gray-500">
          결과는 0~100점 참고 지수이며 사고 확률이나 진단이 아닙니다.
        </p>
      </div>
    </div>
  );
}

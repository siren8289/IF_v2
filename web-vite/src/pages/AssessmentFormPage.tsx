import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { createAssessment, getJobs, type Job } from "@/shared/api/api";

// 입력칸에 반복해서 쓰는 Tailwind 클래스. 칸의 생김새만 모아 둔 것이다.
const INPUT = "w-full px-4 py-3 bg-white border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#2F8F6B]";

const HEALTH_OPTIONS = [
  { value: 1, label: "1 - 매우 좋음" },
  { value: 2, label: "2 - 좋음" },
  { value: 3, label: "3 - 보통" },
  { value: 4, label: "4 - 나쁨" },
  { value: 5, label: "5 - 매우 나쁨" },
];

// 새 평가를 입력하는 화면. 제출하면 Spring이 AI 분석을 하고, 결과 페이지로 이동한다.
export default function AssessmentFormPage() {
  // navigate: 코드에서 주소만 바꾸는 함수. 폼 제출 성공 후 결과 화면으로 간다.
  const navigate = useNavigate();
  // jobs: 서버에서 받아 온 직무 목록. 처음엔 빈 배열이다.
  const [jobs, setJobs] = useState<Job[]>([]);

  // 입력값은 전부 이 컴포넌트가 기억한다. 글자가 바뀔 때마다 set 함수로 다시 그린다.
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  // 건강은 기본 "보통"(3). 셀렉트 박스의 value와 맞춘다.
  const [physicalLevel, setPhysicalLevel] = useState(3);
  // 셀렉트는 문자열만 다루기 쉬워서 "yes" / "no"로 두고, 보낼 때만 true/false로 바꾼다.
  const [chronicDisease, setChronicDisease] = useState("no");
  const [workHourLimit, setWorkHourLimit] = useState("8");
  const [jobId, setJobId] = useState("");

  const [error, setError] = useState<string | null>(null);
  // 분석 요청 중에는 버튼을 막고 "AI 분석 중..."을 보여 준다. 두 번 누르는 것을 막는다.
  const [submitting, setSubmitting] = useState(false);

  // 화면이 처음 나타날 때 직무 목록을 한 번만 가져온다. [] 는 "마운트 때 한 번"이라는 뜻이다.
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

  // 버튼 클릭. 검사에 걸리면 서버로 보내지 않는다.
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
      // 서버가 만든 평가 번호로 결과 주소에 간다. 예: /assessments/12/result
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

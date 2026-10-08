import { useState } from "react";
import { ChevronRight } from "lucide-react";
import { motion } from "motion/react";
import type { HealthStatus } from "@/shared/model/assessment";
import {
  registerAssessment,
  validateAssessmentForm,
  type AssessmentFormValues,
} from "../service";
import { useJobs } from "../useJobs";

interface AssessmentFormProps {
  // 등록 성공 시 생성된 평가 ID를 넘기고, 이동은 페이지가 결정한다.
  onCreated: (assessmentId: number) => void;
}

const HEALTH_OPTIONS: { value: HealthStatus; label: string }[] = [
  { value: "good", label: "좋음" },
  { value: "average", label: "보통" },
  { value: "bad", label: "나쁨" },
];

export function AssessmentForm({ onCreated }: AssessmentFormProps) {
  const jobs = useJobs();
  const [values, setValues] = useState<AssessmentFormValues>({
    applicantName: "",
    age: "",
    healthStatus: "average",
    jobId: "",
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [submitting, setSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState<string | null>(null);

  const handleSubmit = async () => {
    // 검증 실패 시 API를 호출하지 않는다.
    const nextErrors = validateAssessmentForm(values);
    setErrors(nextErrors);
    if (Object.keys(nextErrors).length > 0) return;

    setSubmitting(true);
    setSubmitError(null);
    try {
      const id = await registerAssessment({
        applicantName: values.applicantName,
        age: Number(values.age),
        healthStatus: values.healthStatus,
        jobId: Number(values.jobId),
      });
      onCreated(id);
    } catch (e) {
      setSubmitError(e instanceof Error ? e.message : "등록에 실패했습니다.");
    } finally {
      setSubmitting(false);
    }
  };

  const inputBase =
    "w-full px-5 py-4 bg-white border rounded-xl focus:outline-none focus:ring-2 focus:ring-[#2F8F6B] focus:border-transparent transition-all text-gray-800 placeholder-gray-400";

  return (
    <div className="max-w-3xl mx-auto pb-12 pt-8">
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
      >
        <div className="mb-10 text-center">
          <h2 className="text-xl font-medium text-slate-600">
            정확한 판단을 위해 신청자의 기본 정보를 입력해주세요.
          </h2>
        </div>

        <div className="bg-white p-10 rounded-3xl shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-100 space-y-10">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
              <label htmlFor="applicant-name" className="block text-sm font-bold text-gray-800 mb-3">이름</label>
              <input
                id="applicant-name"
                type="text"
                value={values.applicantName}
                onChange={(e) => setValues({ ...values, applicantName: e.target.value })}
                className={`${inputBase} ${errors.applicantName ? "border-red-500" : "border-gray-200"}`}
                placeholder="홍길동"
              />
              {errors.applicantName && <p className="text-red-500 text-xs mt-2 ml-1">{errors.applicantName}</p>}
            </div>

            <div>
              <label htmlFor="applicant-age" className="block text-sm font-bold text-gray-800 mb-3">연령</label>
              <input
                id="applicant-age"
                type="number"
                value={values.age}
                onChange={(e) => setValues({ ...values, age: e.target.value })}
                className={`${inputBase} ${errors.age ? "border-red-500" : "border-gray-200"}`}
                placeholder="65"
              />
              {errors.age && <p className="text-red-500 text-xs mt-2 ml-1">{errors.age}</p>}
            </div>
          </div>

          <div>
            <span className="block text-sm font-bold text-gray-800 mb-3">건강 상태</span>
            <div className="grid grid-cols-3 gap-4">
              {HEALTH_OPTIONS.map((opt) => (
                <button
                  key={opt.value}
                  type="button"
                  aria-pressed={values.healthStatus === opt.value}
                  onClick={() => setValues({ ...values, healthStatus: opt.value })}
                  className={`py-4 rounded-xl border font-bold transition-all ${
                    values.healthStatus === opt.value
                      ? "bg-[#E5F2ED] border-[#2F8F6B] text-[#2F8F6B] shadow-sm"
                      : "bg-white border-gray-200 text-gray-400 hover:border-gray-300 hover:text-gray-600"
                  }`}
                >
                  {opt.label}
                </button>
              ))}
            </div>
          </div>

          <div>
            <label htmlFor="job" className="block text-sm font-bold text-gray-800 mb-3">검토 대상 직무</label>
            <select
              id="job"
              value={values.jobId}
              onChange={(e) =>
                setValues({ ...values, jobId: e.target.value === "" ? "" : Number(e.target.value) })
              }
              className={`w-full px-5 py-4 bg-white border rounded-xl focus:outline-none focus:ring-2 focus:ring-[#2F8F6B] focus:border-transparent text-gray-800 ${errors.job ? "border-red-500" : "border-gray-200"}`}
            >
              <option value="">선택하세요</option>
              {jobs.map((j) => (
                <option key={j.id} value={j.id}>{j.jobTitle} ({j.workplace})</option>
              ))}
            </select>
            {errors.job && <p className="text-red-500 text-xs mt-2 ml-1">{errors.job}</p>}
            {jobs.length === 0 && !errors.job && (
              <p className="text-gray-500 text-sm mt-1">백엔드에 직무가 없으면 먼저 DB에 등록해주세요.</p>
            )}
          </div>

          {submitError && (
            <div role="alert" className="p-4 bg-red-50 border border-red-200 rounded-xl text-red-700 text-sm">
              {submitError}
            </div>
          )}

          <div className="pt-6">
            <button
              type="button"
              onClick={handleSubmit}
              disabled={submitting}
              className="w-full bg-[#2F8F6B] hover:bg-[#257A5A] disabled:opacity-60 text-white font-bold py-5 rounded-xl shadow-lg shadow-[#2F8F6B]/30 transition-all flex items-center justify-center gap-2 transform active:scale-[0.99] text-lg"
            >
              <span>{submitting ? "등록 중…" : "위험도 분석 시작"}</span>
              <ChevronRight size={24} />
            </button>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

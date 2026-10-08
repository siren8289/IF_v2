import { useState } from "react";
import { STATUS_OPTIONS } from "@/shared/model/assessment";

interface StatusEditModalProps {
  initialStatus: string;
  onSave: (status: string) => void;
  onClose: () => void;
}

/** 상태 수정 모달. 선택값은 모달 내부 state로 두고, 저장 시에만 부모에 전달한다. */
export function StatusEditModal({ initialStatus, onSave, onClose }: StatusEditModalProps) {
  const [status, setStatus] = useState(initialStatus);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50" onClick={onClose}>
      <div
        role="dialog"
        aria-label="상태 수정"
        className="bg-white rounded-2xl shadow-xl p-8 max-w-sm w-full mx-4"
        onClick={(e) => e.stopPropagation()}
      >
        <h4 className="font-bold text-lg text-gray-800 mb-4">상태 수정</h4>
        <select
          aria-label="상태"
          value={status}
          onChange={(e) => setStatus(e.target.value)}
          className="w-full px-4 py-3 border border-gray-200 rounded-xl text-gray-800 font-medium mb-6"
        >
          {STATUS_OPTIONS.map((opt) => (
            <option key={opt.value} value={opt.value}>{opt.label}</option>
          ))}
        </select>
        <div className="flex gap-3">
          <button
            type="button"
            onClick={onClose}
            className="flex-1 py-3 border border-gray-200 text-gray-600 rounded-xl font-bold hover:bg-gray-50"
          >
            취소
          </button>
          <button
            type="button"
            onClick={() => onSave(status)}
            className="flex-1 py-3 bg-[#2F8F6B] text-white rounded-xl font-bold hover:bg-[#257A5A]"
          >
            저장
          </button>
        </div>
      </div>
    </div>
  );
}

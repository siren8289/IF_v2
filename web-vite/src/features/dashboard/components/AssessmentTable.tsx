import { Fragment } from "react";
import { AnimatePresence, motion } from "motion/react";
import { ChevronDown, ChevronUp, FileText, Pencil, Trash2, User } from "lucide-react";
import type { Assessment } from "@/shared/model/assessment";

// 상태/위험도 뱃지 색상
const statusColor = (status: string) => {
  switch (status) {
    case "Completed": return "bg-blue-100 text-blue-700 border-blue-200";
    case "Analyzed": return "bg-yellow-100 text-yellow-700 border-yellow-200";
    default: return "bg-gray-100 text-gray-700 border-gray-200";
  }
};

const riskColor = (level: string) => {
  switch (level) {
    case "High": return "text-red-500 bg-red-50 px-2.5 py-1 rounded-md";
    case "Medium": return "text-amber-500 bg-amber-50 px-2.5 py-1 rounded-md";
    case "Low": return "text-green-500 bg-green-50 px-2.5 py-1 rounded-md";
    default: return "text-gray-500";
  }
};

// 표시 전용: 행 펼침/수정/삭제/리포트 동작은 모두 콜백으로 페이지에 위임한다.
interface AssessmentTableProps {
  items: Assessment[];
  expandedId: string | null;
  onToggle: (item: Assessment) => void;
  onViewReport: (item: Assessment) => void;
  onEdit: (item: Assessment) => void;
  onDelete: (item: Assessment) => void;
}

export function AssessmentTable({
  items,
  expandedId,
  onToggle,
  onViewReport,
  onEdit,
  onDelete,
}: AssessmentTableProps) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-left border-collapse">
        <thead className="bg-gray-50/50">
          <tr>
            <th className="px-8 py-5 text-sm font-bold text-gray-500">상태</th>
            <th className="px-8 py-5 text-sm font-bold text-gray-500">신청자</th>
            <th className="px-8 py-5 text-sm font-bold text-gray-500 hidden md:table-cell">나이/건강</th>
            <th className="px-8 py-5 text-sm font-bold text-gray-500 hidden md:table-cell">위험도</th>
            <th className="px-8 py-5 text-sm font-bold text-gray-500 hidden md:table-cell">날짜</th>
            <th className="px-8 py-5 text-sm font-bold text-gray-500 text-right">관리</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-100">
          {items.map((item, index) => {
            const expanded = expandedId === item.id;
            return (
              <Fragment key={item.id}>
                <motion.tr
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ delay: index * 0.05 }}
                  className={`hover:bg-gray-50/80 transition-colors cursor-pointer group ${expanded ? "bg-gray-50" : ""}`}
                  onClick={() => onToggle(item)}
                >
                  <td className="px-8 py-5 whitespace-nowrap">
                    <span className={`px-3 py-1.5 rounded-full text-xs font-bold border ${statusColor(item.status)}`}>
                      {item.status}
                    </span>
                  </td>
                  <td className="px-8 py-5 whitespace-nowrap">
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center text-gray-500 group-hover:bg-white group-hover:shadow-sm transition-all">
                        <User size={18} />
                      </div>
                      <span className="font-bold text-gray-800 text-lg block">{item.applicantName}</span>
                    </div>
                  </td>
                  <td className="px-8 py-5 hidden md:table-cell">
                    <span className="text-gray-600 font-medium">{item.age}세 <span className="text-gray-300 mx-2">|</span> {item.healthStatus}</span>
                  </td>
                  <td className="px-8 py-5 hidden md:table-cell">
                    <span className={`text-sm font-bold ${riskColor(item.riskLevel)}`}>{item.riskLevel}</span>
                  </td>
                  <td className="px-8 py-5 hidden md:table-cell text-gray-500">
                    {new Date(item.date).toLocaleDateString()}
                  </td>
                  <td className="px-8 py-5 text-right">
                    <div className="inline-flex items-center justify-center w-8 h-8 rounded-full hover:bg-gray-200 transition-colors">
                      {expanded ? (
                        <ChevronUp size={20} className="text-[#2F8F6B]" />
                      ) : (
                        <ChevronDown size={20} className="text-gray-400 group-hover:text-[#2F8F6B]" />
                      )}
                    </div>
                  </td>
                </motion.tr>

                <AnimatePresence>
                  {expanded && (
                    <motion.tr
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                      transition={{ duration: 0.2 }}
                    >
                      <td colSpan={6} className="p-0 border-0">
                        <motion.div
                          initial={{ height: 0 }}
                          animate={{ height: "auto" }}
                          exit={{ height: 0 }}
                          transition={{ duration: 0.3, ease: "easeInOut" }}
                          className="overflow-hidden bg-gray-50"
                        >
                          <div className="p-8 border-b border-gray-100">
                            <div className="flex justify-between items-start mb-6">
                              <h4 className="font-bold text-gray-800 text-lg">상세 정보</h4>
                              <div className="flex flex-wrap gap-3">
                                <button
                                  type="button"
                                  onClick={() => onViewReport(item)}
                                  className="px-4 py-2 bg-white border border-gray-200 text-gray-600 rounded-lg font-bold text-sm hover:bg-gray-50 transition-colors flex items-center gap-2"
                                >
                                  <FileText size={16} />
                                  상세 리포트 보기
                                </button>
                                <button
                                  type="button"
                                  onClick={() => onEdit(item)}
                                  className="px-4 py-2 bg-white border border-amber-200 text-amber-700 rounded-lg font-bold text-sm hover:bg-amber-50 transition-colors flex items-center gap-2"
                                >
                                  <Pencil size={16} />
                                  상태 수정
                                </button>
                                <button
                                  type="button"
                                  onClick={() => onDelete(item)}
                                  className="px-4 py-2 bg-white border border-red-200 text-red-600 rounded-lg font-bold text-sm hover:bg-red-50 transition-colors flex items-center gap-2"
                                >
                                  <Trash2 size={16} />
                                  삭제
                                </button>
                              </div>
                            </div>
                          </div>
                        </motion.div>
                      </td>
                    </motion.tr>
                  )}
                </AnimatePresence>
              </Fragment>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

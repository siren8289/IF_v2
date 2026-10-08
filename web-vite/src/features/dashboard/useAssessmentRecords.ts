import { useCallback, useEffect, useState } from "react";
import {
  deleteAssessment,
  getAssessmentSummary,
  listAssessmentRecords,
  updateAssessment,
} from "@/shared/api/assessments";
import type { AssessmentSummaryResponse } from "@/shared/api/types";
import type { Assessment } from "@/shared/model/assessment";
import { mapRecordToAssessment } from "./mappers";

const PAGE_SIZE = 20;

/** 목록(join+페이지네이션)과 요약(COUNT 집계)을 함께 불러오고, 삭제/상태 수정 후 현재 페이지를 다시 조회한다. */
export function useAssessmentRecords() {
  const [assessments, setAssessments] = useState<Assessment[]>([]);
  const [summary, setSummary] = useState<AssessmentSummaryResponse | null>(null);
  const [pageIndex, setPageIndex] = useState(0);
  const [totalPages, setTotalPages] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const load = useCallback(async (page = 0) => {
    setLoading(true);
    setError(null);
    try {
      const [list, summaryRes] = await Promise.all([
        listAssessmentRecords(page, PAGE_SIZE),
        getAssessmentSummary(),
      ]);
      setAssessments(list.content.map(mapRecordToAssessment));
      setTotalPages(list.totalPages);
      setPageIndex(list.number);
      setSummary(summaryRes);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Failed to load");
      setAssessments([]);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    load(0);
  }, [load]);

  const remove = async (id: string) => {
    try {
      await deleteAssessment(Number(id));
      await load(pageIndex);
    } catch (e) {
      setError(e instanceof Error ? e.message : "삭제 실패");
    }
  };

  const changeStatus = async (id: string, status: string) => {
    try {
      await updateAssessment(Number(id), { status });
      await load(pageIndex);
    } catch (e) {
      setError(e instanceof Error ? e.message : "수정 실패");
    }
  };

  return {
    assessments,
    summary,
    pageIndex,
    totalPages,
    loading,
    error,
    reload: () => load(pageIndex),
    goToPage: load,
    remove,
    changeStatus,
  };
}

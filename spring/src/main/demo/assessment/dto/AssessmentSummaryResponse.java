package com.example.demo.assessment.dto;

/** 대시보드 요약 카드: 전체 / 고위험 / 분석 완료 건수 */
public record AssessmentSummaryResponse(
        long totalCount,
        long highRiskCount,
        long analyzedCount
) {
}

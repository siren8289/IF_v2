package com.example.demo.assessment.dto;

import java.util.List;

/** 결과 화면에 보여줄 값 */
public record AssessmentResultResponse(
        Long id,
        String applicantName,
        Integer age,
        String jobTitle,
        String status,
        Integer riskScore,
        String riskGrade,
        String explanation,
        String explanationSource,   // "gemini" 또는 "basic"
        List<Factor> factors,
        List<TaskScore> taskScores
) {
    /** 점수 항목. 예: 나이 10점 / 최대 20점 */
    public record Factor(String name, double points, int max) {
    }

    /** 작업 특성별 ML, DL 점수 (0~1) */
    public record TaskScore(String name, double mlScore, double dlScore) {
    }
}

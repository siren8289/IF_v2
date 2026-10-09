
package com.example.demo.assessment.dto;

import com.fasterxml.jackson.databind.JsonNode;

import java.util.ArrayList;
import java.util.List;

/**
 * AI 평가 상세 응답 DTO.
 *
 * [사용 API]
 * GET /api/assessments/{assessmentId}/risk-detail
 *
 * [연결 기능]
 * AI-F-002 : 직무별 산업재해 통계 근거 조회
 * AI-F-003 : 통계 근거 기반 설명 생성
 *
 * [현재 정책]
 * F-002 / F-003은 개인 위험점수를 산출하지 않는다.
 *
 * 따라서 EVIDENCE_ONLY 결과에서는
 * riskScore, riskBand, riskGrade가 null이다.
 *
 * 기존 필드는 하위 호환성을 위해 유지한다.
 */
public class AssessmentRiskDetailResponse {

    // ========================================================
    // 1. 기존 위험도 응답 필드
    // ========================================================

    /**
     * 개인 위험점수.
     *
     * 현재 F-002에서는 계산하지 않으므로 null.
     */
    private Integer riskScore;

    /**
     * 위험 구간.
     *
     * 예: 낮음 / 보통 / 높음
     *
     * 현재 F-002에서는 null.
     */
    private String riskBand;

    /**
     * 위험 등급.
     *
     * 예: LOW / MID / HIGH
     *
     * 현재 F-002에서는 null.
     */
    private String riskGrade;

    /**
     * 통계 근거 및 설명 요약.
     */
    private String summary;

    /**
     * 주요 설명 및 한계사항.
     */
    private List<String> factorSummaries = new ArrayList<>();

    /**
     * 결과 해석 가이드.
     */
    private String guidance;

    /**
     * 면책 및 주의 문구.
     */
    private String disclaimer;

    // ========================================================
    // 2. F-002 / F-003 신규 응답 필드
    // ========================================================

    /**
     * F-002 통계 근거 원본 JSON.
     *
     * 포함 가능한 항목:
     * - job_id
     * - title
     * - industry_candidate
     * - mapping_status
     * - evidence_status
     * - evidence_year
     * - industry_accident_count
     * - evidence_usable
     */
    private JsonNode evidence;

    /**
     * F-003 설명 원본 JSON.
     *
     * 포함 가능한 항목:
     * - summary
     * - limitations
     * - explanation_method
     * - explanation_status
     */
    private JsonNode explanation;

    /**
     * 결과 처리 상태.
     *
     * 현재 값:
     * EVIDENCE_ONLY
     */
    private String dataStatus;

    /**
     * 저장된 결과 버전.
     *
     * 예:
     * EVIDENCE_ONLY_V1
     */
    private String modelVersion;

    // ========================================================
    // 3. Getter / Setter
    // ========================================================

    public Integer getRiskScore() {
        return riskScore;
    }

    public void setRiskScore(Integer riskScore) {
        this.riskScore = riskScore;
    }

    public String getRiskBand() {
        return riskBand;
    }

    public void setRiskBand(String riskBand) {
        this.riskBand = riskBand;
    }

    public String getRiskGrade() {
        return riskGrade;
    }

    public void setRiskGrade(String riskGrade) {
        this.riskGrade = riskGrade;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public List<String> getFactorSummaries() {
        return factorSummaries;
    }

    public void setFactorSummaries(
            List<String> factorSummaries
    ) {
        this.factorSummaries =
                factorSummaries != null
                        ? factorSummaries
                        : new ArrayList<>();
    }

    public String getGuidance() {
        return guidance;
    }

    public void setGuidance(String guidance) {
        this.guidance = guidance;
    }

    public String getDisclaimer() {
        return disclaimer;
    }

    public void setDisclaimer(String disclaimer) {
        this.disclaimer = disclaimer;
    }

    public JsonNode getEvidence() {
        return evidence;
    }

    public void setEvidence(JsonNode evidence) {
        this.evidence = evidence;
    }

    public JsonNode getExplanation() {
        return explanation;
    }

    public void setExplanation(JsonNode explanation) {
        this.explanation = explanation;
    }

    public String getDataStatus() {
        return dataStatus;
    }

    public void setDataStatus(String dataStatus) {
        this.dataStatus = dataStatus;
    }

    public String getModelVersion() {
        return modelVersion;
    }

    public void setModelVersion(String modelVersion) {
        this.modelVersion = modelVersion;
    }
}

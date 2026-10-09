
package com.example.demo.ai.client;

import com.example.demo.global.exception.ApiException;
import com.fasterxml.jackson.databind.JsonNode;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

import java.net.SocketTimeoutException;
import java.util.Map;
import java.util.concurrent.TimeoutException;

/**
 * Spring Boot -> FastAPI HTTP 통신.
 *
 * F-001 : 직무 분석
 * F-002 : 통계 근거
 * F-003 : 근거 기반 설명
 *
 * F-004 : 개인 참고 위험 지수 (사고 확률이 아님)
 */
@Component
public class AIClient {

    private final RestTemplate restTemplate;
    private final String baseUrl;

    public AIClient(
            RestTemplate restTemplate,
            @Value("${app.ai.base-url:http://localhost:8000}")
            String baseUrl
    ) {
        this.restTemplate = restTemplate;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
    }

    /**
     * F-001 통합 직무 분석.
     */
    public JsonNode analyzeJob(
            String title,
            String taskModel
    ) {
        try {
            return restTemplate.postForObject(
                    baseUrl + "/api/v1/jobs/analyze-integrated",
                    Map.of(
                            "title", title,
                            "task_model", taskModel
                    ),
                    JsonNode.class
            );
        } catch (RestClientException ex) {
            throw mapException("F-001 직무 분석 실패", ex);
        }
    }

    public JsonNode calculatePersonalRisk(Map<String, Object> request) {
        try {
            return restTemplate.postForObject(
                    baseUrl + "/api/v1/risk/personal-score", request, JsonNode.class);
        } catch (RestClientException ex) {
            throw mapException("개인 참고 위험 지수 산출 실패", ex);
        }
    }

    /**
     * F-001 직무 예측.
     */
    public JsonNode predictJob(String title) {
        try {
            return restTemplate.postForObject(
                    baseUrl + "/api/v1/jobs/predict",
                    Map.of("title", title),
                    JsonNode.class
            );
        } catch (RestClientException ex) {
            throw mapException("F-001 직무 예측 실패", ex);
        }
    }

    /**
     * F-002 직무별 산업재해 통계 근거.
     */
    public JsonNode getRiskEvidence(String jobId) {
        try {
            return restTemplate.getForObject(
                    jobUrl(jobId) + "/risk-evidence",
                    JsonNode.class
            );
        } catch (RestClientException ex) {
            throw mapException("F-002 통계 근거 조회 실패", ex);
        }
    }

    /**
     * F-002 통합 통계 근거.
     */
    public JsonNode getRiskSummary(String jobId) {
        try {
            return restTemplate.getForObject(
                    jobUrl(jobId) + "/risk-summary",
                    JsonNode.class
            );
        } catch (RestClientException ex) {
            throw mapException("F-002 통합 근거 조회 실패", ex);
        }
    }

    /**
     * F-002 연령별 통계.
     */
    public JsonNode getAgeStatistics(int year) {
        try {
            return restTemplate.getForObject(
                    baseUrl + "/api/v1/risk/age-statistics?year={year}",
                    JsonNode.class,
                    year
            );
        } catch (RestClientException ex) {
            throw mapException("F-002 연령별 통계 조회 실패", ex);
        }
    }

    /**
     * F-003 규칙 기반 설명.
     */
    public JsonNode explainRisk(String jobId) {
        try {
            return restTemplate.getForObject(
                    jobUrl(jobId) + "/risk-explanation",
                    JsonNode.class
            );
        } catch (RestClientException ex) {
            throw mapException("F-003 설명 조회 실패", ex);
        }
    }

    /**
     * F-003 LLM 혼합 설명.
     */
    public JsonNode explainRiskHybrid(String jobId) {
        try {
            return restTemplate.getForObject(
                    jobUrl(jobId) + "/risk-explanation-hybrid",
                    JsonNode.class
            );
        } catch (RestClientException ex) {
            throw mapException("F-003 혼합 설명 조회 실패", ex);
        }
    }

    /**
     * FastAPI 헬스 체크.
     */
    public boolean isHealthy() {
        try {
            restTemplate.getForObject(
                    baseUrl + "/health",
                    String.class
            );
            return true;
        } catch (RestClientException ex) {
            return false;
        }
    }

    /**
     * 외부 공고 ID를 안전하게 URL에 사용.
     */
    private String jobUrl(String jobId) {
        if (jobId == null
                || !jobId.matches("[A-Za-z0-9_-]+")) {
            throw ApiException.badRequest(
                    "Invalid external job ID"
            );
        }

        return baseUrl + "/api/v1/jobs/" + jobId;
    }

    /**
     * HTTP 오류를 공통 예외로 변환.
     */
    private static ApiException mapException(
            String message,
            RestClientException cause
    ) {
        Throwable current = cause;

        while (current != null) {
            if (current instanceof SocketTimeoutException
                    || current instanceof TimeoutException) {
                return ApiException.aiTimeout(message, cause);
            }

            String detail = current.getMessage();

            if (detail != null) {
                String lower = detail.toLowerCase();

                if (lower.contains("timed out")
                        || lower.contains("timeout")) {
                    return ApiException.aiTimeout(message, cause);
                }
            }

            current = current.getCause();
        }

        return ApiException.aiUnavailable(message, cause);
    }
}

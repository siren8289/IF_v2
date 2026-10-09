
package com.example.demo.ai.service;

import com.example.demo.ai.client.AIClient;
import com.example.demo.ai.entity.AIRiskResult;
import com.example.demo.ai.repository.AIRiskResultRepository;
import com.example.demo.assessment.dto.AssessmentRiskDetailResponse;
import com.example.demo.assessment.entity.Assessment;
import com.example.demo.assessment.entity.AssessmentStatus;
import com.example.demo.assessment.repository.AssessmentRepository;
import com.example.demo.global.exception.ApiException;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.support.TransactionTemplate;

import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.LinkedHashMap;

/** F-004 개인 참고 지수를 저장한다. F-002/F-003 근거와 이전 결과 조회는 유지한다.
 * 외부 추론은 DB 트랜잭션 밖에서 실행하며 점수는 사고 확률이 아니다. */
@Service
public class AIRiskService {

    private static final Logger log =
            LoggerFactory.getLogger(AIRiskService.class);

    private static final String MODEL_VERSION =
            "PERSONAL_INDEX_V1";

    private final AIClient aiClient;
    private final AssessmentRepository assessmentRepository;
    private final AIRiskResultRepository riskResultRepository;
    private final ObjectMapper objectMapper;
    private final TransactionTemplate transactionTemplate;

    public AIRiskService(
            AIClient aiClient,
            AssessmentRepository assessmentRepository,
            AIRiskResultRepository riskResultRepository,
            ObjectMapper objectMapper,
            PlatformTransactionManager transactionManager
    ) {
        this.aiClient = aiClient;
        this.assessmentRepository = assessmentRepository;
        this.riskResultRepository = riskResultRepository;
        this.objectMapper = objectMapper;
        this.transactionTemplate =
                new TransactionTemplate(transactionManager);
    }

    public void computeAndSaveRisk(Long assessmentId) {
        Map<String, Object> request = transactionTemplate.execute(status -> scoreInputs(findAssessment(assessmentId)));
        JsonNode payload = aiClient.calculatePersonalRisk(request);
        validateResult(payload, request);
        transactionTemplate.executeWithoutResult(status -> {
            Assessment assessment = assessmentRepository.findByIdForUpdate(assessmentId)
                    .orElseThrow(() -> ApiException.notFound("Assessment not found: " + assessmentId));
            if (!request.equals(scoreInputs(assessment))) {
                throw ApiException.badRequest("Assessment inputs changed during scoring");
            }
            AIRiskResult result = riskResultRepository.findByAssessment_Id(assessmentId).orElseGet(AIRiskResult::new);
            result.setAssessment(assessment);
            result.setTotalRiskPercent(payload.get("risk_score").intValue());
            result.setRiskGrade(payload.get("risk_grade").asText());
            result.setModelVersion(MODEL_VERSION);
            result.setGeneratedAt(OffsetDateTime.now(ZoneOffset.UTC));
            result.setExplanationJson(payload.toString());
            assessment.setAiRiskResult(riskResultRepository.save(result));
            if (assessment.getStatus() == AssessmentStatus.PENDING_AI) {
                assessment.setStatus(AssessmentStatus.AI_COMPLETED);
            }
            assessmentRepository.save(assessment);
        });
    }

    private Map<String, Object> scoreInputs(Assessment assessment) {
        if (assessment.getStatus() == AssessmentStatus.FINALIZED) {
            throw ApiException.invalidTransition("Finalized assessment cannot be recalculated");
        }
        if (assessment.getJob() == null || assessment.getApplicant() == null || assessment.getHealthSnapshot() == null) {
            throw ApiException.badRequest("Job, applicant and health snapshot are required");
        }
        var health = assessment.getHealthSnapshot();
        var job = assessment.getJob();
        Integer age = assessment.getApplicant().getAge();
        if (age == null || age < 1 || age > 120 || health.getPhysicalLevel() == null
                || health.getPhysicalLevel() < 1 || health.getPhysicalLevel() > 5
                || health.getChronicDiseaseFlag() == null || health.getWorkHourLimit() == null
                || health.getWorkHourLimit() < 1 || health.getWorkHourLimit() > 24
                || job.getJobTitle() == null || job.getJobTitle().isBlank() || job.getJobTitle().trim().length() > 300) {
            throw ApiException.badRequest("Incomplete or invalid personal scoring inputs");
        }
        Map<String, Object> request = new LinkedHashMap<>();
        String externalId = job.getExternalJobId();
        request.put("job_id", externalId == null || externalId.isBlank() ? null : externalId.trim());
        request.put("title", job.getJobTitle().trim());
        request.put("age", age);
        request.put("physical_level", health.getPhysicalLevel());
        request.put("chronic_disease", health.getChronicDiseaseFlag());
        request.put("work_hour_limit", health.getWorkHourLimit());
        return request;
    }

    private void validateResult(JsonNode payload, Map<String, Object> request) {
        if (payload == null || !payload.isObject()) throw ApiException.invalidAiScore("Missing score response");
        JsonNode score = payload.path("risk_score");
        if (!score.isIntegralNumber() || !score.canConvertToInt() || score.intValue() < 0 || score.intValue() > 100
                || !gradeOf(score.intValue()).equals(payload.path("risk_grade").asText())
                || !"REFERENCE_INDEX".equals(payload.path("score_type").asText())
                || !MODEL_VERSION.equals(payload.path("model_version").asText())
                || !"SCORED_REVIEW_REQUIRED".equals(payload.path("assessment_status").asText())
                || !payload.path("review_required").isBoolean() || !payload.path("review_required").booleanValue()
                || !payload.has("risk_probability") || !payload.get("risk_probability").isNull()
                || !objectMapper.valueToTree(request).equals(payload.path("inputs"))
                || !payload.path("factors").isArray() || payload.path("factors").isEmpty()
                || !payload.path("limitations").isArray() || payload.path("limitations").isEmpty()) {
            throw ApiException.invalidAiScore("Invalid reference index response");
        }
    }

    public static String gradeOf(double score) {
        if (!Double.isFinite(score) || score < 0 || score > 100) {
            throw ApiException.invalidAiScore("Score must be finite and within 0~100");
        }
        return score <= 40 ? "LOW" : score <= 60 ? "MID" : "HIGH";
    }

    /** 이전 한글 등급 표현과의 호환. 계산되지 않은 점수에는 사용하지 않는다. */
    public static String gradeOfBand(String band) {
        if ("낮음".equals(band)) return "LOW";
        if ("높음".equals(band) || "매우 높음".equals(band)) return "HIGH";
        return "MID";
    }

    /**
     * [기능] 저장된 통계 근거 및 설명 조회.
     *
     * 이전 EVIDENCE_ONLY 데이터에서는 점수와 등급을 null로 유지한다.
     */
    public AssessmentRiskDetailResponse getRiskDetail(
            Long assessmentId
    ) {

        return transactionTemplate.execute(status -> {

            Assessment assessment =
                    findAssessment(assessmentId);

            AIRiskResult result = riskResultRepository
                    .findByAssessment_Id(assessmentId)
                    .orElseThrow(() -> ApiException.notFound(
                            "AI evidence not found: " + assessmentId
                    ));

            AssessmentRiskDetailResponse response =
                    new AssessmentRiskDetailResponse();

            response.setRiskScore(
                    result.getTotalRiskPercent()
            );

            response.setRiskGrade(
                    result.getRiskGrade()
            );

            response.setRiskBand(null);
            response.setModelVersion(result.getModelVersion());

            String storedJson =
                    result.getExplanationJson();

            if (storedJson == null || storedJson.isBlank()) {
                return response;
            }

            try {
                JsonNode payload =
                        objectMapper.readTree(storedJson);

                if ("SCORED_REVIEW_REQUIRED".equals(payload.path("assessment_status").asText())) {
                    response.setDataStatus("SCORED_REVIEW_REQUIRED");
                    response.setScoreType(payload.path("score_type").asText());
                    response.setReviewRequired(true);
                    response.setCalculation(payload);
                    response.setEvidence(payload.get("evidence"));
                    response.setExplanation(payload.get("explanation"));
                    response.setSummary(payload.path("summary").asText());
                    response.setGuidance(payload.path("guidance").asText());
                    List<String> limitations = new ArrayList<>();
                    payload.path("limitations").forEach(item -> limitations.add(item.asText()));
                    response.setLimitations(limitations);
                    response.setDisclaimer(String.join("\n", limitations));
                    List<String> factors = new ArrayList<>();
                    payload.path("factors").forEach(item -> factors.add(
                            item.path("label").asText() + ": " + item.path("points").asText() + "점 / "
                            + item.path("maximum").asText() + "점 — " + item.path("basis").asText()));
                    response.setFactorSummaries(factors);
                    return response;
                }

                // 이전 EVIDENCE_ONLY 구조
                if ("EVIDENCE_ONLY".equals(
                        payload.path("assessment_status").asText()
                )) {

                    JsonNode evidence =
                            payload.path("evidence");

                    JsonNode explanation =
                            payload.path("explanation");

                    response.setEvidence(
                            evidence.isMissingNode()
                                    || evidence.isNull()
                                    ? null
                                    : evidence
                    );

                    response.setExplanation(
                            explanation.isMissingNode()
                                    || explanation.isNull()
                                    ? null
                                    : explanation
                    );

                    response.setDataStatus(
                            payload.path("assessment_status")
                                    .asText()
                    );

                    response.setSummary(
                            explanation.path("summary")
                                    .asText(
                                            "직무 관련 통계 근거가 조회되었습니다."
                                    )
                    );

                    response.setGuidance(
                            "산업재해 통계는 직무 참고 자료이며 "
                                    + "개인의 사고 확률이나 위험점수가 아닙니다."
                    );

                    response.setDisclaimer(
                            "산업 분류 매핑은 검토가 필요하며, "
                                    + "통계 자료만으로 개인의 적합성이나 "
                                    + "안전성을 판정할 수 없습니다."
                    );

                    List<String> factors =
                            new ArrayList<>();

                    JsonNode limitations =
                            explanation.path("limitations");

                    if (!limitations.isArray()) {
                        limitations =
                                evidence.path("limitations");
                    }

                    if (limitations.isArray()) {
                        for (JsonNode item : limitations) {
                            factors.add(item.asText());
                        }
                    }

                    response.setFactorSummaries(factors);

                    return response;
                }

                // 이전 형식의 점수 데이터와 호환
                response.setSummary(
                        payload.path("summary").asText(null)
                );

                response.setGuidance(
                        payload.path("guidance").asText(null)
                );

                response.setDisclaimer(
                        payload.path("disclaimer").asText(null)
                );

                JsonNode factors =
                        payload.path("factor_explanations");

                if (factors.isArray()) {
                    List<String> summaries =
                            new ArrayList<>();

                    for (JsonNode factor : factors) {
                        String name =
                                factor.path("name").asText("");

                        String description =
                                factor.path("text").asText("");

                        summaries.add(
                                name.isBlank()
                                        ? description
                                        : name + ": " + description
                        );
                    }

                    response.setFactorSummaries(summaries);
                }

                return response;

            } catch (JsonProcessingException ex) {

                log.warn(
                        "Invalid stored AI JSON: assessmentId={}",
                        assessmentId,
                        ex
                );

                response.setSummary(
                        "저장된 AI 결과를 해석할 수 없습니다."
                );

                return response;
            }
        });
    }

    /**
     * 평가 ID로 Assessment 조회.
     */
    private Assessment findAssessment(Long assessmentId) {

        if (assessmentId == null || assessmentId <= 0) {
            throw ApiException.badRequest(
                    "assessmentId must be positive"
            );
        }

        return assessmentRepository.findById(assessmentId)
                .orElseThrow(() -> ApiException.notFound(
                        "Assessment not found: " + assessmentId
                ));
    }
}

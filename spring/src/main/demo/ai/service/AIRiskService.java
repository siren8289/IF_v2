
package com.example.demo.ai.service;

import com.example.demo.ai.client.AIClient;
import com.example.demo.ai.entity.AIRiskResult;
import com.example.demo.ai.repository.AIRiskResultRepository;
import com.example.demo.assessment.dto.AssessmentRiskDetailResponse;
import com.example.demo.assessment.entity.Assessment;
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

/**
 * AI-F-002 / AI-F-003 통합 서비스.
 *
 * [처리 흐름]
 * Assessment 조회
 *   -> Job.externalJobId 확인
 *   -> FastAPI F-002 통계 근거 조회
 *   -> FastAPI F-003 설명 조회
 *   -> PostgreSQL 결과 저장
 *
 * [중요]
 * F-002는 개인 위험점수 산출 모델이 아니다.
 * 따라서 riskScore, riskGrade는 null로 유지한다.
 *
 * 통계 근거만 조회했을 때 Assessment 상태를
 * AI_COMPLETED로 변경하지 않는다.
 *
 * 외부 HTTP 호출 중 DB 트랜잭션을 유지하지 않는다.
 */
@Service
public class AIRiskService {

    private static final Logger log =
            LoggerFactory.getLogger(AIRiskService.class);

    private static final String MODEL_VERSION =
            "EVIDENCE_ONLY_V1";

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

    /**
     * [기능] 통계 근거 및 설명 조회 후 저장.
     *
     * 기존 Controller의 computeAndSaveRisk() 호출을
     * 유지하기 위해 메서드 이름은 변경하지 않는다.
     */
    public void computeAndSaveRisk(Long assessmentId) {

        // 1. DB에서 외부 공고 ID 조회
        String externalJobId = transactionTemplate.execute(
                status -> {
                    Assessment assessment =
                            findAssessment(assessmentId);

                    if (assessment.getJob() == null) {
                        throw ApiException.badRequest(
                                "Assessment has no linked job"
                        );
                    }

                    String externalId =
                            assessment.getJob().getExternalJobId();

                    if (externalId == null
                            || externalId.isBlank()) {
                        throw ApiException.badRequest(
                                "Job has no externalJobId: "
                                        + assessment.getJob().getId()
                        );
                    }

                    return externalId.trim();
                }
        );

        log.info(
                "AI evidence lookup started: assessmentId={}, externalJobId={}",
                assessmentId,
                externalJobId
        );

        // 2. FastAPI F-002 호출 (트랜잭션 밖)
        JsonNode evidence =
                aiClient.getRiskEvidence(externalJobId);

        if (evidence == null
                || evidence.isNull()
                || !evidence.isObject()) {
            throw ApiException.badRequest(
                    "Invalid F-002 evidence response"
            );
        }

        // 응답의 공고 ID가 요청 ID와 일치하는지 확인
        String returnedJobId =
                evidence.path("job_id").asText("");

        if (!externalJobId.equals(returnedJobId)) {
            throw ApiException.badRequest(
                    "F-002 job_id mismatch"
            );
        }

        // 3. FastAPI F-003 호출
        // 설명 호출에 실패해도 F-002 근거는 저장
        JsonNode explanation = null;

        try {
            explanation =
                    aiClient.explainRisk(externalJobId);

        } catch (ApiException ex) {
            String errorCode = ex.getErrorCode();

            if (!"AI_SERVICE_TIMEOUT".equals(errorCode)
                    && !"AI_SERVICE_UNAVAILABLE".equals(errorCode)) {
                throw ex;
            }

            log.warn(
                    "F-003 explanation unavailable: assessmentId={}, error={}",
                    assessmentId,
                    errorCode
            );
        }

        // 4. 저장할 JSON 구성
        ObjectNode payload = objectMapper.createObjectNode();

        payload.put("assessment_status", "EVIDENCE_ONLY");
        payload.put("external_job_id", externalJobId);
        payload.set("evidence", evidence);

        if (explanation != null && explanation.isObject()) {
            payload.set("explanation", explanation);
        } else {
            payload.putNull("explanation");
        }

        // 5. 별도 트랜잭션에서 저장
        transactionTemplate.executeWithoutResult(status ->
                saveEvidence(assessmentId, payload)
        );

        log.info(
                "AI evidence saved: assessmentId={}, externalJobId={}",
                assessmentId,
                externalJobId
        );
    }

    /**
     * [기능] F-002 / F-003 결과 저장.
     *
     * 동일 Assessment에 기존 결과가 있으면 갱신한다.
     */
    private void saveEvidence(
            Long assessmentId,
            ObjectNode payload
    ) {

        Assessment assessment =
                findAssessment(assessmentId);

        // 외부 API 호출 중 공고가 변경되었는지 재확인
        String currentExternalId =
                assessment.getJob() == null
                        ? null
                        : assessment.getJob().getExternalJobId();

        String requestedExternalId =
                payload.path("external_job_id").asText("");

        if (currentExternalId == null
                || !currentExternalId.equals(requestedExternalId)) {
            throw ApiException.badRequest(
                    "Assessment job changed during evidence lookup"
            );
        }

        AIRiskResult result = riskResultRepository
                .findByAssessment_Id(assessmentId)
                .orElseGet(AIRiskResult::new);

        result.setAssessment(assessment);

        // F-002는 개인 위험점수를 계산하지 않는다.
        result.setTotalRiskPercent(null);
        result.setRiskGrade(null);

        result.setGeneratedAt(
                OffsetDateTime.now(ZoneOffset.UTC)
        );

        result.setModelVersion(MODEL_VERSION);

        result.setExplanationJson(
                payload.toString()
        );

        AIRiskResult saved =
                riskResultRepository.save(result);

        assessment.setAiRiskResult(saved);

        // 통계 근거 확보만으로 평가를 완료 처리하지 않는다.
        assessmentRepository.save(assessment);
    }

    /**
     * [기능] 저장된 통계 근거 및 설명 조회.
     *
     * 기존 응답 DTO의 점수 관련 필드는 null로 유지한다.
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

                // 현재 EVIDENCE_ONLY 구조
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

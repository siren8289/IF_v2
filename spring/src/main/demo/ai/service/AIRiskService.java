
package com.example.demo.ai.service;

import com.example.demo.ai.client.AIClient;
import com.example.demo.ai.dto.ExplainRequestDto;
import com.example.demo.ai.dto.ExplainResponseDto;
import com.example.demo.ai.dto.ScoreRequestDto;
import com.example.demo.ai.dto.ScoreResponseDto;
import com.example.demo.ai.entity.AIRiskResult;
import com.example.demo.ai.repository.AIRiskResultRepository;
import com.example.demo.applicant.entity.Applicant;
import com.example.demo.applicant.entity.HealthSnapshot;
import com.example.demo.assessment.dto.AssessmentRiskDetailResponse;
import com.example.demo.assessment.entity.Assessment;
import com.example.demo.assessment.entity.AssessmentStatus;
import com.example.demo.assessment.repository.AssessmentRepository;
import com.example.demo.global.exception.ApiException;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.support.TransactionTemplate;

import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.ArrayList;
import java.util.List;

/**
 * AI 위험도 평가 서비스.
 *
 * [업무 흐름]
 * Assessment 조회
 *   -> FastAPI 요청 데이터 생성
 *   -> POST /score
 *   -> 점수 검증
 *   -> POST /explain (선택)
 *   -> AI 결과 DB 저장
 *   -> 평가 상태 AI_COMPLETED
 *
 * [트랜잭션]
 * 외부 HTTP 요청 중에는 DB 트랜잭션을 유지하지 않는다.
 *
 * [장애 처리]
 * /score 실패   : 저장하지 않고 오류 반환
 * /explain 실패 : 점수만 저장하고 정상 완료
 */
@Service
public class AIRiskService {

    private static final Logger log =
            LoggerFactory.getLogger(AIRiskService.class);

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
     * [기능] AI 위험도 계산 및 저장.
     *
     * 1. DB에서 평가 데이터 조회
     * 2. FastAPI 점수 계산
     * 3. AI 응답값 검증
     * 4. 설명 생성 시도
     * 5. DB에 결과 저장
     */
    public void computeAndSaveRisk(Long assessmentId) {

        // 1. DB 조회만 짧은 트랜잭션에서 수행한다.
        Prep prep = transactionTemplate.execute(status -> {

            ScoreRequestDto request =
                    buildScoreRequest(assessmentId);

            Assessment assessment = findAssessment(assessmentId);

            Integer age =
                    assessment.getApplicant().getAge();

            return new Prep(request, age);
        });

        if (prep == null) {
            throw ApiException.badRequest(
                    "Failed to prepare AI risk request"
            );
        }

        ScoreRequestDto scoreRequest = prep.scoreRequest();

        log.info(
                "AI scoring started: assessmentId={}",
                assessmentId
        );

        // 2. 외부 API 호출: DB 트랜잭션 밖에서 실행한다.
        ScoreResponseDto scoreResponse =
                aiClient.score(scoreRequest);

        // 3. AI 응답이 정상인지 확인한다.
        validateRiskScore(scoreResponse);

        // 4. 설명 생성 요청을 준비한다.
        ExplainRequestDto explainRequest =
                new ExplainRequestDto();

        explainRequest.setRiskScore(
                scoreResponse.getRiskScore()
        );
        explainRequest.setRiskBand(
                scoreResponse.getRiskBand()
        );
        explainRequest.setTopFactors(
                scoreResponse.getTopFactors()
        );
        explainRequest.setCaseSummary(
                buildCaseSummary(scoreRequest, prep.age())
        );

        ExplainResponseDto explainResponse = null;

        try {
            // 설명 생성은 선택 기능이다.
            explainResponse = aiClient.explain(explainRequest);

        } catch (ApiException ex) {

            // 외부 AI 서비스 장애인 경우에만 fallback 처리한다.
            String code = ex.getErrorCode();

            if (!"AI_SERVICE_TIMEOUT".equals(code)
                    && !"AI_SERVICE_UNAVAILABLE".equals(code)) {
                throw ex;
            }

            log.warn(
                    "AI explanation fallback: assessmentId={}, error={}",
                    assessmentId,
                    code
            );
        }

        // 람다에서 사용할 최종 참조값.
        ExplainResponseDto finalExplanation = explainResponse;

        // 5. 결과 저장은 별도 트랜잭션에서 실행한다.
        transactionTemplate.executeWithoutResult(status ->
                persistScoreResult(
                        assessmentId,
                        scoreResponse,
                        finalExplanation
                )
        );

        log.info(
                "AI scoring completed: assessmentId={}, riskScore={}",
                assessmentId,
                scoreResponse.getRiskScore()
        );
    }

    /**
     * DB 조회 결과를 외부 API 호출까지 전달하기 위한 내부 자료형.
     */
    private record Prep(
            ScoreRequestDto scoreRequest,
            Integer age
    ) {}

    /**
     * [기능] Assessment -> FastAPI 요청 DTO 변환.
     */
    private ScoreRequestDto buildScoreRequest(Long assessmentId) {

        Assessment assessment = findAssessment(assessmentId);

        Applicant applicant = assessment.getApplicant();
        HealthSnapshot health = assessment.getHealthSnapshot();
        var job = assessment.getJob();

        ScoreRequestDto request = new ScoreRequestDto();

        // 신청자 연령 구간
        request.setAgeBand(
                ageToBand(applicant.getAge())
        );

        // 일자리 지역
        request.setRegion(
                defaultText(job.getWorkplace(), "기타")
        );

        // 일자리 직무명
        request.setJobCategory(
                defaultText(job.getJobTitle(), "기타")
        );

        // 신청자의 신체 수준
        Integer physicalLevel = health.getPhysicalLevel();

        request.setPhysicalLevel(physicalLevel);

        /*
         * 주의:
         * 현재 Job 엔티티에는 별도 업무 강도 필드가 없다.
         *
         * 기존 코드는 신체 수준을 업무 강도로 변환했지만,
         * 두 값은 서로 다른 개념이다.
         *
         * 따라서 현재는 null로 전달한다.
         * FastAPI가 허용하는지 API 스키마 확인이 필요하다.
         *
         * 추후 Job.workIntensity 추가 후 연결한다.
         */
        request.setWorkIntensity(null);

        // 아직 구조화되지 않은 위험 요인은 빈 목록으로 전달.
        request.setEnvironmentFlags(new ArrayList<>());
        request.setHealthFlags(new ArrayList<>());

        // 만성질환 여부
        request.setChronicDiseaseFlag(
                health.getChronicDiseaseFlag()
        );

        return request;
    }

    /**
     * [기능] AI 점수 유효성 검증.
     *
     * 허용 범위: 0 ~ 100
     *
     * NaN, Infinity, 범위 밖 숫자는 저장하지 않는다.
     */
    private void validateRiskScore(ScoreResponseDto response) {

        if (response == null) {
            throw ApiException.invalidAiScore(
                    "AI scoring response is empty"
            );
        }

        double score = response.getRiskScore();

        if (!Double.isFinite(score)
                || score < 0.0
                || score > 100.0) {

            throw ApiException.invalidAiScore(
                    "Invalid AI risk score: " + score
            );
        }
    }

    /**
     * [기능] AI 계산 결과 저장.
     *
     * 동일 assessmentId에 결과가 있으면 업데이트한다.
     */
    private void persistScoreResult(
            Long assessmentId,
            ScoreResponseDto scoreResponse,
            ExplainResponseDto explainResponse
    ) {

        Assessment assessment = findAssessment(assessmentId);

        // 설명 응답을 JSON 문자열로 변환한다.
        String explanationJson = null;

        if (explainResponse != null) {
            try {
                explanationJson =
                        objectMapper.writeValueAsString(
                                explainResponse
                        );
            } catch (JsonProcessingException ex) {
                log.warn(
                        "Failed to serialize AI explanation: assessmentId={}",
                        assessmentId,
                        ex
                );
            }
        }

        // 기존 결과가 있다면 재사용한다.
        AIRiskResult result = riskResultRepository
                .findByAssessment_Id(assessmentId)
                .orElseGet(assessment::getAiRiskResult);

        if (result == null) {
            result = new AIRiskResult();
        }

        result.setAssessment(assessment);

        result.setTotalRiskPercent(
                (int) Math.round(scoreResponse.getRiskScore())
        );

        result.setRiskGrade(
                gradeOf(scoreResponse.getRiskScore())
        );

        result.setGeneratedAt(
                OffsetDateTime.now(ZoneOffset.UTC)
        );

        String version = scoreResponse.getScoringVersion();

        result.setModelVersion(
                version != null && !version.isBlank()
                        ? version
                        : "rule_stat_v1"
        );

        result.setExplanationJson(explanationJson);

        AIRiskResult saved =
                riskResultRepository.save(result);

        assessment.setAiRiskResult(saved);

        // AI 계산 완료 후에만 상태를 변경한다.
        if (assessment.getStatus() == AssessmentStatus.PENDING_AI) {

            if (!assessment.getStatus()
                    .canTransitionTo(AssessmentStatus.AI_COMPLETED)) {

                throw ApiException.invalidTransition(
                        "Cannot complete AI assessment: "
                                + assessmentId
                );
            }

            assessment.setStatus(AssessmentStatus.AI_COMPLETED);
        }

        assessmentRepository.save(assessment);
    }

    /**
     * [규칙] 위험도 점수를 LOW/MID/HIGH로 변환.
     */
    public static String gradeOf(double score) {

        if (score <= 40.0) {
            return "LOW";
        }

        if (score <= 60.0) {
            return "MID";
        }

        return "HIGH";
    }

    /**
     * FastAPI 한글 위험 구간 -> 내부 위험 등급.
     */
    public static String gradeOfBand(String band) {

        if (band == null) {
            return "MID";
        }

        return switch (band) {
            case "낮음" -> "LOW";
            case "높음", "매우 높음" -> "HIGH";
            default -> "MID";
        };
    }

    /**
     * [기능] 저장된 AI 위험도 상세 조회.
     */
    @Transactional(readOnly = true)
    public AssessmentRiskDetailResponse getRiskDetail(
            Long assessmentId
    ) {

        Assessment assessment = findAssessment(assessmentId);

        AIRiskResult result = assessment.getAiRiskResult();

        if (result == null
                || result.getTotalRiskPercent() == null) {

            throw ApiException.notFound(
                    "AI risk result not found: " + assessmentId
            );
        }

        AssessmentRiskDetailResponse response =
                new AssessmentRiskDetailResponse();

        response.setRiskScore(result.getTotalRiskPercent());
        response.setRiskGrade(result.getRiskGrade());

        String band = switch (
                result.getRiskGrade() != null
                        ? result.getRiskGrade()
                        : "MID"
                ) {
            case "LOW" -> "낮음";
            case "HIGH" -> "높음";
            default -> "보통";
        };

        response.setRiskBand(band);

        String explanationJson = result.getExplanationJson();

        if (explanationJson == null
                || explanationJson.isBlank()) {

            return response;
        }

        try {
            ExplainResponseDto explanation =
                    objectMapper.readValue(
                            explanationJson,
                            ExplainResponseDto.class
                    );

            response.setSummary(explanation.getSummary());
            response.setGuidance(explanation.getGuidance());
            response.setDisclaimer(explanation.getDisclaimer());

            if (explanation.getFactorExplanations() != null) {

                List<String> factors = new ArrayList<>();

                explanation.getFactorExplanations().forEach(factor -> {

                    String name =
                            defaultText(factor.getName(), "");

                    String description =
                            defaultText(factor.getText(), "");

                    factors.add(
                            name.isBlank()
                                    ? description
                                    : name + ": " + description
                    );
                });

                response.setFactorSummaries(factors);
            }

        } catch (JsonProcessingException ex) {

            log.warn(
                    "Invalid stored AI explanation: assessmentId={}",
                    assessmentId,
                    ex
            );

            response.setSummary(
                    "저장된 AI 설명을 불러오지 못했습니다."
            );

            response.setDisclaimer(
                    "본 결과는 판단 보조 자료이며 최종 판단은 담당자가 수행합니다."
            );
        }

        return response;
    }

    /**
     * 평가 ID로 조회하고 존재하지 않으면 404 반환.
     */
    private Assessment findAssessment(Long assessmentId) {

        return assessmentRepository.findById(assessmentId)
                .orElseThrow(() -> ApiException.notFound(
                        "Assessment not found: " + assessmentId
                ));
    }

    /**
     * 연령 -> FastAPI 연령 구간.
     *
     * 현재 65세 미만 입력에 대한 별도 구간이 없으므로
     * 기존 API 계약을 유지한다.
     * 추후 입력 검증 또는 구간 확장이 필요하다.
     */
    private static String ageToBand(Integer age) {

        if (age == null) return "65-69";
        if (age >= 75) return "75+";
        if (age >= 70) return "70-74";

        return "65-69";
    }

    /**
     * null/공백 문자열을 기본값으로 변환한다.
     */
    private static String defaultText(
            String value,
            String fallback
    ) {
        return value == null || value.isBlank()
                ? fallback
                : value;
    }

    /**
     * AI 설명 생성을 위한 입력 요약.
     */
    private static String buildCaseSummary(
            ScoreRequestDto request,
            Integer age
    ) {

        String chronicDisease =
                Boolean.TRUE.equals(request.getChronicDiseaseFlag())
                        ? ", 만성질환=예"
                        : "";

        String intensity = request.getWorkIntensity() == null
                ? "미확인"
                : request.getWorkIntensity();

        return String.format(
                "%s, %s세, %s 직무, 업무 강도=%s%s",
                request.getRegion(),
                age != null ? age : "-",
                request.getJobCategory(),
                intensity,
                chronicDisease
        );
    }
}

package com.example.demo.assessment.service;

import com.example.demo.ai.client.AIClient;
import com.example.demo.ai.entity.AIRiskResult;
import com.example.demo.ai.repository.AIRiskResultRepository;
import com.example.demo.applicant.entity.Applicant;
import com.example.demo.applicant.entity.HealthSnapshot;
import com.example.demo.applicant.repository.ApplicantRepository;
import com.example.demo.applicant.repository.HealthSnapshotRepository;
import com.example.demo.assessment.dto.AssessmentCreateRequest;
import com.example.demo.assessment.dto.AssessmentRecordResponse;
import com.example.demo.assessment.dto.AssessmentResultResponse;
import com.example.demo.assessment.dto.AssessmentResultResponse.Factor;
import com.example.demo.assessment.dto.AssessmentResultResponse.TaskScore;
import com.example.demo.assessment.dto.AssessmentSummaryResponse;
import com.example.demo.assessment.entity.Assessment;
import com.example.demo.assessment.entity.AssessmentStatus;
import com.example.demo.assessment.repository.AssessmentRepository;
import com.example.demo.global.exception.ApiException;
import com.example.demo.job.entity.Job;
import com.example.demo.job.repository.JobRepository;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class AssessmentService {

    private final AssessmentRepository assessmentRepository;
    private final ApplicantRepository applicantRepository;
    private final HealthSnapshotRepository healthRepository;
    private final JobRepository jobRepository;
    private final AIRiskResultRepository riskResultRepository;
    private final AIClient aiClient;
    private final ObjectMapper objectMapper;

    public AssessmentService(AssessmentRepository assessmentRepository,
                             ApplicantRepository applicantRepository,
                             HealthSnapshotRepository healthRepository,
                             JobRepository jobRepository,
                             AIRiskResultRepository riskResultRepository,
                             AIClient aiClient,
                             ObjectMapper objectMapper) {
        this.assessmentRepository = assessmentRepository;
        this.applicantRepository = applicantRepository;
        this.healthRepository = healthRepository;
        this.jobRepository = jobRepository;
        this.riskResultRepository = riskResultRepository;
        this.aiClient = aiClient;
        this.objectMapper = objectMapper;
    }

    /**
     * 평가를 저장하고 AI 분석까지 한 번에 한다.
     * AI 호출이 실패해도 평가는 남고 상태는 PENDING_AI로 유지된다.
     */
    public Long createAndAnalyze(AssessmentCreateRequest request) {
        Job job = jobRepository.findById(request.jobId())
                .orElseThrow(() -> ApiException.notFound("직무를 찾을 수 없습니다: " + request.jobId()));

        // 1. 신청자, 건강 정보, 평가 저장
        Applicant applicant = applicantRepository.save(
                new Applicant(request.applicantName().trim(), request.age()));

        HealthSnapshot health = healthRepository.save(new HealthSnapshot(
                applicant, request.physicalLevel(), request.chronicDisease(), request.workHourLimit()));

        Assessment assessment = new Assessment();
        assessment.setApplicant(applicant);
        assessment.setJob(job);
        assessment.setHealthSnapshot(health);
        assessment.setStatus(AssessmentStatus.PENDING_AI);
        assessment.setAssessedAt(OffsetDateTime.now(ZoneOffset.UTC));
        assessment = assessmentRepository.save(assessment);

        // 2. AI 서버 호출 (ML + DL + 점수 + 생성형 AI 설명)
        Map<String, Object> body = new HashMap<>();
        body.put("title", job.getJobTitle());
        body.put("age", request.age());
        body.put("physical_level", request.physicalLevel());
        body.put("chronic_disease", request.chronicDisease());
        body.put("work_hour_limit", request.workHourLimit());

        JsonNode aiResult = aiClient.analyze(body);
        checkAiResult(aiResult);

        // 3. AI 결과 저장
        AIRiskResult result = new AIRiskResult();
        result.setAssessment(assessment);
        result.setTotalRiskPercent(aiResult.get("risk_score").asInt());
        result.setRiskGrade(aiResult.get("risk_grade").asText());
        result.setModelVersion(aiResult.path("model_version").asText("SIMPLE_V1"));
        result.setGeneratedAt(OffsetDateTime.now(ZoneOffset.UTC));
        result.setExplanationJson(aiResult.toString());
        result = riskResultRepository.save(result);

        assessment.setAiRiskResult(result);
        assessment.setStatus(AssessmentStatus.AI_COMPLETED);
        assessmentRepository.save(assessment);

        return assessment.getId();
    }

    private void checkAiResult(JsonNode aiResult) {
        if (aiResult == null) {
            throw ApiException.aiError("AI 응답이 비어 있습니다.", null);
        }
        JsonNode score = aiResult.get("risk_score");
        if (score == null || !score.isIntegralNumber() || score.asInt() < 0 || score.asInt() > 100) {
            throw ApiException.aiError("AI 점수가 0~100 범위가 아닙니다.", null);
        }
        String grade = aiResult.path("risk_grade").asText();
        if (!grade.equals("LOW") && !grade.equals("MID") && !grade.equals("HIGH")) {
            throw ApiException.aiError("AI 등급 값이 올바르지 않습니다.", null);
        }
    }

    @Transactional(readOnly = true)
    public Page<AssessmentRecordResponse> list(Pageable pageable) {
        return assessmentRepository.findAllRecords(pageable);
    }

    @Transactional(readOnly = true)
    public AssessmentSummaryResponse summary() {
        return new AssessmentSummaryResponse(
                assessmentRepository.count(),
                assessmentRepository.countByAiRiskResult_RiskGrade("HIGH"),
                assessmentRepository.countByAiRiskResultIsNotNull());
    }

    @Transactional(readOnly = true)
    public AssessmentResultResponse getResult(Long id) {
        Assessment assessment = findAssessment(id);
        AIRiskResult ai = assessment.getAiRiskResult();

        Integer score = null;
        String grade = null;
        String explanation = null;
        String source = null;
        List<Factor> factors = new ArrayList<>();
        List<TaskScore> taskScores = new ArrayList<>();

        if (ai != null) {
            score = ai.getTotalRiskPercent();
            grade = ai.getRiskGrade();

            JsonNode json = readJson(ai.getExplanationJson());
            // 이전 버전에서 저장한 데이터는 필드 이름이 달라서 둘 다 읽는다.
            explanation = json.has("explanation")
                    ? json.get("explanation").asText()
                    : json.path("summary").asText(null);
            source = json.path("explanation_source").asText("basic");

            for (JsonNode f : json.path("factors")) {
                String name = f.has("name") ? f.get("name").asText() : f.path("label").asText();
                int max = f.has("max") ? f.get("max").asInt() : f.path("maximum").asInt();
                factors.add(new Factor(name, f.path("points").asDouble(), max));
            }

            JsonNode tasks = json.has("task_scores") ? json.get("task_scores") : json.path("task_basis");
            for (JsonNode t : tasks) {
                String name = t.has("name") ? t.get("name").asText() : t.path("label").asText();
                taskScores.add(new TaskScore(name, t.path("ml_score").asDouble(), t.path("dl_score").asDouble()));
            }
        }

        return new AssessmentResultResponse(
                assessment.getId(),
                assessment.getApplicant().getDisplayName(),
                assessment.getApplicant().getAge(),
                assessment.getJob().getJobTitle(),
                assessment.getStatus().name(),
                score, grade, explanation, source, factors, taskScores);
    }

    @Transactional
    public void delete(Long id) {
        Assessment assessment = findAssessment(id);

        // assessment ↔ ai_risk_result 가 서로를 참조하므로 연결을 먼저 끊고 지운다.
        AIRiskResult ai = assessment.getAiRiskResult();
        if (ai != null) {
            assessment.setAiRiskResult(null);
            assessmentRepository.saveAndFlush(assessment);
            riskResultRepository.delete(ai);
        }
        assessmentRepository.delete(assessment);
    }

    private Assessment findAssessment(Long id) {
        return assessmentRepository.findById(id)
                .orElseThrow(() -> ApiException.notFound("평가를 찾을 수 없습니다: " + id));
    }

    private JsonNode readJson(String text) {
        try {
            return objectMapper.readTree(text == null ? "{}" : text);
        } catch (JsonProcessingException e) {
            return objectMapper.createObjectNode();
        }
    }
}

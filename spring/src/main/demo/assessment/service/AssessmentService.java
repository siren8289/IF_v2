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

/**
 * 평가의 실제 일처리.
 *
 * 화면은 컨트롤러만 부르고, 컨트롤러는 이 클래스만 부른다.
 * 여기서 하는 일:
 *   1. 신청자, 건강 정보, 평가를 DB에 저장
 *   2. AI 서버(FastAPI)에 분석을 요청
 *   3. 점수와 설명을 다시 DB에 저장
 * AI 호출이 실패하면 예외가 나고, 평가는 PENDING_AI 상태로 남는다.
 * (저장과 AI 호출이 한 트랜잭션이 아니라서, 1번 저장은 롤백되지 않는다.)
 */
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
        // 없는 직무 번호면 404. 화면의 선택 목록에 있는 번호만 통과한다.
        Job job = jobRepository.findById(request.jobId())
                .orElseThrow(() -> ApiException.notFound("직무를 찾을 수 없습니다: " + request.jobId()));

        // 1. 신청자, 그 시점의 건강 정보, 평가 행을 각각 저장한다.
        //    건강 정보는 나중에 바꿔도 과거 평가가 흔들리지 않게 스냅샷으로 남긴다.
        Applicant applicant = applicantRepository.save(
                new Applicant(request.applicantName().trim(), request.age()));

        HealthSnapshot health = healthRepository.save(new HealthSnapshot(
                applicant, request.physicalLevel(), request.chronicDisease(), request.workHourLimit()));

        Assessment assessment = new Assessment();
        assessment.setApplicant(applicant);
        assessment.setJob(job);
        assessment.setHealthSnapshot(health);
        // AI가 끝나기 전에는 "분석 대기"다. 호출이 실패하면 이 상태로 남는다.
        assessment.setStatus(AssessmentStatus.PENDING_AI);
        assessment.setAssessedAt(OffsetDateTime.now(ZoneOffset.UTC));
        assessment = assessmentRepository.save(assessment);

        // 2. AI 서버가 이해하는 키 이름으로 요청을 만든다. (snake_case)
        Map<String, Object> body = new HashMap<>();
        body.put("title", job.getJobTitle());
        body.put("age", request.age());
        body.put("physical_level", request.physicalLevel());
        body.put("chronic_disease", request.chronicDisease());
        body.put("work_hour_limit", request.workHourLimit());

        JsonNode aiResult = aiClient.analyze(body);
        // 점수나 등급이 빠지거나 범위 밖이면 저장하지 않고 오류로 돌린다.
        checkAiResult(aiResult);

        // 3. AI가 돌려준 JSON 전체를 문자열로 보관한다.
        //    화면은 나중에 이 JSON에서 설명, 항목 점수, ML/DL 점수를 꺼낸다.
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

    /** AI JSON에 0~100 정수 점수와 LOW/MID/HIGH 등급이 있는지 확인한다. */
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

    /** 대시보드 표. pageable이 페이지 번호, 크기, 정렬을 들고 있다. 읽기만 한다. */
    @Transactional(readOnly = true)
    public Page<AssessmentRecordResponse> list(Pageable pageable) {
        return assessmentRepository.findAllRecords(pageable);
    }

    /** 대시보드 카드 세 개: 전체 건수, HIGH 등급 건수, AI 결과가 있는 건수. */
    @Transactional(readOnly = true)
    public AssessmentSummaryResponse summary() {
        return new AssessmentSummaryResponse(
                assessmentRepository.count(),
                assessmentRepository.countByAiRiskResult_RiskGrade("HIGH"),
                assessmentRepository.countByAiRiskResultIsNotNull());
    }

    /**
     * 결과 화면용 데이터.
     * AI 결과가 아직 없으면 점수와 설명은 null로 두고, 이름·직무만 돌려준다.
     * 예전 저장분은 키 이름이 summary, maximum, task_basis 라서 새 이름과 둘 다 읽는다.
     */
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

    /**
     * 평가 삭제.
     * 평가와 AI 결과가 서로를 가리키므로, 줄을 먼저 끊지 않으면 DB가 삭제를 거절한다.
     */
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

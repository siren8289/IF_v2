package com.example.demo.ai.service;

import com.example.demo.ai.client.AIClient;
import com.example.demo.ai.entity.AIRiskResult;
import com.example.demo.ai.repository.AIRiskResultRepository;
import com.example.demo.applicant.entity.Applicant;
import com.example.demo.applicant.entity.HealthSnapshot;
import com.example.demo.applicant.repository.ApplicantRepository;
import com.example.demo.applicant.repository.HealthSnapshotRepository;
import com.example.demo.assessment.entity.Assessment;
import com.example.demo.assessment.entity.AssessmentStatus;
import com.example.demo.assessment.repository.AssessmentRepository;
import com.example.demo.global.exception.ApiException;
import com.example.demo.job.entity.Job;
import com.example.demo.job.repository.JobRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.context.ActiveProfiles;

import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.anyMap;
import static org.mockito.Mockito.*;

@SpringBootTest
@ActiveProfiles("test")
class PersonalRiskPersistenceTest {
    @Autowired AIRiskService service;
    @Autowired ApplicantRepository applicants;
    @Autowired HealthSnapshotRepository health;
    @Autowired JobRepository jobs;
    @Autowired AssessmentRepository assessments;
    @Autowired AIRiskResultRepository results;
    @Autowired ObjectMapper mapper;
    @MockBean AIClient client;
    Long assessmentId;

    @BeforeEach
    void setup() {
        var applicant = applicants.save(new Applicant("로컬 테스트", 70));
        var snapshot = health.save(new HealthSnapshot(applicant, 3, false, 8));
        var job = new Job(); job.setJobTitle("야간 배송기사 모집"); job.setExternalJobId("KJ21062610080016");
        job = jobs.save(job);
        var assessment = new Assessment();
        assessment.setApplicant(applicant); assessment.setHealthSnapshot(snapshot); assessment.setJob(job);
        assessment.setStatus(AssessmentStatus.PENDING_AI);
        assessmentId = assessments.save(assessment).getId();
    }

    ObjectNode response(Map<String, Object> request, int score) {
        var node = mapper.createObjectNode();
        node.put("risk_score", score); node.put("risk_grade", AIRiskService.gradeOf(score));
        node.put("score_type", "REFERENCE_INDEX"); node.put("model_version", "PERSONAL_INDEX_V1");
        node.put("assessment_status", "SCORED_REVIEW_REQUIRED"); node.put("review_required", true);
        node.putNull("risk_probability"); node.set("inputs", mapper.valueToTree(request));
        node.putArray("factors").addObject().put("label", "건강 상태").put("points", score).put("maximum", 100);
        node.putArray("limitations").add("사고 확률이 아닙니다.");
        node.put("summary", "참고 지수");
        return node;
    }

    @Test
    void storesScoreGradeStatusAndExplanationAndReusesRow() {
        when(client.calculatePersonalRisk(anyMap())).thenAnswer(call -> response(call.getArgument(0), 61));
        service.computeAndSaveRisk(assessmentId);
        var saved = results.findByAssessment_Id(assessmentId).orElseThrow();
        assertEquals(61, saved.getTotalRiskPercent()); assertEquals("HIGH", saved.getRiskGrade());
        assertEquals(AssessmentStatus.AI_COMPLETED, assessments.findById(assessmentId).orElseThrow().getStatus());
        var detail = service.getRiskDetail(assessmentId);
        assertEquals("REFERENCE_INDEX", detail.getScoreType()); assertTrue(detail.getReviewRequired());
        assertEquals("사고 확률이 아닙니다.", detail.getLimitations().get(0));
        Long resultId = saved.getId();
        service.computeAndSaveRisk(assessmentId);
        assertEquals(resultId, results.findByAssessment_Id(assessmentId).orElseThrow().getId());
    }

    @Test
    void zeroIsAValidComputedScore() {
        when(client.calculatePersonalRisk(anyMap())).thenAnswer(call -> response(call.getArgument(0), 0));
        service.computeAndSaveRisk(assessmentId);
        assertEquals(0, service.getRiskDetail(assessmentId).getRiskScore());
        assertEquals("LOW", service.getRiskDetail(assessmentId).getRiskGrade());
    }

    @ParameterizedTest
    @ValueSource(strings = {"null", "-1", "101", "50.5", "\"50\"", "true"})
    void rejectsInvalidScoreWithoutSaving(String value) {
        when(client.calculatePersonalRisk(anyMap())).thenAnswer(call -> {
            var result = response(call.getArgument(0), 50); result.set("risk_score", mapper.readTree(value)); return result;
        });
        assertThrows(ApiException.class, () -> service.computeAndSaveRisk(assessmentId));
        assertTrue(results.findByAssessment_Id(assessmentId).isEmpty());
        assertEquals(AssessmentStatus.PENDING_AI, assessments.findById(assessmentId).orElseThrow().getStatus());
    }

    @Test
    void refusesMismatchedInputsAndGrade() {
        when(client.calculatePersonalRisk(anyMap())).thenAnswer(call -> {
            var result = response(call.getArgument(0), 50); result.put("risk_grade", "LOW"); return result;
        });
        assertThrows(ApiException.class, () -> service.computeAndSaveRisk(assessmentId));
        when(client.calculatePersonalRisk(anyMap())).thenAnswer(call -> {
            var result = response(call.getArgument(0), 50); ((ObjectNode) result.get("inputs")).put("age", 71); return result;
        });
        assertThrows(ApiException.class, () -> service.computeAndSaveRisk(assessmentId));
        assertTrue(results.findByAssessment_Id(assessmentId).isEmpty());
    }

    @Test
    void upstreamFailureKeepsPreviousScore() {
        when(client.calculatePersonalRisk(anyMap())).thenAnswer(call -> response(call.getArgument(0), 50));
        service.computeAndSaveRisk(assessmentId);
        when(client.calculatePersonalRisk(anyMap())).thenThrow(ApiException.aiUnavailable("offline", new RuntimeException()));
        assertThrows(ApiException.class, () -> service.computeAndSaveRisk(assessmentId));
        assertEquals(50, results.findByAssessment_Id(assessmentId).orElseThrow().getTotalRiskPercent());
    }

    @Test
    void finalizedAssessmentCannotBeOverwritten() {
        var assessment = assessments.findById(assessmentId).orElseThrow();
        assessment.setStatus(AssessmentStatus.FINALIZED); assessments.save(assessment);
        assertThrows(ApiException.class, () -> service.computeAndSaveRisk(assessmentId));
        verifyNoInteractions(client);
    }

    @Test
    void legacyEvidenceOnlyStillHasNoScore() {
        var assessment = assessments.findById(assessmentId).orElseThrow();
        var result = new AIRiskResult(); result.setAssessment(assessment);
        result.setModelVersion("EVIDENCE_ONLY_V1");
        result.setExplanationJson("{\"assessment_status\":\"EVIDENCE_ONLY\",\"evidence\":{},\"explanation\":null}");
        results.save(result);
        var detail = service.getRiskDetail(assessmentId);
        assertNull(detail.getRiskScore()); assertNull(detail.getRiskGrade());
        assertEquals("EVIDENCE_ONLY", detail.getDataStatus());
    }

    @Test
    void inputChangeDuringExternalCallIsRejected() {
        when(client.calculatePersonalRisk(anyMap())).thenAnswer(call -> {
            var assessment = assessments.findById(assessmentId).orElseThrow();
            var replacement = new Job(); replacement.setJobTitle("다른 직무");
            assessment.setJob(jobs.save(replacement)); assessments.save(assessment);
            return response(call.getArgument(0), 50);
        });
        assertThrows(ApiException.class, () -> service.computeAndSaveRisk(assessmentId));
        assertTrue(results.findByAssessment_Id(assessmentId).isEmpty());
        assertEquals(AssessmentStatus.PENDING_AI, assessments.findById(assessmentId).orElseThrow().getStatus());
    }

    @Test
    void missingHealthInputIsRejectedBeforeExternalCall() {
        var assessment = assessments.findById(assessmentId).orElseThrow();
        var applicant = applicants.save(new Applicant("정보 누락 테스트", 70));
        assessment.setHealthSnapshot(health.save(new HealthSnapshot(applicant, null, false, 8)));
        assessments.save(assessment);
        assertThrows(ApiException.class, () -> service.computeAndSaveRisk(assessmentId));
        verifyNoInteractions(client);
    }

    @Test
    void probabilityClaimIsRejected() {
        when(client.calculatePersonalRisk(anyMap())).thenAnswer(call -> {
            var result = response(call.getArgument(0), 50); result.put("risk_probability", 0.5); return result;
        });
        assertThrows(ApiException.class, () -> service.computeAndSaveRisk(assessmentId));
        assertTrue(results.findByAssessment_Id(assessmentId).isEmpty());
    }
}

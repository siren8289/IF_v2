package com.example.demo.assessment;

// IF-0094~IF-0152. 격리 H2(if0094)에서만 실행한다. 운영 Postgres에는 연결하지 않는다.

import com.example.demo.ai.client.AIClient;
import com.example.demo.ai.entity.AIRiskResult;
import com.example.demo.ai.repository.AIRiskResultRepository;
import com.example.demo.applicant.entity.Applicant;
import com.example.demo.applicant.entity.HealthSnapshot;
import com.example.demo.applicant.repository.ApplicantRepository;
import com.example.demo.applicant.repository.HealthSnapshotRepository;
import com.example.demo.assessment.dto.AssessmentCreateRequest;
import com.example.demo.assessment.entity.Assessment;
import com.example.demo.assessment.entity.AssessmentStatus;
import com.example.demo.assessment.repository.AssessmentRepository;
import com.example.demo.assessment.service.AssessmentService;
import com.example.demo.global.exception.ApiException;
import com.example.demo.job.entity.Job;
import com.example.demo.job.repository.JobRepository;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.persistence.EntityManager;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.mockito.ArgumentCaptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.boot.test.mock.mockito.SpyBean;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.support.TransactionTemplate;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.Map;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.hamcrest.Matchers.nullValue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.reset;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("test")
class AssessmentPipelineIf0094Test {

    @DynamicPropertySource
    static void isolatedDb(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", () ->
                "jdbc:h2:mem:if0094;MODE=PostgreSQL;DB_CLOSE_DELAY=-1;DATABASE_TO_LOWER=TRUE");
    }

    @Autowired AssessmentService assessmentService;
    @Autowired AssessmentRepository assessmentRepository;
    @Autowired ApplicantRepository applicantRepository;
    @Autowired HealthSnapshotRepository healthRepository;
    @Autowired AIRiskResultRepository riskResultRepository;
    @Autowired JobRepository jobRepository;
    @Autowired ObjectMapper objectMapper;
    @Autowired MockMvc mockMvc;
    @Autowired EntityManager entityManager;
    @Autowired PlatformTransactionManager transactionManager;
    @Autowired RestTemplate restTemplate;

    @MockBean AIClient aiClient;
    @SpyBean AIRiskResultRepository riskSpy;

    @BeforeEach
    void clean() {
        reset(riskSpy);
        wipe();
    }

    @AfterEach
    void cleanAfter() {
        reset(riskSpy);
        wipe();
    }

    @Test
    @DisplayName("IF-0094 jobId=1 조회 후 평가 생성")
    void IF_0094() throws Exception {
        Counts before = counts();
        Job job = job1();
        Long id = create(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        Assessment saved = load(id);
        assertThat(saved.getJob().getId()).isEqualTo(job.getId()).isEqualTo(1L);
        assertThat(saved.getJob().getJobTitle()).isEqualTo(job.getJobTitle());
        assertThat(counts().assessment()).isEqualTo(before.assessment() + 1);
    }

    @Test
    @DisplayName("IF-0095 없는 직무")
    void IF_0095() {
        Counts before = counts();
        assertThatThrownBy(() -> assessmentService.createAndAnalyze(
                request("홍길동", 72, 3, true, 6, 999999L)))
                .isInstanceOf(ApiException.class)
                .extracting(ex -> ((ApiException) ex).getErrorCode())
                .isEqualTo("NOT_FOUND");
        assertThat(counts()).isEqualTo(before);
        assertThat(applicantRepository.count()).isEqualTo(before.applicant());
        assertThat(healthRepository.count()).isEqualTo(before.health());
        assertThat(assessmentRepository.count()).isEqualTo(before.assessment());
    }

    @Test
    @DisplayName("IF-0096 신청자 이름 trim과 나이")
    void IF_0096() throws Exception {
        Counts before = counts();
        Long id = create(request("  홍길동  ", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        Assessment saved = load(id);
        assertThat(saved.getApplicant().getDisplayName()).isEqualTo("홍길동");
        assertThat(saved.getApplicant().getAge()).isEqualTo(72);
        assertThat(counts().applicant()).isEqualTo(before.applicant() + 1);
    }

    @Test
    @DisplayName("IF-0097 건강 스냅샷 보존")
    void IF_0097() throws Exception {
        Long id = create(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        Assessment saved = load(id);
        HealthSnapshot health = saved.getHealthSnapshot();
        assertThat(health.getPhysicalLevel()).isEqualTo(3);
        assertThat(health.getChronicDiseaseFlag()).isTrue();
        assertThat(health.getWorkHourLimit()).isEqualTo(6);
        assertThat(health.getApplicant().getId()).isEqualTo(saved.getApplicant().getId());
    }

    @Test
    @DisplayName("IF-0098 평가 생성 직후 상태")
    void IF_0098() throws Exception {
        Counts before = counts();
        Long id = create(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        Assessment saved = load(id);
        assertThat(counts().assessment()).isEqualTo(before.assessment() + 1);
        assertThat(saved.getAssessedAt().getOffset()).isEqualTo(ZoneOffset.UTC);
        // 시트 기대는 호출이 끝난 뒤 PENDING_AI다. 성공 경로는 그 뒤 AI_COMPLETED로 덮어 쓴다.
        assertThat(saved.getStatus()).isEqualTo(AssessmentStatus.PENDING_AI);
    }

    @Test
    @DisplayName("IF-0099 AI title은 직무명")
    void IF_0099() throws Exception {
        Map<String, Object> body = capture(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        assertThat(body.get("title")).isEqualTo("아파트 야간 경비원");
        assertThat(body).doesNotContainKey("workplace");
        assertThat(body.get("title")).isNotEqualTo(job1().getWorkplace());
    }

    @Test
    @DisplayName("IF-0100 AI age")
    void IF_0100() throws Exception {
        Map<String, Object> body = capture(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        assertThat(body.get("age")).isEqualTo(72);
        assertThat(body.get("age")).isInstanceOf(Integer.class);
    }

    @Test
    @DisplayName("IF-0101 AI physical_level")
    void IF_0101() throws Exception {
        Map<String, Object> body = capture(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        assertThat(body).containsEntry("physical_level", 3);
        assertThat(body).doesNotContainKey("physicalLevel");
    }

    @Test
    @DisplayName("IF-0102 AI chronic_disease")
    void IF_0102() throws Exception {
        Map<String, Object> body = capture(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        assertThat(body).containsEntry("chronic_disease", true);
        assertThat(body).doesNotContainKey("chronicDisease");
    }

    @Test
    @DisplayName("IF-0103 AI work_hour_limit")
    void IF_0103() throws Exception {
        Map<String, Object> body = capture(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        assertThat(body).containsEntry("work_hour_limit", 6);
        assertThat(body).doesNotContainKey("workHourLimit");
    }

    @Test
    @DisplayName("IF-0104 AI 응답 null")
    void IF_0104() {
        Counts before = counts();
        assertThatThrownBy(() -> create(request("홍길동", 72, 3, true, 6, 1L), null))
                .isInstanceOf(ApiException.class)
                .extracting(ex -> ((ApiException) ex).getErrorCode())
                .isEqualTo("AI_ERROR");
        assertThat(counts().assessment()).isEqualTo(before.assessment() + 1);
        assertThat(counts().ai()).isEqualTo(before.ai());
        Assessment saved = onlyAssessment();
        assertThat(saved.getStatus()).isEqualTo(AssessmentStatus.PENDING_AI);
        assertThat(saved.getAiRiskResult()).isNull();
    }

    @Test
    @DisplayName("IF-0105 점수 없음")
    void IF_0105() throws Exception {
        assertRejected("{\"risk_grade\":\"LOW\"}");
    }

    @Test
    @DisplayName("IF-0106 점수 실수")
    void IF_0106() throws Exception {
        assertRejected("{\"risk_score\":40.5,\"risk_grade\":\"LOW\"}");
    }

    @Test
    @DisplayName("IF-0107 점수 문자열")
    void IF_0107() throws Exception {
        assertRejected("{\"risk_score\":\"40\",\"risk_grade\":\"LOW\"}");
    }

    @Test
    @DisplayName("IF-0108 점수 -1")
    void IF_0108() throws Exception {
        assertRejected("{\"risk_score\":-1,\"risk_grade\":\"LOW\"}");
    }

    @Test
    @DisplayName("IF-0109 점수 0")
    void IF_0109() throws Exception {
        assertStoredScore(0, "LOW");
    }

    @Test
    @DisplayName("IF-0110 점수 100")
    void IF_0110() throws Exception {
        assertStoredScore(100, "HIGH");
    }

    @Test
    @DisplayName("IF-0111 점수 101")
    void IF_0111() throws Exception {
        assertRejected("{\"risk_score\":101,\"risk_grade\":\"HIGH\"}");
    }

    @Test
    @DisplayName("IF-0112 등급 없음")
    void IF_0112() throws Exception {
        assertRejected("{\"risk_score\":40}");
    }

    @Test
    @DisplayName("IF-0113 등급 LOW")
    void IF_0113() throws Exception {
        assertStoredScore(40, "LOW");
    }

    @Test
    @DisplayName("IF-0114 등급 MID")
    void IF_0114() throws Exception {
        assertStoredScore(50, "MID");
    }

    @Test
    @DisplayName("IF-0115 등급 HIGH")
    void IF_0115() throws Exception {
        assertStoredScore(70, "HIGH");
    }

    @Test
    @DisplayName("IF-0116 등급 소문자")
    void IF_0116() throws Exception {
        assertRejected("{\"risk_score\":40,\"risk_grade\":\"low\"}");
    }

    @Test
    @DisplayName("IF-0117 등급 UNKNOWN")
    void IF_0117() throws Exception {
        assertRejected("{\"risk_score\":40,\"risk_grade\":\"UNKNOWN\"}");
    }

    @Test
    @DisplayName("IF-0118 모델 버전 기본값")
    void IF_0118() throws Exception {
        Long id = create(request("홍길동", 72, 3, true, 6, 1L),
                "{\"risk_score\":40,\"risk_grade\":\"LOW\"}");
        assertThat(load(id).getAiRiskResult().getModelVersion()).isEqualTo("SIMPLE_V1");
    }

    @Test
    @DisplayName("IF-0119 설명 JSON 저장")
    void IF_0119() throws Exception {
        String json = """
                {"risk_score":40,"risk_grade":"LOW","factors":[{"name":"나이","points":8.0,"max":20}],"task_scores":[{"name":"야간","ml_score":0.2,"dl_score":0.3}]}
                """;
        JsonNode node = objectMapper.readTree(json);
        when(aiClient.analyze(any())).thenReturn(node);
        Long id = assessmentService.createAndAnalyze(request("홍길동", 72, 3, true, 6, 1L));
        String stored = load(id).getAiRiskResult().getExplanationJson();
        assertThat(stored).isEqualTo(node.toString());
        assertThat(objectMapper.readTree(stored)).isEqualTo(node);
    }

    @Test
    @DisplayName("IF-0120 상태 완료와 결과 연결")
    void IF_0120() throws Exception {
        Long id = create(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        Assessment saved = load(id);
        assertThat(saved.getStatus()).isEqualTo(AssessmentStatus.AI_COMPLETED);
        assertThat(saved.getAiRiskResult()).isNotNull();
        assertThat(saved.getAiRiskResult().getAssessment().getId()).isEqualTo(id);
        assertThat(sqlLong("select ai_result_id from assessment where assessment_id = " + id)).isNotNull();
    }

    @Test
    @DisplayName("IF-0121 AI 호출 실패 시 PENDING_AI 잔존")
    void IF_0121() {
        AIClient realClient = new AIClient(restTemplate, "http://127.0.0.1:9");
        assertThatThrownBy(() -> realClient.analyze(Map.of("title", "아파트 야간 경비원")))
                .isInstanceOf(ApiException.class)
                .extracting(ex -> ((ApiException) ex).getErrorCode())
                .isEqualTo("AI_ERROR");

        Counts before = counts();
        when(aiClient.analyze(any())).thenThrow(ApiException.aiError(
                "AI 서버 호출에 실패했습니다.", new RestClientException("Connection refused")));
        assertThatThrownBy(() -> assessmentService.createAndAnalyze(request("홍길동", 72, 3, true, 6, 1L)))
                .isInstanceOf(ApiException.class)
                .extracting(ex -> ((ApiException) ex).getErrorCode())
                .isEqualTo("AI_ERROR");
        assertThat(counts().assessment()).isEqualTo(before.assessment() + 1);
        assertThat(counts().ai()).isEqualTo(before.ai());
        assertThat(onlyAssessment().getStatus()).isEqualTo(AssessmentStatus.PENDING_AI);
    }

    @Test
    @DisplayName("IF-0122 AI 결과 저장 실패")
    void IF_0122() throws Exception {
        Counts before = counts();
        doThrow(new IllegalStateException("save failed")).when(riskSpy).save(any(AIRiskResult.class));
        assertThatThrownBy(() -> create(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW")))
                .isInstanceOf(RuntimeException.class);
        assertThat(counts().applicant()).isEqualTo(before.applicant() + 1);
        assertThat(counts().health()).isEqualTo(before.health() + 1);
        assertThat(counts().assessment()).isEqualTo(before.assessment() + 1);
        assertThat(counts().ai()).isEqualTo(before.ai());
        Assessment saved = onlyAssessment();
        assertThat(saved.getStatus()).isEqualTo(AssessmentStatus.PENDING_AI);
        assertThat(saved.getAiRiskResult()).isNull();
    }

    @Test
    @DisplayName("IF-0123 결과 없음")
    void IF_0123() throws Exception {
        Long id = insertPending(OffsetDateTime.now(ZoneOffset.UTC)).getId();
        Counts before = counts();
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.riskScore").value(nullValue()))
                .andExpect(jsonPath("$.riskGrade").value(nullValue()))
                .andExpect(jsonPath("$.explanation").value(nullValue()))
                .andExpect(jsonPath("$.factors").isEmpty())
                .andExpect(jsonPath("$.taskScores").isEmpty());
        assertThat(counts()).isEqualTo(before);
    }

    @Test
    @DisplayName("IF-0124 설명 신형")
    void IF_0124() throws Exception {
        Long id = insertWithJson("{\"explanation\":\"A\"}");
        Counts before = counts();
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.explanation").value("A"));
        assertThat(counts()).isEqualTo(before);
        assertThat(load(id).getAiRiskResult().getExplanationJson()).contains("\"explanation\":\"A\"");
    }

    @Test
    @DisplayName("IF-0125 설명 구형 summary")
    void IF_0125() throws Exception {
        Long id = insertWithJson("{\"summary\":\"B\"}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.explanation").value("B"));
    }

    @Test
    @DisplayName("IF-0126 설명 없음")
    void IF_0126() throws Exception {
        Long id = insertWithJson("{}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.explanation").value(nullValue()));
    }

    @Test
    @DisplayName("IF-0127 출처 기본값")
    void IF_0127() throws Exception {
        Long id = insertWithJson("{\"explanation\":\"A\"}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.explanationSource").value("basic"));
    }

    @Test
    @DisplayName("IF-0128 출처 gemini")
    void IF_0128() throws Exception {
        Long id = insertWithJson("{\"explanation\":\"A\",\"explanation_source\":\"gemini\"}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.explanationSource").value("gemini"));
    }

    @Test
    @DisplayName("IF-0129 요인 신형")
    void IF_0129() throws Exception {
        Long id = insertWithJson("{\"factors\":[{\"name\":\"나이\",\"max\":20,\"points\":8.5}]}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.factors[0].name").value("나이"))
                .andExpect(jsonPath("$.factors[0].max").value(20))
                .andExpect(jsonPath("$.factors[0].points").value(8.5));
    }

    @Test
    @DisplayName("IF-0130 요인 구형")
    void IF_0130() throws Exception {
        Long id = insertWithJson("{\"factors\":[{\"label\":\"연령\",\"maximum\":15,\"points\":4}]}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.factors[0].name").value("연령"))
                .andExpect(jsonPath("$.factors[0].max").value(15))
                .andExpect(jsonPath("$.factors[0].points").value(4));
    }

    @Test
    @DisplayName("IF-0131 요인 없음")
    void IF_0131() throws Exception {
        Long id = insertWithJson("{\"explanation\":\"A\"}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.factors").isEmpty());
    }

    @Test
    @DisplayName("IF-0132 작업 신형")
    void IF_0132() throws Exception {
        Long id = insertWithJson("{\"task_scores\":[{\"name\":\"야간\",\"ml_score\":0.2,\"dl_score\":0.3}]}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.taskScores[0].name").value("야간"))
                .andExpect(jsonPath("$.taskScores[0].mlScore").value(0.2))
                .andExpect(jsonPath("$.taskScores[0].dlScore").value(0.3));
    }

    @Test
    @DisplayName("IF-0133 작업 구형")
    void IF_0133() throws Exception {
        Long id = insertWithJson("{\"task_basis\":[{\"label\":\"청소\",\"ml_score\":0.1,\"dl_score\":0.4}]}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.taskScores[0].name").value("청소"))
                .andExpect(jsonPath("$.taskScores[0].mlScore").value(0.1))
                .andExpect(jsonPath("$.taskScores[0].dlScore").value(0.4));
    }

    @Test
    @DisplayName("IF-0134 작업 없음")
    void IF_0134() throws Exception {
        Long id = insertWithJson("{\"explanation\":\"A\"}");
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.taskScores").isEmpty());
    }

    @Test
    @DisplayName("IF-0135 깨진 설명 JSON")
    void IF_0135() throws Exception {
        Long id = insertWithJson("{broken");
        Counts before = counts();
        mockMvc.perform(get("/api/assessments/" + id + "/result"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.factors").isEmpty())
                .andExpect(jsonPath("$.taskScores").isEmpty());
        assertThat(counts()).isEqualTo(before);
        assertThat(load(id).getAiRiskResult().getExplanationJson()).isEqualTo("{broken");
    }

    @Test
    @DisplayName("IF-0136 없는 평가")
    void IF_0136() throws Exception {
        Counts before = counts();
        mockMvc.perform(get("/api/assessments/999999/result"))
                .andExpect(status().isNotFound())
                .andExpect(jsonPath("$.errorCode").value("NOT_FOUND"));
        assertThat(counts()).isEqualTo(before);
    }

    @Test
    @DisplayName("IF-0137 AI 결과 있는 평가 삭제")
    void IF_0137() throws Exception {
        Long id = create(request("홍길동", 72, 3, true, 6, 1L), okJson(40, "LOW"));
        Assessment saved = load(id);
        Long applicantId = saved.getApplicant().getId();
        Long healthId = saved.getHealthSnapshot().getId();
        assessmentService.delete(id);
        assertThat(sqlLong("select count(*) from assessment where assessment_id = " + id)).isZero();
        assertThat(sqlLong("select count(*) from ai_risk_result where assessment_id = " + id)).isZero();
        assertThat(applicantRepository.findById(applicantId)).isPresent();
        assertThat(healthRepository.findById(healthId)).isPresent();
    }

    @Test
    @DisplayName("IF-0138 PENDING_AI 삭제")
    void IF_0138() {
        Long id = insertPending(OffsetDateTime.now(ZoneOffset.UTC)).getId();
        assessmentService.delete(id);
        assertThat(assessmentRepository.findById(id)).isEmpty();
        assertThat(riskResultRepository.count()).isZero();
    }

    @Test
    @DisplayName("IF-0139 없는 ID 삭제")
    void IF_0139() {
        assertThatThrownBy(() -> assessmentService.delete(999999L))
                .isInstanceOf(ApiException.class)
                .extracting(ex -> ((ApiException) ex).getErrorCode())
                .isEqualTo("NOT_FOUND");
    }

    @Test
    @DisplayName("IF-0140 같은 ID 두 번 삭제")
    void IF_0140() {
        Long id = insertPending(OffsetDateTime.now(ZoneOffset.UTC)).getId();
        assessmentService.delete(id);
        assertThatThrownBy(() -> assessmentService.delete(id))
                .isInstanceOf(ApiException.class)
                .extracting(ex -> ((ApiException) ex).getErrorCode())
                .isEqualTo("NOT_FOUND");
    }

    @Test
    @DisplayName("IF-0141 삭제 후 조회")
    void IF_0141() {
        Long id = insertPending(OffsetDateTime.now(ZoneOffset.UTC)).getId();
        assessmentService.delete(id);
        assertThatThrownBy(() -> assessmentService.getResult(id))
                .isInstanceOf(ApiException.class)
                .extracting(ex -> ((ApiException) ex).getErrorCode())
                .isEqualTo("NOT_FOUND");
    }

    @Test
    @DisplayName("IF-0142 다른 평가는 유지")
    void IF_0142() throws Exception {
        Long keep = create(request("유지", 70, 2, false, 4, 1L), okJson(10, "LOW"));
        Long drop = create(request("삭제", 71, 4, true, 8, 1L), okJson(80, "HIGH"));
        assessmentService.delete(drop);
        assertThat(assessmentRepository.findById(drop)).isEmpty();
        assertThat(load(keep).getApplicant().getDisplayName()).isEqualTo("유지");
        assertThat(load(keep).getAiRiskResult().getRiskGrade()).isEqualTo("LOW");
    }

    @Test
    @DisplayName("IF-0143 총 평가 0")
    void IF_0143() throws Exception {
        assertSummary(0, null, null);
        assertThat(sqlLong("select count(*) from assessment")).isZero();
    }

    @Test
    @DisplayName("IF-0144 총 평가 1")
    void IF_0144() throws Exception {
        insertPending(OffsetDateTime.now(ZoneOffset.UTC));
        assertSummary(1, null, null);
        assertThat(sqlLong("select count(*) from assessment")).isEqualTo(1);
    }

    @Test
    @DisplayName("IF-0145 미분석 1")
    void IF_0145() throws Exception {
        insertPending(OffsetDateTime.now(ZoneOffset.UTC));
        assertSummary(null, null, 0);
        assertThat(sqlLong("select count(*) from assessment where ai_result_id is not null")).isZero();
    }

    @Test
    @DisplayName("IF-0146 완료 LOW 1")
    void IF_0146() throws Exception {
        insertCompleted("LOW", 20, OffsetDateTime.now(ZoneOffset.UTC));
        assertSummary(null, 0, 1);
        assertThat(sqlLong("select count(*) from ai_risk_result where risk_grade = 'HIGH'")).isZero();
        assertThat(sqlLong("select count(*) from assessment where ai_result_id is not null")).isEqualTo(1);
    }

    @Test
    @DisplayName("IF-0147 완료 HIGH 1")
    void IF_0147() throws Exception {
        insertCompleted("HIGH", 80, OffsetDateTime.now(ZoneOffset.UTC));
        assertSummary(null, 1, 1);
    }

    @Test
    @DisplayName("IF-0148 HIGH 2 MID 1")
    void IF_0148() throws Exception {
        OffsetDateTime at = OffsetDateTime.now(ZoneOffset.UTC);
        insertCompleted("HIGH", 80, at);
        insertCompleted("HIGH", 90, at);
        insertCompleted("MID", 50, at);
        assertSummary(null, 2, null);
        assertThat(sqlLong("select count(*) from ai_risk_result where risk_grade = 'HIGH'")).isEqualTo(2);
    }

    @Test
    @DisplayName("IF-0149 첫 페이지 20")
    void IF_0149() throws Exception {
        insertMany(20);
        mockMvc.perform(get("/api/assessments").param("page", "0"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.content.length()").value(20));
    }

    @Test
    @DisplayName("IF-0150 21건 page 0")
    void IF_0150() throws Exception {
        insertMany(21);
        mockMvc.perform(get("/api/assessments").param("page", "0"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.totalElements").value(21))
                .andExpect(jsonPath("$.content.length()").value(20));
    }

    @Test
    @DisplayName("IF-0151 21건 page 1")
    void IF_0151() throws Exception {
        insertMany(21);
        mockMvc.perform(get("/api/assessments").param("page", "1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.totalElements").value(21))
                .andExpect(jsonPath("$.content.length()").value(1));
    }

    @Test
    @DisplayName("IF-0152 같은 시각이면 id DESC")
    void IF_0152() throws Exception {
        OffsetDateTime at = OffsetDateTime.parse("2026-10-31T00:00:00Z");
        Long first = insertCompleted("LOW", 10, at).getId();
        Long second = insertCompleted("LOW", 11, at).getId();
        String body = mockMvc.perform(get("/api/assessments").param("page", "0"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.content[0].id").value(second))
                .andExpect(jsonPath("$.content[1].id").value(first))
                .andReturn().getResponse().getContentAsString();
        JsonNode page = objectMapper.readTree(body);
        assertThat(page.get("content").get(0).get("assessedAt"))
                .isEqualTo(page.get("content").get(1).get("assessedAt"));
    }

    private AssessmentCreateRequest request(String name, int age, int physical, boolean chronic, int hours, long jobId) {
        return new AssessmentCreateRequest(name, age, physical, chronic, hours, jobId);
    }

    private String okJson(int score, String grade) {
        return "{\"risk_score\":" + score + ",\"risk_grade\":\"" + grade + "\",\"model_version\":\"SIMPLE_V1\"}";
    }

    private Long create(AssessmentCreateRequest request, String json) throws Exception {
        if (json == null) {
            when(aiClient.analyze(any())).thenReturn(null);
        } else {
            when(aiClient.analyze(any())).thenReturn(objectMapper.readTree(json));
        }
        return assessmentService.createAndAnalyze(request);
    }

    @SuppressWarnings("unchecked")
    private Map<String, Object> capture(AssessmentCreateRequest request, String json) throws Exception {
        ArgumentCaptor<Map<String, Object>> captor = ArgumentCaptor.forClass(Map.class);
        when(aiClient.analyze(captor.capture())).thenReturn(objectMapper.readTree(json));
        assessmentService.createAndAnalyze(request);
        return captor.getValue();
    }

    private void assertRejected(String json) throws Exception {
        Counts before = counts();
        assertThatThrownBy(() -> create(request("홍길동", 72, 3, true, 6, 1L), json))
                .isInstanceOf(ApiException.class)
                .extracting(ex -> ((ApiException) ex).getErrorCode())
                .isEqualTo("AI_ERROR");
        assertThat(counts().ai()).isEqualTo(before.ai());
        assertThat(onlyAssessment().getAiRiskResult()).isNull();
    }

    private void assertStoredScore(int score, String grade) throws Exception {
        Long id = create(request("홍길동", 72, 3, true, 6, 1L), okJson(score, grade));
        Assessment saved = load(id);
        assertThat(saved.getStatus()).isEqualTo(AssessmentStatus.AI_COMPLETED);
        assertThat(saved.getAiRiskResult().getTotalRiskPercent()).isEqualTo(score);
        assertThat(saved.getAiRiskResult().getRiskGrade()).isEqualTo(grade);
    }

    private Job job1() {
        return jobRepository.findById(1L).orElseThrow();
    }

    private Assessment onlyAssessment() {
        return tx().execute(status -> {
            Assessment saved = assessmentRepository.findAll().get(0);
            saved.getAiRiskResult();
            return saved;
        });
    }

    private Assessment load(Long id) {
        return tx().execute(status -> {
            Assessment saved = assessmentRepository.findById(id).orElseThrow();
            saved.getApplicant().getDisplayName();
            saved.getHealthSnapshot().getPhysicalLevel();
            saved.getHealthSnapshot().getApplicant().getId();
            saved.getJob().getJobTitle();
            if (saved.getAiRiskResult() != null) {
                saved.getAiRiskResult().getExplanationJson();
                if (saved.getAiRiskResult().getAssessment() != null) {
                    saved.getAiRiskResult().getAssessment().getId();
                }
            }
            return saved;
        });
    }

    private Assessment insertPending(OffsetDateTime at) {
        return tx().execute(status -> {
            Applicant applicant = applicantRepository.save(new Applicant("대기", 70));
            HealthSnapshot health = healthRepository.save(new HealthSnapshot(applicant, 3, false, 6));
            Assessment assessment = new Assessment();
            assessment.setApplicant(applicant);
            assessment.setJob(job1());
            assessment.setHealthSnapshot(health);
            assessment.setStatus(AssessmentStatus.PENDING_AI);
            assessment.setAssessedAt(at);
            return assessmentRepository.save(assessment);
        });
    }

    private Assessment insertCompleted(String grade, int score, OffsetDateTime at) {
        return tx().execute(status -> {
            Assessment assessment = insertPending(at);
            AIRiskResult result = new AIRiskResult();
            result.setAssessment(assessment);
            result.setTotalRiskPercent(score);
            result.setRiskGrade(grade);
            result.setModelVersion("SIMPLE_V1");
            result.setGeneratedAt(at);
            result.setExplanationJson("{\"explanation\":\"저장\"}");
            result = riskResultRepository.save(result);
            assessment.setAiRiskResult(result);
            assessment.setStatus(AssessmentStatus.AI_COMPLETED);
            return assessmentRepository.save(assessment);
        });
    }

    private Long insertWithJson(String explanationJson) {
        Assessment assessment = insertCompleted("LOW", 40, OffsetDateTime.now(ZoneOffset.UTC));
        tx().executeWithoutResult(status -> {
            AIRiskResult result = assessmentRepository.findById(assessment.getId()).orElseThrow().getAiRiskResult();
            result.setExplanationJson(explanationJson);
            riskResultRepository.save(result);
        });
        return assessment.getId();
    }

    private void insertMany(int count) {
        OffsetDateTime start = OffsetDateTime.parse("2026-10-31T00:00:00Z");
        for (int i = 0; i < count; i++) {
            insertPending(start.plusMinutes(i));
        }
    }

    private void assertSummary(Integer total, Integer high, Integer analyzed) throws Exception {
        var result = mockMvc.perform(get("/api/assessments/summary")).andExpect(status().isOk());
        if (total != null) {
            result.andExpect(jsonPath("$.totalCount").value(total));
        }
        if (high != null) {
            result.andExpect(jsonPath("$.highRiskCount").value(high));
        }
        if (analyzed != null) {
            result.andExpect(jsonPath("$.analyzedCount").value(analyzed));
        }
    }

    private Counts counts() {
        return new Counts(
                applicantRepository.count(),
                healthRepository.count(),
                assessmentRepository.count(),
                riskResultRepository.count());
    }

    private long sqlLong(String sql) {
        return tx().execute(status -> ((Number) entityManager.createNativeQuery(sql).getSingleResult()).longValue());
    }

    private TransactionTemplate tx() {
        return new TransactionTemplate(transactionManager);
    }

    private void wipe() {
        tx().executeWithoutResult(status -> {
            for (Assessment assessment : assessmentRepository.findAll()) {
                AIRiskResult ai = assessment.getAiRiskResult();
                if (ai != null) {
                    assessment.setAiRiskResult(null);
                    assessmentRepository.saveAndFlush(assessment);
                    ai.setAssessment(null);
                    riskResultRepository.saveAndFlush(ai);
                    riskResultRepository.delete(ai);
                    riskResultRepository.flush();
                }
                assessmentRepository.delete(assessment);
            }
            assessmentRepository.flush();
            healthRepository.deleteAll();
            applicantRepository.deleteAll();
        });
    }

    private record Counts(long applicant, long health, long assessment, long ai) {
    }
}

package com.example.demo.assessment;

import com.example.demo.ai.client.AIClient;
import com.example.demo.assessment.dto.AssessmentCreateRequest;
import com.example.demo.assessment.dto.AssessmentResultResponse;
import com.example.demo.assessment.dto.AssessmentSummaryResponse;
import com.example.demo.assessment.repository.AssessmentRepository;
import com.example.demo.assessment.service.AssessmentService;
import com.example.demo.global.exception.ApiException;
import com.example.demo.job.entity.Job;
import com.example.demo.job.repository.JobRepository;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.data.domain.PageRequest;
import org.springframework.test.context.ActiveProfiles;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

@SpringBootTest
@ActiveProfiles("test")
class AssessmentServiceTest {

    @Autowired
    AssessmentService assessmentService;

    @Autowired
    AssessmentRepository assessmentRepository;

    @Autowired
    JobRepository jobRepository;

    @Autowired
    ObjectMapper objectMapper;

    @MockBean
    AIClient aiClient;

    Long jobId;

    @BeforeEach
    void setUp() {
        Job job = new Job();
        job.setJobTitle("야간 경비원");
        job.setWorkplace("서울");
        jobId = jobRepository.save(job).getId();
    }

    private AssessmentCreateRequest request() {
        return new AssessmentCreateRequest("홍길동", 72, 3, true, 6, jobId);
    }

    private JsonNode aiResponse(int score, String grade) throws Exception {
        String json = """
                {
                  "risk_score": %d,
                  "risk_grade": "%s",
                  "factors": [{"name": "나이", "points": 8.0, "max": 20}],
                  "task_scores": [{"label": "NIGHT_SHIFT", "name": "야간 근무", "ml_score": 0.9, "dl_score": 0.8}],
                  "explanation": "테스트 설명",
                  "explanation_source": "basic",
                  "model_version": "SIMPLE_V1"
                }
                """.formatted(score, grade);
        return objectMapper.readTree(json);
    }

    @Test
    void 평가를_등록하면_AI_결과가_저장된다() throws Exception {
        when(aiClient.analyze(any())).thenReturn(aiResponse(65, "HIGH"));

        Long id = assessmentService.createAndAnalyze(request());
        AssessmentResultResponse result = assessmentService.getResult(id);

        assertThat(result.status()).isEqualTo("AI_COMPLETED");
        assertThat(result.riskScore()).isEqualTo(65);
        assertThat(result.riskGrade()).isEqualTo("HIGH");
        assertThat(result.explanation()).isEqualTo("테스트 설명");
        assertThat(result.factors()).hasSize(1);
        assertThat(result.taskScores().get(0).name()).isEqualTo("야간 근무");

        AssessmentSummaryResponse summary = assessmentService.summary();
        assertThat(summary.highRiskCount()).isGreaterThanOrEqualTo(1);
        assertThat(assessmentService.list(PageRequest.of(0, 20)).getContent()).isNotEmpty();
    }

    @Test
    void AI_점수가_범위를_벗어나면_오류가_난다() throws Exception {
        when(aiClient.analyze(any())).thenReturn(aiResponse(150, "HIGH"));

        assertThatThrownBy(() -> assessmentService.createAndAnalyze(request()))
                .isInstanceOf(ApiException.class);
    }

    @Test
    void 평가를_삭제할_수_있다() throws Exception {
        when(aiClient.analyze(any())).thenReturn(aiResponse(30, "LOW"));
        Long id = assessmentService.createAndAnalyze(request());

        assessmentService.delete(id);

        assertThat(assessmentRepository.findById(id)).isEmpty();
    }
}

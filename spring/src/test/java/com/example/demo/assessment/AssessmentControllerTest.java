package com.example.demo.assessment;

import com.example.demo.ai.client.AIClient;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("test")
class AssessmentControllerTest {

    @Autowired
    MockMvc mockMvc;

    @MockBean
    AIClient aiClient;

    @Test
    void 나이가_범위를_벗어나면_400() throws Exception {
        String body = """
                {"applicantName":"홍길동","age":200,"physicalLevel":3,
                 "chronicDisease":false,"workHourLimit":8,"jobId":1}
                """;

        mockMvc.perform(post("/api/assessments").contentType(MediaType.APPLICATION_JSON).content(body))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.errorCode").value("VALIDATION_ERROR"));
    }

    @Test
    void 없는_평가를_조회하면_404() throws Exception {
        mockMvc.perform(get("/api/assessments/99999/result"))
                .andExpect(status().isNotFound());
    }

    @Test
    void 요약과_목록을_조회할_수_있다() throws Exception {
        mockMvc.perform(get("/api/assessments/summary")).andExpect(status().isOk());
        mockMvc.perform(get("/api/assessments")).andExpect(status().isOk());
        mockMvc.perform(get("/api/jobs")).andExpect(status().isOk());
    }
}

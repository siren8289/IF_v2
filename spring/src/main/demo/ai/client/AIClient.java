package com.example.demo.ai.client;

import com.example.demo.global.exception.ApiException;
import com.fasterxml.jackson.databind.JsonNode;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

/**
 * FastAPI(AI 서버) 호출.
 * POST /api/v1/risk/analyze 하나만 사용한다.
 */
@Component
public class AIClient {

    private final RestTemplate restTemplate;
    private final String baseUrl;

    public AIClient(RestTemplate restTemplate,
                    @Value("${app.ai.base-url:http://localhost:8000}") String baseUrl) {
        this.restTemplate = restTemplate;
        this.baseUrl = baseUrl;
    }

    public JsonNode analyze(Map<String, Object> request) {
        try {
            return restTemplate.postForObject(baseUrl + "/api/v1/risk/analyze", request, JsonNode.class);
        } catch (RestClientException e) {
            throw ApiException.aiError("AI 서버 호출에 실패했습니다.", e);
        }
    }
}

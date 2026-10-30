package com.example.demo.ai.client;

import com.example.demo.global.exception.ApiException;
import com.fasterxml.jackson.databind.JsonNode;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

/**
 * FastAPI(AI 서버)를 부르는 클라이언트.
 * Spring 안에서 HTTP 요청을 보내는 부분만 모아 두었다.
 * 쓰는 주소는 POST /api/v1/risk/analyze 하나다.
 *
 * 서버 주소는 application.yml 의 app.ai.base-url.
 * 설정이 없으면 http://localhost:8000 이다.
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

    /**
     * 분석 요청을 JSON으로 보내고, 응답 JSON을 트리(JsonNode)로 받는다.
     * 연결 실패나 시간 초과는 502(AI_ERROR)로 바꿔 화면이 오류 문구를 보게 한다.
     */
    public JsonNode analyze(Map<String, Object> request) {
        try {
            return restTemplate.postForObject(baseUrl + "/api/v1/risk/analyze", request, JsonNode.class);
        } catch (RestClientException e) {
            throw ApiException.aiError("AI 서버 호출에 실패했습니다.", e);
        }
    }
}

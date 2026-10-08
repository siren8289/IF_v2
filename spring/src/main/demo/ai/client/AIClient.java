
package com.example.demo.ai.client;

import com.example.demo.ai.dto.ExplainRequestDto;
import com.example.demo.ai.dto.ExplainResponseDto;
import com.example.demo.ai.dto.ScoreRequestDto;
import com.example.demo.ai.dto.ScoreResponseDto;
import com.example.demo.global.exception.ApiException;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

import java.net.SocketTimeoutException;
import java.util.concurrent.TimeoutException;

/**
 * Spring Boot와 FastAPI 간 HTTP 통신 담당.
 *
 * [역할]
 * - /score : 위험도 계산 요청
 * - /explain : 위험도 설명 요청
 *
 * [예외 처리]
 * - 타임아웃 : HTTP 504
 * - 연결 및 응답 오류 : HTTP 502
 *
 * 업무 데이터 저장은 담당하지 않는다.
 */
@Component
public class AIClient {

    private final RestTemplate restTemplate;
    private final String baseUrl;

    /**
     * FastAPI 서버 주소를 주입한다.
     * 마지막 슬래시는 제거해 URL 중복을 방지한다.
     */
    public AIClient(
            RestTemplate restTemplate,
            @Value("${app.ai.base-url:http://localhost:8000}")
            String baseUrl
    ) {
        this.restTemplate = restTemplate;
        this.baseUrl = baseUrl.endsWith("/")
                ? baseUrl.substring(0, baseUrl.length() - 1)
                : baseUrl;
    }

    /**
     * FastAPI /score 호출.
     *
     * @param request 신청자 및 일자리 평가 입력
     * @return FastAPI가 계산한 위험도 결과
     */
    public ScoreResponseDto score(ScoreRequestDto request) {
        try {
            return restTemplate.postForObject(
                    baseUrl + "/score",
                    request,
                    ScoreResponseDto.class
            );
        } catch (RestClientException e) {
            throw mapAiException("AI score API 호출 실패", e);
        }
    }

    /**
     * FastAPI /explain 호출.
     *
     * @param request 위험도 점수 및 설명 생성 입력
     * @return AI 설명 결과
     */
    public ExplainResponseDto explain(ExplainRequestDto request) {
        try {
            return restTemplate.postForObject(
                    baseUrl + "/explain",
                    request,
                    ExplainResponseDto.class
            );
        } catch (RestClientException e) {
            throw mapAiException("AI explain API 호출 실패", e);
        }
    }

    /**
     * HTTP 클라이언트 예외를 서비스 공통 예외로 변환한다.
     *
     * 타임아웃 여부를 원인 예외 체인에서 확인한다.
     */
    private static ApiException mapAiException(
            String message,
            RestClientException cause
    ) {
        if (isTimeout(cause)) {
            return ApiException.aiTimeout(message, cause);
        }

        return ApiException.aiUnavailable(message, cause);
    }

    /**
     * 중첩된 예외 원인까지 검사해 타임아웃 여부를 판별한다.
     */
    private static boolean isTimeout(Throwable throwable) {
        Throwable current = throwable;

        while (current != null) {
            if (current instanceof SocketTimeoutException
                    || current instanceof TimeoutException) {
                return true;
            }

            String message = current.getMessage();

            if (message != null) {
                String lower = message.toLowerCase();

                if (lower.contains("timed out")
                        || lower.contains("timeout")) {
                    return true;
                }
            }

            current = current.getCause();
        }

        return false;
    }
}

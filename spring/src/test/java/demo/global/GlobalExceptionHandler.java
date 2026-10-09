
package com.example.demo.global.exception;

import com.example.demo.global.response.ApiResponse;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import static org.junit.jupiter.api.Assertions.*;

/**
 * [테스트 명세] 공통 예외 응답 테스트
 *
 * 대상 코드:
 * - ApiException
 * - GlobalExceptionHandler.handleApiException()
 *
 * 근거:
 * - IF_v2 ApiException.java
 * - IF_v2 GlobalExceptionHandler.java
 *
 * 테스트 유형: Unit Test
 *
 * 검증:
 * - 업무 오류별 HTTP 상태
 * - 공통 오류 코드
 * - 서버 내부 정보 비노출
 *
 * 실제 HTTP 요청을 보내는 테스트는 아니다.
 */
class GlobalExceptionHandlerTest {

    private GlobalExceptionHandler handler;

    @BeforeEach
    void setUp() {
        handler = new GlobalExceptionHandler();
    }

    /**
     * TC-GLOBAL-001
     * 잘못된 요청 -> HTTP 400
     */
    @Test
    void badRequest_returns400() {

        ApiException exception =
                ApiException.badRequest("잘못된 요청");

        ResponseEntity<ApiResponse<Void>> response =
                handler.handleApiException(exception);

        assertEquals(
                HttpStatus.BAD_REQUEST,
                response.getStatusCode()
        );

        assertNotNull(response.getBody());
        assertFalse(response.getBody().success());
        assertEquals(
                "INVALID_REQUEST",
                response.getBody().errorCode()
        );
    }

    /**
     * TC-GLOBAL-002
     * 데이터 없음 -> HTTP 404
     */
    @Test
    void notFound_returns404() {

        ApiException exception =
                ApiException.notFound("데이터 없음");

        ResponseEntity<ApiResponse<Void>> response =
                handler.handleApiException(exception);

        assertEquals(
                HttpStatus.NOT_FOUND,
                response.getStatusCode()
        );

        assertNotNull(response.getBody());
        assertEquals(
                "NOT_FOUND",
                response.getBody().errorCode()
        );
    }

    /**
     * TC-GLOBAL-003
     * AI 서비스 연결 장애 -> HTTP 502
     */
    @Test
    void aiUnavailable_returns502() {

        ApiException exception =
                ApiException.aiUnavailable(
                        "AI 연결 실패",
                        new RuntimeException("Connection refused")
                );

        ResponseEntity<ApiResponse<Void>> response =
                handler.handleApiException(exception);

        assertEquals(
                HttpStatus.BAD_GATEWAY,
                response.getStatusCode()
        );

        assertNotNull(response.getBody());
        assertEquals(
                "AI_SERVICE_UNAVAILABLE",
                response.getBody().errorCode()
        );

        // 내부 장애 원인은 사용자에게 노출하지 않는다.
        assertFalse(
                response.getBody().message()
                        .contains("Connection refused")
        );
    }

    /**
     * TC-GLOBAL-004
     * AI 타임아웃 -> HTTP 504
     */
    @Test
    void aiTimeout_returns504() {

        ApiException exception =
                ApiException.aiTimeout(
                        "AI timeout",
                        new RuntimeException("timeout")
                );

        ResponseEntity<ApiResponse<Void>> response =
                handler.handleApiException(exception);

        assertEquals(
                HttpStatus.GATEWAY_TIMEOUT,
                response.getStatusCode()
        );

        assertNotNull(response.getBody());
        assertEquals(
                "AI_SERVICE_TIMEOUT",
                response.getBody().errorCode()
        );
    }

    /**
     * TC-GLOBAL-005
     * 평가 상태 전이 오류 -> HTTP 400
     */
    @Test
    void invalidTransition_returns400() {

        ApiException exception =
                ApiException.invalidTransition(
                        "Invalid transition"
                );

        ResponseEntity<ApiResponse<Void>> response =
                handler.handleApiException(exception);

        assertEquals(
                HttpStatus.BAD_REQUEST,
                response.getStatusCode()
        );

        assertNotNull(response.getBody());
        assertEquals(
                "INVALID_STATUS_TRANSITION",
                response.getBody().errorCode()
        );
    }

    /**
     * TC-GLOBAL-006
     * 예상하지 못한 서버 오류 -> HTTP 500
     */
    @Test
    void unexpectedError_returns500() {

        ResponseEntity<ApiResponse<Void>> response =
                handler.handleUnexpected(
                        new RuntimeException("Secret DB error")
                );

        assertEquals(
                HttpStatus.INTERNAL_SERVER_ERROR,
                response.getStatusCode()
        );

        assertNotNull(response.getBody());
        assertEquals(
                "INTERNAL_ERROR",
                response.getBody().errorCode()
        );

        assertFalse(
                response.getBody().message()
                        .contains("Secret DB error")
        );
    }
}

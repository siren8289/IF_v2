
package com.example.demo.global.exception;

import org.springframework.http.HttpStatus;

/**
 * IF_v2 공통 API 예외 클래스.
 *
 * [역할]
 * - 서비스 계층에서 발생한 업무 오류를 표현한다.
 * - HTTP 상태 코드와 서비스 에러 코드를 함께 관리한다.
 * - GlobalExceptionHandler에서 일관된 JSON 응답으로 변환한다.
 *
 * [사용 모듈]
 * - applicant : 신청자 및 건강정보 검증
 * - assessment : 평가 생성 및 상태 전이 검증
 * - ai : FastAPI 연동 및 위험도 계산 오류
 *
 * [설계 원칙]
 * - 도메인별 단순 예외 클래스 중복 생성을 방지한다.
 * - 내부 서버 오류와 사용자 입력 오류를 구분한다.
 */
public class ApiException extends RuntimeException {

    // 클라이언트에 반환할 HTTP 상태 코드
    private final HttpStatus status;

    // 프론트엔드에서 오류를 식별하기 위한 코드
    private final String errorCode;

    /**
     * 업무 예외 생성.
     *
     * @param status HTTP 상태 코드
     * @param errorCode 서비스 에러 코드
     * @param message 오류 설명
     */
    public ApiException(
            HttpStatus status,
            String errorCode,
            String message
    ) {
        super(message);
        this.status = status;
        this.errorCode = errorCode;
    }

    /**
     * 외부 서비스 오류처럼 원인 예외를 보존해야 할 때 사용한다.
     */
    public ApiException(
            HttpStatus status,
            String errorCode,
            String message,
            Throwable cause
    ) {
        super(message, cause);
        this.status = status;
        this.errorCode = errorCode;
    }

    public HttpStatus getStatus() {
        return status;
    }

    public String getErrorCode() {
        return errorCode;
    }

    /**
     * 400 Bad Request
     * 필수 입력값 오류 또는 업무 규칙 위반.
     */
    public static ApiException badRequest(String message) {
        return new ApiException(
                HttpStatus.BAD_REQUEST,
                "INVALID_REQUEST",
                message
        );
    }

    /**
     * 404 Not Found
     * 신청자, 일자리, 평가 등 요청한 데이터가 없을 때 발생.
     */
    public static ApiException notFound(String message) {
        return new ApiException(
                HttpStatus.NOT_FOUND,
                "NOT_FOUND",
                message
        );
    }

    /**
     * 400 Bad Request
     * 평가 상태가 허용되지 않은 순서로 변경될 때 발생.
     *
     * 정상 흐름:
     * PENDING_AI → AI_COMPLETED → FINALIZED
     */
    public static ApiException invalidTransition(String message) {
        return new ApiException(
                HttpStatus.BAD_REQUEST,
                "INVALID_STATUS_TRANSITION",
                message
        );
    }

    /**
     * 502 Bad Gateway
     * FastAPI 연결 실패 또는 정상 응답을 받지 못한 경우.
     */
    public static ApiException aiUnavailable(
            String message,
            Throwable cause
    ) {
        return new ApiException(
                HttpStatus.BAD_GATEWAY,
                "AI_SERVICE_UNAVAILABLE",
                message,
                cause
        );
    }

    /**
     * 504 Gateway Timeout
     * FastAPI 응답 시간이 제한을 초과한 경우.
     */
    public static ApiException aiTimeout(
            String message,
            Throwable cause
    ) {
        return new ApiException(
                HttpStatus.GATEWAY_TIMEOUT,
                "AI_SERVICE_TIMEOUT",
                message,
                cause
        );
    }

    /**
     * 502 Bad Gateway
     * 위험도 점수가 0~100 범위를 벗어나거나
     * NaN, Infinity 등 유효하지 않은 값일 때 발생.
     */
    public static ApiException invalidAiScore(String message) {
        return new ApiException(
                HttpStatus.BAD_GATEWAY,
                "INVALID_AI_SCORE",
                message
        );
    }
}

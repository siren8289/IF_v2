
package com.example.demo.global.exception;

import com.example.demo.global.response.ApiResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.stream.Collectors;

/**
 * IF_v2 전역 예외 처리기.
 *
 * [역할]
 * - Controller/Service에서 발생한 예외를 HTTP 응답으로 변환
 * - 오류 응답 형식 통일
 * - 내부 오류 정보의 외부 노출 방지
 *
 * [처리 흐름]
 * Controller
 *    ↓
 * Service
 *    ↓ 예외 발생
 * GlobalExceptionHandler
 *    ↓
 * ApiResponse(JSON)
 */
@RestControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger log =
            LoggerFactory.getLogger(GlobalExceptionHandler.class);

    /**
     * 공통 업무 예외 처리.
     *
     * ApiException에 저장된 HTTP 상태와 에러 코드를 사용한다.
     * 서버 측 오류는 상세 메시지 대신 일반화된 문구를 반환한다.
     */
    @ExceptionHandler(ApiException.class)
    public ResponseEntity<ApiResponse<Void>> handleApiException(
            ApiException ex
    ) {
        if (ex.getStatus().is5xxServerError()) {
            log.error("API error: {}", ex.getErrorCode(), ex);
        }

        String message = ex.getStatus().is5xxServerError()
                ? "요청 처리 중 외부 서비스 오류가 발생했습니다."
                : ex.getMessage();

        return error(
                ex.getStatus(),
                ex.getErrorCode(),
                message
        );
    }

    /**
     * Bean Validation 오류 처리.
     *
     * @Valid로 검증한 DTO의 필수값, 범위,
     * 형식 등이 올바르지 않으면 HTTP 400을 반환한다.
     */
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ApiResponse<Void>> handleValidation(
            MethodArgumentNotValidException ex
    ) {
        String message = ex.getBindingResult()
                .getFieldErrors()
                .stream()
                .map(e -> e.getField() + ": "
                        + e.getDefaultMessage())
                .distinct()
                .collect(Collectors.joining(", "));

        return error(
                HttpStatus.BAD_REQUEST,
                "VALIDATION_ERROR",
                message
        );
    }

    /**
     * 요청 JSON 파싱 오류 처리.
     *
     * JSON 문법 오류 또는 필드 타입 불일치 시
     * HTTP 400을 반환한다.
     */
    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<ApiResponse<Void>> handleInvalidJson(
            HttpMessageNotReadableException ex
    ) {
        return error(
                HttpStatus.BAD_REQUEST,
                "INVALID_JSON",
                "요청 JSON 형식 또는 타입이 올바르지 않습니다."
        );
    }

    /**
     * 예상하지 못한 서버 오류 처리.
     *
     * 상세 스택 트레이스는 서버 로그에만 기록하고,
     * 사용자에게는 일반 오류 메시지만 반환한다.
     */
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiResponse<Void>> handleUnexpected(
            Exception ex
    ) {
        log.error("Unhandled exception", ex);

        return error(
                HttpStatus.INTERNAL_SERVER_ERROR,
                "INTERNAL_ERROR",
                "서버에서 예기치 않은 오류가 발생했습니다."
        );
    }

    /**
     * 공통 오류 응답 생성.
     *
     * @param status HTTP 상태
     * @param code 서비스 에러 코드
     * @param message 사용자에게 반환할 메시지
     */
    private ResponseEntity<ApiResponse<Void>> error(
            HttpStatus status,
            String code,
            String message
    ) {
        return ResponseEntity.status(status)
                .body(ApiResponse.<Void>error(code, message));
    }
}

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

/**
 * 컨트롤러 밖으로 새어 나온 예외를 JSON 오류로 바꾼다.
 * 모양은 { success:false, data:null, message, errorCode }.
 *
 * 화면의 apiRequest는 이 message만 꺼내 빨간 안내 문구로 보여 준다.
 * 예상 못 한 오류는 원인 문장을 숨기고 "서버 오류"만 돌려, 내부 정보를 노출하지 않는다.
 */
@RestControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    /** 서비스가 의도적으로 던진 오류. 없는 평가(404), AI 실패(502) 등. */
    @ExceptionHandler(ApiException.class)
    public ResponseEntity<ApiResponse<Void>> handleApiException(ApiException e) {
        if (e.getStatus().is5xxServerError()) {
            log.error("API error: {}", e.getMessage(), e);
        }
        return error(e.getStatus(), e.getErrorCode(), e.getMessage());
    }

    /** 나이 범위, 빈 이름처럼 @Valid 검사에 걸린 경우. 칸 이름과 이유를 이어 붙인다. */
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ApiResponse<Void>> handleValidation(MethodArgumentNotValidException e) {
        StringBuilder message = new StringBuilder();
        e.getBindingResult().getFieldErrors().forEach(fieldError ->
                message.append(fieldError.getField()).append(": ").append(fieldError.getDefaultMessage()).append(" "));
        return error(HttpStatus.BAD_REQUEST, "VALIDATION_ERROR", message.toString().trim());
    }

    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<ApiResponse<Void>> handleInvalidJson(HttpMessageNotReadableException e) {
        return error(HttpStatus.BAD_REQUEST, "INVALID_JSON", "요청 JSON 형식이 올바르지 않습니다.");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiResponse<Void>> handleUnexpected(Exception e) {
        log.error("Unhandled exception", e);
        return error(HttpStatus.INTERNAL_SERVER_ERROR, "INTERNAL_ERROR", "서버 오류가 발생했습니다.");
    }

    private ResponseEntity<ApiResponse<Void>> error(HttpStatus status, String code, String message) {
        return ResponseEntity.status(status).body(ApiResponse.error(code, message));
    }
}

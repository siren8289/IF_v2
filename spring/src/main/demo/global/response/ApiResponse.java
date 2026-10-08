
package com.example.demo.global.response;

/**
 * IF_v2 공통 API 응답 객체.
 *
 * [역할]
 * - 성공/실패 응답 구조 통일
 * - 프론트엔드에서 결과와 오류 코드 식별
 *
 * [JSON 구조]
 * {
 *   "success": true,
 *   "data": {},
 *   "message": null,
 *   "errorCode": null
 * }
 *
 * Java 17 record를 사용하여
 * 불필요한 필드 선언 및 getter 코드를 줄인다.
 *
 * @param success 요청 성공 여부
 * @param data 응답 데이터
 * @param message 사용자 메시지
 * @param errorCode 서비스 오류 코드
 */
public record ApiResponse<T>(
        boolean success,
        T data,
        String message,
        String errorCode
) {

    /**
     * 데이터가 있는 성공 응답.
     */
    public static <T> ApiResponse<T> ok(T data) {
        return new ApiResponse<>(
                true, data, null, null
        );
    }

    /**
     * 데이터와 안내 메시지가 있는 성공 응답.
     */
    public static <T> ApiResponse<T> ok(
            T data,
            String message
    ) {
        return new ApiResponse<>(
                true, data, message, null
        );
    }

    /**
     * 실패 응답.
     *
     * 실패 시 data는 null이며
     * errorCode와 message를 반환한다.
     */
    public static <T> ApiResponse<T> error(
            String errorCode,
            String message
    ) {
        return new ApiResponse<>(
                false, null, message, errorCode
        );
    }
}

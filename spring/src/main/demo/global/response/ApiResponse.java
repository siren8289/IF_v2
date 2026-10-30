package com.example.demo.global.response;

/**
 * 오류 응답 형식.
 * record 는 칸을 적으면 생성자와 getter가 자동으로 생기는 자료 상자다.
 * 성공 응답은 컨트롤러가 데이터 객체를 바로 돌려주고, 이 상자는 오류에만 쓴다.
 */
public record ApiResponse<T>(boolean success, T data, String message, String errorCode) {

    public static <T> ApiResponse<T> error(String errorCode, String message) {
        return new ApiResponse<>(false, null, message, errorCode);
    }
}

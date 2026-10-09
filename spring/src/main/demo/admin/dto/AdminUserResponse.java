
package com.example.demo.admin.dto;

/**
 * 관리자 조회 응답 DTO.
 *
 * [목적]
 * - Entity 직접 반환 방지
 * - 화면에 필요한 정보만 전달
 *
 * createdAt 등 내부 관리 필드는 제외한다.
 */
public record AdminUserResponse(
        Long id,
        String name,
        String organization,
        String role
) {
}


package com.example.demo.admin.service;

import com.example.demo.admin.dto.AdminUserResponse;
import com.example.demo.admin.entity.AdminUser;
import com.example.demo.admin.repository.AdminUserRepository;
import com.example.demo.global.exception.ApiException;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

/**
 * [테스트 명세] 관리자 조회 단위 테스트
 *
 * 대상 코드:
 * - AdminUserService.getAdmin()
 * - AdminUserService.getAdmins()
 *
 * 근거:
 * - IF_v2 AdminUserService.java (리팩터링안)
 * - IF_v2 AdminUserRepository.java
 * - IF_v2 ApiException.java
 *
 * 테스트 유형: Unit Test
 * 검증 범위: 조회 성공, 미존재, 입력값 검증
 *
 * 실제 DB 연결 및 인증/인가 검증은 포함하지 않는다.
 */
@ExtendWith(MockitoExtension.class)
class AdminUserServiceTest {

    @Mock
    private AdminUserRepository adminRepository;

    private AdminUserService adminService;

    @BeforeEach
    void setUp() {
        adminService = new AdminUserService(adminRepository);
    }

    /**
     * TC-ADMIN-001
     * 근거: getAdmin()
     * Given: 관리자 ID 1 존재
     * When: 관리자 조회
     * Then: DTO 필드 일치
     */
    @Test
    void getAdmin_success() {

        AdminUser admin = new AdminUser();
        admin.setId(1L);
        admin.setName("테스트 관리자");
        admin.setOrganization("테스트 기관");
        admin.setRole("operator");

        when(adminRepository.findById(1L))
                .thenReturn(Optional.of(admin));

        AdminUserResponse result = adminService.getAdmin(1L);

        assertAll(
                () -> assertEquals(1L, result.id()),
                () -> assertEquals("테스트 관리자", result.name()),
                () -> assertEquals("테스트 기관", result.organization()),
                () -> assertEquals("operator", result.role())
        );

        verify(adminRepository).findById(1L);
    }

    /**
     * TC-ADMIN-002
     * 근거: getAdmin()의 미존재 처리
     * 기대: NOT_FOUND
     */
    @Test
    void getAdmin_notFound() {

        when(adminRepository.findById(999L))
                .thenReturn(Optional.empty());

        ApiException exception = assertThrows(
                ApiException.class,
                () -> adminService.getAdmin(999L)
        );

        assertEquals("NOT_FOUND", exception.getErrorCode());
    }

    /**
     * TC-ADMIN-003
     * 근거: adminId 양수 검증
     * 기대: INVALID_REQUEST
     */
    @Test
    void getAdmin_invalidId() {

        ApiException exception = assertThrows(
                ApiException.class,
                () -> adminService.getAdmin(-1L)
        );

        assertEquals(
                "INVALID_REQUEST",
                exception.getErrorCode()
        );

        verifyNoInteractions(adminRepository);
    }

    /**
     * TC-ADMIN-004
     * 근거: getAdmins()의 페이지 크기 검증
     * 기대: size 101 차단
     */
    @Test
    void getAdmins_invalidSize() {

        assertThrows(
                ApiException.class,
                () -> adminService.getAdmins(0, 101)
        );

        verifyNoInteractions(adminRepository);
    }

    /**
     * TC-ADMIN-005
     * 근거: getAdmins()의 페이지 번호 검증
     * 기대: 음수 page 차단
     */
    @Test
    void getAdmins_invalidPage() {

        assertThrows(
                ApiException.class,
                () -> adminService.getAdmins(-1, 20)
        );

        verifyNoInteractions(adminRepository);
    }
}

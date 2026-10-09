
package com.example.demo.admin.service;

import com.example.demo.admin.dto.AdminUserResponse;
import com.example.demo.admin.entity.AdminUser;
import com.example.demo.admin.repository.AdminUserRepository;
import com.example.demo.global.exception.ApiException;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * 관리자 조회 서비스.
 *
 * [기능]
 * 1. 관리자 목록 조회
 * 2. 관리자 상세 조회
 *
 * [설계]
 * - 조회 전용 트랜잭션
 * - 페이지네이션
 * - Entity -> DTO 변환
 *
 * [보안]
 * 인증/인가를 구현하기 전에는
 * 이 API를 외부에 공개하지 않는다.
 */
@Service
@Transactional(readOnly = true)
public class AdminUserService {

    private final AdminUserRepository adminRepository;

    public AdminUserService(
            AdminUserRepository adminRepository
    ) {
        this.adminRepository = adminRepository;
    }

    /**
     * [기능] 관리자 목록 조회.
     *
     * page: 0부터 시작
     * size: 최대 100
     */
    public Page<AdminUserResponse> getAdmins(
            int page,
            int size
    ) {

        if (page < 0) {
            throw ApiException.badRequest(
                    "page must be 0 or greater"
            );
        }

        if (size < 1 || size > 100) {
            throw ApiException.badRequest(
                    "size must be between 1 and 100"
            );
        }

        Pageable pageable = PageRequest.of(
                page,
                size,
                Sort.by(Sort.Direction.ASC, "id")
        );

        return adminRepository.findAll(pageable)
                .map(this::toResponse);
    }

    /**
     * [기능] 관리자 상세 조회.
     *
     * 존재하지 않는 관리자는 404.
     */
    public AdminUserResponse getAdmin(Long adminId) {

        if (adminId == null || adminId <= 0) {
            throw ApiException.badRequest(
                    "adminId must be positive"
            );
        }

        AdminUser admin = adminRepository.findById(adminId)
                .orElseThrow(() -> ApiException.notFound(
                        "Admin not found: " + adminId
                ));

        return toResponse(admin);
    }

    /**
     * [공통] Entity -> Response DTO.
     */
    private AdminUserResponse toResponse(AdminUser admin) {

        return new AdminUserResponse(
                admin.getId(),
                admin.getName(),
                admin.getOrganization(),
                admin.getRole()
        );
    }
}

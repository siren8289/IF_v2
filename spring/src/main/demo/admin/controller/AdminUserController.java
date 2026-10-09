
package com.example.demo.admin.controller;

import com.example.demo.admin.dto.AdminUserResponse;
import com.example.demo.admin.service.AdminUserService;

import org.springframework.data.domain.Page;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * 관리자 REST API.
 *
 * [API]
 * GET /api/admins
 * GET /api/admins/{adminId}
 *
 * [주의]
 * 현재는 개발용 조회 API다.
 * Spring Security 인증/인가 적용 전까지
 * 운영 환경에 공개하면 안 된다.
 */
@RestController
@RequestMapping("/api/admins")
public class AdminUserController {

    private final AdminUserService adminService;

    public AdminUserController(
            AdminUserService adminService
    ) {
        this.adminService = adminService;
    }

    /**
     * [API] 관리자 목록 조회.
     */
    @GetMapping
    public Page<AdminUserResponse> getAdmins(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "20") int size
    ) {
        return adminService.getAdmins(page, size);
    }

    /**
     * [API] 관리자 상세 조회.
     */
    @GetMapping("/{adminId}")
    public AdminUserResponse getAdmin(
            @PathVariable Long adminId
    ) {
        return adminService.getAdmin(adminId);
    }
}

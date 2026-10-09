
package com.example.demo.admin.repository;

import com.example.demo.admin.entity.AdminUser;

import org.springframework.data.jpa.repository.JpaRepository;

/**
 * 관리자 DB 접근 계층.
 *
 * JpaRepository에서 제공하는 기본 조회 기능을 사용한다.
 *
 * - findAll(Pageable)
 * - findById(Long)
 * - existsById(Long)
 *
 * 현재 추가 쿼리는 필요하지 않다.
 */
public interface AdminUserRepository
        extends JpaRepository<AdminUser, Long> {
}

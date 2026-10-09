
package com.example.demo.admin.entity;

import jakarta.persistence.*;

import java.time.OffsetDateTime;
import java.time.ZoneOffset;

/**
 * 관리자 엔티티.
 *
 * [DB]
 * admin_user
 *
 * [역할]
 * - 관리자 기본 정보 관리
 * - Assessment의 담당 관리자 참조
 *
 * [권한]
 * operator   : 일반 담당자
 * supervisor : 관리자
 *
 * 주의: role 필드는 권한 정보일 뿐,
 * 실제 접근 제어는 인증/인가 구현 후 적용한다.
 */
@Entity
@Table(name = "admin_user")
public class AdminUser {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "admin_id")
    private Long id;

    // 관리자 이름
    @Column(name = "name")
    private String name;

    // 소속 기관
    @Column(name = "organization")
    private String organization;

    // 관리자 역할
    @Column(name = "role")
    private String role;

    // 최초 등록 시각
    @Column(
            name = "created_at",
            nullable = false,
            updatable = false
    )
    private OffsetDateTime createdAt;

    /**
     * 신규 관리자 저장 시 생성 시각 자동 설정.
     */
    @PrePersist
    public void prePersist() {
        if (createdAt == null) {
            createdAt = OffsetDateTime.now(ZoneOffset.UTC);
        }
    }

    // Getter / Setter

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public OffsetDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(OffsetDateTime createdAt) {
        this.createdAt = createdAt;
    }
}

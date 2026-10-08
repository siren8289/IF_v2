
package com.example.demo.applicant.entity;

import jakarta.persistence.*;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;

/**
 * 신청자 엔티티.
 *
 * [DB] applicant
 * [PK] applicant_id
 *
 * 신청자의 기본 정보를 저장한다.
 * 건강정보는 별도 HealthSnapshot 엔티티에서 관리한다.
 */
@Entity
@Table(name = "applicant")
public class Applicant {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "applicant_id")
    private Long id;

    @Column(name = "display_name")
    private String displayName;

    @Column(name = "age")
    private Integer age;

    @Column(name = "created_at", nullable = false, updatable = false)
    private OffsetDateTime createdAt;

    protected Applicant() {
        // JPA 객체 생성용 기본 생성자
    }

    /**
     * 신규 신청자 생성.
     * ID는 DB에서 자동 생성한다.
     */
    public Applicant(String displayName, Integer age) {
        this.displayName = displayName;
        this.age = age;
        this.createdAt = OffsetDateTime.now(ZoneOffset.UTC);
    }

    public Long getId() { return id; }
    public String getDisplayName() { return displayName; }
    public Integer getAge() { return age; }
    public OffsetDateTime getCreatedAt() { return createdAt; }
}

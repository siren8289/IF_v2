
package com.example.demo.job.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.PrePersist;
import jakarta.persistence.Table;

import java.time.OffsetDateTime;
import java.time.ZoneOffset;

/**
 * 일자리 엔티티.
 *
 * [DB 테이블]
 * job
 *
 * [역할]
 * - 일자리 기본 정보 저장
 * - Assessment에서 평가 대상 일자리로 참조
 *
 * [주의]
 * DB 컬럼명은 기존 스키마와 동일하게 유지한다.
 */
@Entity
@Table(name = "job")
public class Job {

    // 일자리 고유 식별자
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "job_id")
    private Long id;

    // 일자리명
    @Column(name = "job_title")
    private String jobTitle;

    // 근무지역
    @Column(name = "workplace")
    private String workplace;

    // 근무시간
    @Column(name = "work_hours")
    private String workHours;

    // 일자리 상세 설명
    @Column(name = "description", columnDefinition = "text")
    private String description;

    // 최초 생성 일시
    @Column(
            name = "created_at",
            nullable = false,
            updatable = false
    )
    private OffsetDateTime createdAt;

    /**
     * 신규 Entity 저장 직전에 생성 시간을 설정한다.
     *
     * 외부 ETL에서 생성 시간이 제공되면
     * 기존 값을 덮어쓰지 않는다.
     */
    @PrePersist
    public void prePersist() {
        if (createdAt == null) {
            createdAt = OffsetDateTime.now(ZoneOffset.UTC);
        }
    }

    // ==============================
    // Getter / Setter
    // ==============================

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getJobTitle() {
        return jobTitle;
    }

    public void setJobTitle(String jobTitle) {
        this.jobTitle = jobTitle;
    }

    public String getWorkplace() {
        return workplace;
    }

    public void setWorkplace(String workplace) {
        this.workplace = workplace;
    }

    public String getWorkHours() {
        return workHours;
    }

    public void setWorkHours(String workHours) {
        this.workHours = workHours;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public OffsetDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(OffsetDateTime createdAt) {
        this.createdAt = createdAt;
    }
}

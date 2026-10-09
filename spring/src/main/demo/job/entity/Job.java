
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
 * - Assessment 평가 대상 일자리 참조
 * - 공공데이터 원본 공고 ID 관리
 * - FastAPI F-001 / F-002 / F-003 연결
 *
 * [ID 구분]
 * id            : Spring DB 내부 PK
 * externalJobId : 공공데이터 원본 공고 ID
 *
 * [주의]
 * 기존 컬럼은 유지하고 external_job_id만 추가한다.
 */
@Entity
@Table(name = "job")
public class Job {

    /**
     * Spring 내부 일자리 ID.
     *
     * PostgreSQL에서 자동 생성한다.
     * Assessment.job_id가 참조한다.
     */
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "job_id")
    private Long id;

    /**
     * 공공데이터 원본 공고 ID.
     *
     * 예: KJ21062610080016
     *
     * FastAPI F-002 / F-003에서 사용하는
     * job_id와 연결하기 위한 필드다.
     *
     * 수동 등록 일자리에는 외부 ID가
     * 없을 수 있으므로 nullable로 둔다.
     */
    @Column(name = "external_job_id", length = 100)
    private String externalJobId;

    /**
     * 일자리명.
     */
    @Column(name = "job_title")
    private String jobTitle;

    /**
     * 근무지역.
     */
    @Column(name = "workplace")
    private String workplace;

    /**
     * 근무시간.
     */
    @Column(name = "work_hours")
    private String workHours;

    /**
     * 일자리 상세 설명.
     */
    @Column(name = "description", columnDefinition = "text")
    private String description;

    /**
     * 최초 생성 일시.
     */
    @Column(
            name = "created_at",
            nullable = false,
            updatable = false
    )
    private OffsetDateTime createdAt;

    /**
     * 신규 데이터 저장 직전에 생성 시간을 설정한다.
     *
     * ETL에서 createdAt을 제공했다면
     * 기존 값을 덮어쓰지 않는다.
     */
    @PrePersist
    public void prePersist() {
        if (createdAt == null) {
            createdAt = OffsetDateTime.now(ZoneOffset.UTC);
        }
    }

    // ========================================================
    // Getter / Setter
    // ========================================================

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getExternalJobId() {
        return externalJobId;
    }

    public void setExternalJobId(String externalJobId) {
        this.externalJobId = externalJobId;
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

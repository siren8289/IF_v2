
package com.example.demo.applicant.entity;

import jakarta.persistence.*;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;

/**
 * 신청자 건강정보 스냅샷.
 *
 * [DB] health_snapshot
 * [PK] health_id
 * [FK] applicant_id → applicant.applicant_id
 *
 * 신청자 한 명이 여러 건강정보 기록을 가질 수 있다.
 * 평가 시 선택한 스냅샷을 기준으로 위험도를 계산한다.
 */
@Entity
@Table(name = "health_snapshot")
public class HealthSnapshot {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "health_id")
    private Long id;

    /** 건강정보 소유 신청자. 지연 로딩으로 불필요한 조회를 줄인다. */
    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "applicant_id", nullable = false)
    private Applicant applicant;

    /** 신체활동 수준: 1~5 */
    @Column(name = "physical_level")
    private Integer physicalLevel;

    /** 만성질환 여부 */
    @Column(name = "chronic_disease_flag")
    private Boolean chronicDiseaseFlag;

    /** 근무 가능 시간 */
    @Column(name = "work_hour_limit")
    private Integer workHourLimit;

    /** 스냅샷 생성 시각 */
    @Column(name = "created_at", nullable = false, updatable = false)
    private OffsetDateTime createdAt;

    protected HealthSnapshot() {
        // JPA 객체 생성용
    }

    /**
     * 신청자에게 귀속된 건강정보 스냅샷을 생성한다.
     * 기존 기록을 수정하지 않고 새로운 기록을 저장한다.
     */
    public HealthSnapshot(
            Applicant applicant,
            Integer physicalLevel,
            Boolean chronicDiseaseFlag,
            Integer workHourLimit
    ) {
        this.applicant = applicant;
        this.physicalLevel = physicalLevel;
        this.chronicDiseaseFlag = chronicDiseaseFlag;
        this.workHourLimit = workHourLimit;
        this.createdAt = OffsetDateTime.now(ZoneOffset.UTC);
    }

    public Long getId() { return id; }
    public Applicant getApplicant() { return applicant; }
    public Integer getPhysicalLevel() { return physicalLevel; }
    public Boolean getChronicDiseaseFlag() { return chronicDiseaseFlag; }
    public Integer getWorkHourLimit() { return workHourLimit; }
    public OffsetDateTime getCreatedAt() { return createdAt; }
}

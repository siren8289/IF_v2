package com.example.demo.assessment.entity;

import com.example.demo.ai.entity.AIRiskResult;
import com.example.demo.applicant.entity.Applicant;
import com.example.demo.applicant.entity.HealthSnapshot;
import com.example.demo.job.entity.Job;
import jakarta.persistence.*;

import java.time.OffsetDateTime;

/**
 * 평가 한 건. DB 테이블 이름은 assessment.
 *
 * 한 평가는 신청자, 직무, 그 시점의 건강 정보, AI 결과를 가리킨다.
 * @Entity 는 이 클래스가 DB 행과 대응한다는 표시다.
 * @ManyToOne 은 "여러 평가가 신청자 한 명을 가리킬 수 있다"는 뜻이고,
 * @OneToOne 은 평가와 건강 스냅샷, 평가와 AI 결과가 1:1 이라는 뜻이다.
 * LAZY 는 그 연결 대상을 실제로 쓸 때만 DB에서 가져오라는 설정이다.
 */
@Entity
@Table(name = "assessment")
public class Assessment {

    /** DB가 1, 2, 3... 순으로 자동으로 매기는 번호. */
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "assessment_id")
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "applicant_id")
    private Applicant applicant;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "job_id")
    private Job job;

    @OneToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "health_id")
    private HealthSnapshot healthSnapshot;

    @OneToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "ai_result_id")
    private AIRiskResult aiRiskResult;

    @Enumerated(EnumType.STRING)
    @Column(name = "status", nullable = false)
    private AssessmentStatus status;

    @Column(name = "assessed_at")
    private OffsetDateTime assessedAt;

    public Long getId() { return id; }
    public Applicant getApplicant() { return applicant; }
    public void setApplicant(Applicant applicant) { this.applicant = applicant; }
    public Job getJob() { return job; }
    public void setJob(Job job) { this.job = job; }
    public HealthSnapshot getHealthSnapshot() { return healthSnapshot; }
    public void setHealthSnapshot(HealthSnapshot healthSnapshot) { this.healthSnapshot = healthSnapshot; }
    public AIRiskResult getAiRiskResult() { return aiRiskResult; }
    public void setAiRiskResult(AIRiskResult aiRiskResult) { this.aiRiskResult = aiRiskResult; }
    public AssessmentStatus getStatus() { return status; }
    public void setStatus(AssessmentStatus status) { this.status = status; }
    public OffsetDateTime getAssessedAt() { return assessedAt; }
    public void setAssessedAt(OffsetDateTime assessedAt) { this.assessedAt = assessedAt; }
}

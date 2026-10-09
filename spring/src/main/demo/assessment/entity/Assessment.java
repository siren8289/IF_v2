package com.example.demo.assessment.entity;

import com.example.demo.ai.entity.AIRiskResult;
import com.example.demo.applicant.entity.Applicant;
import com.example.demo.applicant.entity.HealthSnapshot;
import com.example.demo.job.entity.Job;
import jakarta.persistence.*;

import java.time.OffsetDateTime;

@Entity
@Table(name = "assessment")
public class Assessment {

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

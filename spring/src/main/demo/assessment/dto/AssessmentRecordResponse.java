package com.example.demo.assessment.dto;

import com.example.demo.assessment.entity.AssessmentStatus;

import java.time.OffsetDateTime;

/** 대시보드 목록 한 줄. AssessmentRepository.findAllRecords 쿼리가 이 생성자로 값을 채운다. */
public class AssessmentRecordResponse {

    private final Long id;
    private final String applicantName;
    private final Integer age;
    private final String jobTitle;
    private final Integer physicalLevel;
    private final String status;
    private final Integer riskScore;
    private final String riskGrade;
    private final OffsetDateTime assessedAt;

    public AssessmentRecordResponse(Long id, String applicantName, Integer age, String jobTitle,
                                    Integer physicalLevel, AssessmentStatus status,
                                    Integer riskScore, String riskGrade, OffsetDateTime assessedAt) {
        this.id = id;
        this.applicantName = applicantName;
        this.age = age;
        this.jobTitle = jobTitle;
        this.physicalLevel = physicalLevel;
        this.status = status.name();
        this.riskScore = riskScore;
        this.riskGrade = riskGrade;
        this.assessedAt = assessedAt;
    }

    public Long getId() { return id; }
    public String getApplicantName() { return applicantName; }
    public Integer getAge() { return age; }
    public String getJobTitle() { return jobTitle; }
    public Integer getPhysicalLevel() { return physicalLevel; }
    public String getStatus() { return status; }
    public Integer getRiskScore() { return riskScore; }
    public String getRiskGrade() { return riskGrade; }
    public OffsetDateTime getAssessedAt() { return assessedAt; }
}

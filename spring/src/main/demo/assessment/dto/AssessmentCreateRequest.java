
package com.example.demo.assessment.dto;

import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;

public class AssessmentCreateRequest {

    @NotNull(message = "jobId는 필수입니다.")
    @Positive(message = "jobId는 1 이상이어야 합니다.")
    private Long jobId;

    @NotNull(message = "healthId는 필수입니다.")
    @Positive(message = "healthId는 1 이상이어야 합니다.")
    private Long healthId;

    public Long getJobId() {
        return jobId;
    }

    public void setJobId(Long jobId) {
        this.jobId = jobId;
    }

    public Long getHealthId() {
        return healthId;
    }

    public void setHealthId(Long healthId) {
        this.healthId = healthId;
    }
}

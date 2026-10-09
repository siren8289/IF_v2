package com.example.demo.assessment.dto;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

/** 평가 입력 화면에서 보내는 값 */
public record AssessmentCreateRequest(
        @NotBlank @Size(max = 50) String applicantName,
        @NotNull @Min(1) @Max(120) Integer age,
        @NotNull @Min(1) @Max(5) Integer physicalLevel,   // 1=좋음 ~ 5=나쁨
        @NotNull Boolean chronicDisease,
        @NotNull @Min(1) @Max(24) Integer workHourLimit,
        @NotNull Long jobId
) {
}

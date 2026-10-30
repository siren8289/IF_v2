package com.example.demo.assessment.dto;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

/**
 * 평가 입력 화면에서 보내는 JSON.
 * 어노테이션이 범위를 검사한다. 나이 1~120, 건강 1~5, 근무시간 1~24.
 * 하나라도 어기면 컨트롤러의 @Valid 가 400을 돌려주고 서비스까지 가지 않는다.
 */
public record AssessmentCreateRequest(
        @NotBlank @Size(max = 50) String applicantName,
        @NotNull @Min(1) @Max(120) Integer age,
        @NotNull @Min(1) @Max(5) Integer physicalLevel,   // 1=좋음 ~ 5=나쁨
        @NotNull Boolean chronicDisease,
        @NotNull @Min(1) @Max(24) Integer workHourLimit,
        @NotNull Long jobId
) {
}

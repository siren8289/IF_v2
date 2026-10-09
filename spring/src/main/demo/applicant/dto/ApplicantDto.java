
package com.example.demo.applicant.dto;

import jakarta.validation.constraints.*;
import java.time.OffsetDateTime;

/**
 * 신청자 및 건강정보 API의 요청·응답 DTO 모음.
 *
 * Entity를 API 응답으로 직접 노출하지 않는다.
 * 각 record는 독립된 JSON 요청 또는 응답 구조를 나타낸다.
 */
public final class ApplicantDto {

    private ApplicantDto() {
        // DTO 컨테이너이므로 객체 생성을 금지한다.
    }

    /**
     * 신청자 등록 요청.
     * 기존 JSON 필드 displayName, age를 유지한다.
     */
    public record CreateRequest(
            @NotBlank(message = "이름은 필수입니다.")
            String displayName,

            @NotNull(message = "나이는 필수입니다.")
            @Min(value = 1, message = "나이는 1 이상이어야 합니다.")
            @Max(value = 120, message = "나이는 120 이하여야 합니다.")
            Integer age
    ) {}

    /** 신청자 등록·조회 응답. */
    public record Response(
            Long id,
            String displayName,
            Integer age,
            OffsetDateTime createdAt
    ) {}

    /**
     * 건강정보 등록 요청.
     *
     * physicalLevel : 신체활동 수준 1~5
     * chronicDiseaseFlag : 만성질환 여부
     * workHourLimit : 근무 가능 시간
     */
    public record HealthCreateRequest(
            @NotNull(message = "신체활동 수준은 필수입니다.")
            @Min(1) @Max(5)
            Integer physicalLevel,

            @NotNull(message = "만성질환 여부는 필수입니다.")
            Boolean chronicDiseaseFlag,

            @NotNull(message = "근무 가능 시간은 필수입니다.")
            @Positive
            @Max(24)
            Integer workHourLimit
    ) {}

    /** 건강정보 등록 응답. */
    public record HealthResponse(
            Long id,
            Long applicantId,
            Integer physicalLevel,
            Boolean chronicDiseaseFlag,
            Integer workHourLimit,
            OffsetDateTime createdAt
    ) {}
}

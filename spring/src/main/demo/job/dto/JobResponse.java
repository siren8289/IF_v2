
package com.example.demo.job.dto;

import java.time.OffsetDateTime;

/**
 * 일자리 API 응답 DTO.
 *
 * [역할]
 * - Job Entity의 데이터를 클라이언트에 전달
 * - JPA Entity 직접 노출 방지
 *
 * [사용 API]
 * GET /api/jobs
 * GET /api/jobs/{jobId}
 */
public record JobResponse(

        // 일자리 ID
        Long id,

        // 일자리명
        String jobTitle,

        // 근무지역
        String workplace,

        // 근무시간
        String workHours,

        // 상세 설명
        String description,

        // 등록 일시
        OffsetDateTime createdAt

) {
}

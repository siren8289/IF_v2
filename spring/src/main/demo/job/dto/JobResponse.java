
package com.example.demo.job.dto;

import java.time.OffsetDateTime;

/**
 * 일자리 API 응답 DTO.
 *
 * [사용 API]
 * GET /api/jobs
 * GET /api/jobs/{jobId}
 *
 * [연결 기능]
 * - Spring: 일자리 목록 및 상세 조회
 * - FastAPI F-001: 직무 분석
 * - FastAPI F-002: 산업재해 통계 근거 조회
 * - FastAPI F-003: 통계 근거 기반 설명
 *
 * [ID 구분]
 * id            : Spring 내부 일자리 PK
 * externalJobId : 공공데이터 원본 공고 ID
 *
 * Entity를 외부에 직접 노출하지 않기 위해
 * 불변 record DTO를 사용한다.
 */
public record JobResponse(

        /**
         * Spring 내부 일자리 ID.
         */
        Long id,

        /**
         * 공공데이터 원본 공고 ID.
         *
         * 예: KJ21062610080016
         *
         * 외부 공고와 연결되지 않은 경우 null.
         */
        String externalJobId,

        /**
         * 일자리명.
         */
        String jobTitle,

        /**
         * 근무지역.
         */
        String workplace,

        /**
         * 근무시간.
         */
        String workHours,

        /**
         * 일자리 상세 설명.
         */
        String description,

        /**
         * 등록 일시.
         */
        OffsetDateTime createdAt

) {
}

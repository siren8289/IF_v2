
package com.example.demo.job.controller;

import com.example.demo.job.dto.JobResponse;
import com.example.demo.job.service.JobService;

import org.springframework.data.domain.Page;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * 일자리 REST API Controller.
 *
 * [API 목록]
 *
 * GET /api/jobs
 * - 일자리 목록 조회
 *
 * GET /api/jobs?keyword=서울
 * - 키워드 검색
 *
 * GET /api/jobs?page=0&size=20
 * - 페이지네이션
 *
 * GET /api/jobs/{jobId}
 * - 일자리 상세 조회
 *
 * [역할]
 * HTTP 요청 파라미터를 받아 Service에 전달한다.
 * 업무 규칙은 Controller에 작성하지 않는다.
 */
@RestController
@RequestMapping("/api/jobs")
public class JobController {

    private final JobService jobService;

    public JobController(JobService jobService) {
        this.jobService = jobService;
    }

    /**
     * [API-001] 일자리 목록 조회 및 검색.
     *
     * @param keyword 검색어 (선택)
     * @param page 페이지 번호 (기본 0)
     * @param size 페이지 크기 (기본 20)
     */
    @GetMapping
    public Page<JobResponse> searchJobs(
            @RequestParam(required = false)
            String keyword,

            @RequestParam(defaultValue = "0")
            int page,

            @RequestParam(defaultValue = "20")
            int size
    ) {

        return jobService.searchJobs(
                keyword,
                page,
                size
        );
    }

    /**
     * [API-002] 일자리 상세 조회.
     *
     * @param jobId 일자리 고유 ID
     */
    @GetMapping("/{jobId}")
    public JobResponse getJob(
            @PathVariable Long jobId
    ) {

        return jobService.getJob(jobId);
    }
}


package com.example.demo.job.service;

import com.example.demo.global.exception.ApiException;
import com.example.demo.job.dto.JobResponse;
import com.example.demo.job.entity.Job;
import com.example.demo.job.repository.JobRepository;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * 일자리 비즈니스 로직.
 *
 * [기능]
 * 1. 전체 목록 조회
 * 2. 키워드 검색
 * 3. 상세 조회
 *
 * [처리 순서]
 * Controller -> Service -> Repository
 *
 * [트랜잭션]
 * 조회 전용이므로 readOnly=true.
 */
@Service
@Transactional(readOnly = true)
public class JobService {

    private final JobRepository jobRepository;

    public JobService(JobRepository jobRepository) {
        this.jobRepository = jobRepository;
    }

    /**
     * [기능] 일자리 목록 검색.
     *
     * page: 0부터 시작
     * size: 1~100
     *
     * 최신 등록순으로 조회한다.
     */
    public Page<JobResponse> searchJobs(
            String keyword,
            int page,
            int size
    ) {

        // 페이지 번호 검증
        if (page < 0) {
            throw ApiException.badRequest(
                    "page must be 0 or greater"
            );
        }

        // 페이지 크기 검증
        if (size < 1 || size > 100) {
            throw ApiException.badRequest(
                    "size must be between 1 and 100"
            );
        }

        // 검색어 정규화
        String normalizedKeyword =
                keyword == null || keyword.isBlank()
                        ? null
                        : keyword.trim();

        // 검색어 길이 제한
        if (normalizedKeyword != null
                && normalizedKeyword.length() > 100) {

            throw ApiException.badRequest(
                    "keyword must be 100 characters or less"
            );
        }

        // 최신 등록순 + ID 역순
        Pageable pageable = PageRequest.of(
                page,
                size,
                Sort.by(
                        Sort.Order.desc("createdAt"),
                        Sort.Order.desc("id")
                )
        );

        // DB 검색 후 응답 DTO로 변환
        return jobRepository
                .searchJobs(normalizedKeyword, pageable)
                .map(this::toResponse);
    }

    /**
     * [기능] 일자리 상세 조회.
     *
     * 존재하지 않으면 404 오류.
     */
    public JobResponse getJob(Long jobId) {

        if (jobId == null || jobId <= 0) {
            throw ApiException.badRequest(
                    "jobId must be positive"
            );
        }

        Job job = jobRepository.findById(jobId)
                .orElseThrow(() -> ApiException.notFound(
                        "Job not found: " + jobId
                ));

        return toResponse(job);
    }

    /**
     * [공통] Entity -> DTO 변환.
     *
     * DTO는 record이므로 생성자로 값을 전달한다.
     */
    private JobResponse toResponse(Job job) {

        return new JobResponse(
                job.getId(),
                job.getJobTitle(),
                job.getWorkplace(),
                job.getWorkHours(),
                job.getDescription(),
                job.getCreatedAt()
        );
    }
}


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
 * 1. 전체 일자리 목록 조회
 * 2. 키워드 검색
 * 3. 페이지네이션
 * 4. 일자리 상세 조회
 * 5. 공공데이터 원본 공고 ID 응답 매핑
 *
 * [처리 흐름]
 * JobController
 *   -> JobService
 *   -> JobRepository
 *   -> PostgreSQL
 *
 * [ID 구분]
 * Job.id            : Spring 내부 PK
 * Job.externalJobId : 공공데이터 원본 공고 ID
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
     * [기능] 일자리 목록 조회 및 검색.
     *
     * @param keyword 검색어 (선택)
     * @param page 페이지 번호 (0부터 시작)
     * @param size 페이지 크기 (1~100)
     *
     * [처리]
     * 1. 요청 파라미터 검증
     * 2. 검색어 정규화
     * 3. 최신 등록순 정렬
     * 4. DB 조회
     * 5. Entity -> DTO 변환
     */
    public Page<JobResponse> searchJobs(
            String keyword,
            int page,
            int size
    ) {

        // 1. 페이지 번호 검증
        if (page < 0) {
            throw ApiException.badRequest(
                    "page must be 0 or greater"
            );
        }

        // 2. 페이지 크기 검증
        if (size < 1 || size > 100) {
            throw ApiException.badRequest(
                    "size must be between 1 and 100"
            );
        }

        // 3. 검색어 정규화
        String normalizedKeyword =
                keyword == null || keyword.isBlank()
                        ? null
                        : keyword.trim();

        // 4. 검색어 길이 제한
        if (normalizedKeyword != null
                && normalizedKeyword.length() > 100) {

            throw ApiException.badRequest(
                    "keyword must be 100 characters or less"
            );
        }

        // 5. 최신 등록순 정렬
        Pageable pageable = PageRequest.of(
                page,
                size,
                Sort.by(
                        Sort.Order.desc("createdAt"),
                        Sort.Order.desc("id")
                )
        );

        // 6. DB 검색
        Page<Job> jobs = normalizedKeyword == null
                ? jobRepository.findAll(pageable)
                : jobRepository.searchJobs(
                        normalizedKeyword,
                        pageable
                );

        // 7. Entity -> DTO 변환
        return jobs.map(this::toResponse);
    }

    /**
     * [기능] 일자리 상세 조회.
     *
     * @param jobId Spring 내부 일자리 ID
     *
     * [처리]
     * 1. ID 유효성 검증
     * 2. DB 조회
     * 3. 존재하지 않으면 404
     * 4. DTO 반환
     */
    public JobResponse getJob(Long jobId) {

        // 1. ID 유효성 검증
        if (jobId == null || jobId <= 0) {
            throw ApiException.badRequest(
                    "jobId must be positive"
            );
        }

        // 2. DB 조회
        Job job = jobRepository.findById(jobId)
                .orElseThrow(() -> ApiException.notFound(
                        "Job not found: " + jobId
                ));

        // 3. 응답 변환
        return toResponse(job);
    }

    /**
     * [공통] Job Entity -> JobResponse DTO 변환.
     *
     * [매핑]
     * Job.id            -> JobResponse.id
     * Job.externalJobId -> JobResponse.externalJobId
     * Job.jobTitle      -> JobResponse.jobTitle
     * Job.workplace     -> JobResponse.workplace
     * Job.workHours     -> JobResponse.workHours
     * Job.description   -> JobResponse.description
     * Job.createdAt     -> JobResponse.createdAt
     *
     * 외부 공고 ID가 없는 경우 null을 유지한다.
     * 내부 ID로 대체하지 않는다.
     */
    private JobResponse toResponse(Job job) {

        return new JobResponse(
                job.getId(),
                job.getExternalJobId(),
                job.getJobTitle(),
                job.getWorkplace(),
                job.getWorkHours(),
                job.getDescription(),
                job.getCreatedAt()
        );
    }
}


package com.example.demo.job.service;

import com.example.demo.global.exception.ApiException;
import com.example.demo.job.dto.JobResponse;
import com.example.demo.job.entity.Job;
import com.example.demo.job.repository.JobRepository;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.Pageable;

import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

/**
 * [테스트 명세] JobService 단위 테스트
 *
 * 대상 코드:
 * - JobService.getJob()
 * - JobService.searchJobs()
 *
 * 근거:
 * - IF_v2 JobService.java
 * - IF_v2 JobRepository.java
 * - IF_v2 ApiException.java
 *
 * 테스트 유형: Unit Test
 * 도구: JUnit 5 + Mockito
 *
 * DB 없이 Service 비즈니스 로직을 검증한다.
 */
@ExtendWith(MockitoExtension.class)
class JobServiceTest {

    @Mock
    private JobRepository jobRepository;

    private JobService jobService;

    @BeforeEach
    void setUp() {
        jobService = new JobService(jobRepository);
    }

    /**
     * TC-JOB-001
     *
     * 근거: JobService.getJob()
     * 조건: 존재하는 일자리 ID
     * 기대: JobResponse 반환
     */
    @Test
    void getJob_success() {

        // Given: DB에 일자리가 존재한다고 가정
        Job job = new Job();
        job.setId(1L);
        job.setJobTitle("시설 관리");
        job.setWorkplace("서울");

        when(jobRepository.findById(1L))
                .thenReturn(Optional.of(job));

        // When: 일자리 상세 조회
        JobResponse result = jobService.getJob(1L);

        // Then: 반환값 검증
        assertEquals(1L, result.id());
        assertEquals("시설 관리", result.jobTitle());
        assertEquals("서울", result.workplace());

        verify(jobRepository).findById(1L);
    }

    /**
     * TC-JOB-002
     *
     * 근거: JobService.getJob()
     * 조건: 존재하지 않는 일자리 ID
     * 기대: NOT_FOUND 예외
     */
    @Test
    void getJob_notFound() {

        // Given
        when(jobRepository.findById(999L))
                .thenReturn(Optional.empty());

        // When
        ApiException exception = assertThrows(
                ApiException.class,
                () -> jobService.getJob(999L)
        );

        // Then
        assertEquals(
                "NOT_FOUND",
                exception.getErrorCode()
        );
    }

    /**
     * TC-JOB-003
     *
     * 근거: JobService.searchJobs()
     * 규칙: page >= 0
     * 기대: 음수 페이지 요청 차단
     */
    @Test
    void searchJobs_invalidPage() {

        ApiException exception = assertThrows(
                ApiException.class,
                () -> jobService.searchJobs(null, -1, 20)
        );

        assertEquals(
                "INVALID_REQUEST",
                exception.getErrorCode()
        );

        // 잘못된 입력이면 DB 조회를 수행하지 않는다.
        verifyNoInteractions(jobRepository);
    }

    /**
     * TC-JOB-004
     *
     * 근거: JobService.searchJobs()
     * 규칙: 1 <= size <= 100
     * 기대: 크기 101 차단
     */
    @Test
    void searchJobs_invalidSize() {

        assertThrows(
                ApiException.class,
                () -> jobService.searchJobs(null, 0, 101)
        );

        verifyNoInteractions(jobRepository);
    }

    /**
     * TC-JOB-005
     *
     * 근거: JobRepository.searchJobs()
     * 조건: keyword="서울"
     * 기대: 검색 결과를 JobResponse로 변환
     */
    @Test
    void searchJobs_success() {

        // Given
        Job job = new Job();
        job.setId(1L);
        job.setJobTitle("시설 관리");
        job.setWorkplace("서울");

        Page<Job> page = new PageImpl<>(
                List.of(job)
        );

        when(jobRepository.searchJobs(
                eq("서울"),
                any(Pageable.class)
        )).thenReturn(page);

        // When
        Page<JobResponse> result =
                jobService.searchJobs("서울", 0, 20);

        // Then
        assertEquals(1, result.getTotalElements());
        assertEquals(
                "시설 관리",
                result.getContent().get(0).jobTitle()
        );

        verify(jobRepository).searchJobs(
                eq("서울"),
                any(Pageable.class)
        );
    }

    /**
     * TC-JOB-006
     *
     * 근거: JobService.searchJobs()
     * 조건: 검색어가 공백
     * 기대: 전체 조회로 처리
     */
    @Test
    void searchJobs_blankKeyword() {

        when(jobRepository.findAll(any(Pageable.class)))
                .thenReturn(Page.empty());

        jobService.searchJobs("   ", 0, 20);

        verify(jobRepository).findAll(any(Pageable.class));
    }
}

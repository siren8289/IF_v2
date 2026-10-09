
package com.example.demo.job.repository;

import com.example.demo.job.entity.Job;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

/**
 * 일자리 Repository.
 *
 * [역할]
 * - PostgreSQL job 테이블 조회
 * - 키워드 검색
 * - 페이지네이션
 *
 * JpaRepository 기본 기능:
 * findById, findAll, save, delete 등
 */
public interface JobRepository extends JpaRepository<Job, Long> {

    /**
     * [기능] 일자리 검색
     *
     * 검색 대상:
     * - 일자리명
     * - 근무지역
     *
     * keyword가 null이면 전체 조회한다.
     *
     * Pageable이 LIMIT/OFFSET과 정렬을 처리한다.
     */
    @Query(
            value = """
            SELECT j
            FROM Job j
            WHERE (
                :keyword IS NULL
                OR LOWER(j.jobTitle)
                    LIKE LOWER(CONCAT('%', :keyword, '%'))
                OR LOWER(j.workplace)
                    LIKE LOWER(CONCAT('%', :keyword, '%'))
            )
            """,
            countQuery = """
            SELECT COUNT(j)
            FROM Job j
            WHERE (
                :keyword IS NULL
                OR LOWER(j.jobTitle)
                    LIKE LOWER(CONCAT('%', :keyword, '%'))
                OR LOWER(j.workplace)
                    LIKE LOWER(CONCAT('%', :keyword, '%'))
            )
            """
    )
    Page<Job> searchJobs(
            @Param("keyword") String keyword,
            Pageable pageable
    );
}

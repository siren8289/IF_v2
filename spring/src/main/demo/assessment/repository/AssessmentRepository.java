package com.example.demo.assessment.repository;

import com.example.demo.assessment.dto.AssessmentRecordResponse;
import com.example.demo.assessment.entity.Assessment;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface AssessmentRepository extends JpaRepository<Assessment, Long> {

    long countByAiRiskResult_RiskGrade(String riskGrade);

    long countByAiRiskResultIsNotNull();

    /** 대시보드 목록: 필요한 컬럼만 골라서 한 번의 쿼리로 조회한다. */
    @Query("""
            select new com.example.demo.assessment.dto.AssessmentRecordResponse(
                a.id, ap.displayName, ap.age, j.jobTitle,
                hs.physicalLevel, a.status,
                ar.totalRiskPercent, ar.riskGrade, a.assessedAt)
            from Assessment a
            join a.applicant ap
            join a.job j
            join a.healthSnapshot hs
            left join a.aiRiskResult ar
            """)
    Page<AssessmentRecordResponse> findAllRecords(Pageable pageable);
}

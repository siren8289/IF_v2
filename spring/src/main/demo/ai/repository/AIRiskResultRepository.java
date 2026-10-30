package com.example.demo.ai.repository;

import com.example.demo.ai.entity.AIRiskResult;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

/** AI 결과 테이블. findByAssessment_Id 는 평가 번호로 결과 한 건을 찾는다. */
public interface AIRiskResultRepository extends JpaRepository<AIRiskResult, Long> {
    Optional<AIRiskResult> findByAssessment_Id(Long assessmentId);
}


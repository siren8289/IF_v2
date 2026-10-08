
package com.example.demo.applicant.repository;

import com.example.demo.applicant.entity.Applicant;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * 신청자 DB 접근 계층.
 *
 * JpaRepository 기본 기능을 사용한다.
 * - save() : 등록
 * - findById() : 단건 조회
 * - findAll() : 전체 조회
 * - existsById() : 존재 여부 확인
 */
public interface ApplicantRepository
        extends JpaRepository<Applicant, Long> {
}

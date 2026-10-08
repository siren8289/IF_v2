
package com.example.demo.applicant.repository;

import com.example.demo.applicant.entity.HealthSnapshot;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * 건강정보 DB 접근 계층.
 *
 * 신청자와 건강정보의 소유 관계는
 * Service에서 확인하고, DB 외래키로도 보장한다.
 */
public interface HealthSnapshotRepository
        extends JpaRepository<HealthSnapshot, Long> {
}

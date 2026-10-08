
package com.example.demo.applicant.service;

import com.example.demo.applicant.dto.ApplicantDto;
import com.example.demo.applicant.entity.Applicant;
import com.example.demo.applicant.entity.HealthSnapshot;
import com.example.demo.applicant.repository.ApplicantRepository;
import com.example.demo.applicant.repository.HealthSnapshotRepository;
import com.example.demo.global.exception.ApiException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

/**
 * 신청자·건강정보 업무 서비스.
 *
 * [역할]
 * 1. 신청자 등록 및 조회
 * 2. 신청자별 건강정보 등록
 * 3. 존재하지 않는 신청자에 대한 요청 차단
 *
 * Controller는 HTTP 처리를 담당하고,
 * Service는 업무 규칙과 트랜잭션을 담당한다.
 */
@Service
@Transactional(readOnly = true)
public class ApplicantService {

    private final ApplicantRepository applicantRepository;
    private final HealthSnapshotRepository healthRepository;

    public ApplicantService(
            ApplicantRepository applicantRepository,
            HealthSnapshotRepository healthRepository
    ) {
        this.applicantRepository = applicantRepository;
        this.healthRepository = healthRepository;
    }

    /**
     * 전체 신청자 조회.
     * Entity를 DTO로 변환해 반환한다.
     */
    public List<ApplicantDto.Response> listApplicants() {
        return applicantRepository.findAll()
                .stream()
                .map(this::toResponse)
                .toList();
    }

    /**
     * 신청자 단건 조회.
     * 신청자가 존재하지 않으면 HTTP 404 오류를 발생시킨다.
     */
    public ApplicantDto.Response getApplicant(Long id) {
        Applicant applicant = findApplicant(id);
        return toResponse(applicant);
    }

    /**
     * 신규 신청자 등록.
     *
     * 입력 검증은 Controller의 @Valid가 수행하고,
     * Service는 DB 저장과 응답 변환을 담당한다.
     */
    @Transactional
    public ApplicantDto.Response createApplicant(
            ApplicantDto.CreateRequest request
    ) {
        Applicant applicant = new Applicant(
                request.displayName().trim(),
                request.age()
        );

        Applicant saved = applicantRepository.save(applicant);
        return toResponse(saved);
    }

    /**
     * 신청자 건강정보 스냅샷 생성.
     *
     * 1. 신청자 존재 여부 확인
     * 2. 건강정보 객체 생성
     * 3. applicant_id 관계 설정
     * 4. DB 저장
     */
    @Transactional
    public ApplicantDto.HealthResponse createHealthSnapshot(
            Long applicantId,
            ApplicantDto.HealthCreateRequest request
    ) {
        Applicant applicant = findApplicant(applicantId);

        HealthSnapshot snapshot = new HealthSnapshot(
                applicant,
                request.physicalLevel(),
                request.chronicDiseaseFlag(),
                request.workHourLimit()
        );

        HealthSnapshot saved = healthRepository.save(snapshot);

        return new ApplicantDto.HealthResponse(
                saved.getId(),
                applicant.getId(),
                saved.getPhysicalLevel(),
                saved.getChronicDiseaseFlag(),
                saved.getWorkHourLimit(),
                saved.getCreatedAt()
        );
    }

    /**
     * 공통 신청자 조회 메서드.
     * 중복된 findById + 예외 처리 코드를 한 곳에 모은다.
     */
    private Applicant findApplicant(Long id) {
        return applicantRepository.findById(id)
                .orElseThrow(() -> ApiException.notFound(
                        "Applicant not found: " + id
                ));
    }

    /** 신청자 Entity를 API 응답 DTO로 변환한다. */
    private ApplicantDto.Response toResponse(Applicant applicant) {
        return new ApplicantDto.Response(
                applicant.getId(),
                applicant.getDisplayName(),
                applicant.getAge(),
                applicant.getCreatedAt()
        );
    }
}

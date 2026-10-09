
package com.example.demo.assessment.service;

import com.example.demo.admin.entity.AdminUser;
import com.example.demo.admin.repository.AdminUserRepository;
import com.example.demo.ai.repository.AIRiskResultRepository;
import com.example.demo.applicant.entity.Applicant;
import com.example.demo.applicant.entity.HealthSnapshot;
import com.example.demo.applicant.repository.ApplicantRepository;
import com.example.demo.applicant.repository.HealthSnapshotRepository;
import com.example.demo.assessment.dto.*;
import com.example.demo.assessment.entity.Assessment;
import com.example.demo.assessment.entity.AssessmentStatus;
import com.example.demo.assessment.repository.AssessmentRepository;
import com.example.demo.global.exception.ApiException;
import com.example.demo.job.entity.Job;
import com.example.demo.job.repository.JobRepository;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.util.List;

/**
 * 평가(Assessment) 업무 서비스.
 *
 * [주요 역할]
 * 1. 신청자별 평가 생성
 * 2. 평가 목록 및 대시보드 조회
 * 3. 평가 상태 변경
 * 4. 평가 기록 삭제
 *
 * [연관 모듈]
 * applicant  : 신청자 및 건강정보
 * job        : 평가 대상 일자리
 * ai         : AI 위험도 결과
 * admin      : 평가 담당 관리자
 *
 * [설계 원칙]
 * - Controller: HTTP 요청/응답 처리
 * - Service: 업무 규칙 및 트랜잭션
 * - Repository: DB 조회 및 저장
 * - 예외: 공통 ApiException 사용
 */
@Service
@Transactional(readOnly = true)
public class AssessmentService {

    private final AssessmentRepository assessmentRepository;
    private final ApplicantRepository applicantRepository;
    private final HealthSnapshotRepository healthRepository;
    private final JobRepository jobRepository;
    private final AdminUserRepository adminRepository;
    private final AIRiskResultRepository riskRepository;

    public AssessmentService(
            AssessmentRepository assessmentRepository,
            ApplicantRepository applicantRepository,
            HealthSnapshotRepository healthRepository,
            JobRepository jobRepository,
            AdminUserRepository adminRepository,
            AIRiskResultRepository riskRepository
    ) {
        this.assessmentRepository = assessmentRepository;
        this.applicantRepository = applicantRepository;
        this.healthRepository = healthRepository;
        this.jobRepository = jobRepository;
        this.adminRepository = adminRepository;
        this.riskRepository = riskRepository;
    }

    /**
     * [기능] 신규 평가 생성
     *
     * [입력]
     * applicantId : 신청자 ID
     * request     : 일자리 ID, 건강정보 ID
     *
     * [처리 흐름]
     * 1. 신청자 존재 확인
     * 2. 일자리 존재 확인
     * 3. 건강정보 존재 확인
     * 4. 건강정보 소유자 검증
     * 5. 평가 초기 상태 설정
     * 6. DB 저장
     *
     * [초기 상태]
     * PENDING_AI
     */
    @Transactional
    public AssessmentResponse createAssessment(
            Long applicantId,
            AssessmentCreateRequest request
    ) {

        Applicant applicant = applicantRepository.findById(applicantId)
                .orElseThrow(() -> ApiException.notFound(
                        "Applicant not found: " + applicantId
                ));

        Job job = jobRepository.findById(request.getJobId())
                .orElseThrow(() -> ApiException.notFound(
                        "Job not found: " + request.getJobId()
                ));

        HealthSnapshot health = healthRepository
                .findById(request.getHealthId())
                .orElseThrow(() -> ApiException.notFound(
                        "HealthSnapshot not found: "
                                + request.getHealthId()
                ));

        // 다른 신청자의 건강정보 사용을 차단한다.
        if (!health.getApplicant().getId().equals(applicantId)) {
            throw ApiException.badRequest(
                    "HealthSnapshot does not belong to applicant"
            );
        }

        Assessment assessment = new Assessment();

        assessment.setApplicant(applicant);
        assessment.setJob(job);
        assessment.setHealthSnapshot(health);

        // 관리자 자동 배정은 하지 않는다.
        // 인증/담당자 지정 기능 구현 후 명시적으로 설정한다.
        assessment.setAdminUser(null);

        assessment.setStatus(AssessmentStatus.PENDING_AI);
        assessment.setAssessedAt(
                OffsetDateTime.now(ZoneOffset.UTC)
        );

        Assessment saved = assessmentRepository.save(assessment);

        return toResponse(saved);
    }

    /**
     * [기능] 신청자별 평가 목록 조회
     *
     * 최신 평가부터 반환한다.
     */
    public List<AssessmentResponse> listByApplicantId(Long applicantId) {

        if (!applicantRepository.existsById(applicantId)) {
            throw ApiException.notFound(
                    "Applicant not found: " + applicantId
            );
        }

        return assessmentRepository
                .findByApplicant_IdOrderByAssessedAtDesc(applicantId)
                .stream()
                .map(this::toResponse)
                .toList();
    }

    /**
     * [기능] 관리자 대시보드 평가 목록
     *
     * [특징]
     * - 페이지네이션
     * - DTO Projection
     * - 필요한 컬럼만 조회
     */
    public Page<AssessmentRecordResponse> listAllRecords(
            Pageable pageable
    ) {
        return assessmentRepository.findAllRecords(pageable);
    }

    /**
     * [기능] 대시보드 요약 통계
     *
     * 전체 평가 / 고위험 / 최종 완료 건수
     */
    public AssessmentSummaryResponse getSummary() {

        long total = assessmentRepository.count();

        long highRisk =
                assessmentRepository
                        .countByAiRiskResult_RiskGrade("HIGH");

        long finalized =
                assessmentRepository
                        .countByStatus(AssessmentStatus.FINALIZED);

        return new AssessmentSummaryResponse(
                total,
                highRisk,
                finalized
        );
    }

    /**
     * [기능] 평가 상태 변경
     *
     * [허용 상태 전이]
     * PENDING_AI → AI_COMPLETED
     * AI_COMPLETED → FINALIZED
     *
     * 그 외 상태 변경은 거부한다.
     */
    @Transactional
    public void updateAssessment(
            Long assessmentId,
            AssessmentUpdateRequest request
    ) {

        Assessment assessment = findAssessment(assessmentId);

        if (request == null
                || request.getStatus() == null
                || request.getStatus().isBlank()) {

            throw ApiException.badRequest(
                    "Assessment status is required"
            );
        }

        AssessmentStatus target;

        try {
            target = AssessmentStatus.valueOf(
                    request.getStatus().trim()
            );
        } catch (IllegalArgumentException ex) {
            throw ApiException.badRequest(
                    "Unknown assessment status: "
                            + request.getStatus()
            );
        }

        AssessmentStatus current = assessment.getStatus();

        if (!current.canTransitionTo(target)) {
            throw ApiException.invalidTransition(
                    "Invalid transition: "
                            + current + " -> " + target
            );
        }

        assessment.setStatus(target);
    }

    /**
     * [기능] 평가 기록 삭제
     *
     * [처리 흐름]
     * 1. 평가 조회
     * 2. 연결된 AI 결과 확인
     * 3. AI 결과 연결 해제 및 삭제
     * 4. 평가 삭제
     *
     * [트랜잭션]
     * 삭제 과정에서 오류 발생 시 전체 롤백.
     */
    @Transactional
    public void deleteAssessment(Long assessmentId) {

        Assessment assessment = findAssessment(assessmentId);

        if (assessment.getAiRiskResult() != null) {

            var riskResult = assessment.getAiRiskResult();

            assessment.setAiRiskResult(null);

            assessmentRepository.saveAndFlush(assessment);

            riskRepository.delete(riskResult);
        }

        assessmentRepository.delete(assessment);
    }

    /**
     * [공통] 평가 ID 조회 및 404 처리
     */
    private Assessment findAssessment(Long id) {

        return assessmentRepository.findById(id)
                .orElseThrow(() -> ApiException.notFound(
                        "Assessment not found: " + id
                ));
    }

    /**
     * [공통] Entity → Response DTO 변환
     *
     * Entity를 Controller에 직접 반환하지 않는다.
     */
    private AssessmentResponse toResponse(Assessment assessment) {

        AssessmentResponse response = new AssessmentResponse();

        response.setId(assessment.getId());
        response.setApplicantId(
                assessment.getApplicant().getId()
        );
        response.setStatus(
                assessment.getStatus().name()
        );
        response.setAssessedAt(
                assessment.getAssessedAt()
        );

        return response;
    }
}

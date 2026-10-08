
package com.example.demo.applicant.controller;

import com.example.demo.applicant.dto.ApplicantDto;
import com.example.demo.applicant.service.ApplicantService;
import jakarta.validation.Valid;
import jakarta.validation.constraints.Positive;
import org.springframework.http.HttpStatus;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * 신청자 및 건강정보 REST API.
 *
 * [역할]
 * - HTTP 요청 접수
 * - 요청 DTO 검증
 * - Service 호출
 * - HTTP 상태 및 응답 반환
 *
 * 실제 DB 처리와 업무 규칙은 ApplicantService가 담당한다.
 */
@RestController
@Validated
@RequestMapping("/api/applicants")
public class ApplicantController {

    private final ApplicantService applicantService;

    public ApplicantController(ApplicantService applicantService) {
        this.applicantService = applicantService;
    }

    /**
     * GET /api/applicants
     * 전체 신청자 목록 조회.
     */
    @GetMapping
    public List<ApplicantDto.Response> listApplicants() {
        return applicantService.listApplicants();
    }

    /**
     * GET /api/applicants/{id}
     * 신청자 ID 기준 단건 조회.
     */
    @GetMapping("/{id}")
    public ApplicantDto.Response getApplicant(
            @PathVariable @Positive Long id
    ) {
        return applicantService.getApplicant(id);
    }

    /**
     * POST /api/applicants
     * 신청자 등록.
     *
     * @Valid가 요청 필드의 필수값과 범위를 검증한다.
     */
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ApplicantDto.Response createApplicant(
            @Valid @RequestBody ApplicantDto.CreateRequest request
    ) {
        return applicantService.createApplicant(request);
    }

    /**
     * POST /api/applicants/{applicantId}/health-snapshots
     * 특정 신청자에게 건강정보 스냅샷을 등록한다.
     */
    @PostMapping("/{applicantId}/health-snapshots")
    @ResponseStatus(HttpStatus.CREATED)
    public ApplicantDto.HealthResponse createHealthSnapshot(
            @PathVariable @Positive Long applicantId,
            @Valid @RequestBody ApplicantDto.HealthCreateRequest request
    ) {
        return applicantService.createHealthSnapshot(
                applicantId,
                request
        );
    }
}

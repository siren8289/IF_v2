package com.example.demo.assessment.controller;

import com.example.demo.assessment.dto.AssessmentCreateRequest;
import com.example.demo.assessment.dto.AssessmentRecordResponse;
import com.example.demo.assessment.dto.AssessmentResultResponse;
import com.example.demo.assessment.dto.AssessmentSummaryResponse;
import com.example.demo.assessment.service.AssessmentService;
import jakarta.validation.Valid;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.web.PageableDefault;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

/**
 * GET    /api/assessments              대시보드 목록
 * GET    /api/assessments/summary      대시보드 요약 카드
 * POST   /api/assessments              평가 등록 + AI 분석
 * GET    /api/assessments/{id}/result  결과 화면
 * DELETE /api/assessments/{id}         삭제
 */
@RestController
@RequestMapping("/api/assessments")
public class AssessmentController {

    private final AssessmentService assessmentService;

    public AssessmentController(AssessmentService assessmentService) {
        this.assessmentService = assessmentService;
    }

    @GetMapping
    public Page<AssessmentRecordResponse> list(
            @PageableDefault(size = 20, sort = {"assessedAt", "id"}, direction = Sort.Direction.DESC)
            Pageable pageable) {
        return assessmentService.list(pageable);
    }

    @GetMapping("/summary")
    public AssessmentSummaryResponse summary() {
        return assessmentService.summary();
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Map<String, Long> create(@Valid @RequestBody AssessmentCreateRequest request) {
        Long id = assessmentService.createAndAnalyze(request);
        return Map.of("id", id);
    }

    @GetMapping("/{id}/result")
    public AssessmentResultResponse result(@PathVariable Long id) {
        return assessmentService.getResult(id);
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void delete(@PathVariable Long id) {
        assessmentService.delete(id);
    }
}

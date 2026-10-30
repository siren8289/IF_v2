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
 * 평가 API의 입구. 주소만 받고, 저장과 AI 호출은 AssessmentService에 넘긴다.
 *
 * GET    /api/assessments              대시보드 목록 (20개씩, 최신순)
 * GET    /api/assessments/summary      대시보드 요약 카드
 * POST   /api/assessments              평가 등록 + AI 분석. 바디는 JSON, 성공 시 { "id": 1 }
 * GET    /api/assessments/{id}/result  결과 화면
 * DELETE /api/assessments/{id}         삭제. 본문 없이 204
 *
 * @RestController 는 반환값을 JSON으로 바꾼다.
 * @RequestMapping 은 아래 메서드 주소 앞에 공통으로 /api/assessments 를 붙인다.
 */
@RestController
@RequestMapping("/api/assessments")
public class AssessmentController {

    private final AssessmentService assessmentService;

    public AssessmentController(AssessmentService assessmentService) {
        this.assessmentService = assessmentService;
    }

    /** 목록. page, size, sort 는 Spring이 쿼리스트링에서 Pageable로 조립한다. */
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

    /** 등록. @Valid 가 DTO의 @NotNull, @Min 같은 검사를 먼저 돌린다. 실패하면 400. */
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Map<String, Long> create(@Valid @RequestBody AssessmentCreateRequest request) {
        Long id = assessmentService.createAndAnalyze(request);
        return Map.of("id", id);
    }

    /** 결과. {id} 는 주소의 숫자이고, @PathVariable 이 그 숫자를 인자로 넣는다. */
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

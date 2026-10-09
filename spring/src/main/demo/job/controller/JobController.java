package com.example.demo.job.controller;

import com.example.demo.job.dto.JobResponse;
import com.example.demo.job.entity.Job;
import com.example.demo.job.repository.JobRepository;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

/** GET /api/jobs  평가 입력 화면의 직무 선택 목록 */
@RestController
@RequestMapping("/api/jobs")
public class JobController {

    private final JobRepository jobRepository;

    public JobController(JobRepository jobRepository) {
        this.jobRepository = jobRepository;
    }

    @GetMapping
    public List<JobResponse> list() {
        List<JobResponse> result = new ArrayList<>();
        for (Job job : jobRepository.findTop50ByOrderByIdAsc()) {
            result.add(new JobResponse(job.getId(), job.getJobTitle(), job.getWorkplace()));
        }
        return result;
    }
}

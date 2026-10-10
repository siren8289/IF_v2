package com.example.demo.job;

import com.example.demo.job.entity.Job;
import com.example.demo.job.repository.JobRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

/** 직무 테이블이 비어 있으면(새 DB) 평가 화면에서 고를 기본 직무를 넣는다. */
@Component
public class JobDataInitializer implements CommandLineRunner {

    private static final String[][] DEFAULT_JOBS = {
            {"아파트 야간 경비원", "서울 강남구"},
            {"택배 배송 기사", "경기 성남시"},
            {"건물 청소원", "서울 종로구"},
            {"요양보호사", "인천 남동구"},
            {"시설 관리원", "부산 해운대구"},
            {"주차 관리원", "대구 수성구"},
            {"학교 급식 보조원", "광주 북구"},
            {"사무 보조원", "대전 서구"},
    };

    private final JobRepository jobRepository;

    public JobDataInitializer(JobRepository jobRepository) {
        this.jobRepository = jobRepository;
    }

    @Override
    public void run(String... args) {
        if (jobRepository.count() > 0) {
            return;
        }
        for (String[] data : DEFAULT_JOBS) {
            Job job = new Job();
            job.setJobTitle(data[0]);
            job.setWorkplace(data[1]);
            jobRepository.save(job);
        }
    }
}

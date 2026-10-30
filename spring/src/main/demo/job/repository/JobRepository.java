package com.example.demo.job.repository;

import com.example.demo.job.entity.Job;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/** 직무 테이블. findTop50ByOrderByIdAsc 는 id가 작은 순으로 50개만 가져온다. */
public interface JobRepository extends JpaRepository<Job, Long> {

    /** 평가 입력 화면의 직무 선택 목록 (앞에서 50개) */
    List<Job> findTop50ByOrderByIdAsc();
}

package com.example.demo.job.dto;

/** 직무 선택 상자에 내려 주는 값. 화면은 id, 제목, 근무지만 필요하다. */
public record JobResponse(Long id, String jobTitle, String workplace) {
}

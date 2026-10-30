package com.example.demo.assessment.entity;

/**
 * 평가가 지금 어느 단계인지.
 * DB에는 이 이름 문자열이 그대로 저장된다. (PENDING_AI 등)
 */
public enum AssessmentStatus {
    PENDING_AI,    // 방금 저장됨. AI 분석 전이거나, AI 호출이 실패한 상태
    AI_COMPLETED,  // AI 점수와 설명이 저장됨
    FINALIZED      // 예전 버전 데이터와 맞추려고 남겨 둔 값. 새 코드는 쓰지 않는다
}

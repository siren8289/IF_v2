package com.example.demo.assessment.entity;

public enum AssessmentStatus {
    PENDING_AI,    // 등록됨, AI 분석 전(또는 실패)
    AI_COMPLETED,  // AI 분석 완료
    FINALIZED      // 이전 버전에서 저장된 데이터 호환용
}

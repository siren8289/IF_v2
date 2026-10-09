
package com.example.demo.ai.service;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

/**
 * [테스트 명세] AI 위험도 등급 규칙 테스트
 *
 * 대상 코드:
 * - AIRiskService.gradeOf()
 * - AIRiskService.gradeOfBand()
 *
 * 근거:
 * - IF_v2 AIRiskService.java
 *
 * 현재 구현 규칙:
 * 0~40      : LOW
 * 40 초과~60 : MID
 * 60 초과    : HIGH
 *
 * 주의:
 * 위 기준은 현재 코드의 정책이며,
 * 최종 승인된 요구사항과는 별도 대조가 필요하다.
 *
 * 테스트 유형: Unit Test
 */
class AIRiskServiceTest {

    /**
     * TC-AI-001
     *
     * 점수 경계값 검증.
     *
     * @CsvSource:
     * 입력 점수, 예상 등급
     */
    @ParameterizedTest
    @CsvSource({
            "0, LOW",
            "20, LOW",
            "40, LOW",
            "40.1, MID",
            "50, MID",
            "60, MID",
            "60.1, HIGH",
            "80, HIGH",
            "100, HIGH"
    })
    void gradeOf_boundaryTest(
            double score,
            String expectedGrade
    ) {

        // When
        String result = AIRiskService.gradeOf(score);

        // Then
        assertEquals(expectedGrade, result);
    }

    /**
     * TC-AI-002
     *
     * FastAPI 한글 위험 구간 -> 내부 등급.
     */
    @Test
    void gradeOfBand_mappingTest() {

        assertAll(
                () -> assertEquals(
                        "LOW",
                        AIRiskService.gradeOfBand("낮음")
                ),
                () -> assertEquals(
                        "MID",
                        AIRiskService.gradeOfBand("보통")
                ),
                () -> assertEquals(
                        "HIGH",
                        AIRiskService.gradeOfBand("높음")
                ),
                () -> assertEquals(
                        "HIGH",
                        AIRiskService.gradeOfBand("매우 높음")
                )
        );
    }

    /**
     * TC-AI-003
     *
     * 근거: gradeOfBand() 기본 처리
     * 조건: null 입력
     * 기대: MID 반환
     */
    @Test
    void gradeOfBand_nullInput() {

        String result = AIRiskService.gradeOfBand(null);

        assertEquals("MID", result);
    }
}

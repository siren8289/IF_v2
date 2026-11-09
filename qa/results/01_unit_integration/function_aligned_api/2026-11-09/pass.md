# pass

RUN 20261109T2305-349tc

## 20261109T2305-349tc / IF-0047
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): 필드 누락 HTTP 400 VALIDATION_ERROR. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0048
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): 빈 이름 HTTP 400 VALIDATION_ERROR. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0049
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): 공백 이름 HTTP 400 VALIDATION_ERROR. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0050
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): 50자 이름 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0051
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): 51자 이름 HTTP 400. 백엔드 @Size(max=50) 이 거절. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0053
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): age 누락 HTTP 400 VALIDATION_ERROR. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0054
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): age -1 HTTP 400 VALIDATION_ERROR. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0055
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): age 0 HTTP 400 VALIDATION_ERROR. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0056
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): age 1 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0057
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): age 120 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0058
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): age 121 HTTP 400 VALIDATION_ERROR. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0061
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): physicalLevel 누락 HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0062
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): physicalLevel 0 HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0063
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): physicalLevel 1 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0064
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): physicalLevel 3 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0065
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): physicalLevel 5 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0066
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): physicalLevel 6 HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0068
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): chronicDisease 누락 HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0069
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): chronicDisease true HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0070
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): chronicDisease false HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0071
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): chronicDisease 문자열 yes HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0073
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): workHourLimit 누락 HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0074
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): workHourLimit 0 HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0075
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): workHourLimit 1 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0076
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): workHourLimit 8 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0077
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): workHourLimit 24 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0078
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): workHourLimit 25 HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0080
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): jobId 누락 HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0081
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): jobId 1 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0082
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): jobId 2 HTTP 201. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0083
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): jobId 999999 HTTP 404 NOT_FOUND. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0084
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): jobId -1 HTTP 404 NOT_FOUND. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0085
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): jobId 문자열 abc HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0086
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): 깨진 JSON HTTP 400 INVALID_JSON. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0088
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): 본문 [] HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0089
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): 본문 null HTTP 400. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0090
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): page=-1 HTTP 200. Spring Data 가 음수 page 를 0으로 맞춘 페이지를 돌려준다. 4xx 거절은 없음. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0091
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): size=0 HTTP 200. Spring Pageable 이 기본 페이지로 응답. 전용 4xx 는 없음. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0092
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): size=20 HTTP 200 페이지. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0093
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): page=9999 HTTP 200. 범위 밖 페이지도 Pageable 응답. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

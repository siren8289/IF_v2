# fail

RUN 20261109T2305-349tc

## 20261109T2305-349tc / IF-0052
- 상태: Fail
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): applicantName 숫자 17 이 HTTP 201. Jackson 이 문자열로 변환했다. 타입 오류 4xx 가 아님. 수정하지 않음. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0059
- 상태: Fail
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): age 60.5 가 HTTP 201. 소수 타입을 4xx 로 거절하지 않음. 수정하지 않음. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0060
- 상태: Fail
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): age 문자열 70 이 HTTP 201. Jackson 이 정수로 변환. 타입 오류 4xx 가 아님. 수정하지 않음. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0067
- 상태: Fail
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): physicalLevel 문자열 3 이 HTTP 201. Jackson 변환. 수정하지 않음. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0072
- 상태: Fail
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): chronicDisease 숫자 1 이 HTTP 201. 타입 오류 4xx 가 아님. 수정하지 않음. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0079
- 상태: Fail
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): workHourLimit 2.5 가 HTTP 201. 소수 타입을 4xx 로 거절하지 않음. 수정하지 않음. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

## 20261109T2305-349tc / IF-0087
- 상태: Fail
- 결과: RUN 20261109T2305-349tc. A(urllib :8080): text/plain HTTP 500 INTERNAL_ERROR. 기대는 4xx. 수정하지 않음. B: AssessmentCreateRequest / GlobalExceptionHandler / AssessmentController.

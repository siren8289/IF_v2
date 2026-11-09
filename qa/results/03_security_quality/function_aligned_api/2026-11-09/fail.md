# fail

RUN 20261109T2305-349tc

## 20261109T2305-349tc / IF-0334
- 상태: Blocked
- 결과: RUN 20261109T2305-349tc. GET /api/assessments/2/result 200 필드=['age', 'applicantName', 'explanation', 'explanationSource', 'factors', 'id', 'jobTitle', 'riskGrade', 'riskScore', 'status', 'taskScores']. 자격증명 필드=[]. 어떤 개인정보가 불필요한지 정책이 없음

## 20261109T2305-349tc / IF-0335
- 상태: Blocked
- 결과: RUN 20261109T2305-349tc. Authorization 없이 GET /api/assessments HTTP 200. Spring Security 설정이 없음. 공개 허용인지 거절인지 정책 미설정. RISK-SEC-001

## 20261109T2305-349tc / IF-0336
- 상태: Blocked
- 결과: RUN 20261109T2305-349tc. 인증 헤더 없이 POST 201 후 DELETE 204. 접근통제 허용/거절 기준이 없고 삭제가 인증 없이 동작. RISK-SEC-001. 프로브만 삭제

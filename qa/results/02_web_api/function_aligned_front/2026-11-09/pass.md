# pass

RUN 20261109T2305-349tc

## 20261109T2305-349tc / IF-0001
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 '이름을 입력해주세요.', POST 0건 | B(source): validate()가 빈 이름에서 "이름을 입력해주세요."

## 20261109T2305-349tc / IF-0002
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 '이름을 입력해주세요.', POST 0건 | B(source): validate()가 빈 이름에서 "이름을 입력해주세요."

## 20261109T2305-349tc / IF-0003
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST 1건, applicantName 길이 3, 값일치=true | B(source): createAssessment에 name.trim() 전달

## 20261109T2305-349tc / IF-0004
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST 1건, applicantName 길이 3, 값일치=true | B(source): createAssessment에 name.trim() 전달

## 20261109T2305-349tc / IF-0005
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST 1건, applicantName 길이 50, 값일치=true | B(source): createAssessment에 name.trim() 전달

## 20261109T2305-349tc / IF-0006
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST 1건, applicantName 길이 51, 값일치=true | B(source): createAssessment에 name.trim() 전달 | API 재확인: 51자는 HTTP 400.

## 20261109T2305-349tc / IF-0007
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST 1건, applicantName 길이 4, 값일치=true | B(source): createAssessment에 name.trim() 전달

## 20261109T2305-349tc / IF-0008
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 연령 범위, POST 0건, 입력='-1' | B(source): validate() 정수 1~120 아니면 오류

## 20261109T2305-349tc / IF-0009
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 연령 범위, POST 0건, 입력='0' | B(source): validate() 정수 1~120 아니면 오류

## 20261109T2305-349tc / IF-0010
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST age=1 | B(source): validate() 정수 1~120 통과 후 Number(age)

## 20261109T2305-349tc / IF-0011
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST age=2 | B(source): validate() 정수 1~120 통과 후 Number(age)

## 20261109T2305-349tc / IF-0012
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST age=60 | B(source): validate() 정수 1~120 통과 후 Number(age)

## 20261109T2305-349tc / IF-0013
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST age=90 | B(source): validate() 정수 1~120 통과 후 Number(age)

## 20261109T2305-349tc / IF-0014
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST age=119 | B(source): validate() 정수 1~120 통과 후 Number(age)

## 20261109T2305-349tc / IF-0015
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST age=120 | B(source): validate() 정수 1~120 통과 후 Number(age)

## 20261109T2305-349tc / IF-0016
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 연령 범위, POST 0건, 입력='121' | B(source): validate() 정수 1~120 아니면 오류

## 20261109T2305-349tc / IF-0017
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 연령 범위, POST 0건, 입력='60.5' | B(source): validate() 정수 1~120 아니면 오류

## 20261109T2305-349tc / IF-0018
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 연령 범위, POST 0건, 입력='abc' | B(source): validate() 정수 1~120 아니면 오류

## 20261109T2305-349tc / IF-0019
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 연령 범위, POST 0건, 입력='' | B(source): validate() 정수 1~120 아니면 오류

## 20261109T2305-349tc / IF-0020
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 근무시간, POST 0건, 입력='-1' | B(source): validate() 정수 1~24 아니면 오류

## 20261109T2305-349tc / IF-0021
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 근무시간, POST 0건, 입력='0' | B(source): validate() 정수 1~24 아니면 오류

## 20261109T2305-349tc / IF-0022
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST workHourLimit=1 | B(source): validate() 정수 1~24

## 20261109T2305-349tc / IF-0023
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST workHourLimit=7 | B(source): validate() 정수 1~24

## 20261109T2305-349tc / IF-0024
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST workHourLimit=8 | B(source): validate() 정수 1~24

## 20261109T2305-349tc / IF-0025
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST workHourLimit=23 | B(source): validate() 정수 1~24

## 20261109T2305-349tc / IF-0026
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST workHourLimit=24 | B(source): validate() 정수 1~24

## 20261109T2305-349tc / IF-0027
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 근무시간, POST 0건, 입력='25' | B(source): validate() 정수 1~24 아니면 오류

## 20261109T2305-349tc / IF-0028
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 근무시간, POST 0건, 입력='7.5' | B(source): validate() 정수 1~24 아니면 오류

## 20261109T2305-349tc / IF-0029
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 근무시간, POST 0건, 입력='abc' | B(source): validate() 정수 1~24 아니면 오류

## 20261109T2305-349tc / IF-0030
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 근무시간, POST 0건, 입력='' | B(source): validate() 정수 1~24 아니면 오류

## 20261109T2305-349tc / IF-0031
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST physicalLevel=1 | B(source): select value를 숫자로 payload에 넣음

## 20261109T2305-349tc / IF-0032
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST physicalLevel=2 | B(source): select value를 숫자로 payload에 넣음

## 20261109T2305-349tc / IF-0033
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST physicalLevel=3 | B(source): select value를 숫자로 payload에 넣음

## 20261109T2305-349tc / IF-0034
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST physicalLevel=4 | B(source): select value를 숫자로 payload에 넣음

## 20261109T2305-349tc / IF-0035
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST physicalLevel=5 | B(source): select value를 숫자로 payload에 넣음

## 20261109T2305-349tc / IF-0036
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST chronicDisease=false | B(source): chronicDisease === "yes" 이면 true

## 20261109T2305-349tc / IF-0037
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST chronicDisease=true | B(source): chronicDisease === "yes" 이면 true

## 20261109T2305-349tc / IF-0038
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 알림 직무 미선택, POST 0건 | B(source): validate() jobId === ""

## 20261109T2305-349tc / IF-0039
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST jobId=1 | B(source): Number(jobId)로 전송

## 20261109T2305-349tc / IF-0040
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): POST jobId=2 | B(source): Number(jobId)로 전송

## 20261109T2305-349tc / IF-0041
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 요청 완료 전 option 1개 | B(source): jobs 초기값은 빈 배열

## 20261109T2305-349tc / IF-0042
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 오류 문구 표시 | B(source): getJobs().catch가 고정 문구를 넣음

## 20261109T2305-349tc / IF-0044
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 오류 표시 후 버튼이 다시 활성화 | B(source): finally에서 setSubmitting(false)

## 20261109T2305-349tc / IF-0045
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 주소 /assessments/77/result | B(source): 성공 시 navigate result

## 20261109T2305-349tc / IF-0046
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 빈 201 본문 후 알림: Unexpected end of JSON input | B(source): apiRequest가 본문을 res.json()으로 읽음

## 20261109T2305-349tc / IF-0269
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 응답 전에 불러오는 중 표시 | B(source): result가 null이면 로딩 문구

## 20261109T2305-349tc / IF-0270
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 오류 알림 표시 | B(source): catch가 error를 alert로 렌더

## 20261109T2305-349tc / IF-0271
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 문구 '아직 AI 분석 결과가 없습니다.' | B(source): riskScore null 문구와 GRADE_TEXT 배지

## 20261109T2305-349tc / IF-0272
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 문구 '위험도 낮음' | B(source): riskScore null 문구와 GRADE_TEXT 배지

## 20261109T2305-349tc / IF-0273
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 문구 '위험도 보통' | B(source): riskScore null 문구와 GRADE_TEXT 배지

## 20261109T2305-349tc / IF-0274
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 문구 '위험도 높음' | B(source): riskScore null 문구와 GRADE_TEXT 배지

## 20261109T2305-349tc / IF-0275
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 기본 설명 문구 | B(source): explanationSource !== gemini

## 20261109T2305-349tc / IF-0276
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): Gemini 작성 문구와 설명 본문 | B(source): gemini면 생성형 문구

## 20261109T2305-349tc / IF-0277
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 요인 0개라 점수 구성 카드 없음 | B(source): factors.length > 0일 때만 카드

## 20261109T2305-349tc / IF-0278
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 이름과 6.67 / 20점 | B(source): 요인 이름·점수·만점 렌더

## 20261109T2305-349tc / IF-0279
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 막대 width=0% | B(source): 만점 0이면 width 0%

## 20261109T2305-349tc / IF-0280
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 태스크 0개라 ML/DL 표 없음 | B(source): taskScores.length > 0일 때만 표

## 20261109T2305-349tc / IF-0281
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 12% 셀 2개 | B(source): Math.round(score * 100)

## 20261109T2305-349tc / IF-0282
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 이동 후 주소 /dashboard | B(source): 버튼이 /dashboard로 이동

## 20261109T2305-349tc / IF-0283
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 목록 요청 중 로딩 문구 | B(source): loading이면 로딩 문구

## 20261109T2305-349tc / IF-0284
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 빈 목록 문구 | B(source): records.length === 0

## 20261109T2305-349tc / IF-0285
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 오류 배너 표시 | B(source): load() catch가 error 배너

## 20261109T2305-349tc / IF-0286
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 요약 null일 때 0건 카드 3개 | B(source): summary null이면 ?? 0

## 20261109T2305-349tc / IF-0287
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 카드 3건/1건/2건 | B(source): summary 세 필드를 카드에 매핑

## 20261109T2305-349tc / IF-0288
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 점수 null이면 - | B(source): null 점수는 대시

## 20261109T2305-349tc / IF-0289
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 등급 null이면 분석 전 | B(source): riskGrade 없으면 분석 전

## 20261109T2305-349tc / IF-0290
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 첫 요청 http://localhost:8080/api/assessments?page=0&size=20 | B(source): getAssessments가 page와 size=20

## 20261109T2305-349tc / IF-0291
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 다음 클릭 후 page=1 요청 | B(source): 다음 버튼이 page+1

## 20261109T2305-349tc / IF-0292
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 첫 페이지 이전 버튼 disabled | B(source): page === 0이면 이전 비활성

## 20261109T2305-349tc / IF-0293
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 마지막 페이지 다음 버튼 disabled | B(source): page+1 >= totalPages면 다음 비활성

## 20261109T2305-349tc / IF-0294
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 취소 시 DELETE 0건 | B(source): confirm false면 return

## 20261109T2305-349tc / IF-0295
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): DELETE 1건, 목록 GET 2건 | B(source): 삭제 후 load(page) 재호출

## 20261109T2305-349tc / IF-0296
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 삭제 500 오류 배너 | B(source): delete catch가 error 배너

## 20261109T2305-349tc / IF-0297
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 200 JSON을 객체로 파싱 | B(source): res.ok이면 res.json()

## 20261109T2305-349tc / IF-0298
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 204는 undefined | B(source): 204면 JSON을 읽지 않음

## 20261109T2305-349tc / IF-0299
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): content-length 0은 undefined | B(source): content-length 0이면 undefined

## 20261109T2305-349tc / IF-0300
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): API 400: 실패 | B(source): JSON message를 예외 문장에 붙임

## 20261109T2305-349tc / IF-0301
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): API 500: 서버 다운 | B(source): JSON이 아니면 원문을 예외에 사용

## 20261109T2305-349tc / IF-0302
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 성공 상태의 깨진 JSON은 SyntaxError | B(source): res.json() 파싱 오류가 전파

## 20261109T2305-349tc / IF-0303
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): 네트워크 예외가 그대로 전파 | B(source): fetch 실패를 삼키지 않음

## 20261109T2305-349tc / IF-0304
- 상태: Pass
- 결과: RUN 20261109T2305-349tc. A(vitest/jsdom): Content-Type=application/json | B(source): 기본 헤더는 application/json

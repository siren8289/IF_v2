# fail

RUN 20261109T2305-349tc

## 20261109T2305-349tc / IF-0320
- 상태: Blocked
- 결과: RUN 20261109T2305-349tc. 측정: if-app-stack-spring-1 cpu=1.14% mem=332.7MiB / 3.827GiB | if-app-stack-postgres-1 cpu=0.03% mem=40.14MiB / 3.827GiB | if-app-stack-fastapi-1 cpu=1.14% mem=352.2MiB / 3.827GiB | if-app-stack-frontend-1 cpu=0.00% mem=6.051MiB / 3.827GiB. compose에 mem_limit이나 합격 수치가 없어 기준 미정의

## 20261109T2305-349tc / IF-0333
- 상태: Fail
- 결과: RUN 20261109T2305-349tc. A: docker compose build 가 180초 안에 끝나지 않고 TimeoutExpired. 이미지 성공으로 보지 않는다. B: Dockerfile 은 수정하지 않았다.

## 20261109T2305-349tc / IF-0342
- 상태: Blocked
- 결과: RUN 20261109T2305-349tc. jobs n=30 모두 200. p50=43.8ms p95=118.6ms max=181.0ms. 합격 SLO 없음

## 20261109T2305-349tc / IF-0344
- 상태: Blocked
- 결과: RUN 20261109T2305-349tc. 15초 지연을 넣는 테스트 스위치가 없음. AppConfig read timeout은 40초. 15초를 실패로 볼 기준이 없음

## 20261109T2305-349tc / IF-0345
- 상태: Fail
- 결과: RUN 20261109T2305-349tc. spring stop 후 frontend restart exit=0 state=3 running false host_not_found=True 복구=True

## 20261109T2305-349tc / IF-0348
- 상태: Blocked
- 결과: RUN 20261109T2305-349tc. POST 201. spring/fastapi 최근 로그에 공통 request id 없음

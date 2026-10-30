# 모니터링과 알림

## 기존 상태

애플리케이션 자체에 Prometheus 엔드포인트는 없다. FastAPI `GET /health` 와 Spring `GET /api/jobs` 가 살아 있는지를 보는 기존 확인이다. CloudWatch 알람이나 Grafana 는 저장소에 없었다.

## 추가한 것

CloudWatch 알람은 만들지 않았다. 과금되는 AWS 변경이고, 승인 없이 계정을 바꾸지 않기 때문이다. 같은 신호를 로컬에서 띄울 수 있는 Prometheus 규칙으로 적었다.

`infra/monitoring/alerts.yml` 네 규칙:

| 알림 | 조건 |
|---|---|
| HostCpuHigh | CPU 5분 평균 80% 초과 |
| HostMemoryHigh | 사용 가능 메모리 15% 미만이 5분 |
| HttpProbeFailing | blackbox `probe_success == 0` 이 2분 |
| HttpLatencyHigh | `probe_duration_seconds > 1` 이 5분 |

`infra/monitoring/compose.yaml` 은 Prometheus, Alertmanager, node-exporter, blackbox 다. 루트 `compose.yaml` 에 넣지 않았다. 기본 `docker compose up` 은 이전과 같다.

Alertmanager 수신자는 `local-null` 이다. 메일, Slack, Pager 로 나가지 않는다. 알림 대상을 승인받지 않았기 때문이다.

`infra/monitoring/grafana-dashboard.json` 은 CPU, 메모리, probe 실패 수, probe 시간을 보는 대시다. Grafana 에 import 하지 않았다.

## 검증

```sh
docker run --rm --entrypoint promtool \
  -v "$PWD/infra/monitoring/alerts.yml:/alerts.yml:ro" \
  prom/prometheus:v2.54.1 check rules /alerts.yml
```

결과: `SUCCESS: 4 rules found`. 기록은 `docs/evidence/promtool.txt`.

관측용 compose 는 띄우지 않았다. 그래서 이 호스트의 CPU 와 메모리 알림이 실제로 울렸는지는 측정하지 않았다.

## 한계

에러율은 애플리케이션 메트릭이 아니라 blackbox 성공 여부다. Spring 은 Micrometer 를 추가하지 않았다. 알림이 사람에게 전달되는 경로는 아직 없다.

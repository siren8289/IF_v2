import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 5,
  duration: '15s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<1000'],
  },
};

export default function () {
  const jobs = http.get('http://127.0.0.1:8080/api/jobs');
  check(jobs, { 'jobs 200': (r) => r.status === 200 });
  const health = http.get('http://127.0.0.1:8000/health');
  check(health, { 'health 200': (r) => r.status === 200 });
  const web = http.get('http://127.0.0.1/');
  check(web, { 'web 200': (r) => r.status === 200 });
  sleep(0.2);
}

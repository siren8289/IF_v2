# IF_v2 시스템 및 QA·Security 자동화 아키텍처 (`docs/ARCHITECTURE.md`)

## 1. 전체 시스템 및 QA·Security V2.5 아키텍처 다이어그램

```mermaid
flowchart TD
    subgraph Client_Layer ["클라이언트 & 프록시 계층"]
        Browser["웹 브라우저 (React 18 / Vite / TS)"]
        Nginx["Nginx Reverse Proxy (:80)<br/>web-vite/nginx.conf"]
        Browser -->|"GET /* (SPA 정적 파일)"| Nginx
        Browser -->|"/api/* 요청 전달"| Nginx
    end

    subgraph Backend_Layer ["백엔드 & 데이터 계층"]
        Spring["Spring Boot 3.2 API (:8080)<br/>AssessmentController / Service"]
        FastAPI["FastAPI AI 서버 (:8000)<br/>ML(scikit-learn) + DL(PyTorch CNN) + Gemini"]
        Postgres[("PostgreSQL 16 (:5432)<br/>assessment / applicant / health_snapshot / ai_risk_result / job")]

        Nginx -->|"proxy_pass http://spring:8080"| Spring
        Spring -->|"JPA (Hibernate)"| Postgres
        Spring -->|"POST /api/v1/risk/analyze (RestTemplate)"| FastAPI
    end

    subgraph QA_Security_V25 ["바이브 코딩 QA·Security 자동화 시스템 (V2.5)"]
        AgentsMD["AGENTS.md & qa-policy.md<br/>(상시 적용 규칙)"]
        SkillHook[".agents/skills/qa-security-v25/SKILL.md<br/>& .agents/hooks.json"]
        Runner["qa/run_qa.py<br/>(교차 검증 테스트 실행기)"]
        Recorder["qa/recorder.py<br/>(MD·TSV 누적 기록 생성기)"]
        Reports["qa/reports/{test-type}/{YYYY-MM-DD}/<br/>pass.md | fail.md | risk.md | results.tsv"]
        CIGate[".github/workflows/githubactions.yml<br/>(qa-security-gate Job)"]

        AgentsMD --> Runner
        SkillHook --> Runner
        CIGate --> Runner
        Runner -->|"Tool A: curl / Gradle / Vitest / unittest / OWASP Probe"| Nginx
        Runner -->|"Tool B: Python HTTP / psql / tsc / SAST / npm audit"| Spring
        Runner -->|"Tool A & B 교차 검증"| FastAPI
        Runner -->|"DB 행 증감·무결성 대조"| Postgres
        Runner --> Recorder
        Recorder --> Reports
    end
```

---

## 2. 아키텍처 변경 이력

| 일자 (KST) | 버전 | 변경 대상 | 변경 내용 요약 |
| :--- | :--- | :--- | :--- |
| 2026-10-30 | V2.5 | `AGENTS.md`, `qa-policy.md`, `.agents/`, `qa/`, `.github/workflows/githubactions.yml` | 바이브 코딩 QA·Security 자동화 지침 V2.5 구축 (최소 2개 도구 교차 검증 실행기, 날짜별·종류별 4종 리포트 생성기, Antigravity 훅/스킬, GitHub Actions CI 게이트 연동) |
| 2026-10-31 | 인프라 코드 | `infra/`, `.github/workflows/githubactions.yml` | 기존 EC2·Compose 배포를 Terraform, Kubernetes 매니페스트, Prometheus 규칙으로 코드화. AWS 에는 적용하지 않음 |

## 3. 지금 돌아가는 경로와 CI/CD

운영 경로는 Kubernetes 가 아니다. EC2 한 대에서 `compose.yaml` 이 Postgres, Spring, FastAPI, Nginx 를 띄운다. 배포는 GitHub Actions 가 OIDC 로 AWS 역할을 맡은 뒤 SSM 으로 `scripts/deploy.sh` 를 실행한다.

```mermaid
flowchart LR
  subgraph dev [개발자]
    Git[Git push main]
  end
  subgraph gha [GitHub Actions]
    CI[CI 워크플로]
    CD[deploy.yml]
  end
  subgraph aws [AWS ap-northeast-2]
    Role[OIDC IAM 역할]
    SSM[SSM Run Command]
    EC2[EC2 한 대]
  end
  Git --> CI
  CI -->|성공한 main SHA| CD
  CD --> Role --> SSM --> EC2
  EC2 --> Compose[docker compose]
```

Kubernetes 매니페스트는 같은 컨테이너를 다른 실행 환경에 올리기 위한 정의다. 클러스터에 배포하지 않았다. 상세는 `docs/infrastructure.md` 에 있다.

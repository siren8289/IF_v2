// Spring 서버 주소. 배포(PROD) 환경에서는 Nginx 리버스 프록시를 통해 상대 경로("")로 요청하고,
// 로컬 개발 및 테스트 환경에서는 기본값("http://localhost:8080")을 사용한다.
export const API_BASE_URL: string =
  import.meta.env.VITE_API_URL !== undefined
    ? import.meta.env.VITE_API_URL
    : (import.meta.env.PROD ? "" : "http://localhost:8080");

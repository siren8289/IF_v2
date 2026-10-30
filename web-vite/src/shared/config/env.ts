// Spring 서버 주소.
//
// VITE_API_URL 이 있으면 그 값을 그대로 쓴다. 빈 문자열("")도 "설정함"으로 본다.
// 설정이 없고 배포 빌드(PROD)이면 "" 이다.
//   같은 주소의 Nginx가 /api 를 Spring으로 넘겨 주므로, 앞에 호스트를 붙이지 않는다.
// 설정이 없고 로컬 개발이면 Spring이 떠 있는 http://localhost:8080 을 붙인다.
export const API_BASE_URL: string =
  import.meta.env.VITE_API_URL !== undefined
    ? import.meta.env.VITE_API_URL
    : (import.meta.env.PROD ? "" : "http://localhost:8080");

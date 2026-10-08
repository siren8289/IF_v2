// Spring 서버 주소. Next의 NEXT_PUBLIC_API_URL 대신 Vite의 VITE_API_URL을 읽는다.
export const API_BASE_URL: string =
  import.meta.env.VITE_API_URL || "http://localhost:8080";

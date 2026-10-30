import { API_BASE_URL } from "@/shared/config/env";

// 모든 HTTP 호출은 이 함수를 거친다.
// path 예: "/api/jobs". 앞에 API_BASE_URL을 붙여 실제 주소를 만든다.
// 성공하면 JSON을 T 타입으로 돌려주고, 실패하면 Error를 던진다.
export async function apiRequest<T>(path: string, options: RequestInit = {}): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers: {
      // 기본은 JSON. 호출자가 헤더를 넘기면 그 값이 이 기본값을 덮어쓴다.
      "Content-Type": "application/json",
      ...options.headers,
    },
  });

  // 200번대가 아니면 실패. Spring은 { message: "..." } 로 이유를 준다.
  if (!res.ok) {
    const text = await res.text();
    let message = text || res.statusText;
    try {
      message = JSON.parse(text).message || message;
    } catch {
      // 응답이 JSON이 아니면(HTML 오류 페이지 등) 원문을 그대로 쓴다.
    }
    throw new Error(`API ${res.status}: ${message}`);
  }

  // 삭제 API는 204 No Content 라서 본문이 없다. JSON으로 읽으면 오류가 난다.
  if (res.status === 204 || res.headers.get("content-length") === "0") {
    return undefined as T;
  }
  return res.json() as Promise<T>;
}

import { API_BASE_URL } from "@/shared/config/env";

// API Client 계층: 모든 HTTP 호출의 단일 진입점. 응답은 JSON으로 파싱해 돌려준다.

export async function apiRequest<T>(
  path: string,
  options: RequestInit = {}
): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  });
  // 서버 오류 본문을 메시지에 포함해 화면에서 그대로 보여줄 수 있게 한다.
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`API ${res.status}: ${text || res.statusText}`);
  }
  // 본문이 없는 응답(DELETE/PATCH/POST 등)은 JSON 파싱을 건너뛴다.
  if (res.status === 204 || res.headers.get("content-length") === "0") {
    return undefined as T;
  }
  return res.json() as Promise<T>;
}

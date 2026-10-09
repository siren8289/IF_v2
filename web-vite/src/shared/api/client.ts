import { API_BASE_URL } from "@/shared/config/env";

// 모든 HTTP 호출은 이 함수를 거친다. 응답은 JSON으로 바꿔서 돌려준다.
export async function apiRequest<T>(path: string, options: RequestInit = {}): Promise<T> {
  const res = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  });

  if (!res.ok) {
    // Spring 오류 응답은 { message: "..." } 형태라서 message만 꺼내 보여준다.
    const text = await res.text();
    let message = text || res.statusText;
    try {
      message = JSON.parse(text).message || message;
    } catch {
      // JSON이 아니면 그대로 쓴다.
    }
    throw new Error(`API ${res.status}: ${message}`);
  }

  if (res.status === 204 || res.headers.get("content-length") === "0") {
    return undefined as T;
  }
  return res.json() as Promise<T>;
}

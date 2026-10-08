import { vi } from "vitest";

// 테스트용 요청 내역(경로/메서드/파싱된 본문)
interface MockRequest {
  path: string;
  method: string;
  body: unknown;
}
type MockResponse = { status?: number; json?: unknown };
type Handler = MockResponse | ((req: MockRequest) => MockResponse);

/** "METHOD /path" 키로 응답을 지정하는 fetch 목. 정의되지 않은 요청은 404를 돌려준다. */
export function mockApi(handlers: Record<string, Handler>) {
  const fetchMock = vi.fn(async (input: RequestInfo | URL, init?: RequestInit) => {
    const url = new URL(String(input));
    const method = init?.method ?? "GET";
    const handler = handlers[`${method} ${url.pathname}`];
    if (!handler) return new Response("not mocked", { status: 404 });

    const req: MockRequest = {
      path: url.pathname,
      method,
      body: init?.body ? JSON.parse(String(init.body)) : undefined,
    };
    const { status = 200, json } = typeof handler === "function" ? handler(req) : handler;
    if (status === 204 || json === undefined) return new Response(null, { status });
    return new Response(JSON.stringify(json), {
      status,
      headers: { "Content-Type": "application/json" },
    });
  });
  vi.stubGlobal("fetch", fetchMock);
  return fetchMock;
}

// 특정 요청("METHOD /path")이 호출된 내역만 추려 호출 순서/본문을 검증할 때 쓴다.
export function callsTo(fetchMock: ReturnType<typeof mockApi>, key: string) {
  return fetchMock.mock.calls.filter(
    ([input, init]) => `${init?.method ?? "GET"} ${new URL(String(input)).pathname}` === key
  );
}

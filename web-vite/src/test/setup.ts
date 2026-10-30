// 모든 테스트 전에 한 번 로드된다.
// jest-dom: 화면에 글자가 있는지 검사하는 매처를 추가한다.
// afterEach cleanup: 이전 테스트가 그린 화면을 지워 다음 테스트에 남지 않게 한다.
import "@testing-library/jest-dom/vitest";
import { afterEach } from "vitest";
import { cleanup } from "@testing-library/react";

afterEach(() => {
  cleanup();
});

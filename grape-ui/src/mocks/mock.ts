import fetchMock from "fetch-mock";
export function addMocks(): void {
  fetchMock.get("http://localhost:5000/api/entity/version", [
    "v0.0.1 test",
    "v0.0.4 another_test",
  ]);
}

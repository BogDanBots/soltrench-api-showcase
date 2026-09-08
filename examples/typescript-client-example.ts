/** Fresh portfolio example; it does not use production endpoints or code. */

type DemoStatus = {
  status: string;
  network: string;
};

export async function fetchStatus(baseUrl = "http://127.0.0.1:8000"): Promise<DemoStatus> {
  const response = await fetch(`${baseUrl}/demo/status`);
  if (!response.ok) {
    throw new Error(`Demo API request failed: ${response.status}`);
  }
  return (await response.json()) as DemoStatus;
}

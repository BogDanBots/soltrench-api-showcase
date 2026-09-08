"""Demo client for the local example API.

This standalone example demonstrates request handling and is independent of
the private SolTrenchAPI implementation.
"""

from __future__ import annotations

import os
from typing import Any

import httpx


def fetch_status() -> dict[str, Any]:
    base_url = os.environ.get("DEMO_API_URL", "http://127.0.0.1:8000")
    response = httpx.get(f"{base_url}/demo/status", timeout=5.0)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(fetch_status())

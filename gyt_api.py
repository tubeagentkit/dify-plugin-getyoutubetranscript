from typing import Any

import httpx

BASE_URL = "https://getyoutubetranscript.com/api/v1"
TIMEOUT_SECONDS = 60


class GetYouTubeTranscriptError(Exception):
    pass


def get(api_key: str, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    """GET an API path and return the `data` object. Empty params are dropped."""
    query = {k: v for k, v in (params or {}).items() if v not in (None, "")}
    try:
        response = httpx.get(
            f"{BASE_URL}{path}",
            params=query,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=TIMEOUT_SECONDS,
        )
    except httpx.HTTPError as e:
        raise GetYouTubeTranscriptError(f"Could not reach GetYouTubeTranscript: {type(e).__name__}") from e

    try:
        body = response.json()
    except ValueError:
        body = {}

    if response.status_code != 200 or not body.get("success"):
        message = body.get("message") or f"Request failed with HTTP {response.status_code}"
        raise GetYouTubeTranscriptError(message)
    return body.get("data") or {}

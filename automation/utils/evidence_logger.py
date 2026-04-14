"""Helpers for storing API evidence and execution notes."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

from automation.utils.config import Config

logger = logging.getLogger(__name__)


def ensure_evidence_directories() -> None:
    Path(Config.LOG_DIR).mkdir(parents=True, exist_ok=True)
    Path(Config.SCREENSHOT_DIR).mkdir(parents=True, exist_ok=True)


def _timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def safe_json(response: requests.Response) -> Any:
    try:
        return response.json()
    except ValueError:
        return {"raw_text": response.text}


def build_api_evidence(
    *,
    test_name: str,
    method: str,
    url: str,
    request_payload: dict[str, Any] | None,
    response: requests.Response,
) -> dict[str, Any]:
    return {
        "captured_at_utc": _timestamp(),
        "test_name": test_name,
        "request": {
            "method": method.upper(),
            "url": url,
            "payload": request_payload,
        },
        "response": {
            "status_code": response.status_code,
            "body": safe_json(response),
        },
    }


def write_api_evidence(
    *,
    test_name: str,
    method: str,
    url: str,
    request_payload: dict[str, Any] | None,
    response: requests.Response,
) -> Path:
    ensure_evidence_directories()
    output_path = Path(Config.LOG_DIR) / f"{test_name}_{_timestamp()}.json"
    evidence = build_api_evidence(
        test_name=test_name,
        method=method,
        url=url,
        request_payload=request_payload,
        response=response,
    )
    output_path.write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    logger.info("Saved API evidence to %s", output_path)
    return output_path

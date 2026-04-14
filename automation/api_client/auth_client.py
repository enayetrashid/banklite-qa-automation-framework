"""HTTP client wrappers for authentication endpoints."""

from __future__ import annotations

from typing import Any

import requests

from automation.utils.config import Config
from automation.utils.evidence_logger import write_api_evidence


class AuthClient:
    """Small wrapper around BankLite authentication requests."""

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()

    def login(self, username: str, password: str, test_name: str = "login") -> requests.Response:
        payload: dict[str, Any] = {
            "username": username,
            "password": password,
        }
        url = Config.api_url("/login")
        response = self.session.post(
            url,
            json=payload,
            timeout=Config.REQUEST_TIMEOUT,
        )
        write_api_evidence(
            test_name=test_name,
            method="POST",
            url=url,
            request_payload=payload,
            response=response,
        )
        return response

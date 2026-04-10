"""HTTP client wrappers for authentication endpoints."""

from __future__ import annotations

from typing import Any

import requests

from automation.utils.config import Config


class AuthClient:
    """Small wrapper around BankLite authentication requests."""

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()

    def login(self, username: str, password: str) -> requests.Response:
        payload: dict[str, Any] = {
            "username": username,
            "password": password,
        }
        return self.session.post(
            Config.api_url("/login"),
            json=payload,
            timeout=Config.REQUEST_TIMEOUT,
        )

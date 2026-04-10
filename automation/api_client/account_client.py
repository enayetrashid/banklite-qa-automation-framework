"""HTTP client wrappers for account-based endpoints."""

from __future__ import annotations

from typing import Any

import requests

from automation.utils.config import Config


class AccountClient:
    """Wrapper around balance and transaction endpoints."""

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()

    def get_balance(self, account_id: str) -> requests.Response:
        return self.session.get(
            Config.api_url(f"/accounts/{account_id}/balance"),
            timeout=Config.REQUEST_TIMEOUT,
        )

    def deposit(self, account_id: str, amount: str | int | float) -> requests.Response:
        payload: dict[str, Any] = {"amount": str(amount)}
        return self.session.post(
            Config.api_url(f"/accounts/{account_id}/deposit"),
            json=payload,
            timeout=Config.REQUEST_TIMEOUT,
        )

    def withdraw(self, account_id: str, amount: str | int | float) -> requests.Response:
        payload: dict[str, Any] = {"amount": str(amount)}
        return self.session.post(
            Config.api_url(f"/accounts/{account_id}/withdraw"),
            json=payload,
            timeout=Config.REQUEST_TIMEOUT,
        )

    def transfer(self, account_id: str, target_account_id: str, amount: str | int | float) -> requests.Response:
        payload: dict[str, Any] = {
            "target_account_id": target_account_id,
            "amount": str(amount),
        }
        return self.session.post(
            Config.api_url(f"/accounts/{account_id}/transfer"),
            json=payload,
            timeout=Config.REQUEST_TIMEOUT,
        )

    def get_transactions(self, account_id: str) -> requests.Response:
        return self.session.get(
            Config.api_url(f"/accounts/{account_id}/transactions"),
            timeout=Config.REQUEST_TIMEOUT,
        )

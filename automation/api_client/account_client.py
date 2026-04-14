"""HTTP client wrappers for account-based endpoints."""

from __future__ import annotations

from typing import Any

import requests

from automation.utils.config import Config
from automation.utils.evidence_logger import write_api_evidence


class AccountClient:
    """Wrapper around balance and transaction endpoints."""

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session = session or requests.Session()

    def get_balance(self, account_id: str, test_name: str = "get_balance") -> requests.Response:
        url = Config.api_url(f"/accounts/{account_id}/balance")
        response = self.session.get(url, timeout=Config.REQUEST_TIMEOUT)
        write_api_evidence(
            test_name=test_name,
            method="GET",
            url=url,
            request_payload=None,
            response=response,
        )
        return response

    def deposit(self, account_id: str, amount: str | int | float, test_name: str = "deposit") -> requests.Response:
        payload: dict[str, Any] = {"amount": str(amount)}
        url = Config.api_url(f"/accounts/{account_id}/deposit")
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

    def withdraw(self, account_id: str, amount: str | int | float, test_name: str = "withdraw") -> requests.Response:
        payload: dict[str, Any] = {"amount": str(amount)}
        url = Config.api_url(f"/accounts/{account_id}/withdraw")
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

    def transfer(
        self,
        account_id: str,
        target_account_id: str,
        amount: str | int | float,
        test_name: str = "transfer",
    ) -> requests.Response:
        payload: dict[str, Any] = {
            "target_account_id": target_account_id,
            "amount": str(amount),
        }
        url = Config.api_url(f"/accounts/{account_id}/transfer")
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

    def get_transactions(self, account_id: str, test_name: str = "get_transactions") -> requests.Response:
        url = Config.api_url(f"/accounts/{account_id}/transactions")
        response = self.session.get(url, timeout=Config.REQUEST_TIMEOUT)
        write_api_evidence(
            test_name=test_name,
            method="GET",
            url=url,
            request_payload=None,
            response=response,
        )
        return response

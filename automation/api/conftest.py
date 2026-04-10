"""Shared pytest fixtures for BankLite API tests."""

from __future__ import annotations

import pytest
import requests

from automation.api_client.account_client import AccountClient
from automation.api_client.auth_client import AuthClient
from automation.utils.config import Config


@pytest.fixture(scope="session")
def session() -> requests.Session:
    """Reusable requests session for the test run."""
    return requests.Session()


@pytest.fixture(scope="session")
def auth_client(session: requests.Session) -> AuthClient:
    return AuthClient(session)


@pytest.fixture(scope="session")
def account_client(session: requests.Session) -> AccountClient:
    return AccountClient(session)


@pytest.fixture(scope="session")
def valid_credentials() -> dict[str, str]:
    return {
        "username": Config.LOGIN_USERNAME,
        "password": Config.LOGIN_PASSWORD,
    }

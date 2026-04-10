"""Authentication API tests."""

from __future__ import annotations

import pytest

from automation.utils.assertions import (
    assert_failure_payload,
    assert_message_present,
    assert_success_payload,
)
from automation.utils.config import Config


@pytest.mark.api
@pytest.mark.smoke
def test_login_with_valid_credentials(auth_client, valid_credentials) -> None:
    response = auth_client.login(**valid_credentials)

    assert response.status_code == 200
    payload = response.json()
    assert_success_payload(payload)
    assert payload["username"] == Config.LOGIN_USERNAME
    assert payload["account_id"] == Config.ACCOUNT_ID


@pytest.mark.api
def test_login_with_invalid_password(auth_client) -> None:
    response = auth_client.login(Config.LOGIN_USERNAME, Config.INVALID_PASSWORD)

    assert response.status_code == 401
    payload = response.json()
    assert_failure_payload(payload)
    assert_message_present(payload)

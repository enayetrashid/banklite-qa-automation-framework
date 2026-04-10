"""Balance API tests."""

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
def test_get_balance_with_valid_account(account_client) -> None:
    response = account_client.get_balance(Config.ACCOUNT_ID)

    assert response.status_code == 200
    payload = response.json()
    assert_success_payload(payload)
    assert payload["account_id"] == Config.ACCOUNT_ID
    assert isinstance(payload["balance"], (int, float))


@pytest.mark.api
def test_get_balance_with_invalid_account(account_client) -> None:
    response = account_client.get_balance(Config.INVALID_ACCOUNT_ID)

    assert response.status_code == 404
    payload = response.json()
    assert_failure_payload(payload)
    assert_message_present(payload)

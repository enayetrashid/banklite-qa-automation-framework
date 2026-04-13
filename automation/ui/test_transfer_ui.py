"""UI tests for transfer flow."""

from __future__ import annotations

import pytest

from automation.pages.login_page import LoginPage
from automation.pages.transfer_page import TransferPage


@pytest.mark.ui
def test_transfer_with_valid_target_and_amount_shows_success_message(page) -> None:
    login_page = LoginPage(page)
    transfer_page = TransferPage(page)

    login_page.open()
    login_page.login("customer1", "Pass123!")
    transfer_page.open()
    transfer_page.submit_transfer("A1002", "20")

    transfer_page.wait_for_message()
    assert transfer_page.has_success_message()
    assert "Transfer completed. New balance: 980.00" in transfer_page.get_message_text()


@pytest.mark.ui
def test_transfer_to_same_account_shows_error_message(page) -> None:
    login_page = LoginPage(page)
    transfer_page = TransferPage(page)

    login_page.open()
    login_page.login("customer1", "Pass123!")
    transfer_page.open()
    transfer_page.submit_transfer("A1001", "20")

    transfer_page.wait_for_message()
    assert transfer_page.has_error_message()
    assert "You cannot transfer to your own account." in transfer_page.get_message_text()

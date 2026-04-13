"""UI tests for withdrawal flow."""

from __future__ import annotations

import pytest

from automation.pages.login_page import LoginPage
from automation.pages.withdraw_page import WithdrawPage


@pytest.mark.ui
def test_withdraw_with_valid_amount_shows_success_message(page) -> None:
    login_page = LoginPage(page)
    withdraw_page = WithdrawPage(page)

    login_page.open()
    login_page.login("customer1", "Pass123!")
    withdraw_page.open()
    withdraw_page.submit_withdrawal("25")

    withdraw_page.wait_for_message()
    assert withdraw_page.has_success_message()
    assert "Withdrawal completed. New balance: 975.00" in withdraw_page.get_message_text()


@pytest.mark.ui
def test_withdraw_with_large_amount_shows_error_message(page) -> None:
    login_page = LoginPage(page)
    withdraw_page = WithdrawPage(page)

    login_page.open()
    login_page.login("customer1", "Pass123!")
    withdraw_page.open()
    withdraw_page.submit_withdrawal("1000000.99")

    withdraw_page.wait_for_message()
    assert withdraw_page.has_error_message()
    assert "Insufficient funds." in withdraw_page.get_message_text()

"""UI tests for deposit flow."""

from __future__ import annotations

import pytest

from automation.pages.deposit_page import DepositPage
from automation.pages.login_page import LoginPage


@pytest.mark.ui
def test_deposit_with_valid_amount_shows_success_message(page) -> None:
    login_page = LoginPage(page)
    deposit_page = DepositPage(page)

    login_page.open()
    login_page.login("customer1", "Pass123!")
    deposit_page.open()
    deposit_page.submit_deposit("50")

    deposit_page.wait_for_message()
    assert deposit_page.has_success_message()
    assert "Deposit completed. New balance: 1050.00" in deposit_page.get_message_text()


@pytest.mark.ui
def test_deposit_with_blank_amount_shows_error_message(page) -> None:
    login_page = LoginPage(page)
    deposit_page = DepositPage(page)

    login_page.open()
    login_page.login("customer1", "Pass123!")
    deposit_page.open()
    deposit_page.submit_deposit("")

    deposit_page.wait_for_message()
    assert deposit_page.has_error_message()
    assert "Amount is required." in deposit_page.get_message_text()

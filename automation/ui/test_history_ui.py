"""UI tests for transaction history page."""

from __future__ import annotations

import pytest

from automation.pages.deposit_page import DepositPage
from automation.pages.history_page import HistoryPage
from automation.pages.login_page import LoginPage


@pytest.mark.ui
def test_transaction_history_page_shows_empty_state_for_fresh_session(page) -> None:
    login_page = LoginPage(page)
    history_page = HistoryPage(page)

    login_page.open()
    login_page.login("customer1", "Pass123!")
    history_page.open()

    assert history_page.is_loaded()
    assert history_page.get_empty_state_text() == "No transactions available yet."


@pytest.mark.ui
def test_transaction_history_page_displays_rows_after_transaction(page) -> None:
    login_page = LoginPage(page)
    deposit_page = DepositPage(page)
    history_page = HistoryPage(page)

    login_page.open()
    login_page.login("customer1", "Pass123!")
    deposit_page.open()
    deposit_page.submit_deposit("10")
    deposit_page.wait_for_message()

    history_page.open()

    assert history_page.is_loaded()
    assert history_page.get_transaction_row_count() >= 1

"""UI tests for dashboard balance display."""

from __future__ import annotations

import pytest

from automation.pages.dashboard_page import DashboardPage
from automation.pages.login_page import LoginPage


@pytest.mark.ui
def test_dashboard_displays_account_summary_after_login(page) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.open()
    login_page.login("customer1", "Pass123!")
    page.wait_for_url("**/dashboard")
    dashboard_page.wait_until_loaded()

    assert dashboard_page.get_displayed_username() == "customer1"
    assert dashboard_page.get_displayed_full_name() == "Customer One"
    assert dashboard_page.get_displayed_account_id() == "A1001"
    assert dashboard_page.get_displayed_balance() == "1000.00"

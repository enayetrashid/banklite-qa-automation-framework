"""UI tests for login flow."""

from __future__ import annotations

import pytest

from automation.pages.dashboard_page import DashboardPage
from automation.pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_login_with_valid_credentials_redirects_to_dashboard(page) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.open()
    assert login_page.is_loaded(), "Login page did not load."

    login_page.login("customer1", "Pass123!")

    page.wait_for_url("**/dashboard")
    dashboard_page.wait_until_loaded()

    assert dashboard_page.is_loaded()
    assert dashboard_page.get_displayed_username() == "customer1"
    assert dashboard_page.get_displayed_account_id() == "A1001"


@pytest.mark.ui
def test_login_with_invalid_password_shows_error_message(page) -> None:
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("customer1", "WrongPass123!")

    login_page.wait_for_message()
    assert login_page.has_error_message()
    assert "Invalid username or password." in login_page.get_message_text()

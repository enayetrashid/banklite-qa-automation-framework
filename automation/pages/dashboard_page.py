"""Page object for the dashboard page."""

from __future__ import annotations

from automation.pages.base_page import BasePage


class DashboardPage(BasePage):
    PATH = "/dashboard"

    def open(self) -> None:
        self.open_path(self.PATH)

    def wait_until_loaded(self) -> None:
        self.page.locator("#account-id-value").wait_for(state="visible")

    def is_loaded(self) -> bool:
        return self.page.locator("h2").inner_text().strip() == "Dashboard"

    def get_displayed_username(self) -> str:
        return self.page.locator("#username-value").inner_text().strip()

    def get_displayed_full_name(self) -> str:
        return self.page.locator("#full-name-value").inner_text().strip()

    def get_displayed_account_id(self) -> str:
        return self.page.locator("#account-id-value").inner_text().strip()

    def get_displayed_balance(self) -> str:
        return self.page.locator("#balance-value").inner_text().strip()

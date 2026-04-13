"""Page object for the deposit page."""

from __future__ import annotations

from automation.pages.base_page import BasePage


class DepositPage(BasePage):
    PATH = "/deposit"

    def open(self) -> None:
        self.open_path(self.PATH)

    def submit_deposit(self, amount: str) -> None:
        self.page.fill("#amount", amount)
        self.page.click("button[type='submit']")

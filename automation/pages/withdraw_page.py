"""Page object for the withdraw page."""

from __future__ import annotations

from automation.pages.base_page import BasePage


class WithdrawPage(BasePage):
    PATH = "/withdraw"

    def open(self) -> None:
        self.open_path(self.PATH)

    def submit_withdrawal(self, amount: str) -> None:
        self.page.fill("#amount", amount)
        self.page.click("button[type='submit']")

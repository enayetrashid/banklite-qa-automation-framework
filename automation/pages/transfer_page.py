"""Page object for the transfer page."""

from __future__ import annotations

from automation.pages.base_page import BasePage


class TransferPage(BasePage):
    PATH = "/transfer"

    def open(self) -> None:
        self.open_path(self.PATH)

    def submit_transfer(self, target_account_id: str, amount: str) -> None:
        self.page.fill("#target_account_id", target_account_id)
        self.page.fill("#amount", amount)
        self.page.click("button[type='submit']")

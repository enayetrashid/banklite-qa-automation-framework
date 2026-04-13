"""Page object for the transaction history page."""

from __future__ import annotations

from automation.pages.base_page import BasePage


class HistoryPage(BasePage):
    PATH = "/transactions"

    def open(self) -> None:
        self.open_path(self.PATH)

    def is_loaded(self) -> bool:
        return (
            self.page.locator("#transactions-table").count() > 0
            and self.page.locator("#empty-state").count() > 0
        )

    def get_empty_state_text(self) -> str:
        return self.page.locator("#empty-state").inner_text().strip()

    def get_transaction_row_count(self) -> int:
        return self.page.locator("#transactions-body tr").count()

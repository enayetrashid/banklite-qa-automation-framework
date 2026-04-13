"""Base Playwright page object utilities."""

from __future__ import annotations

from playwright.sync_api import Page

from automation.utils.config import UIConfig


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open_path(self, path: str) -> None:
        self.page.goto(f"{UIConfig.BASE_URL}{path}")

    def wait_for_message(self) -> None:
        self.page.locator("#message-box .message").wait_for(state="visible")

    def get_message_text(self) -> str:
        return self.page.locator("#message-box .message").inner_text().strip()

    def has_success_message(self) -> bool:
        return self.page.locator("#message-box .message.success").count() > 0

    def has_error_message(self) -> bool:
        return self.page.locator("#message-box .message.error").count() > 0

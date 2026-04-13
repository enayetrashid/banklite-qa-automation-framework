"""Page object for the login page."""

from __future__ import annotations

from automation.pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    def open(self) -> None:
        self.open_path(self.PATH)

    def login(self, username: str, password: str) -> None:
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")

    def is_loaded(self) -> bool:
        return self.page.locator("#login-form").count() > 0

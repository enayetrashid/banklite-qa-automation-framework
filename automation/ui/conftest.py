"""Shared Playwright fixtures for BankLite UI tests."""

from __future__ import annotations

from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from automation.utils.config import UIConfig


@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    browser = playwright_instance.chromium.launch(headless=UIConfig.HEADLESS)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_default_timeout(UIConfig.DEFAULT_TIMEOUT_MS)
    yield page


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request: pytest.FixtureRequest, page: Page):
    yield
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        screenshot_dir = Path(UIConfig.SCREENSHOT_DIR)
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        screenshot_path = screenshot_dir / f"{request.node.name}.png"
        page.screenshot(path=str(screenshot_path), full_page=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

"""Project-wide configuration helpers for API and UI automation."""

from __future__ import annotations

import os


class Config:
    """Central place for runtime configuration used by API tests."""

    BASE_URL = os.getenv("BANKLITE_BASE_URL", "http://127.0.0.1:5000")
    API_PREFIX = os.getenv("BANKLITE_API_PREFIX", "/api")
    LOGIN_USERNAME = os.getenv("BANKLITE_USERNAME", "customer1")
    LOGIN_PASSWORD = os.getenv("BANKLITE_PASSWORD", "Pass123!")
    INVALID_USERNAME = os.getenv("BANKLITE_INVALID_USERNAME", "unknown_user")
    INVALID_PASSWORD = os.getenv("BANKLITE_INVALID_PASSWORD", "WrongPass123!")
    ACCOUNT_ID = os.getenv("BANKLITE_ACCOUNT_ID", "A1001")
    INVALID_ACCOUNT_ID = os.getenv("BANKLITE_INVALID_ACCOUNT_ID", "A9999")
    REQUEST_TIMEOUT = int(os.getenv("BANKLITE_TIMEOUT", "10"))

    @classmethod
    def api_url(cls, path: str) -> str:
        path = path if path.startswith("/") else f"/{path}"
        return f"{cls.BASE_URL}{cls.API_PREFIX}{path}"


class UIConfig:
    """Runtime configuration for Playwright UI automation."""

    BASE_URL = os.getenv("BANKLITE_UI_BASE_URL", Config.BASE_URL)
    HEADLESS = os.getenv("BANKLITE_HEADLESS", "true").lower() == "true"
    DEFAULT_TIMEOUT_MS = int(os.getenv("BANKLITE_UI_TIMEOUT_MS", "8000"))
    SCREENSHOT_DIR = os.getenv(
        "BANKLITE_SCREENSHOT_DIR",
        "automation/evidence/screenshots",
    )

"""Project-wide configuration helpers for API automation and evidence capture."""

from __future__ import annotations

import os


class Config:
    """Central place for runtime configuration."""

    BASE_URL = os.getenv("BANKLITE_BASE_URL", "http://127.0.0.1:5000")
    API_PREFIX = os.getenv("BANKLITE_API_PREFIX", "/api")
    LOGIN_USERNAME = os.getenv("BANKLITE_USERNAME", "customer1")
    LOGIN_PASSWORD = os.getenv("BANKLITE_PASSWORD", "Pass123!")
    INVALID_USERNAME = os.getenv("BANKLITE_INVALID_USERNAME", "unknown_user")
    INVALID_PASSWORD = os.getenv("BANKLITE_INVALID_PASSWORD", "WrongPass123!")
    ACCOUNT_ID = os.getenv("BANKLITE_ACCOUNT_ID", "A1001")
    INVALID_ACCOUNT_ID = os.getenv("BANKLITE_INVALID_ACCOUNT_ID", "A9999")
    REQUEST_TIMEOUT = int(os.getenv("BANKLITE_TIMEOUT", "10"))

    EVIDENCE_ROOT = os.getenv("BANKLITE_EVIDENCE_ROOT", "automation/evidence")
    LOG_DIR = os.getenv("BANKLITE_LOG_DIR", f"{EVIDENCE_ROOT}/logs")
    SCREENSHOT_DIR = os.getenv("BANKLITE_SCREENSHOT_DIR", f"{EVIDENCE_ROOT}/screenshots")

    @classmethod
    def api_url(cls, path: str) -> str:
        path = path if path.startswith("/") else f"/{path}"
        return f"{cls.BASE_URL}{cls.API_PREFIX}{path}"

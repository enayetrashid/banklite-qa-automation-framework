"""Reusable assertions for API tests."""

from __future__ import annotations


def assert_success_payload(payload: dict) -> None:
    assert payload.get("success") is True, f"Expected success=True, got: {payload}"


def assert_failure_payload(payload: dict) -> None:
    assert payload.get("success") is False, f"Expected success=False, got: {payload}"


def assert_message_present(payload: dict) -> None:
    message = payload.get("message")
    assert isinstance(message, str) and message.strip(), f"Expected non-empty message, got: {payload}"

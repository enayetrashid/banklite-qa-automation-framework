# UI Automation Guide

This folder contains the Stage 3 Playwright + pytest UI automation layer for the BankLite application.

## Coverage
The starter UI layer includes tests for:
- login
- dashboard balance display
- deposit
- withdrawal
- transfer
- transaction history

## Design Approach
UI automation is organised using the Page Object Model (POM) so selectors and browser interactions stay separate from test assertions.

## Important Notes
- The UI uses `sessionStorage` to keep the current logged-in session.
- Each test runs with a new browser context to keep test state isolated.
- The application stores account data in memory only, so restarting the Flask app resets balances and transaction history.
- Some UI tests intentionally rely on a fresh application state for predictable balances.

## Install
```bash
pip install -r requirements.txt
playwright install
```

## Run all UI tests
```bash
pytest automation/ui -m ui
```

## Run only smoke UI tests
```bash
pytest automation/ui -m "ui and smoke"
```

## Useful environment variables
- `BANKLITE_UI_BASE_URL`
- `BANKLITE_HEADLESS`
- `BANKLITE_UI_TIMEOUT_MS`

Example:
```bash
BANKLITE_HEADLESS=false pytest automation/ui -m ui
```

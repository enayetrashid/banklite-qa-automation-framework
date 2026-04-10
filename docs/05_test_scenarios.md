# Test Scenarios -BankLite QA Automation Framework

This document defines the high-level test scenarios based on the current BankLite application behaviour.

The scenarios are grouped so they can later map cleanly to:
- Excel test cases
- traceability matrix entries
- Postman requests
- pytest API tests
- Playwright UI tests

---

## Test Scenario Summary

| Scenario ID | Module | Scenario | Priority | Planned Coverage |
|---|---|---|---|---|
| TS-LOGIN-001 | Authentication | Verify login with valid credentials | High | API + UI |
| TS-LOGIN-002 | Authentication | Verify login with empty username | High | API + UI |
| TS-LOGIN-003 | Authentication | Verify login with empty password | High | API + UI |
| TS-LOGIN-004 | Authentication | Verify login with invalid password | High | API + UI |
| TS-LOGIN-005 | Authentication | Verify login with unknown username | Medium | API |
| TS-LOGIN-006 | Authentication | Verify login trims surrounding spaces in username | Medium | API |
| TS-BAL-001 | Balance | Verify balance retrieval for valid account | High | API + UI |
| TS-BAL-002 | Balance | Verify balance request for invalid account | High | API |
| TS-BAL-003 | Balance | Verify balance reflects successful deposit | High | API |
| TS-BAL-004 | Balance | Verify balance reflects successful withdrawal | High | API |
| TS-BAL-005 | Balance | Verify balance reflects successful transfer | High | API |
| TS-DEP-001 | Deposit | Verify deposit with valid amount | High | API + UI |
| TS-DEP-002 | Deposit | Verify deposit with missing amount | High | API + UI |
| TS-DEP-003 | Deposit | Verify deposit with blank amount | High | API |
| TS-DEP-004 | Deposit | Verify deposit with non-numeric amount | High | API + UI |
| TS-DEP-005 | Deposit | Verify deposit with zero amount | High | API |
| TS-DEP-006 | Deposit | Verify deposit with negative amount | High | API |
| TS-DEP-007 | Deposit | Verify deposit for invalid account | Medium | API |
| TS-DEP-008 | Deposit | Verify deposit creates transaction history entry | High | API |
| TS-WDR-001 | Withdrawal | Verify withdrawal with valid amount and sufficient balance | High | API + UI |
| TS-WDR-002 | Withdrawal | Verify withdrawal with missing amount | High | API |
| TS-WDR-003 | Withdrawal | Verify withdrawal with blank amount | Medium | API |
| TS-WDR-004 | Withdrawal | Verify withdrawal with non-numeric amount | High | API + UI |
| TS-WDR-005 | Withdrawal | Verify withdrawal with zero amount | High | API |
| TS-WDR-006 | Withdrawal | Verify withdrawal with negative amount | High | API |
| TS-WDR-007 | Withdrawal | Verify withdrawal exceeding available balance | High | API + UI |
| TS-WDR-008 | Withdrawal | Verify withdrawal equal to full balance | Medium | API |
| TS-WDR-009 | Withdrawal | Verify withdrawal for invalid account | Medium | API |
| TS-WDR-010 | Withdrawal | Verify withdrawal creates transaction history entry | High | API |
| TS-TRF-001 | Transfer | Verify transfer with valid target account and valid amount | High | API + UI |
| TS-TRF-002 | Transfer | Verify transfer with missing target account | High | API + UI |
| TS-TRF-003 | Transfer | Verify transfer to non-existent target account | High | API |
| TS-TRF-004 | Transfer | Verify transfer to own account is blocked | High | API + UI |
| TS-TRF-005 | Transfer | Verify transfer with missing amount | High | API |
| TS-TRF-006 | Transfer | Verify transfer with blank amount | Medium | API |
| TS-TRF-007 | Transfer | Verify transfer with non-numeric amount | High | API + UI |
| TS-TRF-008 | Transfer | Verify transfer with zero amount | High | API |
| TS-TRF-009 | Transfer | Verify transfer with negative amount | High | API |
| TS-TRF-010 | Transfer | Verify transfer with insufficient funds | High | API + UI |
| TS-TRF-011 | Transfer | Verify transfer from invalid source account | Medium | API |
| TS-TRF-012 | Transfer | Verify successful transfer updates source balance | High | API |
| TS-TRF-013 | Transfer | Verify successful transfer updates destination balance | High | API |
| TS-TRF-014 | Transfer | Verify successful transfer creates history entries | High | API |
| TS-HIS-001 | Transaction History | Verify empty transaction history for valid account | High | API + UI |
| TS-HIS-002 | Transaction History | Verify transaction history after deposit | High | API + UI |
| TS-HIS-003 | Transaction History | Verify transaction history after withdrawal | High | API + UI |
| TS-HIS-004 | Transaction History | Verify transaction history after transfer | High | API + UI |
| TS-HIS-005 | Transaction History | Verify transaction history request for invalid account | Medium | API |
| TS-HIS-006 | Transaction History | Verify transaction record structure matches current implementation | Medium | API |
| TS-UI-001 | UI Navigation | Verify logout clears session and prevents protected flow continuation | Medium | UI |
| TS-UI-002 | UI Navigation | Verify dashboard requires login session data | Medium | UI |
| TS-UI-003 | UI Messaging | Verify success and error messages are visible to the user | High | UI |

---

## Detailed Scenarios

## Authentication

### TS-LOGIN-001 -Verify login with valid credentials
**Objective:** Confirm that valid login succeeds and returns the correct account details.

### TS-LOGIN-002 -Verify login with empty username
**Objective:** Confirm that login is rejected when username is not provided.

### TS-LOGIN-003 -Verify login with empty password
**Objective:** Confirm that login is rejected when password is not provided.

### TS-LOGIN-004 -Verify login with invalid password
**Objective:** Confirm that login fails when the password is incorrect.

### TS-LOGIN-005 -Verify login with unknown username
**Objective:** Confirm that login fails when the username does not exist.

### TS-LOGIN-006 -Verify login trims surrounding spaces in username
**Objective:** Confirm that leading and trailing spaces in username do not block valid authentication.

---

## Balance

### TS-BAL-001 -Verify balance retrieval for valid account
**Objective:** Confirm that a valid account balance request returns current account details and balance.

### TS-BAL-002 -Verify balance request for invalid account
**Objective:** Confirm that an unknown account ID returns the correct not-found response.

### TS-BAL-003 -Verify balance reflects successful deposit
**Objective:** Confirm that balance updates correctly after a successful deposit within the same app state.

### TS-BAL-004 -Verify balance reflects successful withdrawal
**Objective:** Confirm that balance updates correctly after a successful withdrawal within the same app state.

### TS-BAL-005 -Verify balance reflects successful transfer
**Objective:** Confirm that balance updates correctly after a successful transfer within the same app state.

---

## Deposit

### TS-DEP-001 -Verify deposit with valid amount
**Objective:** Confirm that a valid positive deposit amount increases the balance successfully.

### TS-DEP-002 -Verify deposit with missing amount
**Objective:** Confirm that deposit fails when the amount field is missing.

### TS-DEP-003 -Verify deposit with blank amount
**Objective:** Confirm that deposit fails when the amount field is blank.

### TS-DEP-004 -Verify deposit with non-numeric amount
**Objective:** Confirm that deposit fails when the amount is not numeric.

### TS-DEP-005 -Verify deposit with zero amount
**Objective:** Confirm that deposit fails when the amount is zero.

### TS-DEP-006 -Verify deposit with negative amount
**Objective:** Confirm that deposit fails when the amount is negative.

### TS-DEP-007 -Verify deposit for invalid account
**Objective:** Confirm that deposit fails when the target account does not exist.

### TS-DEP-008 -Verify deposit creates transaction history entry
**Objective:** Confirm that a successful deposit creates a deposit record in transaction history.

---

## Withdrawal

### TS-WDR-001 -Verify withdrawal with valid amount and sufficient balance
**Objective:** Confirm that a valid withdrawal reduces the balance correctly.

### TS-WDR-002 -Verify withdrawal with missing amount
**Objective:** Confirm that withdrawal fails when the amount field is missing.

### TS-WDR-003 -Verify withdrawal with blank amount
**Objective:** Confirm that withdrawal fails when the amount field is blank.

### TS-WDR-004 -Verify withdrawal with non-numeric amount
**Objective:** Confirm that withdrawal fails when the amount is not numeric.

### TS-WDR-005 -Verify withdrawal with zero amount
**Objective:** Confirm that withdrawal fails when the amount is zero.

### TS-WDR-006 -Verify withdrawal with negative amount
**Objective:** Confirm that withdrawal fails when the amount is negative.

### TS-WDR-007 -Verify withdrawal exceeding available balance
**Objective:** Confirm that withdrawal is blocked when funds are insufficient.

### TS-WDR-008 -Verify withdrawal equal to full balance
**Objective:** Confirm that withdrawing the exact current balance succeeds and sets balance to zero.

### TS-WDR-009 -Verify withdrawal for invalid account
**Objective:** Confirm that withdrawal fails when the account does not exist.

### TS-WDR-010 -Verify withdrawal creates transaction history entry
**Objective:** Confirm that a successful withdrawal creates a withdraw record in transaction history.

---

## Transfer

### TS-TRF-001 -Verify transfer with valid target account and valid amount
**Objective:** Confirm that a valid transfer succeeds and updates the source account balance.

### TS-TRF-002 -Verify transfer with missing target account
**Objective:** Confirm that transfer fails when no target account ID is supplied.

### TS-TRF-003 -Verify transfer to non-existent target account
**Objective:** Confirm that transfer fails when the destination account does not exist.

### TS-TRF-004 -Verify transfer to own account is blocked
**Objective:** Confirm that the system blocks a transfer when source and target accounts are the same.

### TS-TRF-005 -Verify transfer with missing amount
**Objective:** Confirm that transfer fails when the amount field is missing.

### TS-TRF-006 -Verify transfer with blank amount
**Objective:** Confirm that transfer fails when the amount field is blank.

### TS-TRF-007 -Verify transfer with non-numeric amount
**Objective:** Confirm that transfer fails when the amount is not numeric.

### TS-TRF-008 -Verify transfer with zero amount
**Objective:** Confirm that transfer fails when the amount is zero.

### TS-TRF-009 -Verify transfer with negative amount
**Objective:** Confirm that transfer fails when the amount is negative.

### TS-TRF-010 -Verify transfer with insufficient funds
**Objective:** Confirm that transfer is rejected when source balance is too low.

### TS-TRF-011 -Verify transfer from invalid source account
**Objective:** Confirm that transfer fails when the source account does not exist.

### TS-TRF-012 -Verify successful transfer updates source balance
**Objective:** Confirm that the source account balance decreases by the transfer amount.

### TS-TRF-013 -Verify successful transfer updates destination balance
**Objective:** Confirm that the destination account balance increases by the transfer amount.

### TS-TRF-014 -Verify successful transfer creates history entries
**Objective:** Confirm that a successful transfer creates transfer-related transaction history entries.

---

## Transaction History

### TS-HIS-001 -Verify empty transaction history for valid account
**Objective:** Confirm that a valid account with no transactions returns an empty list and the UI shows the correct empty-state message.

### TS-HIS-002 -Verify transaction history after deposit
**Objective:** Confirm that transaction history includes a deposit record after a successful deposit.

### TS-HIS-003 -Verify transaction history after withdrawal
**Objective:** Confirm that transaction history includes a withdraw record after a successful withdrawal.

### TS-HIS-004 -Verify transaction history after transfer
**Objective:** Confirm that transaction history includes transfer-related records after a successful transfer.

### TS-HIS-005 -Verify transaction history request for invalid account
**Objective:** Confirm that history lookup fails correctly for an unknown account.

### TS-HIS-006 -Verify transaction record structure matches current implementation
**Objective:** Confirm that returned transaction records follow the current application structure and do not assume unsupported fields.

---

## UI Navigation and Feedback

### TS-UI-001 -Verify logout clears session and prevents protected flow continuation
**Objective:** Confirm that logout removes stored session data and blocks continued use of account-specific pages without login state.

### TS-UI-002 -Verify dashboard requires login session data
**Objective:** Confirm that dashboard behaviour depends on session data in browser storage.

### TS-UI-003 -Verify success and error messages are visible to the user
**Objective:** Confirm that the UI displays meaningful feedback for successful and failed operations.

---

## Suggested Smoke Set for Early Automation

The following scenarios are a good first smoke pack for this framework:
- TS-LOGIN-001
- TS-BAL-001
- TS-DEP-001
- TS-WDR-001
- TS-TRF-001
- TS-HIS-001

These should become the first:
- Postman checks
- pytest API smoke tests
- Playwright UI smoke journeys

---

## Suggested Regression Set for Full Automation

A fuller regression baseline should include:
- all authentication scenarios
- all positive and negative amount validations
- insufficient funds validations
- invalid account handling
- transaction history verification after each successful money movement
- key UI feedback paths

---

## Alignment Notes

Compared with earlier manual test designs, these scenarios are updated to reflect:
- username/password login
- API endpoint testing
- browser-plus-API flow
- current validation message wording
- current transaction structure and in-memory behaviour

This document should now drive the next this framework assets:
- Excel test cases
- traceability matrix
- Postman collection
- pytest automation suite
- Playwright page object model and UI tests

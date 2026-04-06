# Acceptance Criteria — BankLite QA Automation Framework

This document converts the current application implementation into clear, testable acceptance criteria for this framework.

All acceptance criteria in this file are aligned to the current BankLite application behaviour.

---

## 1. Authentication

### AC-LOGIN-001 — Valid login succeeds
**Given** a valid username and valid password are provided  
**When** the client sends `POST /api/login`  
**Then** the response status shall be `200`  
**And** the response shall contain `success: true`  
**And** the response shall contain the correct `username`  
**And** the response shall contain the correct `full_name`  
**And** the response shall contain the correct `account_id`

### AC-LOGIN-002 — Empty username is rejected
**Given** username is empty  
**When** the client sends `POST /api/login`  
**Then** the response status shall be `401`  
**And** the response shall contain `success: false`  
**And** the message shall be `Username is required.`

### AC-LOGIN-003 — Empty password is rejected
**Given** password is empty  
**When** the client sends `POST /api/login`  
**Then** the response status shall be `401`  
**And** the response shall contain `success: false`  
**And** the message shall be `Password is required.`

### AC-LOGIN-004 — Invalid credentials are rejected
**Given** the username does not exist or the password is incorrect  
**When** the client sends `POST /api/login`  
**Then** the response status shall be `401`  
**And** the response shall contain `success: false`  
**And** the message shall be `Invalid username or password.`

### AC-LOGIN-005 — Username is trimmed before authentication
**Given** a valid username is entered with surrounding spaces  
**When** the client sends `POST /api/login`  
**Then** authentication shall use the trimmed username value  
**And** valid credentials shall still succeed

---

## 2. Balance Enquiry

### AC-BAL-001 — Balance is returned for a valid account
**Given** a valid account ID exists  
**When** the client sends `GET /api/accounts/<account_id>/balance`  
**Then** the response status shall be `200`  
**And** the response shall contain `success: true`  
**And** the response shall contain the requested `account_id`  
**And** the response shall contain `username`  
**And** the response shall contain `full_name`  
**And** the response shall contain the current numeric `balance`

### AC-BAL-002 — Unknown account is rejected for balance lookup
**Given** the requested account ID does not exist  
**When** the client sends `GET /api/accounts/<account_id>/balance`  
**Then** the response status shall be `404`  
**And** the response shall contain `success: false`  
**And** the message shall be `Account was not found.`

### AC-BAL-003 — Balance reflects previous successful transactions in the same app instance
**Given** a successful deposit, withdrawal, or transfer has already been completed in the same running application state  
**When** the client requests the account balance  
**Then** the returned balance shall reflect the latest successful transaction outcome

---

## 3. Deposit

### AC-DEP-001 — Valid deposit succeeds
**Given** a valid account ID exists  
**And** the amount is a valid positive number greater than zero  
**When** the client sends `POST /api/accounts/<account_id>/deposit`  
**Then** the response status shall be `200`  
**And** the response shall contain `success: true`  
**And** the response shall contain the requested `account_id`  
**And** the response shall contain `new_balance`  
**And** `new_balance` shall equal previous balance plus deposit amount

### AC-DEP-002 — Missing amount is rejected
**Given** amount is missing, null, or blank  
**When** the client sends a deposit request  
**Then** the response status shall be `400`  
**And** the response shall contain `success: false`  
**And** the message shall be `Amount is required.`

### AC-DEP-003 — Non-numeric amount is rejected
**Given** amount cannot be converted to a number  
**When** the client sends a deposit request  
**Then** the response status shall be `400`  
**And** the response shall contain `success: false`  
**And** the message shall be `Amount must be a number.`

### AC-DEP-004 — Zero amount is rejected
**Given** amount is `0`  
**When** the client sends a deposit request  
**Then** the response status shall be `400`  
**And** the response shall contain `success: false`  
**And** the message shall be `Amount must be greater than zero.`

### AC-DEP-005 — Negative amount is rejected
**Given** amount is less than zero  
**When** the client sends a deposit request  
**Then** the response status shall be `400`  
**And** the response shall contain `success: false`  
**And** the message shall be `Amount must be greater than zero.`

### AC-DEP-006 — Unknown account is rejected for deposit
**Given** the account ID does not exist  
**When** the client sends a deposit request  
**Then** the response status shall be `404`  
**And** the response shall contain `success: false`  
**And** the message shall be `Account was not found.`

### AC-DEP-007 — Successful deposit creates a transaction entry
**Given** a valid deposit succeeds  
**When** the account transaction history is requested afterwards in the same app instance  
**Then** the history shall include a record with type `deposit`  
**And** the record shall include the deposited amount  
**And** the record message shall match the deposit action

---

## 4. Withdrawal

### AC-WDR-001 — Valid withdrawal succeeds
**Given** a valid account ID exists  
**And** sufficient balance is available  
**And** the amount is a valid positive number greater than zero  
**When** the client sends `POST /api/accounts/<account_id>/withdraw`  
**Then** the response status shall be `200`  
**And** the response shall contain `success: true`  
**And** the response shall contain `new_balance`  
**And** `new_balance` shall equal previous balance minus withdrawal amount

### AC-WDR-002 — Missing amount is rejected
**Given** amount is missing, null, or blank  
**When** the client sends a withdraw request  
**Then** the response status shall be `400`  
**And** the message shall be `Amount is required.`

### AC-WDR-003 — Non-numeric amount is rejected
**Given** amount cannot be converted to a number  
**When** the client sends a withdraw request  
**Then** the response status shall be `400`  
**And** the message shall be `Amount must be a number.`

### AC-WDR-004 — Zero amount is rejected
**Given** amount is `0`  
**When** the client sends a withdraw request  
**Then** the response status shall be `400`  
**And** the message shall be `Amount must be greater than zero.`

### AC-WDR-005 — Negative amount is rejected
**Given** amount is less than zero  
**When** the client sends a withdraw request  
**Then** the response status shall be `400`  
**And** the message shall be `Amount must be greater than zero.`

### AC-WDR-006 — Insufficient funds are rejected
**Given** the requested amount exceeds the available balance  
**When** the client sends a withdraw request  
**Then** the response status shall be `400`  
**And** the response shall contain `success: false`  
**And** the message shall be `Insufficient funds.`  
**And** the account balance shall remain unchanged

### AC-WDR-007 — Exact-balance withdrawal succeeds
**Given** the requested amount exactly equals the current available balance  
**When** the client sends a withdraw request  
**Then** the response status shall be `200`  
**And** the response shall contain `success: true`  
**And** the new balance shall be `0.0`

### AC-WDR-008 — Unknown account is rejected for withdrawal
**Given** the account ID does not exist  
**When** the client sends a withdraw request  
**Then** the response status shall be `404`  
**And** the message shall be `Account was not found.`

### AC-WDR-009 — Successful withdrawal creates a transaction entry
**Given** a valid withdrawal succeeds  
**When** the account transaction history is requested afterwards in the same app instance  
**Then** the history shall include a record with type `withdraw`  
**And** the record shall include the withdrawn amount  
**And** the record message shall match the withdraw action

---

## 5. Transfer

### AC-TRF-001 — Valid transfer succeeds
**Given** a valid source account exists  
**And** a different valid target account exists  
**And** sufficient balance is available  
**And** the amount is a valid positive number greater than zero  
**When** the client sends `POST /api/accounts/<account_id>/transfer`  
**Then** the response status shall be `200`  
**And** the response shall contain `success: true`  
**And** the response shall contain `new_balance` for the source account  
**And** the source balance shall be reduced by the transfer amount

### AC-TRF-002 — Missing target account is rejected
**Given** target account ID is missing or blank  
**When** the client sends a transfer request  
**Then** the response status shall be `400`  
**And** the message shall be `Target account is required.`

### AC-TRF-003 — Unknown target account is rejected
**Given** the target account ID does not exist  
**When** the client sends a transfer request  
**Then** the response status shall be `400`  
**And** the message shall be `Target account was not found.`

### AC-TRF-004 — Transfer to own account is rejected
**Given** the source account ID and target account ID are the same  
**When** the client sends a transfer request  
**Then** the response status shall be `400`  
**And** the message shall be `You cannot transfer to your own account.`

### AC-TRF-005 — Missing amount is rejected
**Given** amount is missing, null, or blank  
**When** the client sends a transfer request  
**Then** the response status shall be `400`  
**And** the message shall be `Amount is required.`

### AC-TRF-006 — Non-numeric amount is rejected
**Given** amount cannot be converted to a number  
**When** the client sends a transfer request  
**Then** the response status shall be `400`  
**And** the message shall be `Amount must be a number.`

### AC-TRF-007 — Zero amount is rejected
**Given** amount is `0`  
**When** the client sends a transfer request  
**Then** the response status shall be `400`  
**And** the message shall be `Amount must be greater than zero.`

### AC-TRF-008 — Negative amount is rejected
**Given** amount is less than zero  
**When** the client sends a transfer request  
**Then** the response status shall be `400`  
**And** the message shall be `Amount must be greater than zero.`

### AC-TRF-009 — Insufficient funds block transfer
**Given** the requested transfer amount exceeds the available source balance  
**When** the client sends a transfer request  
**Then** the response status shall be `400`  
**And** the message shall be `Insufficient funds.`  
**And** the source balance shall remain unchanged

### AC-TRF-010 — Unknown source account is rejected
**Given** the source account ID does not exist  
**When** the client sends a transfer request  
**Then** the response status shall be `404`  
**And** the message shall be `Account was not found.`

### AC-TRF-011 — Successful transfer creates transaction history entries
**Given** a valid transfer succeeds  
**When** transaction history is requested after the transfer  
**Then** the source account history shall reflect the transfer activity  
**And** the destination account history shall reflect the transfer activity according to the current implementation

---

## 6. Transaction History

### AC-HIS-001 — Transaction history returns successfully for a valid account
**Given** a valid account ID exists  
**When** the client sends `GET /api/accounts/<account_id>/transactions`  
**Then** the response status shall be `200`  
**And** the response shall contain `success: true`  
**And** the response shall contain the requested `account_id`  
**And** the response shall contain a `transactions` list

### AC-HIS-002 — Empty transaction history is supported
**Given** a valid account has no transactions recorded  
**When** the client requests transaction history  
**Then** the response status shall be `200`  
**And** the `transactions` field shall be an empty list

### AC-HIS-003 — Transaction history contains deposit records after successful deposit
**Given** a successful deposit has been completed in the same app instance  
**When** the client requests transaction history  
**Then** the returned list shall include a deposit transaction entry

### AC-HIS-004 — Transaction history contains withdraw records after successful withdrawal
**Given** a successful withdrawal has been completed in the same app instance  
**When** the client requests transaction history  
**Then** the returned list shall include a withdraw transaction entry

### AC-HIS-005 — Transaction history contains transfer records after successful transfer
**Given** a successful transfer has been completed in the same app instance  
**When** the client requests transaction history  
**Then** the returned list shall include transfer-related transaction entry or entries according to the current implementation

### AC-HIS-006 — Unknown account is rejected for transaction history lookup
**Given** the account ID does not exist  
**When** the client requests transaction history  
**Then** the response status shall be `404`  
**And** the message shall be `Account was not found.`

### AC-HIS-007 — Transaction records follow current structure
**Given** transaction history contains records  
**When** the records are inspected  
**Then** each record shall use the current transaction model returned by the application  
**And** this framework shall not assume timestamp fields unless the application is enhanced later

---

## 7. UI Acceptance Criteria

### AC-UI-001 — Successful UI login redirects to dashboard
**Given** the user enters valid credentials on `/login`  
**When** the login form is submitted  
**Then** the login API shall be called  
**And** session details shall be stored in browser local storage  
**And** the browser shall navigate to `/dashboard`

### AC-UI-002 — Failed UI login shows returned error message
**Given** the user enters invalid or incomplete login details  
**When** the login form is submitted  
**Then** the page shall display the API error message to the user

### AC-UI-003 — Dashboard loads current account details
**Given** a valid login session is present in local storage  
**When** the dashboard page loads  
**Then** the page shall display username, full name, account ID, and current balance

### AC-UI-004 — Deposit page shows success feedback after valid deposit
**Given** a valid login session is present  
**When** the user submits a valid deposit  
**Then** the page shall display a success message including the new balance

### AC-UI-005 — Withdraw page shows validation or business-rule errors
**Given** a valid login session is present  
**When** the user submits an invalid withdraw request or a request exceeding balance  
**Then** the page shall display the returned error message

### AC-UI-006 — Transfer page shows validation or business-rule errors
**Given** a valid login session is present  
**When** the user submits an invalid transfer request  
**Then** the page shall display the returned error message

### AC-UI-007 — Transactions page shows empty-state message when no history exists
**Given** a valid login session is present  
**And** no transaction records exist for the account  
**When** the transactions page loads  
**Then** the page shall show `No transactions available yet.`

### AC-UI-008 — Transactions page shows table when history exists
**Given** a valid login session is present  
**And** transaction records exist for the account  
**When** the transactions page loads  
**Then** the page shall display the transactions in a table

---

## 8. Alignment Notes for this framework

These acceptance criteria intentionally replace several older Repo 6 assumptions.

this framework should now assume:
- username/password login instead of account number/PIN login
- API-first validation messages
- in-memory data behaviour
- lightweight transaction structure
- web and API flow coverage together

This document should be the baseline for:
- test scenarios
- Excel test cases
- Postman assertions
- pytest API tests
- Playwright UI tests

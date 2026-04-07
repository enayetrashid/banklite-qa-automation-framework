# Requirements Specification — BankLite QA Automation Framework

## 1. Introduction

### 1.1 Purpose
This document defines the functional requirements baseline for this framework.

This QA automation framework is designed for the BankLite web and API application. The purpose of this document is to convert the current application behaviour into a testable, automation-ready requirements set.

### 1.2 System Under Test
The system under test is the BankLite Web and API Application.

It is a demo banking application built with:
- Flask web routes for page rendering
- JSON API routes for banking operations
- service-layer business logic
- in-memory storage for demo data

### 1.3 Source of Truth
The requirements in this document are aligned to the current application implementation, including:
- API routes
- validation logic
- service-layer business rules
- current response messages
- current data model limitations

### 1.4 Important Alignment Note
These requirements are intentionally aligned to the current implementation, not to ideal banking-system behaviour.

That means this framework should test the current application behaviour, including current limitations such as:
- in-memory storage only
- no database persistence between restarts
- basic authentication only
- transaction history without timestamp fields
- no session-based backend authentication for API calls

---

## 2. Application Overview

The application supports the following core functions:
- user login
- balance enquiry
- deposit
- withdrawal
- fund transfer
- transaction history

The application exposes both:
- browser-accessible pages
- API endpoints used by the frontend JavaScript layer

### 2.1 Demo Accounts
The current seeded demo users are:

| Username | Password | Full Name | Account ID | Opening Balance |
|---|---|---|---|---:|
| customer1 | Pass123! | Customer One | A1001 | 1000.00 |
| customer2 | Pass123! | Customer Two | A1002 | 500.00 |

---

## 3. Functional Requirements

## FR-001: User Authentication

### Description
The system shall authenticate a user through the login API using username and password.

### API Endpoint
`POST /api/login`

### Request Body
```json
{
  "username": "customer1",
  "password": "Pass123!"
}
```

### Expected Behaviour
- The system shall accept a JSON request body.
- The system shall trim leading and trailing spaces from the username field.
- The system shall validate presence of username.
- The system shall validate presence of password.
- The system shall validate the username/password combination against stored user data.
- On success, the system shall return the username, full name, and account ID.
- On failure, the system shall return a failure message.

### Current Business Rules
- Empty username returns `Username is required.`
- Empty password returns `Password is required.`
- Unknown username or wrong password returns `Invalid username or password.`
- Validation and authentication failures currently return HTTP 401.

---

## FR-002: Balance Enquiry

### Description
The system shall allow balance retrieval for a valid account through the balance API.

### API Endpoint
`GET /api/accounts/<account_id>/balance`

### Expected Behaviour
- The system shall locate the user record using the supplied account ID.
- If the account exists, the system shall return current balance information.
- The response shall include:
  - success flag
  - account ID
  - username
  - full name
  - balance
- If the account does not exist, the system shall return an error response.

### Current Business Rules
- Unknown account returns `Account was not found.` with HTTP 404.
- Valid account returns HTTP 200.
- Balance is returned as numeric data.

---

## FR-003: Deposit Funds

### Description
The system shall allow money to be deposited into a valid account through the deposit API.

### API Endpoint
`POST /api/accounts/<account_id>/deposit`

### Request Body
```json
{
  "amount": "50"
}
```

### Expected Behaviour
- The system shall first validate that the account exists.
- The system shall validate the amount value.
- The system shall accept numeric input that can be converted to float.
- The system shall reject missing, blank, non-numeric, zero, and negative amounts.
- On success, the system shall add the deposit amount to the current balance.
- On success, the system shall append a deposit transaction record.
- On success, the system shall return the updated balance.

### Current Business Rules
- Missing or blank amount returns `Amount is required.`
- Non-numeric amount returns `Amount must be a number.`
- Zero or negative amount returns `Amount must be greater than zero.`
- Unknown account returns `Account was not found.` with HTTP 404.
- Validation errors return HTTP 400.
- Successful deposit returns HTTP 200 and `new_balance`.
- Deposit transaction format is currently:
  ```json
  {
    "type": "deposit",
    "amount": 50.0,
    "message": "Deposited 50.00"
  }
  ```

---

## FR-004: Withdraw Funds

### Description
The system shall allow money to be withdrawn from a valid account through the withdraw API.

### API Endpoint
`POST /api/accounts/<account_id>/withdraw`

### Request Body
```json
{
  "amount": "50"
}
```

### Expected Behaviour
- The system shall first validate that the account exists.
- The system shall validate the amount value.
- The system shall reject missing, blank, non-numeric, zero, and negative amounts.
- The system shall reject withdrawal if the amount exceeds the available balance.
- On success, the system shall subtract the amount from the balance.
- On success, the system shall append a withdraw transaction record.
- On success, the system shall return the updated balance.

### Current Business Rules
- Missing or blank amount returns `Amount is required.`
- Non-numeric amount returns `Amount must be a number.`
- Zero or negative amount returns `Amount must be greater than zero.`
- Insufficient balance returns `Insufficient funds.`
- Unknown account returns `Account was not found.` with HTTP 404.
- Validation and business-rule errors return HTTP 400.
- Successful withdrawal returns HTTP 200 and `new_balance`.
- Withdrawal transaction format is currently:
  ```json
  {
    "type": "withdraw",
    "amount": 50.0,
    "message": "Withdrew 50.00"
  }
  ```

---

## FR-005: Fund Transfer

### Description
The system shall allow money transfer from one valid account to another through the transfer API.

### API Endpoint
`POST /api/accounts/<account_id>/transfer`

### Request Body
```json
{
  "target_account_id": "A1002",
  "amount": "100"
}
```

### Expected Behaviour
- The system shall first validate that the source account exists.
- The system shall validate that target account ID is provided.
- The system shall validate the amount value.
- The system shall validate that the target account exists.
- The system shall prevent transfer to the same account.
- The system shall prevent transfer when funds are insufficient.
- On success, the system shall deduct the amount from the source account.
- On success, the system shall add the amount to the destination account.
- On success, the system shall create transfer-related transaction records.
- On success, the system shall return the new balance of the source account.

### Current Business Rules
- Missing target account returns `Target account is required.`
- Non-existent target account returns `Target account was not found.`
- Transfer to own account returns `You cannot transfer to your own account.`
- Missing or blank amount returns `Amount is required.`
- Non-numeric amount returns `Amount must be a number.`
- Zero or negative amount returns `Amount must be greater than zero.`
- Insufficient balance returns `Insufficient funds.`
- Unknown source account returns `Account was not found.` with HTTP 404.
- Validation and business-rule errors return HTTP 400.
- Successful transfer returns HTTP 200 and `new_balance`.

### Current Transaction Logging Behaviour
The current implementation logs transactions for both sender and receiver. this framework automation should validate what is actually returned by the application during execution.

---

## FR-006: Transaction History

### Description
The system shall return the stored transaction history for a valid account through the transactions API.

### API Endpoint
`GET /api/accounts/<account_id>/transactions`

### Expected Behaviour
- The system shall first validate that the account exists.
- The system shall return the account ID and a list of transaction records.
- The system shall return an empty list when no transactions exist.
- The system shall not fail when history is empty.

### Current Business Rules
- Unknown account returns `Account was not found.` with HTTP 404.
- Successful lookup returns HTTP 200.
- The response contains:
  - `success`
  - `account_id`
  - `transactions`
- Transaction list items currently include:
  - `type`
  - `amount`
  - `message`

### Important Limitation
Unlike earlier manual test designs, the current application transaction model does not include timestamps or permanent persistence.persistence. this framework should not assert timestamp fields unless the application is updated first.

---

## 4. UI Behaviour Requirements

Although the main automation baseline should be the API contract, the current browser flows are also relevant for this framework UI automation.

## UI-001: Login Page
- The login page shall provide username and password fields.
- The page shall call the login API through frontend JavaScript.
- On successful login, session details shall be stored in browser local storage.
- On successful login, the browser shall redirect to `/dashboard`.
- On failed login, an error message shall be shown.

## UI-002: Dashboard Page
- The dashboard shall require login information from local storage.
- The page shall call the balance API using the stored account ID.
- The page shall display username, full name, account ID, and current balance.

## UI-003: Deposit Page
- The page shall submit deposit requests through frontend JavaScript.
- On success, the page shall display a success message with new balance.
- On validation failure, the page shall display the returned error message.

## UI-004: Withdraw Page
- The page shall submit withdrawal requests through frontend JavaScript.
- On success, the page shall display a success message with new balance.
- On validation or business-rule failure, the page shall display the returned error message.

## UI-005: Transfer Page
- The page shall submit transfer requests through frontend JavaScript.
- On success, the page shall display a success message with new balance.
- On validation or business-rule failure, the page shall display the returned error message.

## UI-006: Transactions Page
- The page shall request transaction history using the stored account ID.
- If transactions exist, the page shall display them in a table.
- If no transactions exist, the page shall show `No transactions available yet.`

---

## 5. Non-Functional Requirements for this framework Baseline

These are practical QA baseline expectations for the current application.

## NFR-001: Reliability
- The application should return structured JSON responses for API operations.
- Invalid inputs should not crash the application.

## NFR-002: Usability
- Validation messages should be clear enough for manual and automated verification.
- UI flows should present visible feedback for both success and failure paths.

## NFR-003: Testability
- API routes should be callable independently from the UI.
- Business rules should remain reusable through the service layer.
- Application behaviour should be deterministic when a fresh app instance is created.

## NFR-004: Performance Baseline
- Standard API operations should respond within a reasonable local test execution time.
- No formal load or stress target is defined for this framework.

---

## 6. Assumptions
- this framework will test the application as the current system under test.
- Fresh app startup resets data because storage is in memory.
- Test execution may use seeded accounts `customer1` and `customer2`.
- API and UI automation may run against a local Flask instance.

---

## 7. Constraints
- No database persistence is available in the current implementation.
- No role-based authentication exists.
- No backend session or token model exists for API authorization.
- Current transaction records are lightweight and do not include timestamps.

---

## 8. QA Impact Notes for this framework

The earlier manual test design is a strong foundation, but the following items must be adjusted for this framework consistency:

- authentication now uses `username` and `password`, not account number and PIN
- the system under test is now web + API, not CLI
- account operations are API-driven
- transaction history currently returns `type`, `amount`, and `message`
- data persistence between restarts should not be expected

These alignment decisions should also be reflected in acceptance criteria, test scenarios, Postman checks, and pytest automation.

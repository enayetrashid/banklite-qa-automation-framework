# UI Test Scenarios

## UI-AUTH-001
Verify that a user can log in with valid credentials and reach the dashboard.

## UI-AUTH-002
Verify that an error message is shown when login is attempted with invalid credentials.

## UI-DASH-001
Verify that the dashboard displays username, full name, account ID, and balance after successful login.

## UI-DEP-001
Verify that a deposit can be submitted successfully through the UI.

## UI-DEP-002
Verify that a validation error is shown when deposit amount is blank.

## UI-WDR-001
Verify that a withdrawal can be submitted successfully through the UI.

## UI-WDR-002
Verify that an error is shown when withdrawal amount exceeds the available balance.

## UI-TRF-001
Verify that a transfer can be submitted successfully through the UI.

## UI-TRF-002
Verify that an error is shown when a user attempts to transfer funds to the same account.

## UI-HIS-001
Verify that the transaction history page shows the empty state for a fresh session.

## UI-HIS-002
Verify that the transaction history page displays transaction rows after a successful transaction.

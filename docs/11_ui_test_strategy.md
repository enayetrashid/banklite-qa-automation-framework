# UI Test Strategy

## 1. Purpose
This document defines the UI automation strategy for the BankLite application.

The UI layer complements API testing by validating visible user flows, page navigation, message handling, and frontend integration with backend APIs.

## 2. Objectives
The UI automation layer is intended to:
- validate critical browser-based user journeys
- confirm that frontend pages interact correctly with backend APIs
- verify success and error messages shown to users
- reduce regression risk in high-value flows

## 3. Scope
In scope:
- login flow
- dashboard account summary
- deposit flow
- withdrawal flow
- transfer flow
- transaction history display

Out of scope for this stage:
- cross-browser test matrix
- visual regression testing
- accessibility automation
- performance benchmarking

## 4. Tooling
- Playwright (Python)
- pytest
- Page Object Model (POM)

## 5. Execution Approach
UI tests focus on core user journeys and visible outcomes.
Detailed business-rule validation remains primarily covered by API automation because API tests are faster and easier to diagnose.

Recommended execution order:
1. smoke tests for login and dashboard
2. transaction-flow tests
3. targeted reruns after frontend or API changes

## 6. Evidence and Failure Handling
- screenshots are captured automatically on failure
- browser-visible messages should be checked as part of failure analysis
- defects should include reproduction steps and evidence

## 7. Risks and Constraints
- UI tests are more sensitive to selector changes than API tests
- the application stores test data in memory only
- transaction operations modify runtime state, so test isolation matters

## 8. Success Criteria
The Stage 3 UI layer is considered successful when:
- Playwright runs successfully against the local application
- login can be automated end to end
- at least one transaction journey passes through the browser
- page objects are reusable for future coverage growth

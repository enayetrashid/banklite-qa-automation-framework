# 🧭 BankLite QA Automation Framework

## 📌 Project Overview

This repository contains a comprehensive QA automation framework designed to validate a banking application through structured manual testing, API validation, and automation.

The project demonstrates a real-world quality assurance lifecycle, from requirements analysis to automated test execution.

---

## 🎯 Purpose

The goal of this project is to implement a **production-style QA framework** that includes:

* Requirements specification
* Acceptance criteria definition
* Test scenario design
* Test case management
* API testing using Postman
* API automation using pytest
* UI automation using Playwright

This repository emphasizes **test architecture, maintainability, and traceability**, rather than isolated test scripts.

---

## 🏦 System Under Test

The system under test is a demo banking application providing both API and web interfaces.

🔗 **Application Repository:**
https://github.com/enayetrashid/banklite-testable-app

### Core Features

* User authentication
* Balance enquiry
* Deposit funds
* Withdraw funds
* Fund transfer
* Transaction history

---

## 🧪 Testing Strategy Overview

This project follows a layered QA approach:

### 🔹 1. Test Design (Manual QA Foundation)

* Requirements specification
* Acceptance criteria
* Test scenarios
* Test cases
* Traceability matrix

---

### 🔹 2. API Testing (Postman)

* Endpoint validation using Postman
* Environment-based configuration
* Manual and repeatable execution

---

### 🔹 3. API Automation (pytest)

* Structured test framework
* Reusable API client layer
* Fixtures and assertions
* Scalable test design

---

### 🔹 4. UI Automation (Playwright)

* Page Object Model (POM)
* End-to-end user journey validation
* Browser-based interaction testing

---

## 🏗️ Architecture Overview

```
Browser (UI)
    ↓
Frontend JavaScript
    ↓
API Layer (Flask)
    ↓
Service Layer (Business Logic)
    ↓
In-Memory Storage
```

Testing layers:

```
Postman / pytest (API)
        ↓
API Layer
        ↓
Service Layer
        ↓
Data Layer
```

---

## 📂 Repository Structure

```bash
banklite-qa-automation-framework/
│
├── docs/                  # QA documentation (requirements, AC, scenarios, strategy)
├── api_testing/
│   └── postman/           # Postman collection, environment, and usage guide
├── automation/
│   ├── api/               # pytest API tests and shared fixtures
│   ├── api_client/        # reusable request wrappers
│   └── utils/             # config and reusable assertions
├── requirements.txt       # Python dependencies for pytest API testing
├── pytest.ini             # pytest configuration and markers
└── README.md
```

---

## 📊 Current Status

| Area                       | Status         |
| -------------------------- | -------------- |
| Requirements Definition    | ✅ Completed    |
| Acceptance Criteria        | ✅ Completed    |
| Test Scenarios             | ✅ Completed    |
| Test Cases                 | ✅ Completed    |
| Postman Collection         | ✅ Completed    |
| API Automation (pytest)    | ✅ Starter Added |
| UI Automation (Playwright) | 🚧 Planned     |

---

## 🧠 Key QA Principles Applied

* **Testability-first design**
* **Separation of concerns (API, UI, business logic)**
* **Alignment with actual system behaviour**
* **Traceability across all testing layers**
* **Reusable and scalable automation architecture**

---

## 🐞 Defect Management Approach

Defects are tracked using structured templates and managed via GitHub Issues.

Each defect includes:

* Steps to reproduce
* Expected vs actual results
* Severity and priority
* Supporting evidence (screenshots/logs)

---

## 📈 Reporting Approach

The framework supports:

* Execution summaries
* Automation progress tracking
* Release readiness reporting

---

## 🚀 How to Run (Postman)

1. Import collection:

   ```
   api_testing/postman/banklite_collection.json
   ```

2. Import environment:

   ```
   api_testing/postman/banklite_environment.json
   ```

3. Configure variables:

   * base_url
   * username
   * password

4. Run via Postman Runner

---

## 🚀 How to Run (pytest API Automation)

1. Start the BankLite application locally.
2. Create and activate a virtual environment.
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the starter API suite:

   ```
   pytest automation/api -m api
   ```

The current pytest starter layer includes:
- authentication tests
- balance tests
- reusable API client wrappers
- shared fixtures and assertion helpers

---

## 👨‍💻 Author

**Enayet Rashid**

🔗 GitHub: https://github.com/enayetrashid

---

## 🌱 Project Vision

This project represents a structured journey toward building a **realistic, end-to-end QA automation framework**, combining:

* Manual QA foundations
* API validation and automation
* UI automation
* Test architecture design

The objective is to simulate how quality assurance is implemented in real-world engineering environments.

---

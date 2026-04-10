# Postman Collection for BankLite API Testing

This collection supports API testing for the **BankLite Flask application**.

---

## 🔍 API Coverage

The API routes in the application are:

* `POST /api/login`
* `GET /api/accounts/<account_id>/balance`
* `POST /api/accounts/<account_id>/deposit`
* `POST /api/accounts/<account_id>/withdraw`
* `POST /api/accounts/<account_id>/transfer`
* `GET /api/accounts/<account_id>/transactions`

---

## 🔐 Authentication Model

This API does **not** use:

* Bearer tokens
* Authorization headers
* Session-based authentication

### Login Response Includes:

* `success`
* `username`
* `full_name`
* `account_id`

### Important Notes:

* No token is returned
* No authentication header is required for subsequent requests
* The account is identified using the URL path parameter (e.g. `A1001`)

---

## 🧾 Correct Login Payload

```json
{
  "username": "customer1",
  "password": "Pass123!"
}
```

### Demo Users

* `customer1 / Pass123!`
* `customer2 / Pass123!`

---

## 🚀 How to Run Locally

1. Clone the application repository
2. Create and activate a virtual environment
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Start the Flask application:

   ```
   python run.py
   ```
5. Confirm the app is running:

   ```
   http://127.0.0.1:5000
   ```

---

## 📬 How to Use This Collection in Postman

1. Import:

   * `banklite_collection.json`
   * `banklite_environment.json`

2. Select the environment:

   ```
   BankLite Local Environment
   ```

3. Run:

   * **Login - valid credentials**

4. Confirm response includes:

   * `account_id`

5. Execute remaining requests:

   * Balance
   * Deposit
   * Withdrawal
   * Transfer
   * Transaction History

---

## 🔁 Recommended Execution Order

Since the application uses in-memory storage:

1. Login - valid credentials
2. Get balance
3. Deposit
4. Withdraw
5. Transfer
6. Get transactions

---

## ⚠️ Test State Behaviour

* Data is stored **in memory only**

* Restarting the application resets:

  * balances
  * transactions

* Deposit / Withdraw / Transfer operations **modify runtime state**

---

## 📡 Status Code Behaviour

* Login validation failures → `401`
* Invalid credentials → `401`
* Account not found → `404`
* Validation errors → `400`
* Successful requests → `200`

---

## 🔧 Improvements from Initial Version

Earlier drafts used incorrect fields such as:

* `account_number`
* `pin`

These files now use the fields required by the application:

* `username`
* `password`
* `account_id`
* `target_account_id`
* `amount`

---

## ✅ Best Practices

Before running the full collection:

* Verify Flask app is running
* Confirm correct base URL
* Ensure environment is selected
* Run login request first
* Confirm `account_id` is captured

---

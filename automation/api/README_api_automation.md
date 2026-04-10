# API Automation -Stage 2 Starter

This folder contains the initial pytest-based API automation layer for the BankLite application.

## Included in this starter stage
- shared configuration
- reusable API client wrappers
- pytest fixtures
- authentication tests
- balance tests

## How to run
1. Start the BankLite Flask application locally.
2. Create a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the API tests:
   ```bash
   pytest automation/api -m api
   ```

## Notes
- The default base URL is `http://127.0.0.1:5000`.
- Values can be overridden with environment variables such as `BANKLITE_BASE_URL`.

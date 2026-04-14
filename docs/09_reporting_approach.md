# Reporting Approach

## 1. Purpose
This document defines how test results, evidence, and execution outcomes should be recorded in this framework.

## 2. Reporting Objectives
The reporting approach should:
- provide a clear summary of what was executed
- show pass and fail status by test area
- reference evidence and logs for investigation
- support release-readiness assessment

## 3. Report Types
This framework uses the following reporting artifacts:
- pytest console output
- persistent pytest execution log
- API request and response evidence files
- execution summary report
- bug reports and issue records

## 4. Evidence Sources
Evidence may come from:
- JSON request and response logs stored in `automation/evidence/logs/`
- screenshots stored in `automation/evidence/screenshots/`
- execution summaries under `reports/`

## 5. Minimum Reporting Standard
Each execution cycle should capture:
- date and environment used
- scope executed
- overall pass or fail counts
- notable risks or blockers
- links or paths to supporting evidence

## 6. Recommended Workflow
1. Run the selected pytest suite
2. Review the pytest console and file log
3. Inspect generated evidence JSON files for failed API tests
4. Summarise findings in `reports/execution_summary.md`
5. Raise defects for confirmed issues and attach supporting evidence

## 7. Optional Enhancement
HTML reports can be generated with:
```bash
pytest --html=reports/api_test_report.html --self-contained-html
```

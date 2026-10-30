# Lab 5 Report: Static Code Analysis and Code Quality Improvement

**Student:** PES1UG24AM271  
**Course:** Software Engineering Lab  
**Project:** Expense Tracker  
**Tools:** Pylint, Bandit, and Flake8

## 1. Objective

The objective of this lab was to inspect the assigned Python expense-tracker program using static analysis tools, identify code-quality, security, and formatting problems, document the findings, fix the issues, and verify the changes by running the tools again.

The lab required at least four issues to be fixed, all Bandit findings to be handled, a Pylint score above 9.5, and all Flake8 formatting findings to be addressed.

## 2. Tools Used

| Tool | Purpose |
|---|---|
| Pylint | Checks Python code quality, naming conventions, documentation, and maintainability. |
| Bandit | Identifies common security problems and unsafe coding patterns in Python. |
| Flake8 | Checks Python style and formatting, including whitespace and line length. |

## 3. Initial Analysis

The original program was stored as the baseline version. The tools were run against that baseline and their outputs were saved in `reports/before/`.

| Tool | Initial result | Findings |
|---|---:|---|
| Pylint | 5.27/10 | Naming, missing documentation, exception-handling, and other code-quality warnings. |
| Bandit | 3 findings | 2 medium-severity and 1 high-severity finding in the captured baseline report. |
| Flake8 | 4 violations | Whitespace before a colon, blank-line spacing, inline-comment spacing, and line length. |

## 4. Issues Identified and Fixes Applied

The following issues were documented in `issues.md` and addressed in the updated source:

| Issue | Tool/category | Fix applied |
|---|---|---|
| Hardcoded sync password | Bandit / security | Read the credential from an environment variable and compare it using a digest comparison. |
| Insecure temporary-file handling | Bandit / security | Use a safer temporary-file API rather than `tempfile.mktemp()`. |
| Shell command execution | Bandit / security | Remove the unused shell-based file-opening helper. |
| Broad exception handling | Pylint / code quality | Handle the empty-expense case explicitly rather than catching every exception. |
| Non-snake-case names | Pylint / code quality | Rename functions and variables to follow Python naming conventions. |
| Budget validation | Robustness | Reject negative budget values. |
| Empty largest-expense result | Robustness | Check for an empty result before accessing the largest expense. |
| Import-time execution | Maintainability | Place demonstration execution behind a `main()` entry-point guard. |
| Formatting and documentation | Flake8 / Pylint | Correct formatting and add appropriate documentation. |

## 5. Fix and Verification Process

The original source was retained in `baseline/`. Intermediate source versions were retained in `stages/` to show the progression of the fixes. The final source is `expense_tracker.py`.

After applying the changes, the program was executed and the static analysis tools were run again. The generated outputs were saved in `reports/after/`.

## 6. Final Analysis Results

| Tool | Before | After | Outcome |
|---|---:|---:|---|
| Pylint | 5.27/10 | 10.00/10 | Final score exceeds the required 9.5. |
| Bandit | 3 findings | 0 findings | No issues identified in the final report. |
| Flake8 | 4 violations | 0 violations | Final report is empty, indicating no reported violations. |

## 7. Git Commit Evidence

The Lab 5 work was committed separately on the repository's `main` branch:

1. `8321c8c` — Add Lab 5 expense tracker baseline
2. `26bf8ee` — Fix expense tracker security issues
3. `5cc7c1c` — Improve expense tracker code quality
4. `db67061` — Resolve remaining static analysis findings

The three commits after the baseline record the successive fix stages.

## 8. Conclusion

Static analysis helped identify security weaknesses, code-quality problems, and formatting inconsistencies in the original expense tracker. The issues were documented and addressed in the updated source. The final verification reports show a Pylint score of 10.00/10, no Bandit findings, and no Flake8 violations. The exercise demonstrates the value of using multiple static analysis tools together and rerunning them after code changes.

## 9. Submission Contents

The Lab 5 submission includes:

- `expense_tracker.py` — updated Python source
- `baseline/` — original source used for the before analysis
- `stages/` — intermediate source versions
- `reports/before/` — initial Pylint, Bandit, and Flake8 reports
- `reports/after/` — final Pylint, Bandit, and Flake8 reports
- `issues.md` — issue register and fix approaches
- `reflection.md` — answers to the lab reflection questions
- `report.md` — this lab report
- `README.md` and `generate_reports.sh` — project instructions and report-generation script

# Lab 5: Static Code Analysis — Personal Expense Tracker

This repository contains the cleaned expense tracker and the Lab 5 documentation.

## Setup and run

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install pylint bandit flake8
python expense_tracker.py
```

The tracker uses only the Python standard library at runtime.

## Generate authentic before reports

Run these commands **before** replacing the original file, or use the original file from your assignment ZIP:

```bash
python -m pylint expense_tracker.py > reports/before/pylint_report.txt 2>&1
python -m bandit -r expense_tracker.py > reports/before/bandit_report.txt 2>&1
python -m flake8 expense_tracker.py > reports/before/flake8_report.txt 2>&1
```

The supplied `reports/before/` files are manual finding notes, not raw tool output, because the preparation environment could not access the package index. Do not present them as actual tool-generated output.

## Generate after reports

```bash
python -m pylint expense_tracker.py > reports/after/pylint_report.txt 2>&1
python -m bandit -r expense_tracker.py > reports/after/bandit_report.txt 2>&1
python -m flake8 expense_tracker.py > reports/after/flake8_report.txt 2>&1
```

If Pylint is below 9.5 or either tool reports remaining findings, inspect the report, fix the issue, and rerun the command. Exact results can vary by tool version.

## Deliverables

- `expense_tracker.py` — updated source.
- `issues.md` — issue register and fix approaches.
- `reflection.md` — reflection answers.
- `reports/before/` and `reports/after/` — clearly labelled analysis notes / report destinations.

## Security note

Set `BANK_SYNC_PASSWORD` in the environment if the password check should accept a configured password. No password is stored in the source file. The report directory can be changed with `EXPENSE_REPORT_DIR`.

#!/bin/bash
set -u

mkdir -p reports/before reports/after

# Capture genuine tool output. `|| true` ensures all reports are written even
# when a tool returns non-zero because it found findings or lint errors.
python -m pylint baseline/expense_tracker.py > reports/before/pylint_report.txt 2>&1 || true
python -m bandit -r baseline/expense_tracker.py > reports/before/bandit_report.txt 2>&1 || true
python -m flake8 baseline/expense_tracker.py > reports/before/flake8_report.txt 2>&1 || true

python -m pylint expense_tracker.py > reports/after/pylint_report.txt 2>&1 || true
python -m bandit -r expense_tracker.py > reports/after/bandit_report.txt 2>&1 || true
python -m flake8 expense_tracker.py > reports/after/flake8_report.txt 2>&1 || true

echo "Reports written to reports/before/ and reports/after/."
echo "Review reports/after/pylint_report.txt for a score above 9.5."
echo "Review Bandit output for remaining findings; Flake8 should be empty."

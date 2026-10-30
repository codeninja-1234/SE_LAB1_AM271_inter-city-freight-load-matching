# Lab 6 — Code and Branch Coverage (SRN suffix: 32)

Application under test: `weather_alert.py` (original application logic retained).

## Code coverage

```bash
python -m coverage erase
python -m coverage run --source=weather_alert -m pytest -q CodeCoverageTest_32_application.py
python -m coverage report -m
```

Result: **4 tests passed; 92% statement/line coverage**.

Screenshot: `screenshots/code_coverage.png`

## Branch coverage

```bash
python -m coverage erase
python -m coverage run --branch --source=weather_alert -m pytest -q BranchCoverageTest_32_application.py
python -m coverage report -m
```

Result: **18 tests passed; 100% branch-aware coverage (28 branches, 0 partial)**.

Screenshot: `screenshots/branch_coverage.png`

The handout asks for at least 90% code coverage and at least 90% branch coverage. The code-coverage suite reaches 92%; the branch-coverage suite reaches 100%.

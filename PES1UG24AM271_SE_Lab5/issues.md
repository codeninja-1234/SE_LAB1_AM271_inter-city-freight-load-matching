# Static Analysis Issue Register

The line numbers below refer to the **original** `expense_tracker.py` supplied for Lab 5.

| Issue | Type / tool | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Hardcoded sync password | Security — Bandit | 5 | A credential-like value is stored directly in source code and could be exposed in version control. | Read `BANK_SYNC_PASSWORD` from an environment variable and return `False` if it is not configured. Use `hmac.compare_digest` for comparison. |
| Insecure temporary filename | Security — Bandit | 34 | `tempfile.mktemp()` returns a path without securely creating the file, creating a race condition. | Use `NamedTemporaryFile(delete=False)` to create the file safely. |
| Shell command execution | Security — Bandit | 39 | `os.system("xdg-open " + path)` passes a path through a shell and can allow command injection. | Removed the unused shell-opening helper; the demo does not need it. |
| Overly broad exception | Quality — Pylint | 29–30 | `except Exception` hides unrelated programming errors. | Check whether `expenses` is empty and return `None` explicitly. |
| Non-PEP 8 names | Quality — Pylint | Multiple | Function names use camelCase instead of Python's conventional snake_case. | Renamed functions to `add_expense`, `total_by_category`, etc. |
| Global budget validation | Quality / robustness | 22–24 | Any value, including a negative budget, could be set. | Validate the budget and raise `ValueError` for negative values. |
| Unsafe assumption about largest expense | Robustness | 52 | The demo immediately indexes the result of `biggestExpense()` and would fail if no expense exists. | Store the result and check for `None` before reading its note. |
| Missing entry-point guard | Maintainability — Pylint | Last line | Importing the module immediately runs the demo, making reuse and testing harder. | Run `main()` only under `if __name__ == "__main__":`. |
| Inconsistent formatting and documentation | Style — Flake8 / Pylint | Multiple | Spacing, naming, and missing docstrings reduce readability and consistency. | Reformatted the source and added module/function docstrings. |

## Verification note

The execution environment used to prepare these files was offline and did not have Pylint, Bandit, or Flake8 installed. The `reports/before/` and `reports/after/` files therefore identify themselves as analysis notes rather than pretending to be raw tool output. Run the commands in `README.md` on your machine to generate authentic tool reports before submission.

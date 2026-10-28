# Static Analysis Issue Register

Line numbers are approximate and refer to the original file in `baseline/expense_tracker.py`; exact line numbers may vary by tool version.

| Issue | Tool / category | Description | Fix approach |
|---|---|---|---|
| Hardcoded sync password | Bandit/security | A credential-like value in source could be exposed through version control. | Read `BANK_SYNC_PASSWORD` from the environment, reject an unset secret, and use `hmac.compare_digest`. |
| Insecure temporary path | Bandit/security | `tempfile.mktemp()` creates a path without securely creating the file, introducing a race condition. | Use `NamedTemporaryFile` with `delete=False` in the configured report directory. |
| Shell command execution | Bandit/security | Passing a path to `os.system()` can allow shell injection. | Remove the shell-based file-opening helper because it is unused by the tracker. |
| Broad exception handler | Pylint/code quality | Catching `Exception` can conceal unrelated programming errors. | Check whether the expense list is empty and return `None` explicitly. |
| Non-snake-case function names | Pylint/code quality | camelCase names are inconsistent with common Python conventions. | Rename functions to snake_case. |
| Budget validation | Robustness | A negative budget is not meaningful for this tracker. | Raise `ValueError` when a negative budget is provided. |
| Empty largest-expense result | Robustness | Indexing the largest expense without checking for an empty result can raise an error. | Check for `None` before accessing the result. |
| Import-time execution | Maintainability | Running the demo on import makes reuse and testing harder. | Protect the call to `main()` with an entry-point guard. |
| Formatting and documentation | Flake8/Pylint | Inconsistent formatting and missing documentation reduce readability. | Format the code consistently and add module/function docstrings. |

## Evidence
Use `bash generate_reports.sh` to produce the before/after tool outputs. The before reports must show the baseline file; the after reports must show `expense_tracker.py`. Review the actual output before submission rather than assuming all checks pass.

# Lab 5 Reflection — Static Code Analysis

### 1. What is static code analysis, and why is it useful?

I think static code analysis is useful because it examines source code without running the program. It can reveal possible bugs, security risks, and style problems early, making the code easier to maintain and safer to work with.

### 2. What differences did you observe between Pylint, Bandit, and Flake8?

I think the tools complement one another. Pylint checks broader code quality and maintainability, including naming and exception handling. Bandit focuses on common security risks such as hardcoded credentials and unsafe functions. Flake8 checks style and formatting rules such as whitespace and line length.

### 3. Which issues did you fix, and how did the fixes improve the program?

I moved the sync password out of the source file and into an environment variable, used a safer temporary-file API, and removed shell-based file opening. I also removed broad exception handling, improved function naming and documentation, validated the budget, handled an empty expense list, and added an entry-point guard. These changes reduce security risks and make the program clearer and more reliable.

### 4. What did you learn about static analysis tools?

I think static analysis tools are most useful when I understand each finding and decide how to address it rather than changing code blindly. After making a fix, I should rerun the tools and inspect the output. Static analysis supports testing and code review, but it cannot prove that a program is completely secure or free of bugs.

### Verification
After running `bash generate_reports.sh`, compare the before and after reports. Record the actual Pylint score and verify the remaining Bandit and Flake8 findings before claiming the checks passed.

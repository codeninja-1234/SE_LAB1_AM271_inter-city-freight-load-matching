# Lab 5 Reflection — Static Code Analysis

### 1. What is static code analysis, and why is it useful?

I think static code analysis is useful because it checks source code without needing to execute the program. It can point out coding mistakes, security risks, and style problems early, which makes the program easier to maintain and safer to use.

### 2. What differences did you observe between Pylint, Bandit, and Flake8?

I think each tool focuses on a different area. Pylint reviews general code quality and can identify broad exception handling, naming problems, and maintainability issues. Bandit focuses on common security risks, such as hardcoded credentials and unsafe shell or temporary-file operations. Flake8 focuses mainly on Python style and formatting rules.

### 3. Which issues did you fix, and how did the fixes improve the program?

I replaced the hardcoded sync password with an environment variable, removed shell-based file opening, replaced insecure temporary-file creation with `NamedTemporaryFile`, and removed the broad exception handler. I also improved naming, added docstrings, validated negative budgets, and guarded the program's entry point. These changes make the code clearer and reduce avoidable security and runtime risks.

### 4. What did you learn about static analysis tools?

I think static analysis tools are most useful when their findings are reviewed rather than fixed blindly. A warning should be understood in context, corrected, and then checked again. The tools complement testing and code review, but they do not prove that a program is completely secure or bug-free.

**Execution note:** The preparation environment was offline, so the three analysis tools could not be installed and run here. I need to run the commands in the README locally to replace the clearly labelled report notes with actual before-and-after output.

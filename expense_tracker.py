"""A small command-line personal expense tracker."""

from __future__ import annotations

import hmac
import os
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any

DEFAULT_MONTHLY_BUDGET = 20_000.0
REPORT_DIR = Path(
    os.getenv("EXPENSE_REPORT_DIR", str(Path.home() / ".expense_reports"))
)
expenses: list[dict[str, Any]] = []
budget_state = {"monthly": DEFAULT_MONTHLY_BUDGET}


def add_expense(amount: float, category: str = "Misc", note: str = "") -> bool:
    """Record an expense if its amount is positive."""
    if amount <= 0:
        print("Ignoring invalid amount", amount)
        return False

    expenses.append(
        {
            "amount": amount,
            "category": category,
            "note": note,
            "time": datetime.now().isoformat(timespec="seconds"),
        }
    )
    return True


def total_by_category() -> dict[str, float]:
    """Return total spending grouped by category."""
    totals: dict[str, float] = {}
    for expense in expenses:
        category = str(expense["category"])
        totals[category] = totals.get(category, 0.0) + float(expense["amount"])
    return totals


def set_budget(new_budget: float) -> None:
    """Update the monthly budget after validating it."""
    if new_budget < 0:
        raise ValueError("Budget cannot be negative.")

    budget_state["monthly"] = new_budget

def remaining_budget() -> float:
    """Return the budget left after recorded expenses."""
    spent = sum(float(expense["amount"]) for expense in expenses)
    return budget_state["monthly"] - spent


def biggest_expense() -> dict[str, Any] | None:
    """Return the largest expense, or None when there are no expenses."""
    if not expenses:
        return None
    return max(expenses, key=lambda expense: float(expense["amount"]))


def print_ledger() -> None:
    """Print expenses in the order they were recorded."""
    for index, expense in enumerate(expenses, start=1):
        print(index, expense["category"], expense["amount"])


def check_sync_password(password: str) -> bool:
    """Compare a supplied password with the environment-configured secret."""
    expected_password = os.getenv("BANK_SYNC_PASSWORD")
    if not expected_password:
        return False
    return hmac.compare_digest(password, expected_password)


def export_report() -> Path:
    """Create a safely allocated empty report file and return its path."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=".txt",
        prefix="expense-report-",
        dir=REPORT_DIR,
        delete=False,
    ) as report_file:
        return Path(report_file.name)


def main() -> None:
    """Run a short demonstration of the expense tracker."""
    expenses.clear()
    print("Biggest expense before any entries:", biggest_expense())
    add_expense(450, "Food", "Lunch with team")
    add_expense(1200, "Travel", "Cab to airport")
    add_expense(-50, "Food")
    add_expense(300, "Food", "Groceries")
    add_expense(999, "Bills", "Internet")
    set_budget(5000)
    print_ledger()
    print("Totals:", total_by_category())
    print("Remaining budget:", remaining_budget())
    largest = biggest_expense()
    print("Biggest expense:", largest["note"] if largest else None)
    print("Sync password accepted:", check_sync_password("guess"))
    print(
        "Summary:",
        len(expenses),
        "expenses recorded against a budget of",
        budget_state["monthly"],
    )


if __name__ == "__main__":
    main()

import json

import pytest

from expense_tracker.operations import add_expense, delete_expense, total_expenses, validate_amount
from expense_tracker.storage import load_expenses, save_expenses


def test_add_and_total():
    expenses = []
    add_expense(expenses, "Lunch", "150", "Food", "2026-01-01")
    add_expense(expenses, "Bus", 40, "Travel", "2026-01-02")
    assert len(expenses) == 2
    assert total_expenses(expenses) == 190


def test_delete_expense():
    expenses = [{"id": 1, "description": "Lunch", "amount": 150, "category": "Food", "date": "2026-01-01"}]
    assert delete_expense(expenses, 1)["id"] == 1
    assert expenses == []


def test_delete_missing_expense():
    assert delete_expense([], 99) is None


@pytest.mark.parametrize("amount", [0, -1, "not-a-number"])
def test_invalid_amount(amount):
    with pytest.raises(ValueError):
        validate_amount(amount)


def test_empty_total():
    assert total_expenses([]) == 0


def test_json_storage(tmp_path):
    path = tmp_path / "expenses.json"
    expenses = [{"id": 1, "description": "Tea", "amount": 20, "category": "Food", "date": "2026-01-01"}]
    save_expenses(path, expenses)
    assert load_expenses(path) == expenses


def test_corrupt_json(tmp_path):
    path = tmp_path / "expenses.json"
    path.write_text("{", encoding="utf-8")
    with pytest.raises(Exception):
        load_expenses(path)

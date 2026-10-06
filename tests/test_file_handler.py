import os
import json
import tempfile
from finance_tracker.file_handler import save_expenses, load_expenses


def test_save_and_load_expenses():
    expenses = [
        {
            "date": "2026-10-06",
            "amount": 500,
            "category": "Food",
            "description": "Lunch"
        }
    ]

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "expenses.json")

        save_expenses(expenses, file_path)
        loaded = load_expenses(file_path)

        assert loaded == expenses


def test_load_missing_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "missing.json")

        loaded = load_expenses(file_path)

        assert loaded == []

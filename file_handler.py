# File handling for Personal Finance Tracker

import json
import csv
import os

class FileHandler:

    @staticmethod
    def save_expenses(expenses, filename="data/expenses.json"):
        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            data = [expense.to_dict() for expense in expenses]

            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            return True

        except (OSError, TypeError) as error:
            print(f"Error saving expenses: {error}")
            return False

    @staticmethod
    def load_expenses(filename="data/expenses.json"):
        try:
            if not os.path.exists(filename):
                return []

            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)

        except (OSError, json.JSONDecodeError) as error:
            print(f"Error loading expenses: {error}")
            return []

    @staticmethod
    def export_to_csv(expenses, filename="exports/expenses.csv"):
        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["date", "amount", "category", "description"]
                )

                writer.writeheader()

                for expense in expenses:
                    writer.writerow(expense.to_dict())

            return True

        except OSError as error:
            print(f"Error exporting CSV: {error}")
            return False

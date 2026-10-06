# Utility functions for Personal Finance Tracker

from datetime import datetime


def validate_amount(amount):
    try:
        amount = float(amount)

        if amount > 0:
            return amount

        print("Amount must be greater than 0.")
        return None

    except ValueError:
        print("Please enter a valid number.")
        return None


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:
        print("Invalid date. Use YYYY-MM-DD format.")
        return False


def validate_category(category):
    categories = [
        "Food",
        "Transport",
        "Entertainment",
        "Bills",
        "Shopping",
        "Health",
        "Education",
        "Other"
    ]

    if category in categories:
        return True

    print("Invalid category.")
    print("Choose from:", ", ".join(categories))
    return False


def format_currency(amount):
    return f"₹{amount:.2f}"

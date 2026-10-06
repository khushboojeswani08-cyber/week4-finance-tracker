# Reports module for Personal Finance Tracker

from collections import defaultdict


class Reports:

    @staticmethod
    def monthly_total(expenses, month):
        total = 0

        for expense in expenses:
            if expense.date.startswith(month):
                total += expense.amount

        return total

    @staticmethod
    def category_breakdown(expenses):
        breakdown = defaultdict(float)

        for expense in expenses:
            breakdown[expense.category] += expense.amount

        return dict(breakdown)

    @staticmethod
    def highest_expense(expenses):
        if not expenses:
            return None

        return max(expenses, key=lambda expense: expense.amount)

    @staticmethod
    def lowest_expense(expenses):
        if not expenses:
            return None

        return min(expenses, key=lambda expense: expense.amount)

    @staticmethod
    def average_expense(expenses):
        if not expenses:
            return 0

        return sum(expense.amount for expense in expenses) / len(expenses)

    @staticmethod
    def show_report(expenses):
        print("\n" + "=" * 50)
        print("             EXPENSE REPORT")
        print("=" * 50)

        if not expenses:
            print("No expenses available.")
            return

        total = sum(expense.amount for expense in expenses)
        average = Reports.average_expense(expenses)
        highest = Reports.highest_expense(expenses)
        lowest = Reports.lowest_expense(expenses)

        print(f"Total Expenses: ₹{total:.2f}")
        print(f"Average Expense: ₹{average:.2f}")

        if highest:
            print(f"Highest Expense: ₹{highest.amount:.2f}")

        if lowest:
            print(f"Lowest Expense: ₹{lowest.amount:.2f}")

        print("\nCategory Breakdown:")

        breakdown = Reports.category_breakdown(expenses)

        for category, amount in breakdown.items():
            print(f"- {category}: ₹{amount:.2f}")

        print("=" * 50)

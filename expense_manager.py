# Expense Manager for Personal Finance Tracker

from .expense import Expense


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, category, description):
        expense = Expense(date, amount, category, description)
        self.expenses.append(expense)
        return True

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            return True
        return False

    def get_all_expenses(self):
        return self.expenses

    def search_expenses(self, keyword):
        keyword = keyword.lower()

        return [
            expense for expense in self.expenses
            if keyword in expense.category.lower()
            or keyword in expense.description.lower()
        ]

    def get_total(self):
        return sum(expense.amount for expense in self.expenses)

    def get_category_total(self, category):
        return sum(
            expense.amount
            for expense in self.expenses
            if expense.category.lower() == category.lower()
        )

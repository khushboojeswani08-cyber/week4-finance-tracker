import unittest
from finance_tracker.expense import Expense


class TestExpense(unittest.TestCase):

    def test_expense_creation(self):
        expense = Expense(
            "2026-10-06",
            500,
            "Food",
            "Dinner"
        )

        self.assertEqual(expense.date, "2026-10-06")
        self.assertEqual(expense.amount, 500)
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.description, "Dinner")

    def test_to_dict(self):
        expense = Expense(
            "2026-10-06",
            250,
            "Transport",
            "Bus"
        )

        data = expense.to_dict()

        self.assertEqual(data["amount"], 250)
        self.assertEqual(data["category"], "Transport")


if __name__ == "__main__":
    unittest.main()

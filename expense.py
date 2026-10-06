# Expense class for Personal Finance Tracker

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

    def __str__(self):
        return (
            f"{self.date} | ₹{self.amount:.2f} | "
            f"{self.category} | {self.description}"
        )

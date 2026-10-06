# Personal Finance Tracker
# Week 4 - Python Internship

class FinanceTracker:
    def __init__(self):
        self.expenses = []

    def run(self):
        print("=" * 50)
        print("        PERSONAL FINANCE TRACKER")
        print("=" * 50)

        while True:
            print("\n" + "=" * 40)
            print("             MAIN MENU")
            print("=" * 40)
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("6. Set/Update Budget")
            print("7. Export Data to CSV")
            print("8. View Statistics")
            print("9. Backup/Restore Data")
            print("0. Exit")

            choice = input("\nEnter your choice (0-9): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.search_expenses()
            elif choice == "4":
                self.generate_monthly_report()
            elif choice == "5":
                self.view_category_breakdown()
            elif choice == "6":
                self.set_budget()
            elif choice == "7":
                self.export_data()
            elif choice == "8":
                self.view_statistics()
            elif choice == "9":
                self.backup_restore()
            elif choice == "0":
                print("\nThank you for using Personal Finance Tracker!")
                break
            else:
                print("Invalid choice! Please enter 0-9.")

    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        print("Expense feature will be added.")

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        print("No expenses to display yet.")

    def search_expenses(self):
        print("\n--- SEARCH EXPENSES ---")
        print("Search feature will be added.")

    def generate_monthly_report(self):
        print("\n--- MONTHLY REPORT ---")
        print("Monthly report will be generated.")

    def view_category_breakdown(self):
        print("\n--- CATEGORY BREAKDOWN ---")
        print("Category breakdown will be displayed.")

    def set_budget(self):
        print("\n--- SET/UPDATE BUDGET ---")
        print("Budget feature will be added.")

    def export_data(self):
        print("\n--- EXPORT DATA ---")
        print("Export feature will be added.")

    def view_statistics(self):
        print("\n--- STATISTICS ---")
        print("Statistics will be displayed.")

    def backup_restore(self):
        print("\n--- BACKUP/RESTORE ---")
        print("Backup and restore feature will be added.")


def main():
    tracker = FinanceTracker()
    tracker.run()


if __name__ == "__main__":
    main()

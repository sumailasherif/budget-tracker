class Transaction:
    def __init__(self, date, amount, category, description, ttype):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.ttype = ttype  # 'income' or 'expense.'

    # String representation of each transaction
    def __str__(self):
        return f"{self.date} | {self.ttype.upper()} | {self.category} | KSH{self.amount} | {self.description}"


# Automatically assigns transaction type as income
class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "income")


# Automatically assigns transaction type as expense
class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "expense")


class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self):
        print("\n---Record New Income---")
        date = input("Date (YYYY-MM-DD): ")
        amount = self.get_amount()
        category = input("Category: ")
        description = input("Enter a short Description: ")

        income_entry = Income(date, amount, category, description)
        self.transactions.append(income_entry)
        print("Income recorded successfully!")

    def add_expense(self):
        print("\n--- Record New Expense ---")
        date = input("Date (YYYY-MM-DD): ")
        amount = self.get_amount()
        category = input("Category: ")
        description = input("Enter a short Description: ")

        exp = Expense(date, amount, category, description)
        self.transactions.append(exp)
        print("Expense recorded successfully!")

    def list_transactions(self):
        print("\n--- All Transactions ---")
        if len(self.transactions) == 0:
            print("No transactions added yet.")
            return

        # Looping through each transaction to calculate totals
        for t in self.transactions:
            print(t)

    def filter_transactions(self):
        print("\n--- Filter Transactions --- :")
        print("1) By Type (income/expense)")
        print("2) Category")
        print("3) Month (YYYY-MM)")
        choice = input("Choose option: ")

        if choice == "1":
            ttype = input("Enter type (income/expense): ").strip().lower()
            for t in self.transactions:
                if t.ttype == ttype:
                    print(t)

        elif choice == "2":
            category = input("Enter category name: ").lower().strip()
            for t in self.transactions:
                if t.category.lower() == category.lower():
                    print(t)

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            for t in self.transactions:
                if t.date.startswith(month):
                    print(t)

        else:
            print("Invalid selection. Please choose a valid option.")

    def show_summary(self):
        print("\n--- Budget Summary ---")
        total_income = 0
        total_expense = 0
        category_totals = {}

        for t in self.transactions:
            if t.ttype == "income":
                total_income += t.amount
            else:
                total_expense += t.amount

            if t.category not in category_totals:
                category_totals[t.category] = 0
            category_totals[t.category] += t.amount

        balance = total_income - total_expense

        print(f"Total Income: KSH{total_income}")
        print(f"Total Expense: KSH{total_expense}")
        print(f"Balance: KSH{balance}")

        print("\nCategory Totals:")
        for cat, amount in category_totals.items():
            print(f"{cat}: KSH{amount}")

    # Ensures the user enters a valid positive number
    def get_amount(self):
        while True:
            amount = input("Enter amount: ")
            try:
                amount = float(amount)
                if amount > 0:
                    return amount
                else:
                    print("Please enter a positive number.")
            except:
                print("Invalid input. Please enter a valid number.")
def main():
    tracker = BudgetTracker()

    while True:
        print("\n--- Budget Tracker Menu ---")
        print("1) Add Income")
        print("2) Add Expense")
        print("3) List All Transactions")
        print("4) Filter Transactions")
        print("5) Show Summary")
        print("6) Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            tracker.add_income()
        elif choice == "2":
            tracker.add_expense()
        elif choice == "3":
            tracker.list_transactions()
        elif choice == "4":
            tracker.filter_transactions()
        elif choice == "5":
            tracker.show_summary()
        elif choice == "6":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()
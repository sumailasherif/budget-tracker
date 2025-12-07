class Transaction:
    def __init__(self, date, amount, category, description, ttype):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.ttype = ttype   # 'income' or 'expense.'

    def __str__(self):
        return f"{self.date} | {self.type.upper()} | {self.category} | KSH{self.amount} | {self.description}"


class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "income")



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
        self.transactions.append( income_entry)
        print("Income recorded  successfully!")

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
                if t.type == ttype:
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
        print("\n--- Budget  Summary ---")
        total_income = 0
        total_expense = 0
        category_totals = {}

for t in self.transactions:
            if t.type == "income":
                total_income += t.amount
            else:
                total_expense += t.amount


            if t.category not in category_totals:
                category_totals[t.category] = 0
            category_totals[t.category] += t.amount

        balance = total_income - total_expense

        print(f"Total Income: GHC{total_income}")
        print(f"Total Expense: GHC{total_expense}")
        print(f"Balance: GHC{balance}")

        print("\nCategory Totals:")
        for cat, amount in category_totals.items():
            print(f"{cat}: GHC{amount}")


    



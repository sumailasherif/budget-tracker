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


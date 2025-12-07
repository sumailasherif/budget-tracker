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
        print("\Adding income...")
        date = input("Date (YYYY-MM-DD): ")
        amount = self.get_amount()
        category = input("Category: ")
        description = input("Description: ")

        inc = Income(date, amount, category, description)
        self.transactions.append(inc)
        print("Income added successfully!")

            def add_expense(self):
        print("\nAdding expense...")
        date = input("Date (YYYY-MM-DD): ")
        amount = self.get_amount()
        category = input("Category: ")
        description = input("Description: ")

        exp = Expense(date, amount, category, description)
        self.transactions.append(exp)
        print("Expense added successfully!")


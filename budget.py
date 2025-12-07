class Transaction:
    def __init__(self, date, amount, category, description, ttype):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.ttype = ttype   # "income" or "expense"
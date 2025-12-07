class Transaction:
    def __init__(self, date, amount, category, description, ttype):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.ttype = ttype   # 'ncome' or 'expense'

    def __str__(self):
        return f"{self.date} | {self.type.upper()} | {self.category} | KSH{self.amount} | {self.description}"


class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "income")
        

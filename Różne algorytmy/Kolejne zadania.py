class Account:
    def __init__(self, amount:float):
        self.amount = amount
    def __str__(self):
        return f"Saldo konta  {self.amount}"
    def __repr__(self):
        return f"Saldo konta  {self.amount}"

accounts = [
    Account(100),
    Account(1000),
    Account(2100)
]

print(accounts)
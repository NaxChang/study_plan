class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            # self.balance = self.balance - amount
            self.balance -= amount

    def get_balance(self):
        return self.balance


account = BankAccount("nameless", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())

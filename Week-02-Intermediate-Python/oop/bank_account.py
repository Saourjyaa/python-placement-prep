class BankAccount:
    def __init__(self, holder, balance=0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Withdrawal must be positive and within the balance.")
        self.balance -= amount


if __name__ == "__main__":
    account = BankAccount("Aarav", 1000)
    account.deposit(250)
    account.withdraw(100)
    print(f"{account.holder}: {account.balance:.2f}")

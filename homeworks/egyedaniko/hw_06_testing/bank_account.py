import math


# Közös ellenőrzés, hogy ne ismételjük a típusvizsgálatot.
def validate_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"{name} must be finite.")


class BankAccount:
    # Bankszámla létrehozása, alapértelmezetten nulla egyenleggel.
    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(owner, str):
            raise TypeError("Owner must be a string.")
        validate_number(balance, "Balance")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    # Csak pozitív, véges összeg fizethető be.
    def deposit(self, amount: float):
        validate_number(amount, "Amount")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    # A kivét nem haladhatja meg az egyenleget.
    def withdraw(self, amount: float):
        validate_number(amount, "Amount")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    # Az utalás a meglévő kivét és befizetés metódusokra épül.
    def transfer(self, amount: float, target_account: "BankAccount"):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if target_account is self:
            raise ValueError("Cannot transfer money to the same account.")
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

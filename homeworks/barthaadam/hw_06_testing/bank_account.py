import math


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self._validate_number(balance)

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner
        self.balance = balance

    def _validate_number(self, value):
        # A True és False értékeket nem fogadjuk el pénzösszegként.
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Amount must be a number.")

        # A NaN és a végtelen értékeket is elutasítjuk.
        if not math.isfinite(value):
            raise ValueError("Amount must be finite.")

    def deposit(self, amount: float):
        self._validate_number(amount)

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount

    def withdraw(self, amount: float):
        self._validate_number(amount)

        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount

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
        return (
            f"Account owner: {self.owner}, "
            f"Balance: {self.balance:.2f}"
        )
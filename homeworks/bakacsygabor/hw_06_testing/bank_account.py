import math


class BankAccount:
    """A small bank account model with validated money amounts."""

    @staticmethod
    def _validate_amount(amount: float, *, allow_zero: bool, label: str) -> None:
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError(f"{label} must be a number.")
        if isinstance(amount, float) and not math.isfinite(amount):
            raise ValueError(f"{label} must be finite.")
        if amount < 0 or (amount == 0 and not allow_zero):
            if allow_zero:
                raise ValueError("Initial balance cannot be negative.")
            raise ValueError(f"{label} must be positive.")

    def __init__(self, owner: str, balance: float = 0.0):
        self._validate_amount(balance, allow_zero=True, label="Initial balance")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self._validate_amount(amount, allow_zero=False, label="Deposit amount")
        self.balance += amount

    def withdraw(self, amount: float):
        self._validate_amount(amount, allow_zero=False, label="Withdraw amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
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

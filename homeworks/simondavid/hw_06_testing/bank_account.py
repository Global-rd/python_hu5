
import math


class BankAccount:

    # Initialize account and validate owner and initial balance.
    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(owner, str):
            raise TypeError("Account owner must be a string.")

        if not owner.strip():
            raise ValueError("Account owner cannot be empty.")

        self._validate_amount_type(balance)

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner
        self.balance = balance

    # Validate numeric input, excluding booleans and non-finite values.
    @staticmethod
    def _validate_amount_type(amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if not math.isfinite(amount):
            raise ValueError("Amount must be finite.")

    # Deposit a positive amount into the account.
    def deposit(self, amount: float):
        self._validate_amount_type(amount)

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount

    # Withdraw a positive amount if sufficient funds are available.
    def withdraw(self, amount: float):
        self._validate_amount_type(amount)

        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount

    # Transfer money to another valid account.
    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")

        if target_account is self:
            raise ValueError("Cannot transfer money to the same account.")

        self._validate_amount_type(amount)

        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.withdraw(amount)
        target_account.deposit(amount)

    # Return the current account balance.
    def get_balance(self):
        return self.balance

    # Return a readable string representation of the account.
    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: {self.balance:.2f}"

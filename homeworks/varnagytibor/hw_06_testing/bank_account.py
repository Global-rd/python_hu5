import math

#EXTRA: az eredeti (extra_tasks/homework_06_helper) osztály hiányosságai, amiket itt javítottam:
#  1. nem szám input (pl. "100", None, True) - az eredeti TypeError-t dob az összehasonlításnál,
#     vagy (True esetén) csendben 1-nek veszi -> most egyértelmű TypeError, saját üzenettel
#  2. NaN és végtelen (float("nan"), float("inf")) - az eredeti a NaN-t átengedi,
#     és elrontja vele az egyenleget -> most ValueError
#  3. a tulajdonos neve bármi lehetett (üres string, szám) -> most nem üres string kell
#  4. pénzküldés saját magunknak -> most ValueError
#  5. transfer() 0 vagy negatív összeggel a withdraw() hibaüzenetét adta ("Withdraw ...")
#     -> most saját, érthető üzenet


def _validate_amount(amount, action: str):
    """Ellenőrzi, hogy az összeg valódi, véges, pozitív szám-e."""
    #a bool az int alosztálya (True == 1), ezért külön ki kell zárni
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise TypeError(f"{action} amount must be a number.")
    if math.isnan(amount) or math.isinf(amount):
        raise ValueError(f"{action} amount must be a finite number.")
    if amount <= 0:
        raise ValueError(f"{action} amount must be positive.")


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner must be a non-empty string.")
        if isinstance(balance, bool) or not isinstance(balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        if math.isnan(balance) or math.isinf(balance):
            raise ValueError("Initial balance must be a finite number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner.strip()
        self.balance = balance

    def deposit(self, amount: float):
        _validate_amount(amount, "Deposit")
        self.balance += amount

    def withdraw(self, amount: float):
        _validate_amount(amount, "Withdraw")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if target_account is self:
            raise ValueError("Cannot transfer money to the same account.")
        _validate_amount(amount, "Transfer")
        #withdraw előbb: ha nincs fedezet, a célszámla sem változik
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

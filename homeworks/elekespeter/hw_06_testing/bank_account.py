import math


class BankAccount:
    """
    Egyszerű bankszámla befizetéssel, kivéttel és utalással.

    EXTRA kiegészítések az eredeti (extra_tasks/homework_06_helper) verzióhoz képest:
      - a tulajdonos neve csak nem üres szöveg lehet
      - összegnek csak szám (int/float) adható meg, bool nem
        (a Pythonban a True = 1, így az eredeti kód elfogadta a deposit(True)-t)
      - NaN és végtelen összeg nem engedett
        (az eredeti kódban deposit(float("nan")) után az egyenleg "nan" lett)
      - saját számlára nem lehet utalni
    Az eredeti hibaüzenetek nem változtak, csak újak kerültek mellé.
    """

    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner must be a non-empty string.")
        self._validate_amount(balance)
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    @staticmethod
    def _validate_amount(amount) -> None:
        """
        Közös ellenőrzés minden összeghez (DRY elv).
        Csak a típust és a véges értéket nézi; azt, hogy pozitív-e,
        a hívó metódus dönti el, mert ott más-más a szabály.
        """
        # A bool az int "leszármazottja", ezért külön ki kell zárni.
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if math.isnan(amount) or math.isinf(amount):
            raise ValueError("Amount must be a finite number.")

    def deposit(self, amount: float):
        self._validate_amount(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float):
        self._validate_amount(amount)
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if target_account is self:
            raise ValueError("Cannot transfer to the same account.")
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

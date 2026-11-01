"""
BankAccount – a homework_06_helper/bank_account.py kiegészített változata.
 
Az eredeti osztály hiányosságai (Extra feladat):
  1. Nem szám inputok (pl. "100", None, [10]) nincsenek kezelve:
     a "<" / "<=" összehasonlítás str-rel TypeError-t dob ugyan, de nem
     érthető üzenettel, a None-nál pedig szintén csak egy általános hiba jön.
  2. A bool az int alosztálya, így deposit(True) eredetileg 1-et fizetne be.
  3. float("nan") és float("inf") átcsúszik az ellenőrzéseken:
     nan <= 0 -> False, ezért a NaN befizethető, és utána a balance is NaN lesz.
  4. Az owner bármi lehet (üres string, szám, None).
  5. Saját magunknak is küldhetünk pénzt (transfer self-re).
  6. A transfer nem validál előre: ha a cél rossz, az eredeti kódban szerencsére
     a típusellenőrzés előbb fut, de az összeg ellenőrzése csak a withdraw-ban
     történik. Itt mindent az első pénzmozgás előtt ellenőrzünk.
"""
 
import math
 
 
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        # owner: nem üres string legyen
        if not isinstance(owner, str):
            raise TypeError("Owner must be a string.")
        if not owner.strip():
            raise ValueError("Owner cannot be empty.")
 
        self._validate_number(balance, "Initial balance")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
 
        self.owner = owner
        self.balance = balance
 
    # ------------------------------------------------------------------
    # Segédfüggvény: szám-e az input (és véges szám-e)
    # ------------------------------------------------------------------
    @staticmethod
    def _validate_number(value, name: str = "Amount"):
        # a bool külön kizárva, mert isinstance(True, int) -> True
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number.")
        if math.isnan(value) or math.isinf(value):
            raise ValueError(f"{name} must be a finite number.")
 
    def deposit(self, amount: float):
        self._validate_number(amount, "Deposit amount")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
 
    def withdraw(self, amount: float):
        self._validate_number(amount, "Withdraw amount")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
 
    def transfer(self, amount: float, target_account: "BankAccount"):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if target_account is self:
            raise ValueError("Cannot transfer to the same account.")
 
        # minden ellenőrzés a pénzmozgás ELŐTT -> nem maradhat félkész állapot
        self._validate_number(amount, "Transfer amount")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
 
        self.withdraw(amount)
        target_account.deposit(amount)
 
    def get_balance(self):
        return self.balance
 
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
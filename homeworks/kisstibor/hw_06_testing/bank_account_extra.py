import math
from numbers import Real


def _validate_amount(amount, name: str) -> None:
    """Összegellenőrzés a deposit és withdraw számára.
    amount: az ellenőrizendő összeg
    name:   csak a hibaüzenethez kell (pl. "Deposit amount")
    Hiba:   TypeError, ha az összeg nem szám (vagy bool);
            ValueError, ha NaN/inf, vagy nem pozitív.
    """
    if isinstance(amount, bool) or not isinstance(amount, Real):
        raise TypeError(f"{name} must be a number.")

    if not math.isfinite(amount):
        raise ValueError(f"{name} must be a finite number.")

    if amount <= 0:
        raise ValueError(f"{name} must be positive.")


class BankAccount:
    """Egyszerű bankszámla: tulajdonos neve és egyenlege.

    Befizetést, kivételt, másik számlára utalást és az
    egyenleg lekérdezés metódussokkal. Hibák kivételkezeléssekkel.
    """

    def __init__(self, owner: str, balance: float = 0.0):
        """Létrehoz egy számlát.
        owner:   a számla tulajdonosának neve (üres szöveg nem lehet)
        balance: kezdő egyenleg (alapértelmezés: 0.0)
        Hiba:    TypeError, ha az owner nem szöveg vagy a balance nem szám;
                 ValueError, ha az owner üres, vagy a balance NaN/inf/negatív.
        """
        # A tulajdonos csak szöveg lehet, és nem lehet üres vagy csupa szóköz.
        if not isinstance(owner, str):
            raise TypeError("Owner must be a string.")

        if not owner.strip():
            raise ValueError("Owner cannot be empty.")

        # A kezdő egyenlegre ugyanazok a típusszabályok vonatkoznak, mint az
        # összegekre, de a 0 itt megengedett / csak a negatív tilos.
        if isinstance(balance, bool) or not isinstance(balance, Real):
            raise TypeError("Initial balance must be a number.")

        if not math.isfinite(balance):
            raise ValueError("Initial balance must be a finite number.")

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        """Pénzt fizet be a számlára (növeli az egyenleget).
        Hiba: TypeError, ha az összeg nem szám;
              ValueError, ha az összeg NaN/inf, 0 vagy negatív.
        """
        # Az ellenőrzés a módosítás előtt fut, így hibánál az egyenleg nem változik.
        _validate_amount(amount, "Deposit amount")
        self.balance += amount

    def withdraw(self, amount: float):
        """Pénzt vesz ki a számláról (csökkenti az egyenleget).
        Hiba: ValueError, ha az összeg 0 vagy negatív, vagy ha többet venne ki, mint az aktuális egyenleg értéke.            
        """

        _validate_amount(amount, "Withdraw amount")

        # Többet nem lehet kivenni, mint amennyi van,de a pontosan a teljes egyenleg még kivehető.
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        """Utal a saját számlánkról egy másik BankAccount-ra.

        Hiba: TypeError, ha a célpont nem BankAccount (vagy az összeg nem szám);
              ValueError, ha saját magunknak utalnánk, az összeg érvénytelen,
              vagy nincs fedezet (az utóbbiakat a withdraw/deposit dobja).
        """
        # A típusellenőrzés a pénzmozgás ELŐTT történik, így hibánál nem kerül levonásra.
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        
        # Saját számlára utalásnak nincs értelme (hibás művelet)
        # Az "is" azonos objektumot vizsgál, nem csak egyenlő értékűt.
        if target_account is self:
            raise ValueError("Cannot transfer to the same account.")
        
        # Először levonjuk a saját számláról (itt derül ki az érvénytelen összeg vagy a fedezethiány, és csak utána írjuk jóvá a célszámlán.
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self):
        """Visszaadja az aktuális egyenleget."""
        return self.balance

    def __str__(self):
        """Objektum info: Olvasható szöveges formában: Tulajdonos és egyenleg két tizedesre kerekítve."""
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

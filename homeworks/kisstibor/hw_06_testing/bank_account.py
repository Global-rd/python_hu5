class BankAccount:
    """Egyszerű bankszámla: tulajdonos neve és egyenlege.

    Befizetést, kivételt, másik számlára utalást és az
    egyenleg lekérdezés metódussokkal. Hibák kivételkezeléssekkel.
    """

    def __init__(self, owner: str, balance: float = 0.0):
        """Létrehoz egy számlát.
        owner:   a számla tulajdonosának neve
        balance: kezdő egyenleg (kezdő egyenleg: 0.0)
        Hiba:    ValueError, ha a kezdő egyenleg negatív.
        """
        # Negatív kezdő egyenleggel nem nyitható számla.
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        """Pénzt fizet be a számlára (növeli az egyenleget).

        Hiba: ValueError, ha az összeg 0 vagy negatív.
        """
        # Csak pozitív összeg fizethető be.
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float):
        """Pénzt vesz ki a számláról (csökkenti az egyenleget).
        Hiba: ValueError, ha az összeg 0 vagy negatív, vagy ha többet venne ki, mint az aktuális egyenleg értéke.            
        """
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        # Többet nem lehet kivenni, mint amennyi van,de a pontosan a teljes egyenleg még kivehető.
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        """Utalás a számláról egy másik BankAccount-ra.
        Hiba: TypeError, ha a célpont nem BankAccount;
              ValueError, ha az összeg érvénytelen vagy nincs fedezet
              (ezt a withdraw/deposit dobja).
        """
        # A típusellenőrzés a pénzmozgás előtt történik, így hiba esetén nem csökken az egyenleg.
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        # Először levonjuk a saját számláról (itt derül ki, ha nincs fedezet), csak utána írjuk jóvá a célszámlán.
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self):
        """Visszaadja az aktuális egyenleget."""
        return self.balance

    def __str__(self):
        """Olvasható szöveges alak, az egyenleg két tizedesre kerekítve."""
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

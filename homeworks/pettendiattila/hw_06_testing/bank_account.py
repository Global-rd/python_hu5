class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        #Ellenenőrizzük hogya kezdő egyenleg szám
        #Szöveg vagy más nem megfelelő típus esetén TYpeerror
        if not isinstance(balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        
        #Egyenleg nem lehet negatív
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        #Tároljuk a számla tulajdonos és egyeneleget
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        #Ellenőrizzük, hogy az összeg szám
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")

        #Csak pozitív összeget lehet befizetni
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        #Hozzáadjuka befizetett összeget
        self.balance += amount
    
    def withdraw(self, amount: float):
        #Ellenőrizzük, hogy az összeg szám
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdraw amount must be a number.")

        #Csak pozitív összeget lehet kifizetni
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")

        #Van-e elég fedezet
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

         #Levonjuk a felvett összeget
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
         #Ellenőrizzük, hogy a cél valóban egy bankszámla
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")

        #Nem utalhatunk saját magunknak.
        if target_account is self:
            raise ValueError("Cannot transfer to the same account.")
        
        #Levonjuk az összeget a küldő számláról.  
        self.withdraw(amount)

        #Hozzáadjuk az összeget a fogadó számlához.
        target_account.deposit(amount)
    
    def get_balance(self):
         #Visszaadjuk a számla aktuális egyenlegét.
        return self.balance

    def __str__(self):
        #Szöveges formában jelenítjük meg a számla adatait.
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
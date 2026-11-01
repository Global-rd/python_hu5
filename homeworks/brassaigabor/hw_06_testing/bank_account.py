class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.amount_validate(balance)
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    def amount_validate (self, amount):
        if not isinstance(amount, (float, int)) or isinstance(amount, bool):
            raise TypeError("Balance is not a number. Try again!")

    def account_validate(self, acc):
        if not isinstance(acc, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")

    def deposit(self, amount: float):
        self.amount_validate(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        self.amount_validate(amount)
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        self.amount_validate(amount)
        self.account_validate(target_account)
        if target_account is self:
            raise ValueError("Cannot transfer money to your own account!")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
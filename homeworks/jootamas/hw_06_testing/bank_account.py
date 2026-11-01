class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if not(isinstance(balance, float)) or balance < 0:
            raise ValueError("Initial balance must be a positive number.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if not (isinstance(amount, float)) or amount < 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if not (isinstance(amount, float)) or amount < 0:
            raise ValueError("Withdraw amount must be a positive number.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if target_account == self:
            raise TypeError("You can not transfer yourself.")
        if not (isinstance(amount, float)) or amount < 0:
            raise ValueError("Amount must be a positive number.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

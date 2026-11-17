class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        # check the name, it should be a string and not empty
        if not isinstance(owner, str):
            raise TypeError("Owner name must be a string.")
        if len(owner.strip()) == 0:
            raise ValueError("Owner name cannot be empty.")
        # check the balance, it should be a number
        if not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        # check the amount, it should be a number
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        # check the amount, it should be a number
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdraw amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        # check the amount, it should be a number
        if not isinstance(amount, (int, float)):
            raise TypeError("Transfer amount must be a number.")
        # check the amount, it should be positive
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        # check the target_account, it should be a BankAccount
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        # check if the target_account is the same as self
        if target_account is self:
            raise ValueError("Cannot transfer money to the same account.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
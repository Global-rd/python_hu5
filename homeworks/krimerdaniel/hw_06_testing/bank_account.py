class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        try:        #Check if initial balance is a number
            balance = float(balance)
        except:
            raise ValueError("Balance is not a number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        try:        #Check if deposit amount is a number
            amount = float(amount)
        except:
            raise ValueError("Amount to deposit is not a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        try:        #Check if withdraw amount is a number
            amount = float(amount)
        except:
            raise ValueError("Amount to withdraw is not a number.")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        try:        #Check if transfer amount is a number. There is no need to check here if amount > 0, because it is checked in withdraw and deposit methods
            amount = float(amount)
        except:
            raise ValueError("Transfer amount is not a number.")
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if self == target_account:      #Check if target and sender accounts are the same
            raise ValueError("Target and sender are the same accounts, transfer is not supported.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"



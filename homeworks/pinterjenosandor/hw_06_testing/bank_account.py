class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(owner, str) or not owner.strip():    #check the account field is not empty and non numeric (string)
            raise ValueError("Owner must be a non-empty string.")
        if isinstance(balance, bool) or not isinstance(balance, float): #check the balance is number
            raise TypeError("Balance must be a number.")
        if balance < 0:
            raise ValueError("The opening balance cannot be negative") #check the opening not to be a negative number
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)): # check number for deposit
            raise TypeError("Deposit need to be a number")
        if amount <= 0:
            raise ValueError("The value need to be positive number") # the deposit need to be a positive number
        self.balance += amount

    def withdraw(self, amount: float):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Withdraw need to be a number")  # withdraw is numeric
        if amount <= 0:
            raise ValueError("The value need to be positive number") #withdraw is + number 
        if amount > self.balance:
            raise ValueError("Insufficient funds.") # the amount not enough for withdraw
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount): # check transfer to not a bank account
            raise TypeError("Target not in BankAccount")
        if target_account is self:   # to try to send ourselves,
            raise ValueError("Cannot transfer money to ourselves")
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
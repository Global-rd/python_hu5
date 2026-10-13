from datetime import datetime as dt

class InvalidAmountError(Exception):
    """
    Custom exception for invalid amount on deposit/withdraw    
    """
    pass

class InsufficientFundsError(Exception):
    """
    Custom exception for unsifficient funds on withdraw 
    """
    pass

class BankAccount:

    def __init__(self, account_holder: str, account_number: str, balance:float=0) -> None:

        self.account_holder = account_holder
        self.account_number = account_number
        self._balance = balance #protected 
        self._transactions = []

    def deposit(self, amount: int) -> None:

        if amount <= 0: #guard clause
            raise InvalidAmountError("Deposit must be positive!")
        self._balance += amount
        self._record_transaction("deposit", amount)
        

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise InvalidAmountError("Withdraw must be positive!")
        if amount > self._balance:
            raise InsufficientFundsError(f"Not enough money, Current balance: {self._balance}")

        self._balance -= amount
        self._record_transaction("withdraw", amount)

    def get_balance(self):
        return self._balance
        
    def _record_transaction(self, transaction_type: str, amount: int) -> None:

        transaction = {"type": transaction_type,
                       "amount": amount,
                        "date":  dt.now().strftime("%Y-%m-%d %H:%M:%S")}
        self._transactions.append(transaction)

    def get_transaction_history(self) -> str:

        if not self._transactions:
            return "There are no transactions yet!"
        
        history = f"Transaction history for {self.account_holder} \n"

        for transaction in self._transactions:
            history += (f"{transaction['date']} - {transaction['type']} "
                        f"${transaction['amount']}\n")

        return history


print(__name__)
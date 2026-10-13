from bank_account import (BankAccount, 
                          InsufficientFundsError, 
                          InvalidAmountError)

def main():
    account_1 = BankAccount(account_holder="X", account_number="1", balance=500.0)
    print(account_1.get_balance())
    account_1.deposit(5000)
    print(account_1.get_balance())
    account_1.withdraw(300)
    print(account_1.get_balance())
    account_2 = BankAccount(account_holder="Y", account_number="2", balance=1000.0)
    account_2.deposit(5000)

    history = account_1.get_transaction_history()
    print(history)

if __name__ == "__main__":
    main()
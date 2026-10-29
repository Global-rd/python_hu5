import pytest 
from bank_account import BankAccount

#Fixtures

"""
Create new deposit accounts
"""
@pytest.fixture 
def laura_account():
    return BankAccount("Laura",100.0)

@pytest.fixture 
def jack_account():
    return BankAccount("Jack") #default amount is 0

"""
Initial account testing
"""

def test_initial_balance(laura_account):
    assert laura_account.owner == "Laura" #should be Laura
    assert laura_account.balance == 100.0 #should be 100.05

# Default amount must be 0.
   
def test_default_balance():
    account = BankAccount("John")
    assert account.balance == 0.0 # should be 0

# If it is not 0, should get a ValuError Exception

@pytest.mark.parametrize("owner, balance, expected_exception",
                         [
                             ("Laura", -100.0, ValueError), #shouldn't be negative
                             ("Laura", -0.01, ValueError), #shouldn't be negative
                             ("Laura", -500, ValueError) #shouldn't be negative
                         ])
def test_invalid_default_input(owner, balance, expected_exception):
    with pytest.raises(expected_exception, match= "Initial balance cannot be negative."):
        BankAccount(owner, balance)

"""
Deposit test
"""

#Balance checking

def test_deposit_balance(jack_account):
    jack_account.deposit(300)
    assert jack_account.balance == 300

# If amount is negative, should get a ValuError Exception

@pytest.mark.parametrize("amount", [-100.0, 0.0])
def test_invalid_deposit_input(jack_account, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        jack_account.deposit(amount)

"""
Withdraw test
"""

#zero balance must be 0 or higher than 0

def test_withdraw(laura_account):
    initial_balance = laura_account.balance
    amount = 100.00
    laura_account.withdraw(amount)
    assert laura_account.balance == initial_balance - amount

#Amount shouldn't be negative

@pytest.mark.parametrize("amount", [-100.0, 0.0])
def test_invalid_withdraw_input(laura_account, amount):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        laura_account.withdraw(amount) 

def test_insufficient_funds(laura_account):    
    with pytest.raises(ValueError, match="Insufficient funds."):
        laura_account.withdraw(200)

"""
Transfer test
"""

def test_transfer(laura_account, jack_account):
    laura_account.transfer(90, jack_account)
    assert laura_account.balance == 10
    assert jack_account.balance == 90

def test_transfer_invalid_target(jack_account):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        jack_account.transfer(100, "Laura")

"""
Get balance test
"""

def test_get_balance(laura_account):
    assert laura_account.get_balance() == 100
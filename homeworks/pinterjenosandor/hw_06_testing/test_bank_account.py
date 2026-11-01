import pytest
from bank_account import BankAccount

"""BankAccounts"""
@pytest.fixture
def account_kumar():
    return BankAccount("Kumar", 1000.0)


@pytest.fixture
def account_harold():
    return BankAccount("Harold", 500.0)


@pytest.mark.parametrize("invalid_amount", [0, -100]) #testing deposit 0 and negative number
def test_deposit_invalid_numeric_values(account_kumar, invalid_amount):
    with pytest.raises(ValueError, match="The value need to be positive number"):
        account_kumar.deposit(invalid_amount)

@pytest.mark.parametrize("invalid_type", ["100", None, [50], True]) #Testing the non number type inputs
def test_deposit_invalid_types(account_harold, account_kumar, invalid_type):
    with pytest.raises(TypeError, match="Deposit need to be a number"):
        account_harold.deposit(invalid_type)
        account_kumar.deposit(invalid_type)

def test_withdraw_insufficient_funds(account_kumar): #Check if the witdraw amount is higher than balance
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_kumar.withdraw(1500.0)

def test_transfer_to_non_bank_account(account_harold): # send money to non Bank Account, example string
    with pytest.raises(TypeError, match="Target not in BankAccount"):
        account_harold.transfer(100.0, "not_an_account")

def test_transfer_to_self(account_kumar): #send amount to myself
    """Extra edge case: Saját magunknak történő utalás megakadályozása."""
    with pytest.raises(ValueError, match="Cannot transfer money to ourselves"):
        account_kumar.transfer(100.0, account_kumar)

def test_successful_transfer(account_kumar, account_harold): #check transfer between two accounts
    account_kumar.transfer(200.0, account_harold)
    assert account_kumar.get_balance() == 800.0
    assert account_harold.get_balance() == 700.0

def test_initial_balance_negative_raises_error(): # check the BankAccount not made it with negative amount
    with pytest.raises(ValueError, match="The opening balance cannot be negative"):
        BankAccount("Big Bob", -50.0)
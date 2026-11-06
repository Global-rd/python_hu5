import pytest
from bank_account import BankAccount

@pytest.fixture
def empty_account():
    return BankAccount("Test User")

@pytest.fixture
def account():
    return BankAccount("Test User", 100)

def test_initial_balance():
    account = BankAccount("Test User", 100)
    assert account.balance == 100

def test_deposit():
    account = BankAccount("Test User", 100)
    account.deposit(100)
    assert account.balance == 200

def test_non_positive_deposit():
    account = BankAccount("Test User", 100)
    with pytest.raises(ValueError):
        account.deposit(-50)

def test_non_positive_withdraw():
    account = BankAccount("Test User", 100)
    with pytest.raises(ValueError):
        account.withdraw(-50)

def test_withdraw():
    account = BankAccount("Test User", 100)
    account.withdraw(50)
    assert account.balance == 50

def test_withdraw_insufficient_funds():
    account = BankAccount("Test User", 100)
    with pytest.raises(ValueError):
        account.withdraw(150)

@pytest.mark.parametrize("initial_balance, deposit_amount, expected_balance", 
                        [
                            (100, 50, 150),
                            (100, 0, 100),
                            (0, -50, 0)
                        ])
def test_deposit_parametrized(initial_balance, deposit_amount, expected_balance):
    account = BankAccount("Test User", initial_balance)
    account.deposit(deposit_amount)
    assert account.balance == expected_balance

def test_creating_account_with_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("Test User", -100)
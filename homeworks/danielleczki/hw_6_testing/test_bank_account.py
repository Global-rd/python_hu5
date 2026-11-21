import pytest

from bank_account import BankAccount

@pytest.fixture

def account_1():
    return BankAccount(
        owner="Deni",
        balance=1000.0
    )

@pytest.fixture
def account_2():
    return BankAccount(
        owner="Peter",
        balance=500.0
    )

def test_account_balance(account_1):
    assert account_1.get_balance() == 1000.0

def test_account_withdraw(account_2):
    account_2.withdraw(300)
    assert account_2.get_balance() == 200.0
def test_account_withdraw_valueerror(account_1):
    with pytest.raises(ValueError):
        account_1.withdraw(-2000)

    assert account_1.get_balance() == 1000.0

@pytest.mark.parametrize("amount", [0, -100])
def test_deposit_invalid_amount(account_1, amount):
    with pytest.raises(ValueError):
        account_1.deposit(amount)
    assert account_1.get_balance() == 1000.0

def test_transfer(account_1,account_2):
    account_1.transfer(300,account_2)
    assert account_1.get_balance() == 700.0
    assert account_2.get_balance() == 800.0

def test_transfer_invalid_account(account_1):
    with pytest.raises(TypeError):
        account_1.transfer(200, "Jenő")
    assert account_1.get_balance() == 1000.0
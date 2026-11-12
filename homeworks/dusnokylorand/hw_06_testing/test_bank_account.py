import pytest

from bank_account import BankAccount

@pytest.fixture
def account_one():
    return BankAccount("Alice", 1000)

@pytest.fixture
def account_two():
    return BankAccount("Bob", 500)

def test_get_balance(account_one):
    assert account_one.get_balance() == 1000

def test_deposit(account_one):
    account_one.deposit(200)

    assert account_one.get_balance() == 1200
@pytest.mark.parametrize("amount", [0, -100])

def test_deposit_invalid_amount(account_one, amount):
    with pytest.raises(ValueError):
        account_one.deposit(amount)

def test_withdraw(account_one):
    account_one.withdraw(300)

    assert account_one.get_balance() == 700

@pytest.mark.parametrize("amount", [0, -50])
def test_withdraw_invalid_amount(account_one, amount):
    with pytest.raises(ValueError):
        account_one.withdraw(amount)

def test_withdraw_insufficient_funds(account_one):
    with pytest.raises(ValueError):
        account_one.withdraw(1500)

def test_transfer(account_one, account_two):
    account_one.transfer(200, account_two)

    assert account_one.get_balance() == 800
    assert account_two.get_balance() == 700

def test_transfer_invalid_target(account_one):
    with pytest.raises(TypeError):
        account_one.transfer(100, "not_a_bank_account")

def test_transfer_to_same_account(account_one):
    with pytest.raises(ValueError):
        account_one.transfer(100, account_one)

def test_deposit_non_numeric(account_one):
    with pytest.raises(TypeError):
        account_one.deposit("abc")

def test_withdraw_non_numeric(account_one):
    with pytest.raises(TypeError):
        account_one.withdraw("abc")

def test_initial_balance_non_numeric():
    with pytest.raises(TypeError):
        BankAccount("Alice", "abc")

def test_initial_balance_negative():
    with pytest.raises(ValueError):
        BankAccount("Alice", -100)

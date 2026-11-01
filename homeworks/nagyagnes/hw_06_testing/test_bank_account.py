# BankAccount unit tests - HW6

import pytest
from bank_account import BankAccount


@pytest.fixture
def account_anna():
    return BankAccount("Anna", 1000)


def test_initial_balance(account_anna):
    assert account_anna.get_balance() == 1000


@pytest.fixture
def account_agnes():
    return BankAccount("Ágnes", 500)


def test_transfer(account_anna, account_agnes):
    account_anna.transfer(200, account_agnes)

    assert account_anna.get_balance() == 800
    assert account_agnes.get_balance() == 700

@pytest.mark.parametrize("amount", [100, 200, 500])
def test_deposit(account_anna, amount):
    account_anna.deposit(amount)
    assert account_anna.get_balance() == 1000 + amount

@pytest.mark.parametrize("amount", [0, -50, -100])
def test_invalid_deposit(account_anna, amount):
    with pytest.raises(ValueError):
        account_anna.deposit(amount)

def test_withdraw_insufficient_funds(account_anna):
    with pytest.raises(ValueError):
        account_anna.withdraw(1500)

def test_withdraw(account_anna):
    account_anna.withdraw(300)
    assert account_anna.get_balance() == 700

@pytest.mark.parametrize("amount", [0, -50, -100])
def test_invalid_withdraw(account_anna, amount):
    with pytest.raises(ValueError):
        account_anna.withdraw(amount)


def test_transfer_invalid_target(account_anna):
    with pytest.raises(TypeError):
        account_anna.transfer(200, "Ágnes")

def test_negative_initial_balance():
    with pytest.raises(ValueError):
        BankAccount("Anna", -100)

def test_str(account_anna):
    assert str(account_anna) == "Account owner: Anna, Balance: 1000.00"

def test_transfer_insufficient_funds(account_anna, account_agnes):
    with pytest.raises(ValueError):
        account_anna.transfer(1500, account_agnes)

    assert account_anna.get_balance() == 1000
    assert account_agnes.get_balance() == 500

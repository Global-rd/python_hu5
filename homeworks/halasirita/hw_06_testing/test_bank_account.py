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

@pytest.mark.parametrize(
    "amount, expected_exception",
    [
        (-1, ValueError),
        (0, ValueError),
    ]
)
def test_invalid_deposit(account_one, amount, expected_exception):
    with pytest.raises(expected_exception):
        account_one.deposit(amount)

def test_withdraw(account_one):
    account_one.withdraw(200)
    assert account_one.get_balance() == 800

def test_withdraw_all(account_one):
    account_one.withdraw(1000)
    assert account_one.get_balance() == 0

def test_withdraw_too_much(account_one):
    with pytest.raises(ValueError):
        account_one.withdraw(1001)

@pytest.mark.parametrize("amount", [0, -1, -100])
def test_invalid_withdraw(account_one, amount):
    with pytest.raises(ValueError):
        account_one.withdraw(amount)

def test_transfer(account_one, account_two):
    account_one.transfer(200, account_two)
    assert account_one.get_balance() == 800
    assert account_two.get_balance() == 700

def test_transfer_invalid_target(account_one):
    with pytest.raises(TypeError):
        account_one.transfer(200, "not_an_account")

def test_transfer_to_self(account_one):
    with pytest.raises(ValueError):
        account_one.transfer(200, account_one)

@pytest.mark.parametrize("amount", ["a", None])
def test_withdraw_non_number(account_one, amount):
    with pytest.raises(TypeError):
        account_one.withdraw(amount)

@pytest.mark.parametrize("amount", ["a", None])
def test_deposit_non_number(account_one, amount):
    with pytest.raises(TypeError):
        account_one.deposit(amount)

@pytest.mark.parametrize("balance", ["a", None])
def test_initial_balance_non_number(balance):
    with pytest.raises(TypeError):
        BankAccount("Alice", balance)

def test_negative_initial_balance():
    with pytest.raises(ValueError):
        BankAccount("Alice", -100)

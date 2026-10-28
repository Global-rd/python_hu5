import pytest
from bank_account import BankAccount


# Teszteléshez használt bankszámlák

@pytest.fixture
def account():
    return BankAccount("Miklos", 1000.0)


@pytest.fixture
def second_account():
    return BankAccount("Anna", 500.0)


# 1. Bankszámla létrehozása

def test_initial_balance(account):
    assert account.owner == "Miklos"
    assert account.get_balance() == 1000.0


def test_default_balance():
    account = BankAccount("Peter")
    assert account.get_balance() == 0.0


def test_negative_initial_balance():
    with pytest.raises(ValueError):
        BankAccount("Miklos", -100.0)


# 2. Befizetés tesztelése

def test_deposit(account):
    account.deposit(200.0)
    assert account.get_balance() == 1200.0


def test_deposit_zero(account):
    with pytest.raises(ValueError):
        account.deposit(0)


def test_deposit_negative(account):
    with pytest.raises(ValueError):
        account.deposit(-100.0)


# 3. Pénzfelvétel tesztelése

def test_withdraw(account):
    account.withdraw(300.0)
    assert account.get_balance() == 700.0


def test_withdraw_all_money(account):
    account.withdraw(1000.0)
    assert account.get_balance() == 0.0


def test_withdraw_zero(account):
    with pytest.raises(ValueError):
        account.withdraw(0)


def test_withdraw_negative(account):
    with pytest.raises(ValueError):
        account.withdraw(-50.0)


def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError):
        account.withdraw(1500.0)


# 4. Átutalás tesztelése

def test_transfer(account, second_account):
    account.transfer(200.0, second_account)

    assert account.get_balance() == 800.0
    assert second_account.get_balance() == 700.0


def test_transfer_all_money(account, second_account):
    account.transfer(1000.0, second_account)

    assert account.get_balance() == 0.0
    assert second_account.get_balance() == 1500.0


def test_transfer_insufficient_funds(account, second_account):
    with pytest.raises(ValueError):
        account.transfer(1500.0, second_account)

    assert account.get_balance() == 1000.0
    assert second_account.get_balance() == 500.0


def test_transfer_invalid_account(account):
    with pytest.raises(TypeError):
        account.transfer(100.0, "Anna")

    assert account.get_balance() == 1000.0


def test_transfer_negative_amount(account, second_account):
    with pytest.raises(ValueError):
        account.transfer(-100.0, second_account)

    assert account.get_balance() == 1000.0
    assert second_account.get_balance() == 500.0


# 5. Egyenleg lekérdezése

def test_get_balance(account):
    assert account.get_balance() == 1000.0

    account.deposit(500.0)

    assert account.get_balance() == 1500.0


# 6. Szöveges megjelenítés

def test_account_str(account):
    expected = "Account owner: Miklos, Balance: 1000.00"

    assert str(account) == expected

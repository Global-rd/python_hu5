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


@pytest.mark.parametrize("invalid_balance", [-1, -100.0, -1000.0])
def test_negative_initial_balance(invalid_balance):
    with pytest.raises(ValueError):
        BankAccount("Miklos", invalid_balance)


# 2. Befizetés tesztelése

@pytest.mark.parametrize(
    "amount, expected_balance",
    [
        (100.0, 1100.0),
        (200.0, 1200.0),
        (500.0, 1500.0),
    ]
)
def test_deposit(account, amount, expected_balance):
    account.deposit(amount)
    assert account.get_balance() == expected_balance


@pytest.mark.parametrize("invalid_amount", [0, -10, -100.0])
def test_deposit_invalid_amounts(account, invalid_amount):
    with pytest.raises(ValueError):
        account.deposit(invalid_amount)

    assert account.get_balance() == 1000.0


# 3. Pénzfelvétel tesztelése

@pytest.mark.parametrize(
    "amount, expected_balance",
    [
        (100.0, 900.0),
        (300.0, 700.0),
        (500.0, 500.0),
        (1000.0, 0.0),
    ]
)
def test_withdraw(account, amount, expected_balance):
    account.withdraw(amount)
    assert account.get_balance() == expected_balance


@pytest.mark.parametrize("invalid_amount", [0, -10, -50.0])
def test_withdraw_invalid_amounts(account, invalid_amount):
    with pytest.raises(ValueError):
        account.withdraw(invalid_amount)

    assert account.get_balance() == 1000.0


@pytest.mark.parametrize("amount", [1001.0, 1500.0, 2000.0])
def test_withdraw_insufficient_funds(account, amount):
    with pytest.raises(ValueError):
        account.withdraw(amount)

    assert account.get_balance() == 1000.0


# 4. Átutalás tesztelése

@pytest.mark.parametrize(
    "amount, expected_sender, expected_receiver",
    [
        (100.0, 900.0, 600.0),
        (200.0, 800.0, 700.0),
        (500.0, 500.0, 1000.0),
        (1000.0, 0.0, 1500.0),
    ]
)
def test_transfer(
    account,
    second_account,
    amount,
    expected_sender,
    expected_receiver
):
    account.transfer(amount, second_account)

    assert account.get_balance() == expected_sender
    assert second_account.get_balance() == expected_receiver


@pytest.mark.parametrize("amount", [1001.0, 1500.0, 2000.0])
def test_transfer_insufficient_funds(account, second_account, amount):
    with pytest.raises(ValueError):
        account.transfer(amount, second_account)

    assert account.get_balance() == 1000.0
    assert second_account.get_balance() == 500.0


def test_transfer_invalid_account(account):
    with pytest.raises(TypeError):
        account.transfer(100.0, "Anna")

    assert account.get_balance() == 1000.0


@pytest.mark.parametrize("invalid_amount", [0, -10, -100.0])
def test_transfer_invalid_amount(account, second_account, invalid_amount):
    with pytest.raises(ValueError):
        account.transfer(invalid_amount, second_account)

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

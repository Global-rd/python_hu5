import pytest

from bank_account import BankAccount


# A fixture minden teszthez új számlát készít.
@pytest.fixture
def account():
    return BankAccount("Anikó", 1000)


@pytest.fixture
def target_account():
    return BankAccount("Béla", 200)


# Létrehozás, alapértelmezett és megadott kezdőegyenleg.
def test_default_balance():
    account = BankAccount("Anikó")
    assert account.owner == "Anikó"
    assert account.get_balance() == 0


@pytest.mark.parametrize("balance", [0, 100, 12.5])
def test_initial_balance(balance):
    account = BankAccount("Anikó", balance)
    assert account.get_balance() == balance


@pytest.mark.parametrize("owner", [123, None, True])
def test_invalid_owner_type(owner):
    with pytest.raises(TypeError, match="Owner must be a string"):
        BankAccount(owner)


def test_negative_initial_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount("Anikó", -1)


# Az extra típusellenőrzés: a bool sem elfogadott pénzösszeg.
@pytest.mark.parametrize("balance", ["100", None, True, False, [], {}])
def test_invalid_balance_type(balance):
    with pytest.raises(TypeError, match="Balance must be a number"):
        BankAccount("Anikó", balance)


@pytest.mark.parametrize("balance", [float("nan"), float("inf"), -float("inf")])
def test_non_finite_balance(balance):
    with pytest.raises(ValueError, match="Balance must be finite"):
        BankAccount("Anikó", balance)


@pytest.mark.parametrize("amount", [1, 100, 12.5])
def test_deposit(account, amount):
    account.deposit(amount)
    assert account.get_balance() == pytest.approx(1000 + amount)


@pytest.mark.parametrize("amount", [1, 250, 12.5, 1000])
def test_withdraw(account, amount):
    account.withdraw(amount)
    assert account.get_balance() == pytest.approx(1000 - amount)


# A nulla és negatív összeg mindhárom műveletnél hibás.
@pytest.mark.parametrize("operation", ["deposit", "withdraw", "transfer"])
@pytest.mark.parametrize("amount", [0, -1, -12.5])
def test_non_positive_amount(account, target_account, operation, amount):
    with pytest.raises(ValueError, match="must be positive"):
        if operation == "transfer":
            account.transfer(amount, target_account)
        else:
            getattr(account, operation)(amount)
    assert account.get_balance() == 1000
    assert target_account.get_balance() == 200


@pytest.mark.parametrize("operation", ["deposit", "withdraw", "transfer"])
@pytest.mark.parametrize("amount", ["100", None, True, False, [], {}])
def test_invalid_amount_type(account, target_account, operation, amount):
    with pytest.raises(TypeError, match="Amount must be a number"):
        if operation == "transfer":
            account.transfer(amount, target_account)
        else:
            getattr(account, operation)(amount)
    assert account.get_balance() == 1000
    assert target_account.get_balance() == 200


@pytest.mark.parametrize("operation", ["deposit", "withdraw", "transfer"])
@pytest.mark.parametrize("amount", [float("nan"), float("inf"), -float("inf")])
def test_non_finite_amount(account, target_account, operation, amount):
    with pytest.raises(ValueError, match="Amount must be finite"):
        if operation == "transfer":
            account.transfer(amount, target_account)
        else:
            getattr(account, operation)(amount)
    assert account.get_balance() == 1000
    assert target_account.get_balance() == 200


# Sikertelen kivétnél és utalásnál sem változhat az egyenleg.
@pytest.mark.parametrize("operation", ["withdraw", "transfer"])
def test_insufficient_funds(account, target_account, operation):
    with pytest.raises(ValueError, match="Insufficient funds"):
        if operation == "transfer":
            account.transfer(1001, target_account)
        else:
            account.withdraw(1001)
    assert account.get_balance() == 1000
    assert target_account.get_balance() == 200


@pytest.mark.parametrize("amount", [100, 12.5, 1000])
def test_transfer(account, target_account, amount):
    account.transfer(amount, target_account)
    assert account.get_balance() == pytest.approx(1000 - amount)
    assert target_account.get_balance() == pytest.approx(200 + amount)
    assert account.get_balance() + target_account.get_balance() == pytest.approx(1200)


@pytest.mark.parametrize("target", [None, "Béla", 123, True, {}])
def test_invalid_transfer_target(account, target):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance"):
        account.transfer(100, target)
    assert account.get_balance() == 1000


def test_transfer_to_self(account):
    with pytest.raises(ValueError, match="Cannot transfer money to the same account"):
        account.transfer(100, account)
    assert account.get_balance() == 1000


def test_empty_account_withdrawal():
    account = BankAccount("Anikó")
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(1)
    assert account.get_balance() == 0


def test_string_representation(account):
    assert str(account) == "Account owner: Anikó, Balance: 1000.00"


def test_string_rounding():
    account = BankAccount("Anikó", 12.345)
    assert str(account) == "Account owner: Anikó, Balance: 12.35"

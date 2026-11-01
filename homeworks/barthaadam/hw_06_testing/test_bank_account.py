import pytest

from bank_account import BankAccount


# Minden tesztesethez új számla készül 1000 kezdőegyenleggel.
@pytest.fixture
def account():
    return BankAccount("Adam", 1000)


# Második, különálló számla az utalások ellenőrzéséhez.
@pytest.fixture
def other_account():
    return BankAccount("Anna", 500)


def test_account_creation(account):
    assert account.owner == "Adam"
    assert account.balance == 1000


def test_default_balance():
    new_account = BankAccount("New owner")

    assert new_account.balance == 0


@pytest.mark.parametrize("amount", [100, 250.5])
def test_deposit(account, amount):
    account.deposit(amount)

    assert account.balance == pytest.approx(1000 + amount)


def test_withdraw(account):
    account.withdraw(200)

    assert account.balance == 800


def test_transfer(account, other_account):
    account.transfer(300, other_account)

    assert account.balance == 700
    assert other_account.balance == 800


@pytest.mark.parametrize("amount", [0, -10])
def test_deposit_rejects_nonpositive_amount(account, amount):
    with pytest.raises(ValueError):
        account.deposit(amount)

    assert account.balance == 1000


@pytest.mark.parametrize("amount", [0, -10, 1001])
def test_withdraw_rejects_invalid_amount(account, amount):
    with pytest.raises(ValueError):
        account.withdraw(amount)

    assert account.balance == 1000


@pytest.mark.parametrize("amount", [0, -10, 1001])
def test_transfer_rejects_invalid_amount(account, other_account, amount):
    with pytest.raises(ValueError):
        account.transfer(amount, other_account)

    assert account.balance == 1000
    assert other_account.balance == 500


@pytest.mark.parametrize("recipient", [None, "Anna", 123])
def test_transfer_rejects_invalid_recipient(account, recipient):
    with pytest.raises(TypeError):
        account.transfer(100, recipient)

    assert account.balance == 1000


def test_transfer_rejects_same_account(account):
    with pytest.raises(ValueError):
        account.transfer(100, account)

    assert account.balance == 1000


@pytest.mark.parametrize("amount", ["100", None, True])
def test_methods_reject_nonnumeric_amounts(account, other_account, amount):
    with pytest.raises(TypeError):
        account.deposit(amount)

    with pytest.raises(TypeError):
        account.withdraw(amount)

    with pytest.raises(TypeError):
        account.transfer(amount, other_account)

    assert account.balance == 1000
    assert other_account.balance == 500


@pytest.mark.parametrize(
    "amount",
    [float("nan"), float("inf"), -float("inf")],
)
def test_methods_reject_nonfinite_amounts(account, other_account, amount):
    with pytest.raises(ValueError):
        account.deposit(amount)

    with pytest.raises(ValueError):
        account.withdraw(amount)

    with pytest.raises(ValueError):
        account.transfer(amount, other_account)

    assert account.balance == 1000
    assert other_account.balance == 500


@pytest.mark.parametrize(
    "balance",
    [-1, float("nan"), float("inf")],
)
def test_constructor_rejects_invalid_balance(balance):
    with pytest.raises(ValueError):
        BankAccount("Adam", balance)


@pytest.mark.parametrize("balance", ["100", None, True])
def test_constructor_rejects_nonnumeric_balance(balance):
    with pytest.raises(TypeError):
        BankAccount("Adam", balance)


def test_withdraw_entire_balance(account):
    account.withdraw(1000)

    assert account.balance == 0


def test_transfer_entire_balance(account, other_account):
    account.transfer(1000, other_account)

    assert account.balance == 0
    assert other_account.balance == 1500
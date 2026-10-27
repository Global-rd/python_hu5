
import pytest


from bank_account import BankAccount
# ===== Fixtures =====

@pytest.fixture
def source_account():
    return BankAccount("Tamás", 200)


@pytest.fixture
def target_account():
    return BankAccount("Anna", 50)


# ===== Constructor =====

def test_create_account_with_valid_balance():
    account = BankAccount("Tamás", 100)

    assert account.owner == "Tamás"
    assert account.balance == 100


def test_create_account_with_default_balance():
    account = BankAccount("Tamás")

    assert account.balance == 0.0


def test_create_account_with_negative_balance_raises_error():
    with pytest.raises(
        ValueError,
        match="Initial balance cannot be negative."
    ):
        BankAccount("Tamás", -100)


# ===== Deposit =====

def test_deposit_increases_balance(source_account):
    source_account.deposit(50)

    assert source_account.balance == 250


@pytest.mark.parametrize("amount", [0, -10, -100])
def test_deposit_non_positive_amount_raises_error(
    source_account,
    amount
):
    with pytest.raises(
        ValueError,
        match="Deposit amount must be positive."
    ):
        source_account.deposit(amount)


# ===== Withdraw =====

def test_withdraw_decreases_balance(source_account):
    source_account.withdraw(50)

    assert source_account.balance == 150


@pytest.mark.parametrize("amount", [0, -10, -100])
def test_withdraw_non_positive_amount_raises_error(
    source_account,
    amount
):
    with pytest.raises(
        ValueError,
        match="Withdraw amount must be positive."
    ):
        source_account.withdraw(amount)


def test_withdraw_insufficient_funds_raises_error(source_account):
    with pytest.raises(
        ValueError,
        match="Insufficient funds."
    ):
        source_account.withdraw(500)


# ===== Transfer =====

def test_transfer_moves_money_between_accounts(
    source_account,
    target_account
):
    source_account.transfer(75, target_account)

    assert source_account.balance == 125
    assert target_account.balance == 125


def test_transfer_invalid_target_raises_type_error(
    source_account
):
    with pytest.raises(
        TypeError,
        match="Target must be a BankAccount instance."
    ):
        source_account.transfer(50, "not_an_account")


def test_transfer_insufficient_funds_raises_error(
    source_account,
    target_account
):
    with pytest.raises(
        ValueError,
        match="Insufficient funds."
    ):
        source_account.transfer(1000, target_account)

    assert source_account.balance == 200
    assert target_account.balance == 50


# ===== get_balance =====

def test_get_balance_returns_current_balance(
    source_account
):
    assert source_account.get_balance() == 200


# ===== __str__ =====

def test_str_representation():
    account = BankAccount("Tamás", 123.456)

    assert (
        str(account)
        == "Account owner: Tamás, Balance: 123.46"
    )
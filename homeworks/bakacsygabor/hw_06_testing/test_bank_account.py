import pytest

from bank_account import BankAccount


@pytest.fixture
def account():
    return BankAccount("Alice", 100.0)


@pytest.fixture
def recipient():
    return BankAccount("Bob", 25.0)


def test_new_account_defaults_to_zero():
    account = BankAccount("Alice")
    assert account.get_balance() == 0
    assert str(account) == "Account owner: Alice, Balance: 0.00"


@pytest.mark.parametrize("initial_balance", [0, 12, 12.5])
def test_valid_initial_balance(initial_balance):
    assert BankAccount("Alice", initial_balance).get_balance() == initial_balance


@pytest.mark.parametrize("initial_balance", [-1, -0.01])
def test_negative_initial_balance_raises_value_error(initial_balance):
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount("Alice", initial_balance)


@pytest.mark.parametrize("amount", [1, 12.5])
def test_deposit_increases_balance(account, amount):
    account.deposit(amount)
    assert account.get_balance() == pytest.approx(100 + amount)


@pytest.mark.parametrize("amount", [0, -1, -0.01])
def test_deposit_rejects_nonpositive_amount_without_changing_balance(account, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(amount)
    assert account.get_balance() == 100


def test_withdraw_decreases_balance(account):
    account.withdraw(30)
    assert account.get_balance() == 70


def test_withdraw_entire_balance(account):
    account.withdraw(100)
    assert account.get_balance() == 0


@pytest.mark.parametrize("amount", [0, -5])
def test_withdraw_rejects_nonpositive_amount_without_changing_balance(account, amount):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        account.withdraw(amount)
    assert account.get_balance() == 100


def test_withdraw_rejects_insufficient_funds(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(101)
    assert account.get_balance() == 100


def test_transfer_moves_money_between_accounts(account, recipient):
    account.transfer(40, recipient)
    assert account.get_balance() == 60
    assert recipient.get_balance() == 65


def test_transfer_rejects_non_account_target_without_changing_balance(account):
    with pytest.raises(TypeError, match="Target must be a BankAccount"):
        account.transfer(10, object())
    assert account.get_balance() == 100


def test_transfer_rejects_insufficient_funds_without_changing_either_account(
    account, recipient
):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.transfer(101, recipient)
    assert (account.get_balance(), recipient.get_balance()) == (100, 25)


def test_transfer_to_self_is_rejected(account):
    with pytest.raises(ValueError, match="same account"):
        account.transfer(10, account)
    assert account.get_balance() == 100


@pytest.mark.parametrize("invalid", ["10", None, True, object()])
@pytest.mark.parametrize("operation", ["initial", "deposit", "withdraw"])
def test_non_numeric_amounts_raise_type_error(account, operation, invalid):
    with pytest.raises(TypeError, match="must be a number"):
        if operation == "initial":
            BankAccount("Alice", invalid)
        else:
            getattr(account, operation)(invalid)
    assert account.get_balance() == 100


@pytest.mark.parametrize("invalid", [float("nan"), float("inf"), -float("inf")])
@pytest.mark.parametrize("operation", ["initial", "deposit", "withdraw"])
def test_non_finite_amounts_raise_value_error(account, operation, invalid):
    with pytest.raises(ValueError, match="must be finite"):
        if operation == "initial":
            BankAccount("Alice", invalid)
        else:
            getattr(account, operation)(invalid)
    assert account.get_balance() == 100


def test_transfer_rejects_non_numeric_amount_without_changing_either_account(
    account, recipient
):
    with pytest.raises(TypeError, match="must be a number"):
        account.transfer("10", recipient)
    assert (account.get_balance(), recipient.get_balance()) == (100, 25)


def test_string_representation_displays_two_decimal_places(account):
    assert str(account) == "Account owner: Alice, Balance: 100.00"

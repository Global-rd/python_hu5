import pytest
from bank_account import BankAccount

# fixtures for test

@pytest.fixture
def empty_account():
    return BankAccount(owner="DrWho", balance=0.0)

@pytest.fixture
def account_with_balance():
    return BankAccount(owner="MrNobody", balance=111.0)


# function testing

def test_initial_balance(empty_account, account_with_balance):
    assert empty_account.get_balance() == 0.0
    assert account_with_balance.get_balance() == 111.0

def test_deposit(empty_account):
    empty_account.deposit(55.6)
    assert empty_account.get_balance() == 55.6

def test_withdrawal(account_with_balance):
    account_with_balance.withdraw(29.9)
    assert account_with_balance.get_balance() == 81.1

def test_transfer(account_with_balance, empty_account):
    account_with_balance.transfer(44.0, empty_account)
    assert account_with_balance.get_balance() == 67.0
    assert empty_account.get_balance() == 44.0


@pytest.mark.parametrize("initial_balance, deposit_amount, expected_balance", [
    (5.0, 100.0, 105.0),
    (60.0, 50.0, 110.0),
    (90.0, 1.0, 91.0)
])
def test_deposit_parametrized(account_with_balance, initial_balance, deposit_amount, expected_balance):
    account_with_balance.balance = initial_balance
    account_with_balance.deposit(deposit_amount)
    assert account_with_balance.get_balance() == expected_balance

# invalid transfer fail

def test_transfer_to_unknown(account_with_balance):
    with pytest.raises(TypeError):
        account_with_balance.transfer(10.0, "Unknown")

def test_transfer_to_same_account(account_with_balance):
    with pytest.raises(ValueError):
        account_with_balance.transfer(20.0, account_with_balance)

@pytest.mark.parametrize("owner, balance, expected_exception", [
    ("Alice", -10.0, ValueError),   # neg balance
    (123, 100.0, TypeError),        # non-string name
    (None, 100.0, TypeError),       # none
    ("Alice", "100", TypeError),    # str balance
    ("Alice", None, TypeError),     # none as balance
])

def test_init_invalid_inputs(owner, balance, expected_exception):
    with pytest.raises(expected_exception):
        BankAccount(owner, balance)

def test_transfer_insufficient_funds(account_with_balance, empty_account):
    with pytest.raises(ValueError):
        account_with_balance.transfer(200.0, empty_account)

@pytest.mark.parametrize("invalid_amount, expected_exception", [
    (0, ValueError),
    (-25.0, ValueError),
    ("30", TypeError),
    (None, TypeError),
])

def test_transfer_invalid_amount_extra(account_with_balance, empty_account, invalid_amount, expected_exception):
    with pytest.raises(expected_exception):
        account_with_balance.transfer(invalid_amount, empty_account)


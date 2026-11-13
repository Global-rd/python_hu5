# test
# telepítsd fel a pytest-tet

import pytest
from bank_account import BankAccount

# --- Fixtures ---
@pytest.fixture
def basic_account():
    """Default bank account with a balance of 100.0."""
    return BankAccount("Alice", 100.0)

@pytest.fixture
def rich_account():
    """Wealthier bank account with a balance of 1000.0."""
    return BankAccount("Bob", 1000.0)


# --- Basic Tests and Parametrization ---
def test_initial_creation(basic_account):
    assert basic_account.owner == "Alice"
    assert basic_account.get_balance() == 100.0
    assert str(basic_account) == "Account owner: Alice, Balance: 100.00"

@pytest.mark.parametrize("invalid_deposit", [0, -50.0, -0.01])
def test_deposit_invalid_amounts(basic_account, invalid_deposit):
    """Test deposit() method with 0 and negative inputs using @pytest.mark.parametrize."""
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        basic_account.deposit(invalid_deposit)

@pytest.mark.parametrize("valid_deposit, expected_balance", [
    (50.0, 150.0),
    (100, 200.0),  # Test integer input as well
])
def test_deposit_valid_amounts(basic_account, valid_deposit, expected_balance):
    basic_account.deposit(valid_deposit)
    assert basic_account.get_balance() == expected_balance


# --- Exception Handling Tests ---
def test_initial_negative_balance_raises_error():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("Charlie", -10.0)

def test_withdraw_insufficient_funds(basic_account):
    with pytest.raises(ValueError, match="Insufficient funds."):
        basic_account.withdraw(150.0)

def test_withdraw_negative_amount(basic_account):
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        basic_account.withdraw(-20.0)


# --- Edge Cases and Extra Additions Tests ---
def test_transfer_to_non_bank_account(basic_account):
    """Edge case: transferring money to a non-BankAccount object (e.g., string or number)."""
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        basic_account.transfer(50.0, "not_an_account")  # type: ignore

def test_transfer_to_self(basic_account):
    """Edge case: prevent transferring money to the same account."""
    with pytest.raises(ValueError, match="Cannot transfer money to the same account."):
        basic_account.transfer(20.0, basic_account)

def test_successful_transfer(basic_account, rich_account):
    """Test successful money transfer between two valid accounts."""
    rich_account.transfer(250.0, basic_account)
    assert rich_account.get_balance() == 750.0
    assert basic_account.get_balance() == 350.0

@pytest.mark.parametrize("invalid_type_input", ["100", None, True, [50]])
def test_non_number_inputs_raise_type_error(basic_account, invalid_type_input):
    """Test extra validation: non-numeric inputs (e.g., string, bool, None) raise TypeError."""
    with pytest.raises(TypeError):
        basic_account.deposit(invalid_type_input)  # type: ignore

    with pytest.raises(TypeError):
        basic_account.withdraw(invalid_type_input)  # type: ignore

    with pytest.raises(TypeError):
        BankAccount("Dave", invalid_type_input)  # type: ignore

def test_invalid_owner_name():
    """Test extra validation: empty or non-string owner name."""
    with pytest.raises(ValueError, match="Owner must be a non-empty string."):
        BankAccount("", 100.0)
    
    with pytest.raises(ValueError, match="Owner must be a non-empty string."):
        BankAccount(123, 100.0)  # type: ignore

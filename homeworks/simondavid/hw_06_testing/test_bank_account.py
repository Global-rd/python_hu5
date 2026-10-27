
import pytest
from bank_account import BankAccount



# FIXTURES - Reusable test accounts


@pytest.fixture
def account_1():
    return BankAccount("David", 1000)


@pytest.fixture
def account_2():
    return BankAccount("Peter", 500)



# ACCOUNT INITIALIZATION AND REPRESENTATION
#=======================================================

# Verify that a new account has the correct initial balance.
def test_initial_balance(account_1):
    assert account_1.get_balance() == 1000


# Verify that a negative initial balance raises a ValueError.
def test_negative_initial_balance():
    with pytest.raises(ValueError):
        BankAccount("Test", -500)


# Verify that the account's string representation is correct.
def test_account_str(account_1):
    expected = "Account Owner: David, Balance: 1000.00"

    assert str(account_1) == expected


# Verify that non-string account owner names raise a TypeError.
@pytest.mark.parametrize("owner", [123, None, True, ["David"]])
def test_invalid_owner_type(owner):
    with pytest.raises(TypeError):
        BankAccount(owner, 1000)


# Verify that empty or whitespace-only owner names raise a ValueError.
@pytest.mark.parametrize("owner", ["", " ", "   "])
def test_empty_owner(owner):
    with pytest.raises(ValueError):
        BankAccount(owner, 1000)


# Verify that non-numeric initial balances raise a TypeError.
@pytest.mark.parametrize("balance", ["1000", None, True, [1000]])
def test_invalid_initial_balance_type(balance):
    with pytest.raises(TypeError):
        BankAccount("David", balance)


# Verify that NaN and infinite initial balances raise a ValueError.
@pytest.mark.parametrize("balance", [
    float("nan"),
    float("inf"),
    float("-inf")
])
def test_non_finite_initial_balance(balance):
    with pytest.raises(ValueError):
        BankAccount("David", balance)



# DEPOSIT TESTS
#===================================================================

# Verify that depositing money increases the account balance.
def test_deposit(account_1):
    account_1.deposit(250)

    assert account_1.get_balance() == 1250


# Test multiple deposit amounts using parametrization.
@pytest.mark.parametrize("amount", [100, 250, 500])
def test_deposit_multiple_amounts(account_1, amount):
    account_1.deposit(amount)

    assert account_1.get_balance() == 1000 + amount


# Verify that a negative deposit raises a ValueError.
def test_negative_deposit(account_1):
    with pytest.raises(ValueError):
        account_1.deposit(-100)

# Verify that non-numeric deposit amounts raise a TypeError and leave the account balance unchanged.
@pytest.mark.parametrize("amount", ["100", None, True, [100]])
def test_invalid_deposit_type(account_1, amount):
    with pytest.raises(TypeError):
        account_1.deposit(amount)

    assert account_1.get_balance() == 1000


# WITHDRAWAL TESTS
#=====================================================================

# Verify that withdrawing money decreases the account balance.
def test_withdraw(account_1):
    account_1.withdraw(300)

    assert account_1.get_balance() == 700


# Verify that a negative withdrawal raises a ValueError
# and leaves the account balance unchanged.
def test_negative_withdraw(account_1):
    with pytest.raises(ValueError):
        account_1.withdraw(-100)

    assert account_1.get_balance() == 1000


# Verify that withdrawing more than the available balance raises a ValueError.

def test_insufficient_funds(account_1):
    with pytest.raises(ValueError):
        account_1.withdraw(1500)

# Verify that non-numeric withdrawal amounts raise a TypeError and leave the account balance unchanged.
@pytest.mark.parametrize("amount", ["100", None, True, [100]])
def test_invalid_withdraw_type(account_1, amount):
    with pytest.raises(TypeError):
        account_1.withdraw(amount)

    assert account_1.get_balance() == 1000


# TRANSFER TESTS
#====================================================================================

# Verify that transferring money updates both account balances.
def test_transfer(account_1, account_2):
    account_1.transfer(300, account_2)

    assert account_1.get_balance() == 700
    assert account_2.get_balance() == 800


# Verify that a negative transfer raises a ValueError and leaves both account balances unchanged.
def test_negative_transfer(account_1, account_2):
    with pytest.raises(ValueError):
        account_1.transfer(-100, account_2)

    assert account_1.get_balance() == 1000
    assert account_2.get_balance() == 500


# Verify that a transfer with insufficient funds fails without modifying either account balance. 
def test_failed_transfer(account_1, account_2):
    with pytest.raises(ValueError):
        account_1.transfer(1500, account_2)

    assert account_1.get_balance() == 1000
    assert account_2.get_balance() == 500


# Verify that transferring money to the same account does not change its balance.
def test_transfer_to_self(account_1):
    with pytest.raises(ValueError):
        account_1.transfer(300, account_1)

    assert account_1.get_balance() == 1000

# Verify transferring to an invalid account type raises a TypeError and leaves the balance unchanged.
def test_transfer_invalid_account(account_1):
    with pytest.raises(TypeError):
        account_1.transfer(100, "Peter")

    assert account_1.get_balance() == 1000


# Verify that non-numeric transfer amounts raise a TypeError and leave both account balances unchanged.
@pytest.mark.parametrize("amount", ["100", None, True, [100]])
def test_invalid_transfer_type(account_1, account_2, amount):
    with pytest.raises(TypeError):
        account_1.transfer(amount, account_2)

    assert account_1.get_balance() == 1000
    assert account_2.get_balance() == 500


# Verify that NaN and infinite transfer amounts raise a ValueError and leave both account balances unchanged.
@pytest.mark.parametrize("amount", [
    float("nan"),
    float("inf"),
    float("-inf")
])
def test_non_finite_transfer(account_1, account_2, amount):
    with pytest.raises(ValueError):
        account_1.transfer(amount, account_2)

    assert account_1.get_balance() == 1000
    assert account_2.get_balance() == 500





# EDGE CASES - ZERO AMOUNT TRANSACTIONS
#=====================================================================================================

# Verify that zero-value deposits and withdrawals raise a ValueError without modifying the balance.
@pytest.mark.parametrize("method", ["deposit", "withdraw"])
def test_zero_amount(account_1, method):
    with pytest.raises(ValueError):
        getattr(account_1, method)(0)

    assert account_1.get_balance() == 1000


# Verify that NaN and infinite values are rejected and the account balance remains unchanged.
@pytest.mark.parametrize("amount", [
    float("nan"),
    float("inf"),
    float("-inf")
])
@pytest.mark.parametrize("method", ["deposit", "withdraw"])
def test_non_finite_amount(account_1, method, amount):
    with pytest.raises(ValueError):
        getattr(account_1, method)(amount)

    assert account_1.get_balance() == 1000

import pytest
from bank_account import BankAccount

# creating an empty account fixture
@pytest.fixture
def empty_account():
    return BankAccount()

# creating an account with a balance fixture
@pytest.fixture
def account_with_balance():
    account = BankAccount("Johny Cash", 100.0)
    return account

# creating another account fixture
@pytest.fixture
def account_another():
    another_account = BankAccount("Mary Gold", 200.0)
    return another_account

# testing the initialization of the BankAccount class
def test_account_initialization_expected_way():
    account = BankAccount("Johny Cash", 100.0)
    assert account.owner == "Johny Cash"
    assert account.get_balance() == 100.0

# testing the deposit method
def test_deposit_changes_balance_expected_way(account_with_balance):
    account_with_balance.deposit(50.0)
    assert account_with_balance.get_balance() == 150.0

# testing the withdraw method
def test_withdraw_changes_balance_expected_way(account_with_balance):
    account_with_balance.withdraw(30.0)
    assert account_with_balance.get_balance() == 70.0

# testing the transfer method
def test_transfer_changes_balance_expected_way(account_with_balance):
    another_account = BankAccount("Mary Gold", 200.0)
    account_with_balance.transfer(50.0, another_account)
    assert account_with_balance.get_balance() == 50.0
    assert another_account.get_balance() == 250.0

# testing the deposit method with invalid target
def test_transfer_to_non_bank_account(account_with_balance):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_with_balance.transfer(50.0, "not_a_bank_account")

# testing the transfer method with self as target
def test_transfer_to_self(account_with_balance):
    with pytest.raises(ValueError, match="Cannot transfer money to the same account."):
        account_with_balance.transfer(50.0, account_with_balance)

# testing invalid initialization of the BankAccount class
@pytest.mark.parametrize("owner, balance, expected_exception", 
                         [
                             (13, 100.0, TypeError),
                             ("", 100.0, ValueError),
                             ("Johny Cash", 0.0, ValueError),
                             ("Johny Cash", -100.0, ValueError),
                         ])
def test_account_initialization_invalid_input(owner, balance, expected_exception):
    with pytest.raises(expected_exception):
        BankAccount(owner, balance)

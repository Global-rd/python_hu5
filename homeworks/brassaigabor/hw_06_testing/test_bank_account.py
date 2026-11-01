
import pytest
from bank_account import BankAccount


@pytest.fixture
def create_zero_account():
    return BankAccount("Gipsz Jakab")

@pytest.fixture
def create_funded_account():
    return BankAccount("Gipsz Jakab", 1000), BankAccount("Nagy Lajos", 0)

def test_deposit_account(create_zero_account):
    acc = create_zero_account
    acc.deposit(1000)
    assert acc.balance == 1000

def test_withdraw_account(create_funded_account):
    acc1, _ = create_funded_account
    acc1.withdraw(1000)
    assert acc1.balance == 0
    
def test_transfer(create_funded_account):
    acc1, acc2 = create_funded_account
    acc1.transfer(1000, acc2)
    assert acc1.balance == 0
    assert acc2.balance == 1000

@pytest.mark.parametrize("amount", [0, -1])
def test_deposit_zero_or_negativ_amount(create_zero_account, amount):
    with pytest.raises(ValueError):
        create_zero_account.deposit(amount)

@pytest.mark.parametrize("amount, expected_balance",
                         [
                             (1000, 0),
                             (999.99, 0.01),
                             (500, 500)
                             ]
                         )
def test_withdraw_on_edge(create_funded_account, amount, expected_balance):
    acc, _ = create_funded_account
    acc.withdraw(amount)
    assert acc.balance == pytest.approx(expected_balance)

def test_withdraw(create_funded_account):
    acc, _ = create_funded_account
    with pytest.raises(ValueError):
        acc.withdraw(2000)

@pytest.mark.parametrize("owner", ["Gipsz Jakab", 1, None, True])
def test_transfer_with_non_BankAccount(create_funded_account, owner):
    acc, _= create_funded_account
    with pytest.raises(TypeError):
        acc.transfer(1000, owner)
    assert acc.balance == 1000

def test_transfer_to_myself(create_funded_account):
    acc1, acc2 = create_funded_account
    with pytest.raises(ValueError):
        acc1.transfer(100, acc1)
    assert acc1.balance == 1000

@pytest.mark.parametrize("balance", [-1, -0.01])
def test_create_acc_with_negativ_balance(balance):
    with pytest.raises(ValueError):
        BankAccount("Gipsz Jakab", balance)

@pytest.mark.parametrize("balance", ["asd", "100", True, False, None])
def test_create_acc_with_non_numeric(balance):
    with pytest.raises(TypeError):
        BankAccount("Gipsz Jakab", balance)

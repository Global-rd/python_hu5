import pytest
from bank_account import BankAccount


@pytest.fixture
def create_account():
    return BankAccount("Owner", 100)


@pytest.fixture
def create_target_account():
    return BankAccount("Target", 100)


def test_create_account(create_account):
    assert create_account.owner == "Owner"
    assert create_account.balance == 100


@pytest.mark.parametrize("amount, expected_exception", [("ten", ValueError), (None, ValueError), (-20, ValueError)])

def test_create_account_with_invalid_balance(amount, expected_exception):
    with pytest.raises(expected_exception):
        BankAccount("Owner", amount)


def test_depositing_amount(create_account):
    create_account.deposit(10)
    assert create_account.balance == 110


@pytest.mark.parametrize("amount, expected_exception", [("ten", ValueError), (None, ValueError), ((10, 10, 10), ValueError)])

def test_depositing_non_number_amount(create_account, amount, expected_exception):
    with pytest.raises(expected_exception):    
        create_account.deposit(amount)


@pytest.mark.parametrize("amount, expected_exception", [(0, ValueError), (-20, ValueError)])

def test_deposit_invalid_amount(create_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        create_account.deposit(amount)
    

def test_withdrawing_amount(create_account):
    create_account.withdraw(10)
    assert create_account.balance == 90


@pytest.mark.parametrize("amount, expected_exception", [("ten", ValueError), (None, ValueError), ((10, 10, 10), ValueError)])

def test_withdrawing_non_number_amount(create_account, amount, expected_exception):
    with pytest.raises(expected_exception):    
        create_account.withdraw(amount)


@pytest.mark.parametrize("amount, expected_exception", [(0, ValueError), (-20, ValueError), (110, ValueError)])

def test_withdraw_invalid_amount(create_account, amount , expected_exception):
    with pytest.raises(expected_exception):
        create_account.withdraw(amount)


def test_transfer(create_account, create_target_account):
    create_account.transfer(20, create_target_account)
    assert create_account.balance == 80
    assert create_target_account.balance == 120


def test_self_transfer():
    account = BankAccount("Owner", 100)
    with pytest.raises(ValueError):
        account.transfer(100, account)


@pytest.mark.parametrize("amount, expected_exception", [("ten", ValueError), (None, ValueError), ((10, 10, 10), ValueError)])

def test_transfer_non_number_amount(create_account, amount, create_target_account, expected_exception):
    with pytest.raises(expected_exception):    
         create_account.transfer(amount, create_target_account)
       

@pytest.mark.parametrize("amount, expected_exception", [(0, ValueError), (-20, ValueError)])

def test_transfer_invalid_amount(create_account, amount, create_target_account, expected_exception):
    with pytest.raises(expected_exception):
        create_account.transfer(amount, create_target_account)


@pytest.mark.parametrize("target, expected_exception", [(None, TypeError), ("Target", TypeError), ({"Target" : 100}, TypeError)])

def test_transfer_non_bank_object(create_account, target, expected_exception):
    with pytest.raises(expected_exception):
        create_account.transfer(10, target)


def test_get_balance(create_account):
    create_account.get_balance()
    assert create_account.balance == 100


def test_bank_object_representation(create_account):
    assert str(create_account) == "Account owner: Owner, Balance: 100.00"
import pytest
from bank_account import BankAccount

@pytest.fixture
def empty_balance():
    return BankAccount("TesztElek", balance=0)

@pytest.fixture
def bank_account_with_balance():
    bank_account = BankAccount("TesztElek", balance=0)
    bank_account.deposit(500)
    bank_account.deposit(800)
    return bank_account

def test_deposit(empty_balance):
    empty_balance.deposit(500)
    assert empty_balance.balance == 500

def test_withdraw(bank_account_with_balance):
    bank_account_with_balance.withdraw(300)
    assert bank_account_with_balance.balance == 1000

def test_withdraw_money(bank_account_with_balance):
    bank_account_with_balance.withdraw(1300)
    assert bank_account_with_balance.balance == 0

def test_withdraw_money(bank_account_with_balance):
    with pytest.raises(ValueError):
        bank_account_with_balance.withdraw(1500)

    assert bank_account_with_balance.balance == 1300

@pytest.mark.parametrize("deposit, expected_exception",
                         [
                             (-200, ValueError),
                             (0, ValueError),
                         ])
def test_deposit_invalid_input(empty_balance, deposit, expected_exception):
    with pytest.raises(expected_exception):
        empty_balance.deposit(deposit)


@pytest.mark.parametrize("amount, target_account, expected_exception",
                         [
                             (200, "Steve", TypeError),
                         ])
def test_transfer_invalid_input(empty_balance, amount, target_account, expected_exception):
    with pytest.raises(expected_exception):
        empty_balance.transfer(amount, target_account)

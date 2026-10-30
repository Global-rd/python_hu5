import pytest
from bank_account import BankAccount
from unittest.mock import patch

#tesztelni az exceptionoket
#befizetésnél emelkedik-e a balance
#átutalásnál emelkedik-e a másik számlán a pénz
#átutalásnál csökken-e a balance
#homeworks/nadudvarivirag/hw_06_testing

# 2 fixture
@pytest.fixture
def founded_account():
    return BankAccount("Kovács Jenő", 7000)

@pytest.fixture
def empty_account():
    return BankAccount("Szlávik János", 0)

def test_add_deposit_change_expected_way(empty_account):
    empty_account.deposit(6400)
    assert empty_account.owner == "Szlávik János"
    assert empty_account.balance == 6400

def test_withdraw_decrease_amount_expected_way(founded_account):
    founded_account.withdraw(2000)
    assert founded_account.balance == 5000

# pytest mark parametrize
# 1. Invalid withdraw
@pytest.mark.parametrize("amount , expected_exception",
                        [
                        (-4000, ValueError),
                        (9000, ValueError ),
                        ],)

def test_invalid_withdraw(founded_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        founded_account.withdraw(amount)

# 2. Invalid deposit
@pytest.mark.parametrize("amount , expected_exception",
                        [
                        (0, ValueError),
                        (-9000, ValueError ),
                        ],)

def test_invalid_deposit(empty_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        empty_account.deposit(amount)

# edge case - transfer for not BankAccount objekt

@pytest.mark.parametrize("amount, target_account, expected_exception",
                        [
                            (6000,"Kovács Juliska", TypeError),
                            (None, empty_account, TypeError ),
                            (2000, 600, TypeError),
                        ],)

def test_invalid_transfers(founded_account, amount, target_account, expected_exception):
    with pytest.raises(expected_exception):
        founded_account.transfer(amount,target_account)

# transfer decrease and increase amounts in the expected ways

def test_transfer_decrease_sender_account_and_increase_target_account(founded_account,empty_account):
    founded_account.transfer(7000,empty_account)
    assert founded_account.balance == 0
    assert empty_account.balance == 7000
import pytest
from bank_account import BankAccount


@pytest.fixture
def account():
    return BankAccount("Miklos", 1000.0)


@pytest.fixture
def second_account():
    return BankAccount("Anna", 500.0)


def test_initial_balance(account):
    assert account.owner == "Miklos"
    assert account.get_balance() == 1000.0

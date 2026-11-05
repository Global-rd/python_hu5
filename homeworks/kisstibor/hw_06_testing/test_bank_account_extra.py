"""A bank_account_extra.py kiegészítéseinek tesztjei."""
import pytest

from bank_account_extra import BankAccount


@pytest.fixture
def lili():
    return BankAccount("Lili", 100.0)


@pytest.fixture
def anna():
    return BankAccount("Anna", 50.0)


@pytest.mark.parametrize("bad", ["10", None, [1], True, 1 + 2j])
def test_amount_wrong_type_raises_typeerror(lili, bad):
    for method in (lili.deposit, lili.withdraw):
        with pytest.raises(TypeError):
            method(bad)
    with pytest.raises(TypeError):
        lili.transfer(bad, BankAccount("X", 1))
    assert lili.get_balance() == 100.0


@pytest.mark.parametrize("bad", [float("nan"), float("inf"), float("-inf")])
def test_amount_nan_inf_raises(lili, bad):
    with pytest.raises(ValueError):
        lili.deposit(bad)
    with pytest.raises(ValueError):
        lili.withdraw(bad)
    assert lili.get_balance() == 100.0


@pytest.mark.parametrize("amount", [0, -3])
def test_non_positive_still_raises(lili, amount):
    with pytest.raises(ValueError, match="positive"):
        lili.deposit(amount)
    with pytest.raises(ValueError, match="positive"):
        lili.withdraw(amount)


def test_transfer_to_self_raises(lili):
    with pytest.raises(ValueError, match="same account"):
        lili.transfer(10, lili)
    assert lili.get_balance() == 100.0


def test_transfer_to_non_account_raises(lili):
    with pytest.raises(TypeError):
        lili.transfer(10, "Anna")


def test_transfer_invalid_amount_leaves_accounts_unchanged(lili, anna):
    with pytest.raises(TypeError):
        lili.transfer("10", anna)
    with pytest.raises(ValueError):
        lili.transfer(1000, anna)
    assert (lili.get_balance(), anna.get_balance()) == (100.0, 50.0)


def test_valid_operations_still_work(lili, anna):
    lili.deposit(10)
    lili.withdraw(20)
    lili.transfer(30, anna)
    assert lili.get_balance() == 60
    assert anna.get_balance() == 80


@pytest.mark.parametrize("owner,exc", [(123, TypeError), (None, TypeError),
                                       ("", ValueError), ("   ", ValueError)])
def test_invalid_owner(owner, exc):
    with pytest.raises(exc):
        BankAccount(owner)


@pytest.mark.parametrize("balance,exc", [("5", TypeError), (None, TypeError),
                                         (True, TypeError), (-1, ValueError),
                                         (float("nan"), ValueError),
                                         (float("inf"), ValueError)])
def test_invalid_initial_balance(balance, exc):
    with pytest.raises(exc):
        BankAccount("Tibi", balance)


def test_str(anna):
    assert str(anna) == "Account owner: Anna, Balance: 50.00"

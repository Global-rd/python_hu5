"""
Unit tesztek a BankAccount osztályhoz (pytest).
 
Futtatás a hw_06_testing mappából:
    pytest -v
"""
 
import pytest
 
from bank_account import BankAccount
 
 
# ======================================================================
# FIXTURE-ÖK – két különböző BankAccount objektum
# ======================================================================
@pytest.fixture
def anna_account():
    """Számla 1000-es kezdő egyenleggel."""
    return BankAccount("Anna", 1000.0)
 
 
@pytest.fixture
def bela_account():
    """Számla alapértelmezett (0) kezdő egyenleggel."""
    return BankAccount("Béla")
 
 
# ======================================================================
# __init__
# ======================================================================
def test_init_with_balance(anna_account):
    assert anna_account.owner == "Anna"
    assert anna_account.balance == 1000.0
 
 
def test_init_default_balance_is_zero(bela_account):
    assert bela_account.get_balance() == 0.0
 
 
def test_init_negative_balance_raises():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount("Csaba", -1)
 
 
# ======================================================================
# deposit
# ======================================================================
def test_deposit_increases_balance(anna_account):
    anna_account.deposit(500)
    assert anna_account.get_balance() == 1500.0
 
 
def test_deposit_float_amount(bela_account):
    bela_account.deposit(0.01)
    assert bela_account.get_balance() == pytest.approx(0.01)
 
 
@pytest.mark.parametrize("amount", [0, -1, -0.01, -1000])
def test_deposit_zero_or_negative_raises(anna_account, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        anna_account.deposit(amount)
    # sikertelen befizetés után az egyenleg nem változhat
    assert anna_account.get_balance() == 1000.0
 
 
# ======================================================================
# withdraw
# ======================================================================
def test_withdraw_decreases_balance(anna_account):
    anna_account.withdraw(300)
    assert anna_account.get_balance() == 700.0
 
 
def test_withdraw_entire_balance(anna_account):
    # edge case: pontosan a teljes egyenleg felvehető
    anna_account.withdraw(1000)
    assert anna_account.get_balance() == 0
 
 
@pytest.mark.parametrize("amount", [0, -5, -0.5])
def test_withdraw_zero_or_negative_raises(anna_account, amount):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        anna_account.withdraw(amount)
 
 
@pytest.mark.parametrize("amount", [1000.01, 2000])
def test_withdraw_insufficient_funds_raises(anna_account, amount):
    with pytest.raises(ValueError, match="Insufficient funds"):
        anna_account.withdraw(amount)
    assert anna_account.get_balance() == 1000.0
 
 
def test_withdraw_from_empty_account_raises(bela_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        bela_account.withdraw(1)
 
 
# ======================================================================
# transfer
# ======================================================================
def test_transfer_moves_money(anna_account, bela_account):
    anna_account.transfer(250, bela_account)
    assert anna_account.get_balance() == 750.0
    assert bela_account.get_balance() == 250.0
 
 
@pytest.mark.parametrize("target", ["Béla", None, 123, {"balance": 0}])
def test_transfer_to_non_bankaccount_raises(anna_account, target):
    # edge case: pénz küldése nem BankAccount objektumnak
    with pytest.raises(TypeError, match="Target must be a BankAccount"):
        anna_account.transfer(100, target)
    assert anna_account.get_balance() == 1000.0
 
 
def test_transfer_insufficient_funds_changes_nothing(anna_account, bela_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        bela_account.transfer(10, anna_account)
    assert anna_account.get_balance() == 1000.0
    assert bela_account.get_balance() == 0.0
 
 
@pytest.mark.parametrize("amount", [0, -100])
def test_transfer_zero_or_negative_raises(anna_account, bela_account, amount):
    with pytest.raises(ValueError):
        anna_account.transfer(amount, bela_account)
    assert anna_account.get_balance() == 1000.0
    assert bela_account.get_balance() == 0.0
 
 
# ======================================================================
# get_balance, __str__
# ======================================================================
def test_get_balance(anna_account):
    assert anna_account.get_balance() == anna_account.balance
 
 
def test_str_format(anna_account, bela_account):
    assert str(anna_account) == "Account owner: Anna, Balance: 1000.00"
    assert str(bela_account) == "Account owner: Béla, Balance: 0.00"
 
 
# ======================================================================
# EXTRA – a kiegészítések tesztjei
# ======================================================================
NON_NUMBERS = ["100", None, [10], {"x": 1}, True, False]
 
 
@pytest.mark.parametrize("amount", NON_NUMBERS)
def test_deposit_non_number_raises(anna_account, amount):
    with pytest.raises(TypeError, match="must be a number"):
        anna_account.deposit(amount)
    assert anna_account.get_balance() == 1000.0
 
 
@pytest.mark.parametrize("amount", NON_NUMBERS)
def test_withdraw_non_number_raises(anna_account, amount):
    with pytest.raises(TypeError, match="must be a number"):
        anna_account.withdraw(amount)
 
 
@pytest.mark.parametrize("amount", NON_NUMBERS)
def test_transfer_non_number_raises(anna_account, bela_account, amount):
    with pytest.raises(TypeError, match="must be a number"):
        anna_account.transfer(amount, bela_account)
    assert anna_account.get_balance() == 1000.0
    assert bela_account.get_balance() == 0.0
 
 
@pytest.mark.parametrize("balance", ["500", None, True])
def test_init_non_number_balance_raises(balance):
    with pytest.raises(TypeError, match="must be a number"):
        BankAccount("Dóra", balance)
 
 
@pytest.mark.parametrize("amount", [float("nan"), float("inf"), float("-inf")])
def test_deposit_nan_or_inf_raises(anna_account, amount):
    with pytest.raises(ValueError, match="finite number"):
        anna_account.deposit(amount)
    assert anna_account.get_balance() == 1000.0
 
 
@pytest.mark.parametrize("balance", [float("nan"), float("inf")])
def test_init_nan_or_inf_balance_raises(balance):
    with pytest.raises(ValueError, match="finite number"):
        BankAccount("Emma", balance)
 
 
def test_transfer_to_self_raises(anna_account):
    with pytest.raises(ValueError, match="same account"):
        anna_account.transfer(100, anna_account)
    assert anna_account.get_balance() == 1000.0
 
 
@pytest.mark.parametrize("owner", [None, 123, ["Anna"]])
def test_init_owner_not_string_raises(owner):
    with pytest.raises(TypeError, match="Owner must be a string"):
        BankAccount(owner, 100)
 
 
@pytest.mark.parametrize("owner", ["", "   "])
def test_init_owner_empty_raises(owner):
    with pytest.raises(ValueError, match="Owner cannot be empty"):
        BankAccount(owner, 100)

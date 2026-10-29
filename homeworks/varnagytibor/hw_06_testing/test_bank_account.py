import pytest

from bank_account import BankAccount


#--- fixture-ök: két különböző BankAccount objektum ---

@pytest.fixture
def alice_account():
    """Számla 100-as kezdő egyenleggel."""
    return BankAccount("Alice", 100.0)


@pytest.fixture
def bob_account():
    """Üres számla (alapértelmezett 0 egyenleg)."""
    return BankAccount("Bob")


#--- létrehozás ---

def test_create_account_with_balance(alice_account):
    assert alice_account.owner == "Alice"
    assert alice_account.get_balance() == 100.0


def test_create_account_default_balance_is_zero(bob_account):
    assert bob_account.get_balance() == 0.0


def test_negative_initial_balance_raises():
    with pytest.raises(ValueError, match="cannot be negative"):
        BankAccount("Carol", -50)


def test_str(alice_account):
    assert str(alice_account) == "Account owner: Alice, Balance: 100.00"


#--- deposit ---

def test_deposit_increases_balance(alice_account):
    alice_account.deposit(50)
    assert alice_account.get_balance() == 150.0


def test_deposit_float_amount(bob_account):
    bob_account.deposit(10.5)
    assert bob_account.get_balance() == pytest.approx(10.5)


@pytest.mark.parametrize("amount", [0, -1, -100.5])
def test_deposit_zero_or_negative_raises(alice_account, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        alice_account.deposit(amount)
    #hibánál az egyenleg nem változhat
    assert alice_account.get_balance() == 100.0


#--- withdraw ---

def test_withdraw_decreases_balance(alice_account):
    alice_account.withdraw(30)
    assert alice_account.get_balance() == 70.0


def test_withdraw_whole_balance(alice_account):
    #edge case: pontosan a teljes egyenleg felvehető
    alice_account.withdraw(100)
    assert alice_account.get_balance() == 0.0


@pytest.mark.parametrize("amount", [0, -1, -0.01])
def test_withdraw_zero_or_negative_raises(alice_account, amount):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        alice_account.withdraw(amount)


@pytest.mark.parametrize("amount", [100.01, 101, 1_000_000])
def test_withdraw_more_than_balance_raises(alice_account, amount):
    with pytest.raises(ValueError, match="Insufficient funds"):
        alice_account.withdraw(amount)
    assert alice_account.get_balance() == 100.0


def test_withdraw_from_empty_account_raises(bob_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        bob_account.withdraw(1)


#--- transfer ---

def test_transfer_moves_money(alice_account, bob_account):
    alice_account.transfer(40, bob_account)
    assert alice_account.get_balance() == 60.0
    assert bob_account.get_balance() == 40.0


def test_transfer_insufficient_funds_changes_nothing(alice_account, bob_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        bob_account.transfer(10, alice_account)
    assert bob_account.get_balance() == 0.0
    assert alice_account.get_balance() == 100.0


@pytest.mark.parametrize("target", ["Bob", 42, None, [], {"owner": "Bob"}])
def test_transfer_to_non_account_raises(alice_account, target):
    #edge case: pénzküldés nem BankAccount objektumnak
    with pytest.raises(TypeError, match="Target must be a BankAccount instance"):
        alice_account.transfer(10, target)
    assert alice_account.get_balance() == 100.0


#--- EXTRA: a javított hiányosságok tesztjei ---

@pytest.mark.parametrize("amount", ["100", None, [10], True])
def test_deposit_non_number_raises(alice_account, amount):
    with pytest.raises(TypeError, match="must be a number"):
        alice_account.deposit(amount)
    assert alice_account.get_balance() == 100.0


@pytest.mark.parametrize("amount", ["50", None, False])
def test_withdraw_non_number_raises(alice_account, amount):
    with pytest.raises(TypeError, match="must be a number"):
        alice_account.withdraw(amount)


@pytest.mark.parametrize("amount", [float("nan"), float("inf"), float("-inf")])
def test_deposit_nan_or_infinite_raises(alice_account, amount):
    with pytest.raises(ValueError, match="finite"):
        alice_account.deposit(amount)
    assert alice_account.get_balance() == 100.0


def test_transfer_to_self_raises(alice_account):
    with pytest.raises(ValueError, match="same account"):
        alice_account.transfer(10, alice_account)
    assert alice_account.get_balance() == 100.0


@pytest.mark.parametrize("amount", [0, -5])
def test_transfer_zero_or_negative_raises(alice_account, bob_account, amount):
    with pytest.raises(ValueError, match="Transfer amount must be positive"):
        alice_account.transfer(amount, bob_account)
    assert bob_account.get_balance() == 0.0


@pytest.mark.parametrize("owner", ["", "   ", None, 123])
def test_invalid_owner_raises(owner):
    with pytest.raises(ValueError, match="Owner must be a non-empty string"):
        BankAccount(owner, 10)


@pytest.mark.parametrize("balance", ["100", None, True])
def test_non_number_initial_balance_raises(balance):
    with pytest.raises(TypeError, match="Initial balance must be a number"):
        BankAccount("Dave", balance)


@pytest.mark.parametrize("balance", [float("nan"), float("inf")])
def test_nan_or_infinite_initial_balance_raises(balance):
    with pytest.raises(ValueError, match="finite"):
        BankAccount("Dave", balance)

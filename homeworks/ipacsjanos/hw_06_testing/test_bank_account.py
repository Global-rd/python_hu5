import pytest
from bank_account import BankAccount

# ==========================================
# 1. FIXTURE-ÖK DEFINIÁLÁSA (Legalább 2 darab)
# ==========================================
@pytest.fixture
def empty_account():
    """Egy üres számlát biztosít a tesztekhez."""
    return BankAccount(owner="János", balance=0.0)

@pytest.fixture
def funded_account():
    """Egy 1000.00 egységgel feltöltött számlát biztosít."""
    return BankAccount(owner="István", balance=1000.0)


# ==========================================
# 2. PARAMETRIZÁLT TESZTEK (Deposit 0 és negatív)
# ==========================================
@pytest.mark.parametrize("invalid_amount", [0, -50, -10.5])
def test_deposit_invalid_amounts(empty_account, invalid_amount):
    """Teszteli, hogy a deposit() ValueError-t dob 0 és negatív értékekre."""
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        empty_account.deposit(invalid_amount)


# ==========================================
# 3. ALAP MŰVELETEK TESZTELÉSE EXCEPTION-ÖKKEL
# ==========================================
def test_initial_balance_negative():
    """Ellenőrzi, hogy negatív kezdő egyenlegnél ValueError keletkezik."""
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount(owner="Teszt", balance=-100.0)

def test_withdraw_insufficient_funds(funded_account):
    """Ellenőrzi a fedezethiány miatti ValueError kivételt."""
    with pytest.raises(ValueError, match="Insufficient funds."):
        funded_account.withdraw(1500.0)

def test_successful_transfer(funded_account, empty_account):
    """Sikeres utalás tesztelése két számla között."""
    funded_account.transfer(400.0, empty_account)
    assert funded_account.get_balance() == 600.0
    assert empty_account.get_balance() == 400.0


# ==========================================
# 4. EDGE CASE-EK ÉS AZ EXTRA FELADATOK TESZTJEI
# ==========================================
def test_transfer_to_non_bank_account(funded_account):
    """Edge Case: Pénz küldése nem BankAccount objektumnak (TypeError)."""
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        funded_account.transfer(100.0, "nem_egy_szamla_objektum")

def test_transfer_to_self(funded_account):
    """Extra feladat tesztje: Saját magunknak való utalás letiltásának ellenőrzése."""
    with pytest.raises(ValueError, match="Cannot transfer money to the same account."):
        funded_account.transfer(100.0, funded_account)

@pytest.mark.parametrize("non_number", ["szöveg", [], None])
def test_invalid_input_types(empty_account, non_number):
    """Extra feladat tesztje: Nem szám típusú inputok kiszűrése (TypeError)."""
    with pytest.raises(TypeError):
        empty_account.deposit(non_number)
    with pytest.raises(TypeError):
        empty_account.withdraw(non_number)

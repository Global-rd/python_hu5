import pytest
from bank_account import BankAccount

#Fixture: létrehoz egy Anna nevű bankszámlát 1000 kezdőegyenleggel
@pytest.fixture
def account_a():
    return BankAccount("Anna", 1000)

#Fixture: létrehoz egy Bela nevű bankszámlát 500 kezdőegyenleggel
@pytest.fixture
def account_b():
    return BankAccount("Bela", 500)

#Teszteli, hogy Anna számlájának kezdőegyenlege 1000
def test_account_a_initial_balance(account_a):
    assert account_a.get_balance() == 1000

#Teszteli, hogy Bela számlájának kezdőegyenlege 500
def test_account_b_initial_balance(account_b):
    assert account_b.get_balance() == 500

#Teszteli, hogy a befizetés növeli a számla egyenlegét
def test_deposit(account_a):
    account_a.deposit(200)
    assert account_a.get_balance() == 1200

#A nulla és a negatív befizetés is hibát okozzon
@pytest.mark.parametrize("amount", [0, -100])
def test_deposit_invalid_amount(account_a, amount):
    with pytest.raises(ValueError):
        account_a.deposit(amount)

#Teszteli, hogy a pénzfelvétel csökkenti a számla egyenlegét
def test_withdraw(account_a):
    account_a.withdraw(300)
    assert account_a.get_balance() == 700

#Teszteli, hogy a számlánál nagyobb összeg felvétele hibát okoz
def test_withdraw_insufficient_funds(account_a):
    with pytest.raises(ValueError):
        account_a.withdraw(1500)

#A nulla és a negatív pénzfelvétel is hibát okozzon
@pytest.mark.parametrize("amount", [0, -100])
def test_withdraw_invalid_amount(account_a, amount):
    with pytest.raises(ValueError):
        account_a.withdraw(amount)

#Sikeres átutalás
def test_transfer(account_a, account_b):
    account_a.transfer(200, account_b)

    assert account_a.get_balance() == 800
    assert account_b.get_balance() == 700

#Hibás átutalási cél
def test_transfer_invalid_target(account_a):
    with pytest.raises(TypeError):
        account_a.transfer(100, "Bela")

#Nincs elég fedezet az átutaláshoz
def test_transfer_insufficient_funds(account_a, account_b):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_a.transfer(1500, account_b)

#Hibakeresés: a szöveges kezdőegyenleg TypeError hibát okoz
def test_initial_balance_is_text():
    with pytest.raises(TypeError):
        BankAccount("Anna", "alma")

#Teszteli, hogy a szöveges befizetés TypeError hibát okoz.
def test_deposit_text_amount(account_a):
    with pytest.raises(TypeError):
        account_a.deposit("alma")

#Teszteli, hogy a szöveges pénzfelvétel TypeError hibát okoz.
def test_withdraw_text_amount(account_a):
    with pytest.raises(TypeError):
        account_a.withdraw("alma")

#Teszteli, hogy a saját számlára utalás hibát okoz,
# és az egyenleg változatlan marad.
def test_transfer_to_same_account(account_a):
    with pytest.raises(ValueError, match="Cannot transfer to the same account."):
        account_a.transfer(100, account_a)

    assert account_a.get_balance() == 1000


#Teszteli, hogy a negatív kezdőegyenleg ValueError hibát okoz.
def test_initial_balance_negative():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("Anna", -100)

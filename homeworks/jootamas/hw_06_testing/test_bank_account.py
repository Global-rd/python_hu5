import pytest
from bank_account import BankAccount

"""
A unit testeknél a következőket vedd figyelembe:
- Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.
- Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak érdekében, 
hogy a tesztet több input-ra is lefuttassa (pl: teszteld a deposit() method-ot pontosan 0 és negatív szám inputtal is).
- Tesztelj edge case-eket (pl: pénz küldése nem BankAccount object-nek).
- Írj teszteket amik arra irányulnak, hogy a megfelelő Exception raise-elődik-e a megadott input-ra.

Extra: a BankAccount class nincs felkészülve minden lehetséges hibára
(non-number inputok, küldhetünk e saját magunknak pénzt stb.). Nézd át
alaposan a kódot, azonosítsd ezeket a hiányosságokat és implementáld a
szükséges változtatásokat a saját mappádban lévő file-ban. Ezután írj
teszteket amik ezeknek a kiegészítéseknek a helyességét ellenőrzik.
"""

@pytest.fixture
def empty_bank_account():
  # uj szamla, 0 egyenleggel
  return BankAccount("John Doe", 0.0)

@pytest.fixture
def another_bank_account():
  # uj szamla, indulo egyenleggel
  return BankAccount("Jane Doe", 200.0)

# sikeresen letrejon-e a bankszamla

def test_create_account(empty_bank_account):
  assert isinstance(empty_bank_account.owner, str) and isinstance(empty_bank_account.get_balance(), float)

# deposit dob-e kivetelt nulla vagy negativ befizetesre

@pytest.mark.parametrize("amount, expected_exception",
                         [
                            (0, ValueError),
                            (-5, ValueError),
                            ("x", ValueError), # extra: nem szamot adok meg osszegnek
                         ])
def test_deposit_raise(empty_bank_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        empty_bank_account.deposit(amount)

# deposit rendben noveli-e az egyenleget

@pytest.mark.parametrize("amount, expected_balance",
                         [
                            (50.0, 250.0),
                            (150.0, 350.0),
                         ])
def test_deposit_success(another_bank_account, amount, expected_balance):
  another_bank_account.deposit(amount)
  assert another_bank_account.get_balance() == expected_balance

# withdraw hibat dob-e, ha negativot akarok kivenni, vagy keves az egyenleg

@pytest.mark.parametrize("amount, expected_exception",
                         [
                            (-1.0, ValueError),
                            (500.0, ValueError),
                         ])
def test_withdraw_raise(another_bank_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        another_bank_account.withdraw(amount)

# transfer rendben mukodik-e

def test_withdraw_success(another_bank_account, empty_bank_account):
  # sajat magamnak utalas raise
  with pytest.raises(TypeError):
    another_bank_account.transfer(100.0, another_bank_account)

  # dobja-e a kivetelt, ha nem bankszamlara akarok utalni, hanem valami masra
  with pytest.raises(TypeError):
    another_bank_account.transfer(100.0, "X")

  # another_bank_account kezdo egyenlege 200, 100-at atutalok, 100-nak kell maradi, a masikon szinten 100-nak, mert az nullaval indult
  another_bank_account.transfer(100.0, empty_bank_account)
  assert another_bank_account.get_balance() == 100.0 and empty_bank_account.get_balance() == 100.0

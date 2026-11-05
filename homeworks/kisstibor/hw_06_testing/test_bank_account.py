"""Az eredeti bank_account.py tesztjei (részletes magyar kommentekkel).

Minden teszt az "Arrange - Act - Assert" mintát követi:
  1. Arrange: előkészítés (fixture vagy új objektum létrehozása)
  2. Act:     a tesztelt művelet meghívása
  3. Assert:  az eredmény ellenőrzése (assert / pytest.raises)
"""
# A pytest modul adja a fixture-öket, a parametrizálást és a pytest.raises-t.
import pytest

# A tesztelendő osztály importja.
from bank_account import BankAccount


# ---------------------------------------------------------------------------
# FIXTURE-ÖK
# A fixture egy előkészítő függvény: minden teszt, ami paraméterként a nevét
# kéri, minden futáskor egy ÚJ, friss objektumot kap. Így a tesztek nem
# befolyásolják egymást (pl. az egyik befizetése nem rontja el a másikat).
# ---------------------------------------------------------------------------
@pytest.fixture
def lili():
    # Első számla: 100 egyenleggel.
    return BankAccount("Lili", 100.0)


@pytest.fixture
def anna():
    # Második számla: 50 egyenleggel (az utalás tesztekhez kell a célszámla).
    return BankAccount("Anna", 50.0)


# ---------------------------------------------------------------------------
# KONSTRUKTOR
# ---------------------------------------------------------------------------
def test_init_defaults():
    # Mit tesztel: a __init__ alapértelmezett értékeit.
    # Hogyan: kezdő egyenleg megadása nélkül hozunk létre számlát, majd
    # ellenőrizzük, hogy a név eltárolódott és az egyenleg 0.0.
    acc = BankAccount("Tibi")
    assert acc.owner == "Tibi"
    assert acc.get_balance() == 0.0


def test_init_negative_balance_raises():
    # Mit tesztel: negatív kezdő egyenleg elutasítását.
    # Hogyan: a pytest.raises elvárja, hogy a with-blokkban ValueError
    # keletkezzen; ha nem keletkezik, a teszt elbukik. A match= a hibaüzenetben
    # keres szövegrészletet (regex), így azt is ellenőrizzük, hogy a jó
    # hibáról van szó.
    with pytest.raises(ValueError, match="negative"):
        BankAccount("Tibi", -1)


# ---------------------------------------------------------------------------
# DEPOSIT (befizetés)
# ---------------------------------------------------------------------------
def test_deposit(lili):
    # Mit tesztel: a sikeres befizetést, tizedes összeggel is.
    # Hogyan: Lilinek (100) befizetünk 25.5-öt, az egyenlegnek 125.5-nek
    # kell lennie.
    lili.deposit(25.5)
    assert lili.get_balance() == 125.5


# A parametrize ugyanazt a tesztet lefuttatja minden felsorolt értékkel,
# külön tesztesetként. Itt a határeset (0) és a negatív számok szerepelnek.
@pytest.mark.parametrize("amount", [0, -1, -0.01, -1000])
def test_deposit_non_positive_raises(lili, amount):
    # Mit tesztel: hogy 0 vagy negatív összeget nem lehet befizetni.
    # Hogyan: mind a 4 értékkel megpróbálunk befizetni, és ValueError-t
    # várunk "positive" szöveggel az üzenetben.
    with pytest.raises(ValueError, match="positive"):
        lili.deposit(amount)
    # A hibás művelet után az egyenleg nem változhatott (nincs mellékhatás).
    assert lili.get_balance() == 100.0


# ---------------------------------------------------------------------------
# WITHDRAW (kivétel)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("amount", [0, -5])
def test_withdraw_non_positive_raises(lili, amount):
    # Mit tesztel: 0 és negatív összeg kivételének tiltását.
    # Hogyan: parametrizálva két értékkel hívjuk a withdraw-t, és
    # ValueError-t várunk.
    with pytest.raises(ValueError, match="positive"):
        lili.withdraw(amount)


def test_withdraw(lili):
    # Mit tesztel: a sikeres kivételt.
    # Hogyan: 100-ból kiveszünk 40-et, az egyenleg 60 lesz.
    lili.withdraw(40)
    assert lili.get_balance() == 60


def test_withdraw_entire_balance(lili):
    # Mit tesztel: a határesetet, amikor pont a teljes egyenleget vesszük ki.
    # Hogyan: a kód csak az "amount > balance" esetet tiltja, tehát az
    # egyenlőnek még működnie kell, és 0 egyenleget kell hagynia.
    lili.withdraw(100)
    assert lili.get_balance() == 0


def test_withdraw_insufficient_funds_raises(lili):
    # Mit tesztel: a fedezethiányt (túlhúzás tiltása).
    # Hogyan: 100.01-et próbálunk kivenni 100-ból, azaz épp egy fillérrel
    # többet, mint amennyi van; "Insufficient funds." hibát várunk.
    with pytest.raises(ValueError, match="Insufficient"):
        lili.withdraw(100.01)
    # Sikertelen kivétel után az egyenleg érintetlen.
    assert lili.get_balance() == 100.0


# ---------------------------------------------------------------------------
# TRANSFER (utalás)
# ---------------------------------------------------------------------------
def test_transfer(lili, anna):
    # Mit tesztel: a sikeres utalást két számla között.
    # Hogyan: két fixture-t használunk; Lili utal 30-at Annának. Mindkét
    # oldalt ellenőrizzük: Lili 100-30=70, Anna 50+30=80.
    lili.transfer(30, anna)
    assert lili.get_balance() == 70
    assert anna.get_balance() == 80


# Edge case: a célpont nem BankAccount (None, szöveg, szám, szótár).
@pytest.mark.parametrize("target", [None, "Anna", 42, {"owner": "Anna"}])
def test_transfer_to_non_account_raises(lili, target):
    # Mit tesztel: hogy az utalás célpontja csak BankAccount lehet.
    # Hogyan: 4 különböző, hibás típusú célponttal próbálkozunk, és
    # TypeError-t várunk, "BankAccount" szöveggel az üzenetben.
    with pytest.raises(TypeError, match="BankAccount"):
        lili.transfer(10, target)
    # A típusellenőrzés a levonás előtt történik, ezért nem veszett el pénz.
    assert lili.get_balance() == 100.0


def test_transfer_insufficient_funds_leaves_both_unchanged(lili, anna):
    # Mit tesztel: hogy sikertelen utalásnál mindkét számla változatlan marad.
    # Hogyan: 500-at utalnánk 100 egyenlegről; a withdraw ValueError-t dob
    # még a befizetés előtt. Utána egy tuple-ben egyszerre hasonlítjuk össze
    # mindkét egyenleget az eredeti értékekkel.
    with pytest.raises(ValueError):
        lili.transfer(500, anna)
    assert (lili.get_balance(), anna.get_balance()) == (100.0, 50.0)


# ---------------------------------------------------------------------------
# __str__
# ---------------------------------------------------------------------------
def test_str(lili):
    # Mit tesztel: a szöveges megjelenítést (str(objektum)).
    # Hogyan: a teljes elvárt szöveget összehasonlítjuk; az egyenleg két
    # tizedesre formázva jelenik meg (100.0 -> 100.00).
    assert str(lili) == "Account owner: Lili, Balance: 100.00"

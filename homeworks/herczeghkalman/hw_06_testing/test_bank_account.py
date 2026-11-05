import pytest
from bank_account import BankAccount


# 1. fixture: egy Alice nevű bankszámla létrehozása
@pytest.fixture
def account1():
    return BankAccount("Alice", 1000.0)


# 2. fixture: egy Bob nevű bankszámla létrehozása
@pytest.fixture
def account2():
    return BankAccount("Bob", 500.0)


# 3. A bankszámla sikeres létrehozásának tesztelése
def test_account_creation(account1):
    # Ellenőrizzük a számlatulajdonos nevét
    assert account1.owner == "Alice"

    # Ellenőrizzük a kezdeti egyenleget
    assert account1.balance == 1000.0


# 4. Negatív kezdőegyenleg tesztelése
def test_negative_initial_balance():
    # Ellenőrizzük, hogy negatív egyenleg esetén ValueError keletkezik
    with pytest.raises(ValueError):
        BankAccount("Alice", -100.0)


# 5. Sikeres pénzbefizetés tesztelése
def test_deposit(account1):
    # 200 egység befizetése a számlára
    account1.deposit(200.0)

    # Ellenőrizzük, hogy az egyenleg 1200 lett
    assert account1.get_balance() == 1200.0


# 6. Paraméterezett teszt a hibás befizetések ellenőrzésére
@pytest.mark.parametrize("amount", [0, -10, -100.5])
def test_invalid_deposit(account1, amount):
    # Ellenőrizzük, hogy nulla vagy negatív befizetés esetén ValueError keletkezik
    with pytest.raises(ValueError):
        account1.deposit(amount)

    # Ellenőrizzük, hogy a hibás befizetés nem módosította az egyenleget
    assert account1.get_balance() == 1000.0


# 7. Sikeres pénzfelvétel tesztelése
def test_withdraw(account1):
    # 300 egység felvétele a számláról
    account1.withdraw(300.0)

    # Ellenőrizzük, hogy az egyenleg 700 lett
    assert account1.get_balance() == 700.0


# 8. Nulla és negatív összegű pénzfelvétel tesztelése
@pytest.mark.parametrize("amount", [0, -50, -200.0])
def test_invalid_withdraw(account1, amount):
    # Ellenőrizzük, hogy hibás pénzfelvételi összeg esetén ValueError keletkezik
    with pytest.raises(ValueError):
        account1.withdraw(amount)

    # Ellenőrizzük, hogy a számla egyenlege változatlan maradt
    assert account1.get_balance() == 1000.0


# 9. Fedezethiány tesztelése
def test_withdraw_insufficient_funds(account1):
    # Ellenőrizzük, hogy a rendelkezésre álló egyenlegnél nagyobb összeg felvétele hibát okoz
    with pytest.raises(ValueError, match="Insufficient funds"):
        account1.withdraw(1500.0)

    # Ellenőrizzük, hogy sikertelen pénzfelvétel esetén nem változik az egyenleg
    assert account1.get_balance() == 1000.0


# 10. Sikeres pénzátutalás tesztelése
def test_transfer(account1, account2):
    # 300 egység átutalása Alice számlájáról Bob számlájára
    account1.transfer(300.0, account2)

    # Ellenőrizzük, hogy Alice egyenlege 700 lett
    assert account1.get_balance() == 700.0

    # Ellenőrizzük, hogy Bob egyenlege 800 lett
    assert account2.get_balance() == 800.0


# 11. Nem BankAccount típusú célobjektum tesztelése
def test_transfer_invalid_target(account1):
    # Ellenőrizzük, hogy hibás célobjektum esetén TypeError keletkezik
    with pytest.raises(TypeError, match="Target must be a BankAccount instance"):
        account1.transfer(100.0, "Bob")

    # Ellenőrizzük, hogy a sikertelen átutalás nem módosította az egyenleget
    assert account1.get_balance() == 1000.0


# 12. Nulla és negatív átutalási összeg tesztelése
@pytest.mark.parametrize("amount", [0, -50, -100.0])
def test_transfer_invalid_amount(account1, account2, amount):
    # Ellenőrizzük, hogy a hibás átutalási összeg ValueError kivételt okoz
    with pytest.raises(ValueError):
        account1.transfer(amount, account2)

    # Ellenőrizzük, hogy a küldő számla egyenlege változatlan maradt
    assert account1.get_balance() == 1000.0

    # Ellenőrizzük, hogy a fogadó számla egyenlege sem változott
    assert account2.get_balance() == 500.0


# 13. Fedezethiányos átutalás tesztelése
def test_transfer_insufficient_funds(account1, account2):
    # Ellenőrizzük, hogy a számlaegyenlegnél nagyobb átutalás ValueError kivételt okoz
    with pytest.raises(ValueError, match="Insufficient funds"):
        account1.transfer(1500.0, account2)

    # Ellenőrizzük, hogy Alice egyenlege változatlan maradt
    assert account1.get_balance() == 1000.0

    # Ellenőrizzük, hogy Bob nem kapott pénzt
    assert account2.get_balance() == 500.0


# 14. Egyenleg lekérdezésének tesztelése
def test_get_balance(account1):
    # Ellenőrizzük, hogy a get_balance() a megfelelő értéket adja vissza
    assert account1.get_balance() == 1000.0


# 15. A __str__ metódus tesztelése
def test_str(account1):
    # Ellenőrizzük a számla szöveges megjelenítését
    assert str(account1) == "Account owner: Alice, Balance: 1000.00"

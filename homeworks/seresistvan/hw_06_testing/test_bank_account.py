import pytest
from bank_account import BankAccount



@pytest.fixture
def account1():
    return BankAccount("Istvan", 100)



@pytest.fixture
def account2():
    return BankAccount("Anna", 50)



def test_create_account(account1):
    assert account1.owner == "Istvan"
    assert account1.get_balance() == 100



def test_deposit(account1):
    account1.deposit(20)
    assert account1.get_balance() == 120


# 0 és -10 -es értékkel is lefut a teszt.
@pytest.mark.parametrize("amount", [0, -10])
def test_wrong_deposit(account1, amount):
    # Nulla vagy negatív befizetésnél ValueError kivételt várunk.
    with pytest.raises(ValueError):
        account1.deposit(amount)


def test_withdraw(account1):
    # 100-ból kiveszek 30-at.
    account1.withdraw(30)
    assert account1.get_balance() == 70


def test_withdraw_all(account1):
    # Teljes eygenleget kivesszük.
    account1.withdraw(100)
    assert account1.get_balance() == 0


def test_not_enough_money(account1):
    # Overwithdrawalt csinálunk. Többet vennénk le, mint amennyi van.
    with pytest.raises(ValueError):
        account1.withdraw(200)


@pytest.mark.parametrize("amount", [0, -10])
def test_wrong_withdraw(account1, amount):
    # Nulla ill. negatív összeget nem lehet kivenni.
    with pytest.raises(ValueError):
        account1.withdraw(amount)


def test_transfer(account1, account2):
    # 20-at utalunk a másodikra.
    account1.transfer(20, account2)

    # Változások.
    assert account1.get_balance() == 80
    assert account2.get_balance() == 70


def test_wrong_transfer(account1):
    # Textet adpok meg.
    # TypeError exception-t várunk.
    with pytest.raises(TypeError):
        account1.transfer(20, "Anna")


def test_negative_balance():
    # Negatív számláról nem lehet levenni.
    with pytest.raises(ValueError):
        BankAccount("Istvan", -100)
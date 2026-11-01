import pytest
from bank_account import BankAccount

#Pytest Fixtures letrehozasa:
@pytest.fixture
def first_bank_account():
    return BankAccount("Anna", 1000)

@pytest.fixture
def second_bank_account():
    return BankAccount("Peter", 500)

#Negativ balance ValueError exception tesztelese:
def test_initial_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("Alex", -200)

#Empty owner name ValueError exception tesztje:
def test_initial_empty_owner():
    with pytest.raises(ValueError):
        BankAccount("", 200.0)
    
#Deposit es Withdraw müködesenek tesztje:
def test_deposit_changes_balance_expected_way(first_bank_account):
    first_bank_account.deposit(200)
    assert first_bank_account.balance == 1200

def test_withdraw_changes_balance_expected_way(first_bank_account):
    first_bank_account.withdraw(300)
    assert first_bank_account.balance == 700

#Deposit es Withdraw ValueError Exception kezelesenek tesztje:
@pytest.mark.parametrize("amount, expected_exception", 
                         [
                            (0, ValueError),
                            (-100, ValueError),
                        ])
def test_deposit_invalid_amount(first_bank_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        first_bank_account.deposit(amount)
    assert first_bank_account.balance == 1000


@pytest.mark.parametrize("amount, expected_exception", 
                         [
                            (0, ValueError),
                            (-100, ValueError),
                            (1200, ValueError),
                        ])
def test_withdraw_invalid_amount(first_bank_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        first_bank_account.withdraw(amount)
    assert first_bank_account.balance == 1000

#Deposit & Withdraw TypeError kezelesenek tesztje:
@pytest.mark.parametrize("amount, expected_exception", 
                         [
                            ("200.0", TypeError),
                            (None, TypeError),
                            ("Hundred", TypeError),
                        ])
def test_deposit_invalid_amount_type(first_bank_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        first_bank_account.deposit(amount)
    assert first_bank_account.balance == 1000

@pytest.mark.parametrize("amount, expected_exception", 
                         [
                            ("200.0", TypeError),
                            (None, TypeError),
                            ("Hundred", TypeError),
                        ])
def test_withdraw_invalid_amount_type(first_bank_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        first_bank_account.withdraw(amount)
    assert first_bank_account.balance == 1000

#Transfer müködesenek tesztje:
def test_transfer_changes_balance_expected_way(first_bank_account, second_bank_account):
    first_bank_account.transfer(200.0, second_bank_account)
    assert first_bank_account.balance == 800
    assert second_bank_account.balance == 700

#Transfer TypeError exception kezelesenek tesztje:
@pytest.mark.parametrize("amount, target_account, expected_exception", 
                         [
                            (200.0, "Peter", TypeError),
                            (300.5, None, TypeError),
                            (500.5, 1000, TypeError),
                        ])
def test_transfer_invalid_target_account(first_bank_account, amount, target_account, expected_exception):
    with pytest.raises(expected_exception):
        first_bank_account.transfer(amount, target_account)
    assert first_bank_account.balance == 1000

#Transfer tesztje, ha nincs elegendö egyenleg (ValueError exception):
def test_transfer_insufficient_funds(first_bank_account, second_bank_account):
    with pytest.raises(ValueError):
        first_bank_account.transfer(1500.0, second_bank_account)
    assert first_bank_account.balance == 1000
    assert second_bank_account.balance == 500

#Get_Balance tesztje:
def test_get_balance_after_multiple_transactions_expected_way(first_bank_account):
    first_bank_account.deposit(200)
    assert first_bank_account.get_balance() == 1200
    first_bank_account.withdraw(100)
    assert first_bank_account.get_balance() == 1100
    first_bank_account.deposit(350)
    assert first_bank_account.get_balance() == 1450

#__str__() tesztelese:
def test_str_expected_output(first_bank_account):
    assert str(first_bank_account) == "Account owner: Anna, Balance: 1000.00"

#Transfer ValueError tesztje, ha sajat magunknak akarunk utalni:
def test_transfer_to_self(first_bank_account):
    with pytest.raises(ValueError):
        first_bank_account.transfer(300.0, first_bank_account)
    assert first_bank_account.balance == 1000
    



import pytest
from bank_account import BankAccount

@pytest.fixture
def poor_account():
    return BankAccount('Poor Guy')

@pytest.fixture
def rich_account():
    return BankAccount('Rich Guy', 1000000.0)

'''
Egyszerű tesztek transfer(), és deposit() ellenörzésre
'''
def test_valid_transfer_poor(rich_account, poor_account):
    rich_account.transfer(1.0, poor_account)
    assert poor_account.get_balance() == 1.0

def test_valid_transfer_rich(rich_account, poor_account):
    rich_account.transfer(1.0, poor_account)
    assert rich_account.get_balance() == 999999.0

def test_deposit_increases_balance(poor_account):
    balance_before = poor_account.get_balance()
    poor_account.deposit(5.0)
    assert poor_account.get_balance() == balance_before+5.0


'''
 transfer() kivételek, edge case

 A parametrizálásnál nem tudtam a target_accountnak a fixturet átadni. AI a request.getfixturevalue() használatát javasolta,
 de ezt nem tanultuk, úgyhogy nem erőltettem
'''

@pytest.mark.parametrize("amount, target_account, expected_exception",
                         [
                            (-1.0,  'valid account', ValueError),
                            (2000000, 'valid account', ValueError),
                            (100.0,  'not an account', TypeError),
                         ])

def test_invalid_transfer(rich_account, amount, target_account, expected_exception):
    with pytest.raises(expected_exception):
        if target_account=='valid account':
            trg_account=BankAccount('Valid Guy')
            rich_account.transfer(amount, trg_account) 
        elif target_account == 'not an account':
            rich_account.transfer(amount, target_account)        


'''
 Viszont nem tudtam hogyan lehet a fenti példában a különböző ValueErrorokat megkülönböztetni, ezért utánanéztem.
 Ha jól emléxem ez sem volt órán, de midenképpen ki akartam próbálni.
 Itt találtam: https://docs.pytest.org/en/stable/how-to/assert.html

 A pontos hibaüzenet ellenörzése
'''
def test_negative_deposit_throws_exception(rich_account):
    with pytest.raises(ValueError)  as excinfo:
        rich_account.deposit(-1.0)

    assert 'Deposit amount must be positive.' == str(excinfo.value)
    
'''
Paraméterezéssel. Itt jön ki a lényeg, mert a két ValueError nem ugyanaz
'''

@pytest.mark.parametrize("amount, expected_exception, expected_error_msg",
                         [
                             (-1.0, ValueError, "Withdraw amount must be positive."),
                             (0.0, ValueError, "Withdraw amount must be positive."),
                             (2000000, ValueError, "Insufficient funds.")
                         ])

def test_withdraw_invalid_amount_with_error_msg(rich_account, amount, expected_exception, expected_error_msg):
    with pytest.raises(expected_exception) as excinfo:
        rich_account.withdraw(amount)
    
    assert expected_error_msg == str(excinfo.value)

'''
Extra 1 Initial balance type check
'''
def test_initial_balance_type():
    with pytest.raises(TypeError) as excinfo:
        test_acct1=BankAccount('N/A', 'One dollar')

    assert 'Initial balance has to be numeric.' == str(excinfo.value)
    



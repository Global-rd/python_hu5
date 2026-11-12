import pytest 
from bank_account import BankAccount 

@pytest.fixture
def steve_account():                    #nem bank_account hogy ne legyen osszezavaro. A zarojel itt uresen maraqd, a BankAccount-bol kapja majd meg az erteket 
    return BankAccount("Steve", 35000)

@pytest.fixture
def bill_account():
    return BankAccount("Bill", 43900)

def test_deposit_increasing_balance (steve_account):
    steve_account.deposit(2000)        # idezojelek nelkul, mert kulonben TypeError-t ad 
    assert steve_account.balance == 37000

@pytest.mark.parametrize("amount, expected_exception",  #ugyanaza a teszt tobbszor fut, minden tuple egy teszt eset
                         [
                         (0, ValueError),
                         (-2000, ValueError),
                         ])
def test_invalid_deposit(steve_account, amount, expected_exception):
    with pytest.raises(expected_exception):     #a teszt akkor sikeres haa deposit tenyleg Value errort dob, 0 es negativ nem engedelyezett
        steve_account.deposit(amount)

def test_transfer_to_non_account(steve_account): #edge case: nem BankAccountnak kuldunk penzt
    with pytest.raises(TypeError):
        steve_account.transfer(1000, "Bill") #Bill string nem accouint -> TypeError 

def test_withdraw_insufficient_funds(steve_account): #edge case: nincs elegendo penz a szamlan -> ValueError
    with pytest.raises(ValueError):
        steve_account.withdraw(38000)

def test_transfer_moves_money(steve_account, bill_account):   #penzkuldes tesztelese, Steve szamlajarol Bill szamlajara 
    steve_account.transfer(2000, bill_account)
    assert steve_account.balance == 33000
    assert bill_account.balance == 45900 

        
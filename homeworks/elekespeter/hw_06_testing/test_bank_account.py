import pytest
from bank_account import BankAccount


# =============================================================================
# 1. LÉPÉS: FIXTURE-ÖK
# =============================================================================
# A fixture egy "előre elkészített kellék": minden teszt, ami a nevét
# paraméterként kéri, egy FRISS objektumot kap. Így a tesztek nem hatnak
# egymásra (ha az egyik teszt pénzt vesz ki, a következő megint 1000-ről indul).

@pytest.fixture
def empty_account():
    """Üres számla, 0 egyenleggel (mint az órai empty_cart)."""
    return BankAccount("Anna")


@pytest.fixture
def funded_account():
    """Feltöltött számla, 1000 egyenleggel (mint az órai cart_with_items)."""
    return BankAccount("Béla", 1000)


@pytest.fixture
def other_account():
    """Második feltöltött számla, az utalások teszteléséhez."""
    return BankAccount("Cecília", 500)


# =============================================================================
# 2. LÉPÉS: ALAPMŰKÖDÉS (happy path) - amikor minden jó bemenetet kap
# =============================================================================

def test_new_account_has_owner_and_balance(funded_account):
    assert funded_account.owner == "Béla"
    assert funded_account.balance == 1000


def test_default_balance_is_zero(empty_account):
    assert empty_account.get_balance() == 0


def test_deposit_increases_balance(empty_account):
    empty_account.deposit(250)
    assert empty_account.get_balance() == 250


def test_withdraw_decreases_balance(funded_account):
    funded_account.withdraw(300)
    assert funded_account.get_balance() == 700


def test_withdraw_whole_balance(funded_account):
    funded_account.withdraw(1000)
    assert funded_account.get_balance() == 0


def test_transfer_moves_money(funded_account, other_account):
    funded_account.transfer(200, other_account)
    assert funded_account.get_balance() == 800
    assert other_account.get_balance() == 700


def test_str_format(funded_account):
    assert str(funded_account) == "Account owner: Béla, Balance: 1000.00"


# =============================================================================
# 3. LÉPÉS: PARAMETRIZE + KIVÉTELEK (pytest.raises)
# =============================================================================
# A @pytest.mark.parametrize ugyanazt a tesztet többször lefuttatja, minden
# alkalommal más bemenettel. A pytest.raises azt ellenőrzi, hogy a kódrészlet
# a várt hibát dobja-e. A match= a hibaüzenet szövegét is ellenőrzi.

@pytest.mark.parametrize("amount", [0, -1, -100.5])
def test_deposit_not_positive_raises(empty_account, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        empty_account.deposit(amount)


@pytest.mark.parametrize("amount", [0, -1, -100.5])
def test_withdraw_not_positive_raises(funded_account, amount):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        funded_account.withdraw(amount)


@pytest.mark.parametrize("initial_balance", [-1, -0.01, -1000])
def test_negative_initial_balance_raises(initial_balance):
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount("Dénes", initial_balance)


def test_withdraw_more_than_balance_raises(funded_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        funded_account.withdraw(1000.01)


# =============================================================================
# 4. LÉPÉS: EDGE CASE-EK (határesetek, szélsőséges helyzetek)
# =============================================================================

@pytest.mark.parametrize("not_an_account", ["Cecília", None, 12345, ["account"]])
def test_transfer_to_non_account_raises(funded_account, not_an_account):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance"):
        funded_account.transfer(100, not_an_account)


def test_failed_transfer_to_non_account_keeps_balance(funded_account):
    # Ha az utalás elbukik, a forrás számláról nem tűnhet el pénz.
    with pytest.raises(TypeError):
        funded_account.transfer(100, "nem számla")
    assert funded_account.get_balance() == 1000


def test_transfer_more_than_balance_raises_and_changes_nothing(funded_account, other_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        funded_account.transfer(5000, other_account)
    # Egyik számla egyenlege sem változhatott meg.
    assert funded_account.get_balance() == 1000
    assert other_account.get_balance() == 500


@pytest.mark.parametrize("amount", [0, -50])
def test_transfer_not_positive_amount_raises(funded_account, other_account, amount):
    # A transfer() maga nem ellenőrzi az összeget, a withdraw()-ra bízza.
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        funded_account.transfer(amount, other_account)


def test_transfer_keeps_total_money(funded_account, other_account):
    # Utalásnál pénz nem keletkezik és nem tűnik el: az összeg ugyanannyi marad.
    total_before = funded_account.get_balance() + other_account.get_balance()
    funded_account.transfer(321.5, other_account)
    total_after = funded_account.get_balance() + other_account.get_balance()
    assert total_after == total_before


def test_withdraw_from_empty_account_raises(empty_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        empty_account.withdraw(1)


def test_float_amounts_are_handled(empty_account):
    # 0.1 + 0.2 a számítógépen 0.30000000000000004, ezért pytest.approx-szal
    # hasonlítunk: "közelítőleg egyenlő".
    empty_account.deposit(0.1)
    empty_account.deposit(0.2)
    assert empty_account.get_balance() == pytest.approx(0.3)


# =============================================================================
# 5. LÉPÉS: EXTRA - a bank_account.py kiegészítéseinek tesztjei
# =============================================================================
# Ezek a tesztek az EREDETI kóddal elbuknának (lásd a megjegyzéseket),
# a javított verzióval mind sikeresek.

@pytest.mark.parametrize("bad_amount", ["50", None, [10], True, False])
def test_deposit_non_number_raises(empty_account, bad_amount):
    # Eredetileg: "50" és None -> zavaros TypeError, True -> sikeres befizetés (+1)!
    with pytest.raises(TypeError, match="Amount must be a number"):
        empty_account.deposit(bad_amount)


@pytest.mark.parametrize("bad_amount", ["50", None, True])
def test_withdraw_non_number_raises(funded_account, bad_amount):
    with pytest.raises(TypeError, match="Amount must be a number"):
        funded_account.withdraw(bad_amount)


@pytest.mark.parametrize("bad_balance", ["100", None, True])
def test_initial_balance_non_number_raises(bad_balance):
    with pytest.raises(TypeError, match="Amount must be a number"):
        BankAccount("Dénes", bad_balance)


@pytest.mark.parametrize("bad_amount", [float("nan"), float("inf"), float("-inf")])
def test_deposit_nan_or_infinite_raises(empty_account, bad_amount):
    # Eredetileg: deposit(nan) után az egyenleg "nan" lett, deposit(inf) után végtelen.
    with pytest.raises(ValueError, match="Amount must be a finite number"):
        empty_account.deposit(bad_amount)


@pytest.mark.parametrize("bad_amount", [float("nan"), float("inf")])
def test_withdraw_nan_or_infinite_raises(funded_account, bad_amount):
    with pytest.raises(ValueError, match="Amount must be a finite number"):
        funded_account.withdraw(bad_amount)
    assert funded_account.get_balance() == 1000


def test_transfer_to_self_raises_and_changes_nothing(funded_account):
    # Eredetileg: sikeres "utalás" saját magunknak.
    with pytest.raises(ValueError, match="Cannot transfer to the same account"):
        funded_account.transfer(100, funded_account)
    assert funded_account.get_balance() == 1000


@pytest.mark.parametrize("bad_owner", ["", "   ", None, 123])
def test_invalid_owner_raises(bad_owner):
    # Eredetileg: üres név és szám is elfogadott volt tulajdonosnak.
    with pytest.raises(ValueError, match="Owner must be a non-empty string"):
        BankAccount(bad_owner, 100)


def test_two_accounts_with_same_data_are_different():
    # Két ugyanolyan adatú számla két külön számla: egymás között utalhatnak.
    account_1 = BankAccount("Erik", 100)
    account_2 = BankAccount("Erik", 100)
    account_1.transfer(50, account_2)
    assert account_1.get_balance() == 50
    assert account_2.get_balance() == 150

# 3. házi feladat – Feladat 1: flat_finder.py
# Felhasznált órai anyag:
#   - lesson_03: input(), típuskonverzió (float), string metódusok (strip, title), f-string
#   - lesson_05: if-elif-else, összehasonlító operátorok (<, <=), membership operátor (in)

# 1. LÉPÉS: adatok bekérése a felhasználótól
# A strip() levágja a felesleges szóközöket, a title() minden szó első betűjét
# naggyá teszi, így a "new york ", "NEW YORK" és "New York" bemenet is ugyanaz lesz.
city = input("Melyik városban van a lakás? ").strip().title()

# Az input() mindig stringet ad vissza, ezért számmá kell alakítani,
# különben nem tudnánk a 4000-rel vagy a 3000-rel összehasonlítani.
rent = float(input("Mennyi a havi lakbér (USD)? "))

# 2. LÉPÉS: Sarah szabályainak lefordítása Python feltételekre
# A sorrend számít (lásd fizz_buzz.py "bad example"): előbb a konkrét városokat
# vizsgáljuk, és csak a legvégén az "összes többi hely" esetet (else).

if city in ["New York", "San Francisco"]:
    # "Bármelyik városban kivenne egy lakást, ha kevesebb mint 4000 USD"
    # -> szigorúan kisebb: <
    can_move = rent < 4000
elif city == "Washington":
    # "Semmi pénzért nem lakna ott" -> az ár nem számít, mindig False
    can_move = False
elif city == "Chicago":
    # "Bármit megadna érte" -> az ár nem számít, mindig True
    can_move = True
else:
    # "Bármilyen más hely: 3000 USD vagy ez alatti" -> kisebb vagy egyenlő: <=
    can_move = rent <= 3000

# 3. LÉPÉS: eredmény kiírása f-stringgel
# Ternary operátorral (ternary_operator.py) választjuk ki a megfelelő szöveget.
answer = "beköltözne" if can_move else "NEM költözne be"
print(f"Sarah {answer} a(z) {city} városi lakásba havi {rent:.2f} USD-ért.")

# 3. házi feladat – Feladat 2: rock_paper_scissors.py
# Felhasznált órai anyag:
#   - lesson_03: input(), int() konverzió, string metódusok, f-string
#   - lesson_04: dictionary (kulcs-érték párok, kulcs szerinti elérés, módosítás)
#   - lesson_05: if-elif-else, %, összehasonlító és logikai operátorok, in
#   - lesson_06: while True + break, continue, for ciklus range()-dzsel

# A feladat szerint a választás kizárólag ez a három string lehet.
VALID_CHOICES = ["rock", "paper", "scissors"]

# Melyik választás melyiket győzi le: a kulcs legyőzi az értéket.
BEATS = {
    "rock": "scissors",    # a kő kicsorbítja az ollót
    "paper": "rock",       # a papír becsomagolja a követ
    "scissors": "paper",   # az olló elvágja a papírt
}

# A pontszámokat egy dictionaryben tároljuk (játékos neve -> pontszám).
scores = {
    "1. játékos": 0,
    "2. játékos": 0,
}

# 1. LÉPÉS: a körök számának bekérése, ellenőrzéssel
# Addig kérdezünk (while True), amíg érvényes számot nem kapunk, ekkor break.
# Érvényes: pozitív, páratlan egész szám, mert páros körszámnál
# (pl. 2 kör, 1-1 győzelem) döntetlen lehetne a végeredmény.
while True:
    rounds_text = input("Hány kört szeretnétek játszani? (páratlan szám) ")

    # Az isdigit() megnézi, hogy a string csak számjegyekből áll-e.
    # Így az int() nem "száll el", ha a felhasználó pl. "abc"-t ír.
    if not rounds_text.isdigit():
        print("Hiba: egész számot adj meg!")
        continue  # vissza a ciklus elejére, újra kérdezünk

    rounds = int(rounds_text)

    if rounds > 0 and rounds % 2 == 1:
        break  # jó a szám, kilépünk a ciklusból
    else:
        print("Hiba: a körök száma pozitív páratlan szám legyen, hogy ne lehessen döntetlen!")

# 2. LÉPÉS: a körök lejátszása
# A for ciklus pontosan annyiszor fut le, ahány kört megadtak.
for round_number in range(1, rounds + 1):
    print(f"\n----- {round_number}. kör (összesen {rounds}) -----")

    # Egy kör addig tart, amíg valaki nem nyer: döntetlennél újrajátsszuk.
    while True:
        # A két játékos választását felváltva kérjük be.
        # A belső ciklus mindkét játékosra lefut (nested_loops.py).
        choices = {}
        for player in scores:
            while True:
                choice = input(f"{player}, válassz (rock, paper, scissors): ").strip().lower()
                if choice in VALID_CHOICES:
                    break
                print("Hiba: csak 'rock', 'paper' vagy 'scissors' választható!")
            choices[player] = choice

        choice_1 = choices["1. játékos"]
        choice_2 = choices["2. játékos"]

        # 3. LÉPÉS: a kör kiértékelése
        if choice_1 == choice_2:
            print(f"Mindketten ezt választottátok: {choice_1}. Döntetlen, a kör újrakezdődik!")
            continue  # nincs pont, ugyanez a kör kezdődik újra
        elif BEATS[choice_1] == choice_2:
            winner = "1. játékos"
        else:
            winner = "2. játékos"

        # 4. LÉPÉS: a kör nyertesének pontszáma +1 (assignment operátor: +=)
        scores[winner] += 1
        print(f"{choice_1} vs {choice_2} -> ezt a kört a(z) {winner} nyerte!")
        print(f"Állás: 1. játékos: {scores['1. játékos']} | 2. játékos: {scores['2. játékos']}")
        break  # megvan a kör nyertese, mehet a következő kör

# 5. LÉPÉS: a végeredmény kiírása
# Páratlan körszám és döntetlen nélküli körök miatt a két pontszám sosem egyenlő.
if scores["1. játékos"] > scores["2. játékos"]:
    overall_winner = "1. játékos"
else:
    overall_winner = "2. játékos"

print(f"\nA győztes: {overall_winner}, {scores[overall_winner]} ponttal!")

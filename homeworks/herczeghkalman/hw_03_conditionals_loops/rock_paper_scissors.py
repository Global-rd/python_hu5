
"""
Írj egy programot ami levezényli a kő-papír-olló játékot két játékos között. A 
program kérje be, hogy hány kört akarnak játszani a játékosok. Figyelj oda, hogy 
olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent 
játszani! Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a 
körök számát amíg páratlan számot nem ad meg. Ezután a program felváltva kérje 
be az első és második játékos válaszát, ami kizárólag a következő stringek 
valamelyik lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát 
ahogy a körök számánál. Egy adott kör addig ne érjen véget, amíg valaki nem nyer 
(döntetlen esetén az adott kört újra kell játszani). Tárold a nyertesek pontjait, és 
minden kör végén növeld az aktuális játékos pontszámát. A végén printeld ki ki 
nyert, és hány ponttal. 
"""

# A körök számának bekérése

#Először a megadott értéket egész számmá alakítom

# A kettővel maradékosztás hatására mindíg 1-nek kell maradni, ez garantálja a páratlan számot így a végeredmény nem lehet döntetlen
# A break parancs hatására azonnal kilép a ciklusból

while True:
    try:
        rounds = int(input("Hány kört szeretnétek játszani? "))

        if rounds > 0 and rounds % 2 == 1:
            break
        else:
            print("Hiba! Pozitív páratlan számot adj meg!")
    except ValueError:
        print("Hiba! Egy egész számot adj meg!")


player1_score = 0
player2_score = 0

choices = ["rock", "paper", "scissors"]

# A megadott számú kör lejátszása

# Az (f"\n) kódrészlettel sorkihagyással egy új sorban írja ki az f-string a kör számát

for round_number in range(1, rounds + 1):
    print(f"\n--- {round_number}. kör ---")

    while True:
        player1 = input("1. játékos (rock/paper/scissors): ").lower()

        if player1 in choices:
            break
        else:
            print("Hiba! Csak ezt választhatod: rock, paper vagy scissors.")

    while True:
        player2 = input("2. játékos (rock/paper/scissors): ").lower()

        if player2 in choices:
            break
        else:
            print("Hiba! Csak ezt választhatod: rock, paper vagy scissors.")


    # Döntetlen esetén a kört addig játsszuk újra, amíg nincs győztes

    while player1 == player2:
        print("Döntetlen! Ezt a kört újra kell játszani.")

        while True:
            player1 = input("1. játékos (rock/paper/scissors): ").lower()

            if player1 in choices:
                break
            else:
                print("Hiba! Csak ezt választhatod: rock, paper vagy scissors.")

        while True:
            player2 = input("2. játékos (rock/paper/scissors): ").lower()

            if player2 in choices:
                break
            else:
                print("Hiba! Csak ezt választhatod: rock, paper vagy scissors.")


    # Leírom milyen esetben melyik játékos nyer

    if (
        (player1 == "rock" and player2 == "scissors")
        or (player1 == "paper" and player2 == "rock")
        or (player1 == "scissors" and player2 == "paper")
    ):
        player1_score += 1
        print("Az 1. játékos nyerte a kört!")
    else:
        player2_score += 1
        print("A 2. játékos nyerte a kört!")

    print(f"Állás: 1. játékos {player1_score} - {player2_score} 2. játékos")


# A végeredmény

print("\n--- VÉGEREDMÉNY ---")

if player1_score > player2_score:
    print(f"Az 1. játékos nyert {player1_score} ponttal!")
else:
    print(f"A 2. játékos nyert {player2_score} ponttal!")


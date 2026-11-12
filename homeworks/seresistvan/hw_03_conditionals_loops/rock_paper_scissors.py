# Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. A
# program kérje be, hogy hány kört akarnak játszani a játékosok. Figyelj oda, hogy
# olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent
# játszani! Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a
# körök számát amíg páratlan számot nem ad meg. Ezután a program felváltva kérje
# be az első és második játékos válaszát, ami kizárólag a következő stringek
# valamelyik lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát
# ahogy a körök számánál. Egy adott kör addig ne érjen véget, amíg valaki nem nyer
# (döntetlen esetén az adott kört újra kell játszani). Tárold a nyertesek pontjait, és
# minden kör végén növeld az aktuális játékos pontszámát. A végén printeld ki ki
# nyert, és hány ponttal.

right_answers = ["rock", "paper", "scissors"]

nr_of_rounds = int(input("Welcome! How many rounds do you want to play? \n"))

if  not nr_of_rounds.isdigit():     # Itt nyilván try és except kellene, de azt még nem vettük, tehát így oldom meg.
    nr_of_rounds = int(nr_of_rounds)
    print("Please enter an integer!")
    nr_of_rounds = int(input("Welcome! How many rounds do you want to play? \n"))
else:

    if nr_of_rounds % 2 == 0:
        while nr_of_rounds % 2 == 0:
            print("Please enter an odd number!")
            nr_of_rounds = int(input("Welcome! How many rounds do you want to play? (Odd nr. please) \n"))
            if nr_of_rounds % 2 != 0:
                print("Thanks!")
                break

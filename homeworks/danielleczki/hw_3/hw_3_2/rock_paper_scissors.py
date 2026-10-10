# A kör számának bekérése
while True:
    korok_szama = input("Hány kört szeretnél játszani?: ")

    if korok_szama.isdigit():
        korok_szama =int(korok_szama)
        if korok_szama > 0 and korok_szama % 2 == 1:
            break
        else:
            print("Pozitív páratlan egész számot adj meg!")
    else:
        print("Egész számot adj meg!")

# A játékosok kezdeti pontszáma
jatekos1_pont = 0
jatekos2_pont = 0
# A kör számainak kiirása
for kor in range(1, korok_szama +1):
    print(f"\n ---------{kor} Kör----------")

    while True:
        # Játékosok válaszainak bekérése
        while True:
            jatekos1 = input("elso válasz!: ").strip().lower()
            if jatekos1 in ["rock","paper","scissors"]:
                break
            else:
                print("Adj normális választ kérlek!")

        while True:
            jatekos2 = input("másik válasz!: ").strip().lower()
            if jatekos2 in ["rock","paper","scissors"]:
                break
            else:
                print("Adj te is normális választ kérlek!: ")
    # A játék szabályának meghatározása
        if jatekos1 == jatekos2:
            print("döntetlen! új játék kell!")
            continue
        elif(
            (jatekos1 == "rock" and jatekos2 == "scissors") or
            (jatekos1 == "paper" and jatekos2 == "rock")or
            (jatekos1 == "scissors" and jatekos2 == "paper")
                ):
            jatekos1_pont += 1
            print("Az elso játékos nyerte a kört!\n")
        else:
            jatekos2_pont += 1
            print("A második játékos nyerte a kört!\n")
        break
print("==========Végeredmény==========\n")
# A játékosok pontszámának kiirása
print(f"Első játékos pontszáma: {jatekos1_pont}")
print(f"Második játékos pontszáma: {jatekos2_pont}")
# Végső eredmény kiirása
print("\n-----------------------\n")
if jatekos1_pont > jatekos2_pont:
    
    print("Az első játékos nyert!")
elif jatekos2_pont > jatekos1_pont:
    print("A második játékos nyert!")
else:
    print("Döntetlen lett!")

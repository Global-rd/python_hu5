VALID_CHOICES = ["rock", "paper", "scissors"]

while True:
    rounds = int(input("Hány kört akartok játszani?: "))
    if rounds % 2 == 0 or rounds <= 0:
        print("Kérlek adj meg pozitív, páratlan számot!")
    else:
        break

player1_score = 0
player2_score = 0

for current_round in range(1, rounds + 1):
    print(f"--- {current_round}. kör ---")

    while True:
        while True:
            player1_choice = input("1. játékos választása (rock/paper/scissors): ").strip().lower()
            if player1_choice in VALID_CHOICES:
                break
            print("Érvénytelen választás! Csak a következők megengedettek: rock, paper, scissors.")

        while True:
            player2_choice = input("2. játékos választása (rock/paper/scissors): ").strip().lower()
            if player2_choice in VALID_CHOICES:
                break
            print("Érvénytelen választás! Csak a következők megengedettek: rock, paper, scissors.")

        if player1_choice == player2_choice:
             print("Döntetlen! A kört újra kell játszani.")
        elif ((player1_choice == "rock" and player2_choice == "scissors") or
            (player1_choice == "paper" and player2_choice == "rock") or
            (player1_choice == "scissors" and player2_choice == "paper")):
            print("Az 1. játékos nyerte ezt a kört!")
            player1_score += 1
            break 
        else:
            print("A 2. játékos nyerte ezt a kört!")
            player2_score += 1
            break

print("--- JÁTÉK VÉGE ---")
if player1_score > player2_score:
    print(f"Az 1. játékos nyert {player1_score} ponttal! (2. játékos: {player2_score} pont)")
else:
    print(f"A 2. játékos nyert {player2_score} ponttal! (1. játékos: {player1_score} pont)")

# --- Kő-papír-olló két játékos között ---
 

# --- játékosok nevének bekérése ---
player_1 = input("Add meg az első játékos nevét: ")
player_2 = input("Add meg a második játékos nevét: ")
 
# --- körök száma: csak pozitív, páratlan szám lehet, hogy ne legyen döntetlen ---
rounds = int(input("Hány kört szeretnétek játszani?: "))
while rounds <= 0 or rounds % 2 != 1:
    print("Pozitív, páratlan számot adj meg!")
    rounds = int(input("Hány kört szeretnétek játszani?: "))
 
# --- pontszámok, mindkét játékos 0-ról indul ---
score_1 = 0
score_2 = 0
 
# --- körök ismétlése ---
for round_number in range(1, rounds + 1):
    print()
    print(f"--- {round_number}. kör ---")
 
    # --- döntetlennél a kört újra kell játszani ---
    while True:
 
        # --- választások bekérése, csak rock, paper vagy scissors lehet ---
        player_1_choice = input(f"{player_1}, válassz: rock, paper vagy scissors: ")
        while player_1_choice != "rock" and player_1_choice != "paper" and player_1_choice != "scissors":
            print("A választod nem érvényes, használd a rock, paper vagy scissors szavakat!")
            player_1_choice = input(f"{player_1}, válassz: rock, paper vagy scissors: ")
 
        player_2_choice = input(f"{player_2}, válassz: rock, paper vagy scissors: ")
        while player_2_choice != "rock" and player_2_choice != "paper" and player_2_choice != "scissors":
            print("A választod nem érvényes, használd a rock, paper vagy scissors szavakat!")
            player_2_choice = input(f"{player_2}, válassz: rock, paper vagy scissors: ")
 
        # --- ha nem döntetlen, akkor a break kilép ---
        if player_1_choice == player_2_choice:
            print("Döntetlen, játszátok újra a kört!")
        else:
            break
 
    # --- a kör győztese kap egy pontot (ha nem az 1. nyert, akkor a 2.) ---
    if (
        (player_1_choice == "rock" and player_2_choice == "scissors")
        or (player_1_choice == "paper" and player_2_choice == "rock")
        or (player_1_choice == "scissors" and player_2_choice == "paper")
    ):
        score_1 += 1
        print(f"Ezt a kört {player_1} nyerte!")
    else:
        score_2 += 1
        print(f"Ezt a kört {player_2} nyerte!")
 
    # --- állás kiírása minden kör után ---
    print(f"Állás: {player_1} {score_1} – {player_2} {score_2}")
 
# --- végeredmény printelése
print()
if score_1 > score_2:
    print(f"{player_1} nyert, {score_1} ponttal!")
else:
    print(f"{player_2} nyert, {score_2} ponttal!")
 
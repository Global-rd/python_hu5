#a megengedett válaszok
valid_choices = ["rock", "paper", "scissors"]
#melyik választás melyiket üti: a kulcs üti az értéket (pl. a kő üti az ollót)
beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

#körök száma: addig kérjük újra, amíg pozitív, páratlan egész számot nem kapunk (így nem lehet döntetlen a végén)
rounds_input = input("How many rounds do you want to play? (odd number): ").strip()
while not rounds_input.isdigit() or int(rounds_input) % 2 == 0:
    print("Error: please enter a positive odd number (e.g. 1, 3, 5)!")
    rounds_input = input("How many rounds do you want to play? (odd number): ").strip()
rounds = int(rounds_input)

#a két játékos pontszáma
player1_score = 0
player2_score = 0

#for loop: annyiszor fut le, ahány kört kértek
for round_number in range(1, rounds + 1):
    print(f"\n--- Round {round_number} ---")

    #while loop: a kör addig tart, amíg valaki nem nyer (döntetlennél újrajátsszuk)
    while True:
        #első játékos válasza, hibás válasznál újra kérjük
        player1_choice = input("Player 1 (rock/paper/scissors): ").strip().lower()
        while player1_choice not in valid_choices:
            print("Error: the answer can only be rock, paper or scissors!")
            player1_choice = input("Player 1 (rock/paper/scissors): ").strip().lower()

        #második játékos válasza, ugyanígy
        player2_choice = input("Player 2 (rock/paper/scissors): ").strip().lower()
        while player2_choice not in valid_choices:
            print("Error: the answer can only be rock, paper or scissors!")
            player2_choice = input("Player 2 (rock/paper/scissors): ").strip().lower()

        if player1_choice == player2_choice:
            #döntetlen: a continue visszaugrik a while elejére, a kört újrajátsszuk
            print("Draw! Play this round again.")
            continue
        elif beats[player1_choice] == player2_choice:
            player1_score += 1
            print(f"Player 1 wins this round ({player1_choice} beats {player2_choice}).")
        else:
            player2_score += 1
            print(f"Player 2 wins this round ({player2_choice} beats {player1_choice}).")

        #van nyertes, a break kilép a while-ból, jöhet a következő kör
        break

    print(f"Score: Player 1: {player1_score} - Player 2: {player2_score}")

#a végén kihirdetjük a győztest (páratlan körszám miatt döntetlen nem lehet)
if player1_score > player2_score:
    print(f"\nPlayer 1 won the game with {player1_score} points (Player 2: {player2_score}).")
else:
    print(f"\nPlayer 2 won the game with {player2_score} points (Player 1: {player1_score}).")

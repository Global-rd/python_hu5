# Körök számának bekérése: csak pozitív páratlan számot fogad el.
while True:
    rounds = int(input("How many rounds do you want to play? "))

    if rounds > 0 and rounds % 2 == 1:
        break

    print("Please enter a positive odd number!")

player1_score = 0
player2_score = 0
current_round = 1

valid_choices = ["rock", "paper", "scissors"]

# A játék a megadott számú, nem döntetlen körig tart.
while current_round <= rounds:
    print(f"\nRound {current_round}")

    # Player 1 választásának ellenőrzése.
    while True:
        player1 = input("Player 1: ").strip().lower()

        if player1 in valid_choices:
            break

        print("Invalid choice! Use rock, paper or scissors.")

    # Player 2 választásának ellenőrzése.
    while True:
        player2 = input("Player 2: ").strip().lower()

        if player2 in valid_choices:
            break

        print("Invalid choice! Use rock, paper or scissors.")

    # Döntetlennél ugyanazt a kört újrajátsszuk.
    if player1 == player2:
        print("Draw! Replay round.")
        continue

    # Player 1 nyer.
    if (
        (player1 == "rock" and player2 == "scissors")
        or (player1 == "paper" and player2 == "rock")
        or (player1 == "scissors" and player2 == "paper")
    ):
        player1_score += 1
        print("Player 1 wins this round!")

    # Player 2 nyer.
    else:
        player2_score += 1
        print("Player 2 wins this round!")

    current_round += 1

# Végeredmény: ez már a játék ciklusán kívül van.
print("\nFinal result:")
print(f"Player 1 score: {player1_score}")
print(f"Player 2 score: {player2_score}")

if player1_score > player2_score:
    print(f"Player 1 wins the game with {player1_score} points!")
else:
    print(f"Player 2 wins the game with {player2_score} points!")
rounds = int(input("How many rounds do you want to play? "))
while rounds % 2 == 0:
    print("The number of rounds must be odd.")
    rounds = int(input("How many rounds do you want to play? "))
player1_score = 0
player2_score = 0
for round_number in range(1, rounds + 1):
    print(f"Round {round_number}")

    while True:
        player1_choice = input(
            "Player 1 - choose rock, paper or scissors: "
        ).strip().lower()

        while player1_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice.")
            player1_choice = input(
                "Player 1 - choose rock, paper or scissors: "
            ).strip().lower()

        player2_choice = input(
            "Player 2 - choose rock, paper or scissors: "
        ).strip().lower()

        while player2_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice.")
            player2_choice = input(
                "Player 2 - choose rock, paper or scissors: "
            ).strip().lower()
        if player1_choice == player2_choice:
            print("Draw! Play this round again.")
            continue
        if (
                (player1_choice == "rock" and player2_choice == "scissors")
                or (player1_choice == "paper" and player2_choice == "rock")
                or (player1_choice == "scissors" and player2_choice == "paper")
        ):
            player1_score += 1
            print("Player 1 wins this round!")
            break
        else:
            player2_score += 1
            print("Player 2 wins this round!")
            break
if player1_score > player2_score:
    print(f"Player 1 wins the game with {player1_score} points!")
else:
    print(f"Player 2 wins the game with {player2_score} points!")



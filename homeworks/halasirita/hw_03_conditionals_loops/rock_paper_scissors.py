valid_choices = ["rock", "paper", "scissors"]

# Páratlan számú kör
rounds = int(input("Enter number of rounds (must be an odd number): "))

while rounds % 2 == 0 or rounds <= 0:
    print("Invalid number of rounds. Please enter a positive odd number.")
    rounds = int(input("Enter number of rounds: "))

player_1_score = 0
player_2_score = 0

for round_number in range(rounds):
    print(f"\nRound {round_number + 1}")

    # A kör folytatódik, amíg nincs nyertes
    while True:
        player_1 = input(
            "Player 1 - rock, paper or scissors: "
        ).strip().lower()

        while player_1 not in valid_choices:
            print("Invalid choice.")
            player_1 = input(
                "Player 1 - rock, paper or scissors: "
            ).strip().lower()

        player_2 = input(
            "Player 2 - rock, paper or scissors: "
        ).strip().lower()

        while player_2 not in valid_choices:
            print("Invalid choice.")
            player_2 = input(
                "Player 2 - rock, paper or scissors: "
            ).strip().lower()

        # Döntetlen - újrajátszás
        if player_1 == player_2:
            print("It's a tie. Replay this round.")
            continue

        # Player 1 nyerő kombinációk
        if (
            (player_1 == "rock" and player_2 == "scissors")
            or (player_1 == "scissors" and player_2 == "paper")
            or (player_1 == "paper" and player_2 == "rock")
        ):
            player_1_score += 1
            print("Player 1 wins this round!")

        else:
            player_2_score += 1
            print("Player 2 wins this round!")

        break

print("\nFinal result:")

if player_1_score > player_2_score:
    print(f"Player 1 wins with {player_1_score} points!")
else:
    print(f"Player 2 wins with {player_2_score} points!")


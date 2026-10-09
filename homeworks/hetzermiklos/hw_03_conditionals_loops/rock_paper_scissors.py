
# Rock Paper Scissors Game

while True:
    try:
        rounds = int(input("How many rounds would you like to play? "))

        if rounds > 0 and rounds % 2 == 1:
            break
        else:
            print("Invalid number! Please enter a positive odd number.")

    except ValueError:
        print("Invalid input! Please enter a number.")

print(f"The game will have {rounds} rounds.")

player1_score = 0
player2_score = 0

valid_choices = ["rock", "paper", "scissors"]

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}")

    while True:

        # Player 1 choice
        while True:
            player1 = input(
                "Player 1 (rock, paper, scissors): "
            ).strip().lower()

            if player1 in valid_choices:
                break
            else:
                print("Invalid choice! Please try again.")

        # Player 2 choice
        while True:
            player2 = input(
                "Player 2 (rock, paper, scissors): "
            ).strip().lower()

            if player2 in valid_choices:
                break
            else:
                print("Invalid choice! Please try again.")

        # Check the result
        if player1 == player2:
            print("It's a tie! Play this round again.")

        elif (
            (player1 == "rock" and player2 == "scissors")
            or (player1 == "paper" and player2 == "rock")
            or (player1 == "scissors" and player2 == "paper")
        ):
            player1_score += 1
            print("Player 1 wins this round!")
            break

        else:
            player2_score += 1
            print("Player 2 wins this round!")
            break

    # Show the score after each round
    print(
        f"Score: Player 1 = {player1_score}, "
        f"Player 2 = {player2_score}"
    )

    # Stop when a player has won the majority
    if (
        player1_score > rounds // 2
        or player2_score > rounds // 2
    ):
        break

# Final result
print("\nFinal Result")

print(f"Player 1 score: {player1_score}")
print(f"Player 2 score: {player2_score}")

if player1_score > player2_score:
    print(f"Player 1 wins the game with {player1_score} points!")

else:
    print(f"Player 2 wins the game with {player2_score} points!")

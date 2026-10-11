
# Homework 03 - Task 2
# Rock, Paper, Scissors - Simon David

print("Welcome to Rock, Paper, Scissors!")

# Asking for an odd number of rounds
while True:
    try:
        rounds = int(input("How many rounds would you like to play? "))

        if rounds <= 0:
            print("Please enter a positive number.")
        elif rounds % 2 == 0:
            print("Please enter an odd number of rounds.")
        else:
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")

# Initial scores
player1_score = 0
player2_score = 0

# Valid choices
valid_choices = ("rock", "paper", "scissors")

# Number of wins needed for victory
wins_needed = rounds // 2 + 1

# Playing the game
for round_number in range(1, rounds + 1):

    print(f"\n--- Round {round_number} of {rounds} ---")

    # Repeat the round in case of a draw
    while True:

        # Player 1 input validation
        while True:
            player1 = input(
                "Player 1 - rock, paper or scissors: "
            ).strip().lower()

            if player1 in valid_choices:
                break

            print("Invalid choice! Try again.")

        # Player 2 input validation
        while True:
            player2 = input(
                "Player 2 - rock, paper or scissors: "
            ).strip().lower()

            if player2 in valid_choices:
                break

            print("Invalid choice! Try again.")

        # Checking for a draw
        if player1 == player2:
            print("It's a draw! Replay this round.")
            continue

        # Determining the winner
        if (
            (player1 == "rock" and player2 == "scissors")
            or (player1 == "paper" and player2 == "rock")
            or (player1 == "scissors" and player2 == "paper")
        ):
            player1_score += 1
            print("Player 1 wins this round!")

        else:
            player2_score += 1
            print("Player 2 wins this round!")

        break

    # Displaying the current score
    print(
        f"Current score: Player 1: {player1_score} | "
        f"Player 2: {player2_score}"
    )

    # Extra: Stop if a player has already won the match
    if player1_score == wins_needed:
        print("\nPlayer 1 has secured the victory!")
        break

    if player2_score == wins_needed:
        print("\nPlayer 2 has secured the victory!")
        break

# Final results
print("\n===== FINAL RESULTS =====")

print(f"Player 1: {player1_score} points")
print(f"Player 2: {player2_score} points")

if player1_score > player2_score:
    print(f"Player 1 wins with {player1_score} points!")
else:
    print(f"Player 2 wins with {player2_score} points!")

print("Thanks for playing!")

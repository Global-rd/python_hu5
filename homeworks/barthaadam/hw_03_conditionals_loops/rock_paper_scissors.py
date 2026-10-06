# Ask for the number of rounds
rounds = int(input("How many rounds would you like to play? (Rounds must be odd): "))

while rounds % 2 == 0:
    print("Error! The number of rounds must be odd.")
    rounds = int(input("How many rounds would you like to play? (Rounds must be odd): "))

player1_score = 0
player2_score = 0

# Play the rounds
for round_number in range(1, rounds + 1):

    print(f"\nRound {round_number}")

    # A round continues until someone wins
    while True:

        player1 = input("Player 1 -> rock, paper or scissors: ").strip().lower()

        while player1 not in ["rock", "paper", "scissors"]:
            print("Error! Please enter rock, paper or scissors.")
            player1 = input("Player 1 -> rock, paper or scissors: ").strip().lower()

        player2 = input("Player 2 -> rock, paper or scissors: ").strip().lower()

        while player2 not in ["rock", "paper", "scissors"]:
            print("Error! Please enter rock, paper or scissors.")
            player2 = input("Player 2 -> rock, paper or scissors: ").strip().lower()

        # Draw
        if player1 == player2:
            print("Draw! Play this round again.")

        # Player 1 wins
        elif (
            (player1 == "rock" and player2 == "scissors")
            or (player1 == "paper" and player2 == "rock")
            or (player1 == "scissors" and player2 == "paper")
        ):
            player1_score += 1
            print("Player 1 wins this round!")
            break

        # Player 2 wins
        else:
            player2_score += 1
            print("Player 2 wins this round!")
            break

    print(f"Score: Player 1: {player1_score} - Player 2: {player2_score}")

# Print final result
if player1_score > player2_score:
    print(f"\nPlayer 1 wins the game with {player1_score} points!")
else:
    print(f"\nPlayer 2 wins the game with {player2_score} points!")
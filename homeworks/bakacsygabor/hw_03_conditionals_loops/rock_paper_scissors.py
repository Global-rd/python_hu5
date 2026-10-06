rounds = int(input("How many rounds would you like to play? "))

while rounds <= 0 or rounds % 2 == 0:
    print("The number of rounds must be a positive odd number.")
    rounds = int(input("How many rounds would you like to play? "))
valid_choices = ("rock", "paper", "scissors")
player_one_score = 0
player_two_score = 0

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}")
    while True:
        player_one = input("Player 1 - rock, paper, or scissors? ").strip().lower()

        while player_one not in valid_choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            player_one = input(
                "Player 1 - rock, paper, or scissors? "
            ).strip().lower()
        player_two = input("Player 2 - rock, paper, or scissors? ").strip().lower()

        while player_two not in valid_choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            player_two = input(
                "Player 2 - rock, paper, or scissors? "
            ).strip().lower()
        if player_one == player_two:
            print("It is a draw. Replay this round.")
            continue

        break
    if (
        (player_one == "rock" and player_two == "scissors")
        or (player_one == "paper" and player_two == "rock")
        or (player_one == "scissors" and player_two == "paper")
    ):
        player_one_score += 1
        print("Player 1 wins this round.")
    else:
        player_two_score += 1
        print("Player 2 wins this round.")

    print(f"Score: Player 1 {player_one_score} - {player_two_score} Player 2")
print("\nFinal result:")

if player_one_score > player_two_score:
    winner = "Player 1"
else:
    winner = "Player 2"

print(f"{winner} wins the match!")
print(f"Final score: Player 1 {player_one_score} - {player_two_score} Player 2")

    



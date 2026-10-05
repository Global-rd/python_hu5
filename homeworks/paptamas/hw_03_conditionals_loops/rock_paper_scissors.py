def get_valid_rounds():
    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds % 2 == 1:
                return rounds
            else:
                print("Error: You must enter an odd number of rounds!")
        except ValueError:
            print("Error: Please enter a valid integer!")


def get_valid_choice(player_name):
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        choice = input(f"{player_name}, enter your choice (rock/paper/scissors): ").strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print("Error: Invalid choice! Please enter rock, paper, or scissors.")


def determine_winner(p1, p2):
    if p1 == p2:
        return None  # tie
    if (p1 == "rock" and p2 == "scissors") or \
       (p1 == "paper" and p2 == "rock") or \
       (p1 == "scissors" and p2 == "paper"):
        return "Player 1"
    else:
        return "Player 2"


rounds = get_valid_rounds()
score_p1 = 0
score_p2 = 0

for current_round in range(1, rounds + 1):
    print(f"\n--- Round {current_round} ---")

    while True:
        p1_choice = get_valid_choice("Player 1")
        p2_choice = get_valid_choice("Player 2")

        winner = determine_winner(p1_choice, p2_choice)

        if winner is None:
            print("Tie! Replay the round.")
        else:
            if winner == "Player 1":
                score_p1 += 1
            else:
                score_p2 += 1
            print(f"{winner} wins this round!")
            break

print("\n=== Final Result ===")
if score_p1 > score_p2:
    print(f"Player 1 wins the game with {score_p1} points!")
else:
    print(f"Player 2 wins the game with {score_p2} points!")

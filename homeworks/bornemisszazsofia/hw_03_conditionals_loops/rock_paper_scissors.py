current_round = 1
score_player_1 = 0
score_player_2 = 0

game_rounds = int(input("How many rounds would you like to play?"))

while game_rounds % 2 == 0 or game_rounds < 0:
    #print("Error. Please provide an uneven number.")
    game_rounds = int(input("Error. Please provide a positive odd number."))

while current_round <= game_rounds:

    #player_1_input = input("Player 1. Please choose rock, paper, or scissors: ").strip().lower()

    while (player_1_input := input("Player 1. Please choose rock, paper, or scissors: ").strip().lower()) not in ["rock", "paper", "scissors"]:
        print("Invalid input.")
        continue

    #player_2_input = input("Player 2. Please choose rock, paper, or scissors: ").strip().lower()

    while (player_2_input := input("Player 2. Please choose rock, paper, or scissors: ").strip().lower()) not in ["rock", "paper", "scissors"]:
        print("Invalid input.")
        continue

    if player_1_input == player_2_input:
        print("It's a tie! Please start again.")
        continue

    elif player_1_input == "rock" and player_2_input == "paper":
        print("Player 2 wins. Congratulations!")
        score_player_2 += 1
    elif player_1_input == "paper" and player_2_input == "scissors":
        print("Player 2 wins. Congratulations!")
        score_player_2 += 1
    elif player_1_input == "scissors" and player_2_input == "rock":
        print("Player 2 wins. Congratulations!")
        score_player_2 += 1
    elif player_1_input == "scissors" and player_2_input == "paper":
        print("Player 1 wins. Congratulations!")
        score_player_1 += 1
    elif player_1_input == "paper" and player_2_input == "rock":
        print("Player 1 wins. Congratulations!")
        score_player_1 += 1
    elif player_1_input == "rock" and player_2_input == "scissors":
        print("Player 1 wins. Congratulations!")
        score_player_1 += 1
    else:
        pass

    current_round += 1

game_winner = "Player 1" if score_player_1 > score_player_2 else "Player 2"
game_score = score_player_1 if score_player_1 > score_player_2 else score_player_2

print(f"Congratulations to {game_winner} who won with {game_score} points!")



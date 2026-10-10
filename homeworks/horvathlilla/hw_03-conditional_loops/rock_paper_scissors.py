score_player_1 = 0
score_player_2 = 0

while True:
    number_of_rounds = int(input("Welcome to rock, paper, scissors! Enter the number of rounds you would like to play. Please enter an odd number: "))
    if number_of_rounds == 0:
        print("You have entered an invalid number. Please select a number greater than 0.")
    elif number_of_rounds % 2 == 0:
        print("You have entered an invalid number. Please select an odd number so the game can end without a tie.")
    else:
        print(f"You have selected {number_of_rounds} rounds. Let's begin!")
        break

for game in range (number_of_rounds):
    player_1_choice = input("Player 1!Please enter your choice (rock, paper, or scissors): ").lower()
    while player_1_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        player_1_choice = input("Player 1! Please enter your choice (rock, paper, or scissors): ").lower()
    print(f"Player 1 chose: {player_1_choice}")

    player_2_choice = input("Player 2! Please select rock, paper, or scissors: ").lower()
    while player_2_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        player_2_choice = input("Player 2! Please select rock, paper, or scissors: ").lower()
    print(f"Player 2 chose: {player_2_choice}")

    while player_1_choice == player_2_choice:
        print("It's a tie, play this round again!")
        player_1_choice = input("Player 1! Please enter your choice (rock, paper, or scissors): ").lower()
        player_2_choice = input("Player 2! Please select rock, paper, or scissors: ").lower()
    if (
        player_1_choice == "rock" and player_2_choice == "scissors"
          or 
        player_1_choice == "paper" and player_2_choice == "rock"
          or 
        player_1_choice == "scissors" and player_2_choice == "paper"
    ):
        score_player_1 += 1
        print("Player 1 wins this round! Current score: Player 1 -", score_player_1, "Player 2 -", score_player_2)
    else:
        score_player_2 += 1
        print("Player 2 wins this round!Current score: Player 1 -", score_player_1, "Player 2 -", score_player_2)

if score_player_1 > score_player_2:
    print("Player 1 wins the game! Final score: Player 1 -", score_player_1, "Player 2 -", score_player_2)
else:
    print("Player 2 wins the game! Final score: Player 1 -", score_player_1, "Player 2 -", score_player_2)

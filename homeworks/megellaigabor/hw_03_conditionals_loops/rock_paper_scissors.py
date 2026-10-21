# I decided to use a list of tuples making the code sherter.
winning_pairs = [("rock", "scissors"),
                 ("paper", "rock"),
                 ("scissors", "paper")]

# I created some variables to cover the rest.
player1_score = 0
player2_score = 0

round_counter = 1

# Start the game by asking the number of rounds. 
number_of_rounds = int(input("How many rounds would you like to play? (Use an odd number) "))
# Checking the input. I tried to remove silly answers as well, like 0 and negatives. 
while number_of_rounds % 2 == 0 or number_of_rounds < 1:
    if number_of_rounds < 1:
        print("You have entered a number less than 1. Please enter a valid number.")
    else:
        print("You have entered an even number. Please enter an odd number.")
    number_of_rounds = int(input("No 0, negative or even numbers allowed. How many rounds would you like to play? (Use an odd number) "))

print(f"Great! We will play {number_of_rounds} rounds. Let's start!")    

# This is the game engine! :) I messed with the round counter a lot and I also had issues using the tuples. 
while round_counter <= number_of_rounds:
    player1_choice = input(f"Round {round_counter}: Player 1, please enter your choice (rock, paper, or scissors): ").lower().strip()
    player2_choice = input(f"Round {round_counter}: Player 2, please enter your choice (rock, paper, or scissors): ").lower().strip()
    if (player1_choice, player2_choice) in winning_pairs:
        print(f"Player 1 wins round {round_counter}!")
        player1_score += 1
        round_counter += 1
    elif (player2_choice, player1_choice) in winning_pairs:
        print(f"Player 2 wins round {round_counter}!")
        player2_score += 1
        round_counter += 1
    else:
        print(f"Round {round_counter} is a tie! Let's play again.")

# Closing the game with a final score and announcing the winner.
if player1_score > player2_score:
    print(f"Player 1 wins the game with a score of {player1_score} to {player2_score}!")
else:
    print(f"Player 2 wins the game with a score of {player2_score} to {player1_score}!")
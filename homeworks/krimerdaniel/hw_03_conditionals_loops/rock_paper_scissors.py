## ROCK-PAPER-SCISSORS GAME
# The program simulates a classic rock-paer-scissors game by the following rules:
#   - odd number of rounds are taken;
#   - if players choose the same move, the round must be repeated;
#   - rock brakes scissors, scissors cut paper, and paper coats rock.

# As the script prints many lines in the terminal, "screen" is cleared before each run
import os
os.system("cls")


# Requesting players' names
player_a_name = input("Enter 1st player's name: ")
player_b_name = input("Enter 2nd player's name: ")
print(f"{player_a_name}, {player_b_name} welcome to rock-paper-scissors! Remember that rock brakes scissors, scissors cut paper, and paper coats rock. Let's play! Good luck!")


# Requesting nr. of rounds
rounds = 0
round_try_count = 0
while True:
    try:
        rounds = int(input("How many rounds do you wanna play? "))
        break
    except ValueError:
        print("You should provide an integer, please try again.")    
while rounds % 2 == 0:
    rounds = int(input(f"As {rounds} is even, it can lead to draw. Please enter an odd number: "))
    round_try_count += 1
print(f"{'Finally and odd number! ' f'{rounds} round(s) it is.' if round_try_count > 2 else f'Thanks! {rounds} round(s) it is.'}")  #Acknowledging the nr. of rounds


# Establising variables for the game
final_score = [0, 0]
counter = 1
score_dict = {("scissors", "paper") : [1, 0],
              ("paper", "scissors") : [0, 1],
              ("scissors", "rock") : [0, 1],
              ("rock", "scissors") : [1, 0],
              ("rock", "paper") : [0, 1],
              ("paper", "rock") : [1, 0]
              }

# Playing the game {rounds} times
while counter <= rounds:
    print(f"{'Final round starts.' if counter == rounds else f'Round {counter} starts.'}")
    # Requesting and validating players' input
    player_a_move = input(f"{player_a_name}, enter your move (rock/paper/scissors): ")
    while player_a_move not in ["rock", "paper", "scissors"]:
        player_a_move = input(f"{player_a_name}'s move is invalid, enter your move again (rock/paper/scissors): ")
    player_b_move = input(f"{player_b_name}, enter your move (rock/paper/scissors): ")
    while player_b_move not in ["rock", "paper", "scissors"]:
        player_b_move = input(f"{player_b_name}'s move is invalid, enter your move again (rock/paper/scissors): ")
    # Comparing players' choices and announcing round's score, if any, or repeating the round
    if player_a_move != player_b_move:
        round_score = score_dict.get(tuple([player_a_move, player_b_move]))
        final_score[0], final_score[1] = final_score[0] + round_score[0], final_score[1] + round_score[1]
        print(f"{f'{player_a_name}' if round_score[0] > round_score[1] else f'{player_b_name}'} wins the round.")
        
        counter += 1
    elif player_a_move == player_b_move:
        print(f"Both players chose the same move ({player_a_move}), it's a draw, round must be repeated.")
#Game ends, announcing final score
print(f"The game has ended. CONGRATS {f'{player_a_name.upper()},' if final_score[0] > final_score[1] else f'{player_b_name.upper()},'} you won by {final_score[0]} : {final_score[1]}")
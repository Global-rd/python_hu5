from pprint import pprint

number_of_rounds = int(input("How many round would you like to play? "))

while number_of_rounds % 2 == 0:
    number_of_rounds = int(input("This is not an odd number. Please enter an other number: "))

player_one_score = 0
player_two_score = 0   
game_history = []


for round in range(number_of_rounds):
    # Player 1's choice
    while True:
        player_one_choice = input("Player ONE: Give me your answer: ").lower()
        if player_one_choice in ("rock", "paper", "scissors"):
            break
        player_one_choice = input("You only can type rock, paper or scissors. Give me your new answer: ").lower()
    
    # Player 2's choice   
    while True:
        player_two_choice = input("Player TWO: Give me your answer: ").lower()
        if player_two_choice in ("rock", "paper", "scissors"):
            break
        player_two_choice = input("You only can type rock, paper or scissors. Give me your new answer: ").lower()
    
    # Same choice
    while player_one_choice == player_two_choice: 
        print("You cannot give the same answer. Enter an other one:")
        player_two_choice = input("Player_2: ").lower()
    
    # Determine the winner
    if player_one_choice == "rock" and player_two_choice == "scissors":
        player_one_score += 1       
        round_winner = "gamer 1"
    elif player_one_choice == "paper" and player_two_choice == "rock":
        player_one_score += 1
        round_winner = "gamer 1"
    elif player_one_choice == "scissors" and player_two_choice == "paper":
        player_one_score += 1
        round_winner = "gamer 1"
    else:
        player_two_score += 1
        round_winner = "gamer 2"

    #Statisctic    
    game_history.append(
    {'round': round + 1,
    'gamer 1': player_one_choice,
    'gamer 2': player_two_choice,
    'gamer 1 score': player_one_score,
    'gamer 2 score': player_two_score,
    'winner': round_winner})

# Determine the overall winner 
final_winner = "player ONE" if player_one_score > player_two_score else "player TWO"

pprint(game_history)

print(f"The player ONE has {player_one_score} scores. The player TWO has {player_two_score} scores . The final winner is {final_winner}")
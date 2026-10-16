# # Feladat 2: while és for loop használata
# Kő, papír, olló játék

correct_answers = ["rock", "paper", "scissors"]

player1_score = 0
player2_score = 0

nr_of_rounds = int(input("How many rounds do you want to play? "))
nr_counter = 1
while nr_of_rounds % 2 == 0:
    print("Please enter an odd number!")
    nr_of_rounds = int(input("How many rounds do you want to play? "))

while nr_of_rounds > 0:

    print(f"-------------------- Round {nr_counter} -------------------- ")

    player_1_choice = input("Player 1, please enter your choice: ")
    if player_1_choice not in correct_answers:
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors' only!")
        continue

    player_2_choice = input("Player 2, please enter your choice: ")
    print("-------------------------------------------------")
    if player_2_choice not in correct_answers:
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors' only!")
        continue

    if player_1_choice == "rock" and player_2_choice == "scissors":
        print("Nice one, Player 1, you won this round!\n")
        player1_score += 1

    elif player_1_choice == "paper" and player_2_choice == "rock":
        print("Player 1, its amazing... you won this round!\n")
        player1_score += 1

    elif player_1_choice == "scissors" and player_2_choice == "paper":
        print("This round is yours Player 1\n")
        player1_score += 1

    elif player_1_choice == player_2_choice:
        print("It's a tie!, need to play again!\n")
        continue

    else:  #minden más eset lefedi az ellenkező eseteket
        print("You are awesome Player 2, you won this time!\n")
        player2_score += 1

    nr_of_rounds -= 1
    nr_counter += 1

print(f"Player 1 score: {player1_score}\n")
print(f"Player 2 score: {player2_score}\n")
if player1_score > player2_score:
    print("Player 1 wins!")
elif player1_score < player2_score:
    print("Player 2 wins!")
else:
    print("It's a tie!")



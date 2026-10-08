

approvable = ("rock", "paper", "scissors")
beat = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

# roundok száma (elfogad amíg páratlan az input)
while True:
    planned_rounds = input("\nHow many rounds do you want to play? ").strip()
    if not planned_rounds.isdecimal():
        print("\nInvalid answer: Only numbers are allowed!")
        continue
    rounds = int(planned_rounds)
    if rounds % 2 == 0:
        print("\nInvalid answer: Give an odd number instead!")
        continue
    break

score1 = 0
score2 = 0
round_counter = 1

# számláló (amíg el nem éri az inputot)
while round_counter <= rounds:
    print(f"\nRound {round_counter}")

    while True:
        player1_input = input("\nPlayer 1! Choose rock, paper, or scissors: ").strip().lower()
        if player1_input in approvable:
            break
        print("\nInvalid answer: Make sure you choose rock, paper, or scissors.")

    while True:
        player2_input = input("\nPlayer 2! Choose rock, paper, or scissors: ").strip().lower()
        if player2_input in approvable:
            break
        print("\nInvalid answer: Make sure you choose rock, paper, or scissors.")

    # a döntetlen nem jó (round se no)
    if player1_input == player2_input:
        print("\nDraw! No score awarded. Choose again!")
        continue  

    if (player1_input == "rock" and player2_input == "scissors") or (player1_input == "scissors" and player2_input == "paper") or (player1_input == "paper" and player2_input == "rock"):
        score1 += 1
        print(f"\nThe {player1_input} beated {player2_input}: Player 1 won Round {round_counter}!")
    else:
        score2 += 1
        print(f"\nThe {player2_input} beated {player1_input}: Player 2 won Round {round_counter}!")

    round_counter += 1

# final score
if score1 > score2:
    diff = score1 - score2
    print(f"\nFinal result: {score1}-{score2}. Winner is Player 1 with {diff} point(s)!")
else:
    diff = score2 - score1
    print(f"\nFinal result: {score2}-{score1}. Winner is Player 2 with {diff} point(s)!")


response = input("\nWanna play again? (y/n): ").strip().lower()

if response == "y":
    print("\nRestart the game!\n")
else:
    print("\nAllright chickens! See you next time!\n")
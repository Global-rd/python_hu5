signs = ["rock", "paper", "scissors"]
gamer_1_wins = 0
gamer_2_wins = 0
played_rounds = 0

rounds=int(input("How many rounds do you want to play?: "))

while rounds % 2 == 0:
        print("Please provide the number of rounds again: ")
        rounds=int(input("How many rounds do you want to play?: "))
print("Let the game begin.") 

while played_rounds < rounds:
    gamer_1_step = input("Gamer 1: Choose: rock, paper, or scissors?: ")
    while gamer_1_step not in signs:
        print("Gamer 1:One more,Choose: rock, paper, or scissors?: ")
        gamer_1_step = input("Choose: rock, paper, or scissors?: ")
    gamer_2_step = input("Gamer 2:Choose: rock, paper, or scissors?: ")
    while gamer_2_step not in signs:
        print("Gamer 2 One more,Choose: rock, paper, or scissors?: ")
        gamer_2_step = input("Choose: rock, paper, or scissors?: ")
    if gamer_1_step == gamer_2_step:
        print("This is equal now.")
    elif (gamer_1_step == "rock" and gamer_2_step == "scissors") or (gamer_1_step == "paper" and gamer_2_step == "rock") or (gamer_1_step == "scissors" and gamer_2_step == "paper"):
        gamer_1_wins += 1
        played_rounds += 1
        print("Gamer 1 scores a point.")
    else: 
        gamer_2_wins += 1
        played_rounds += 1
        print("Gamer 2 scores a point.")

if gamer_1_wins > gamer_2_wins:
    print(f"The winner is Gamer 1, with {gamer_1_wins} points!")
elif gamer_2_wins > gamer_1_wins:
    print(f"The winner is Gamer 2 with {gamer_2_wins} points!")
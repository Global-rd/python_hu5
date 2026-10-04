szam = 6
print(szam % 2)

# körök száma
while True:
    rounds = int(input("Number of rounds:"))
    if ((rounds % 2) != 0):
        break
    print("Try again!")


#játékosok választása (kő/papír/olló)
valid_choices = ["rock", "paper", "scissors"]

player_1_choices = []
player_2_choices = []


current_round = 1 #kezdő/aktuális kör

while  current_round <= rounds:
    while True:
        while True:
            player_1_choice = input("Player 1 (rock/paper/scissors):")
            if player_1_choice in valid_choices:
                break
            print("Invalid choice, try again!")

        while True:
            player_2_choice = input("Player 2 (rock/paper/scissors):")
            if player_2_choice in valid_choices:
                break
            print("Invalid choice, try again!")

        if player_1_choice != player_2_choice:
            break
        print(f"Tie! Replay round {current_round}.")

    player_1_choices.append(player_1_choice)
    player_2_choices.append(player_2_choice)
    current_round += 1

print(player_1_choices)
print(player_2_choices)

# a player choice-okat 1 ciklusba kellene belelírni és kiértékelni, hogy nem-e döntretlen. ha igen, akkor újra kiírni, hogy döntetlen és nem léptetni a kört!
# csak ha már kiderült, hogy nem döntetlen utána kiírni a listába az eredményt. az eredményt meg elég kiértékelni később. külön if-ekkel!
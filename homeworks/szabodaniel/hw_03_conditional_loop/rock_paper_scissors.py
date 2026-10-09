# korok szama
while True:
    rounds = int(input("Number of rounds:"))
    if (rounds > 0 and (rounds % 2) != 0):
        break
    print("Try again!")


#jatekosok valasztasa (ko/papir/ollo)
valid_choices = ["rock", "paper", "scissors"]

player_1_choices = []
player_2_choices = []


current_round = 1                                                      #kezdo/aktuolis kor

while  current_round <= rounds:
    while True:
        while True:                                                     # 1 jaekost valaszt, ha nem potosat valaszt ujra fut
            player_1_choice = input("Player 1 (rock/paper/scissors):")
            if player_1_choice in valid_choices:
                break
            print("Invalid choice, try again!")

        while True:                                                    # 2 jaekost valaszt, ha nem potosat valaszt ujra fut
            player_2_choice = input("Player 2 (rock/paper/scissors):")
            if player_2_choice in valid_choices:
                break
            print("Invalid choice, try again!")

        if player_1_choice != player_2_choice:                          #ha nem dontetlen, kilep a ciklusbol     
            break
        print(f"Tie! Replay round {current_round}.")

    player_1_choices.append(player_1_choice)                            # valasztatsok (ko/papir/ollo) kiirasa listaba
    player_2_choices.append(player_2_choice)
    current_round += 1

print(player_1_choices)
print(player_2_choices)

win = []

for play1, play2 in zip(player_1_choices, player_2_choices):
    if play1 == "rock" and play2 == "scissors":
        win.append(1)
    elif play1 == "paper" and play2 == "rock":
        win.append(1)
    elif play1 == "scissors" and play2 == "paper":
        win.append(1)
    else:
        win.append(0)

print(win)

p1_points = win.count(1)
p2_points = win.count(0)

if win.count(1) >= (rounds // 2) + 1:
    print(f"Player_1 won by {p1_points}!")
else:
    print(f"Player_2 won by {p2_points}!")
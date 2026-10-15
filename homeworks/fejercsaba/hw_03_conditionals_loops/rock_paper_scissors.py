# kő-papír-olló játék

while True:
    round = input("Enter an odd number of rounds: ")
    round_num = int(round)
    if round_num > 0 and round_num % 2 == 1:
        break
    else: 
        print("The number must be odd, greater than 0.")

score_a = 0     # A játékos pontszáma
score_b = 0     # B játékos pontszáma
round = 1       # körszámláló
legal_choices = ["rock", "paper", "scissors"] #olló-papír-kő tömb


while True:
    print(f"{round}. round")
    while True:
        a_choice = input("Player A: ").strip().lower()
        if a_choice in legal_choices:
            break
        else:
            print("illegal choice try again.")

    while True:
        b_choice = input("Player B: ").strip().lower()
        if b_choice in legal_choices:
            break
        else:
            print("illegal choice try again.")



    if a_choice == b_choice:                                        # döntetlen
            print("Draw!")
            #continue
    elif    (   (a_choice == "rock" and b_choice == "scissors")     
            or (a_choice == "paper" and b_choice == "rock")
            or (a_choice == "scissors" and b_choice == "paper")   ):    # esetek amikor A nyer

        score_a +=1
        round +=1
        print("A wins this round!")
    else:   # esetek amikor B nyer   
        score_b +=1
        round +=1
        print("B wins this round!")
        
    if round > round_num:
        break


#eredmény kiíratás
print(f"Player A score: {score_a}")
print(f"Player B score: {score_b}")
print("Summary:")
dif = abs(score_a - score_b)
if score_a > score_b:
    print(f"A won by {dif} ponts.")
else:
    print(f"B won by {dif} ponts.")




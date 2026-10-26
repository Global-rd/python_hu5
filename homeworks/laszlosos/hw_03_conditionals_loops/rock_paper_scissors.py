player1_score = 0
player2_score = 0  #az elejere kell tenni a pontszamok kezdoerteket (cikluson kivulre) hogy ne nullazodjanak le minden korben
#korok szamanak bekerese, addig ismetli amig paratlan szamot nem adunk, mert csak akkor nem lehet dontetlen. 
while True:
    rounds = int(input("How many rounds?"))
    if rounds %2 == 1:
        break
    print("Not valid number of rounds")
'''for ciklus, annyiszor fut le amennyi kort fent megadtak
    azert van a jatek resz felett, mert csak az ismetlodik, ami alatta van'''
for round_number in range(1, rounds +1): 
    #elso loop, a kor addig ismetlodik amig valaki nem nyer, dontetlen eseten. ujra 
    while True:  
    #player1 valasz
        while True: 
            player1_move = input("Player1, choose rock, paper or scissors: ")
            if player1_move in ["rock", "paper", "scissors"]:
                break
            print("Not valid answer")
        #player2 valasz
        while True: 
            player2_move = input("Player2, choose rock, paper or scissors: ")
            if player2_move in ["rock", "paper", "scissors"]:
                break
            print("Not valid answer")
        #kiertekeles: dontetlern, player1 nyer, minden mas esetben p;layer2 
        if player1_move == player2_move:
            print("Draw!")
        elif (player1_move == "rock" and player2_move == "scissors" or player1_move == "paper" and player2_move == "rock" or player1_move == "scissors" and player2_move == "paper"):
            print("Player1 won this round!")
            player1_score +=1
            break
        else:
            print("Player2 won this round!")
            player2_score +=1
            break
if player1_score > player2_score:
    print(f"Player1 won the match with {player1_score} points!")
else:
    print(f"Player2 won the match with {player2_score} points!")

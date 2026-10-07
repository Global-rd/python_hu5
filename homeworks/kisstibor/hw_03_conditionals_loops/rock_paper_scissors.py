""" 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
HW 03 - Feladat 2. (if-elif-else, operátorok)
by Kiss Tibor
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
while True:
    game_rounds_string = input("Add meg a játszmák számát (páratlan pozitív egész számot adj meg): ")
    input_in_digits = game_rounds_string.strip() 
    print(input_in_digits)

    if not (input_in_digits.isdigit()):
        print("Érvénytelen a beírt szám! Próbáld meg újra!")   
    else:
        game_rounds = int(game_rounds_string)       
        if not (game_rounds % 2 == 0):             
            break  
        else:
            print("Kérlek páratlan számot adj meg!")


VALID_BETS = {"rock", "paper", "scissors"}

WIN_STATES = {
    ("rock", "scissors"),
    ("scissors", "paper"),
    ("paper", "rock")
}

players = ["Player 1", "Player 2"]
scores = [0, 0]
round = 1

while round <= game_rounds:
    print(f"")
    print(f"--------------------- ROUND [{round} / {game_rounds}] -----------------------")
    round_bets = []

    for player_id, player in enumerate(players,1):
        while True:
            player_bet = input(f"{player}, add meg a téted (rock, paper, scissors): ").strip().lower()
            if player_bet in VALID_BETS:
                break
            print("Érvénytelen tét! Próbáld újra!")
        if player_id == 1:
            player_1_bet = player_bet
        else:
            player_2_bet = player_bet

    if player_1_bet == player_2_bet:
        print(f"")
        print(f"      [Döntetlen! a Kört újra kell játszani]")
        continue

    if (player_1_bet, player_2_bet) in WIN_STATES:
        print(f"")
        print(f"         [{players[0]} nyert!]")
        scores[0] += 1
    else:
        print(f"")
        print(f"         [{players[1]} nyert!]")
        scores[1] += 1
        
    print(f"")
    print(f"Eddigi pontszámok: {players[0]}: {scores[0]}, {players[1]}: {scores[1]}")
    round += 1
    
print("Játék vége!")
if scores[0] > scores[1]:
    print(f"{players[0]} nyert a játékban!")
elif scores[1] > scores[0]:
    print(f"{players[1]} nyert a játékban!")    
else:
    print("A játék döntetlennel zárult!")   # amennyiben megengedjük a játszmák döntetlen kimenetelét

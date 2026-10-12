import time

print("Hello, welcome to rock, paper, scissors") # game greeting

play_rounds = int(input("How many rounds would you like to play?(please add an odd number: ")) # number of rounds input

while play_rounds <= 0 or play_rounds % 2 == 0: # check the entered number is odd to prevent draw
    print("please am odd number!! example: 1 or 3 etc.") #feedback

    play_rounds = int(input("Add a good number again: ")) #round input again

gamer1 = input("Player one name: ").strip().title() #name of the first player
gamer2 = input("Player two name: ").strip().title() #name of the second player

gamer1_points = 0 
gamer2_points = 0

choice_text = (" please choice from Rock, Paper, Scissors!: ") 
choices = ["Rock" , "Paper" , "Scissors"]
round_text = ("Round")
win_rnd_text = (" win the round!")
winning = {"Rock" : "Scissors",
           "Scissors" : "Paper",
           "Paper" : "Rock"
}
print(type(choices)) #chk for me
print("Start the game")# chek for me
start = time.time() # for gameplay time
for round_nr in range(1, play_rounds + 1): #Start the round
    print(f"{round_text} {round_nr}")

    while True:

        player_1 = input(f"{gamer1}{choice_text}").strip().title() #player 1 choice
        while player_1 not in choices:
            print(choice_text)
            player_1 = input(f"{choice_text}").strip().title()

        player_2 = input(f"{gamer2}{choice_text}").strip().title() #player 2 choice
        while player_2 not in choices:
            print(choice_text)
            player_2 = input(f"{choice_text}").strip().title()

        if player_1 == player_2:
            print("Draw, play again!")

        elif winning[player_1] == player_2:
            print(f"{gamer1}{win_rnd_text}")
            gamer1_points += 1
            break
        else:
            print(f"{gamer2}{win_rnd_text}")
            gamer2_points += 1
            break
end = time.time()
playtime = end - start
winner = gamer1 if gamer1_points > gamer2_points else gamer2
print(f"The Winner is {winner}!")
print(f"Final scores: {gamer1}: {gamer1_points} points and {gamer2}: {gamer2_points} points. Total playtime: {playtime} mp.")






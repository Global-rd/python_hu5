#----------------------#
# HomeWork lessons 6/2 #
#----------------------#

#import pprint

# get rounds number

round_counts = 0
while not(round_counts % 2):
    round_counts = int(input("Round numbers (Enter odd number!): "))
    if not(round_counts % 2):
        print("Error! Please enter an odd number.")
    
#---------------

# get tips every round

score = {"pl1": 0,
         "pl2": 0
                }
for round_number in range(round_counts):

    while True:

        #get players tips
        tips = []
        for player in range(2):
            tip = ""
            while tip not in ("rock", "paper", "scissors"):
                tip = input(f"Your tip player{player+1} (rock / paper / scissors): ")
            tips.append(tip)

        if tips[0] != tips[1]:
            break
        print("Both tips are identical. Please try again!")

    pl1tip = tips[0]
    pl2tip = tips[1]
    
    #----------------

    # play
 
    if (
         (pl1tip == "paper" and pl2tip == "rock")
         or
         (pl1tip == "rock" and pl2tip == "scissors")
         or
         (pl1tip == "scissors" and pl2tip == "paper")
    ):
         score["pl1"] += 1
         print("The round winner is Player1")
    else:
         score["pl2"] += 1
         print("The round winner is Player2")

#-------------

if score["pl1"] > score["pl2"]:
     winner = 1
 #    print(f"The game winner is Player1. Player1 score is {round_winner['pl1score']}, Player2 score is {round_winner['pl1score']}")
if score["pl1"] < score["pl2"]:
     winner = 2

print(f"The game winner is Player{winner}. Player1 score is {score['pl1']}, Player2 score is {score['pl2']}")

print("##########")
print ("# Finish #")    
print("##########")
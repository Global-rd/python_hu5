#kő-papír-olló két játékos között
#a kő erősebb mint az olló, de gyengébb mint a papír
#a papír erősebb mint a kő, de gyengébb mint az olló
#az olló erősebb mint a kő, de gyengébb mint a papír
#kérjük be a körök számát - csak páratlan lehet! különben hibaüzenet és kérjük be újra a körök számát, 
#amíg jó nem lesz - ezzel le is kezeljük azt a feltételt, hogy valakinek nyernie kell.
#A program felváltva kérje be az első és a második játékos válaszát, csak ezek lehetnek: 
# "rock", "paper", "scissors" egyébként kérjen be új választ.
#tárolni kell a pontszámokat és növelni az aktuális játékos pontszámát.
#a végén ki kell írni ki mennyivel nyert

round_number = 0
answer_a_player = ""
answer_b_player= ""
answers = ["rock", "scissors", "paper"]
winner_situations = {
    "paper": "rock",
    "rock": "scissors",
    "scissors": "paper"
}
aplayer_score = 0
bplayer_score = 0


#Kérjük be a körök számát, ami pozitív, páratlan egész szám lehet

while True:
    round_number = int(input("How many rounds would you like to play? "))
    if round_number < 0:
        print("Please enter a positive number!")
    elif round_number % 2 == 0:
        print(f"The number {round_number} is even, please enter an odd number")
    else:
        break

#Annyi körnek kell lefutni, amennyit a választban megadott a játékos
for rn in range(round_number):
    print(f"Round {rn + 1} of {round_number}")

    while True:
#Bekérjük a játékosok válaszait, addig míg egymástól különböző és helyes válaszokat nem adnak
        #A játékos válaszai
            while True:
                answer_a_player = input("First player: please choose an item: rock, paper or scissors: ")
                if answer_a_player in answers:
                    break
                else:
                    print("Invalid answer, please try again: ")
                    continue

        #B játékos válaszai
            while True:
                answer_b_player = input("Second player: please choose an item: rock, paper or scissors: ")
                if answer_b_player in answers:
                    break
                else:
                    print("Invalid answer, please try again: ")
            
        #Egyforma válasz esetén
            if answer_a_player == answer_b_player:
                print("The two answers is equal, please try again ")
                continue
        
        # tárolni kell a pontszámokat és növelni annak a játékosnak a pontszámát, aki nyerte az aktuális kört
            if winner_situations[answer_a_player] == answer_b_player:
                aplayer_score += 1
            else:
                bplayer_score += 1

        #Különböző válasz esetén    
            break
    
#kiírni, hogy ki nyert és hány ponttal
print(f"The winner is Player {'A' if aplayer_score > bplayer_score else 'B'} " 
      f"by {abs(aplayer_score- bplayer_score)} points")


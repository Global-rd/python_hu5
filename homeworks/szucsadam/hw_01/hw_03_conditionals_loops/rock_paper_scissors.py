# Rock - Paper - Scissors game

# Bekérjük, hogy hány kört szeretnének játszani
rounds = int(input("How many rounds do you want to play? "))

# Ellenőrizzük, hogy a körök száma páratlan legyen
while rounds % 2 == 0:
    print("Error! The number of rounds must be odd.")
    rounds = int(input("Please enter the number of rounds again: "))


# A két játékos pontszáma kezdetben 0
player_1_score = 0
player_2_score = 0

# Ezek az elfogadott válaszok
valid_choices = ["rock", "paper", "scissors"]


# A for ciklus vezényli le a köröket
for round_number in range(1, rounds + 1):

    print(f"Round {round_number}")

    # Ez a változó jelzi, hogy véget ért-e az aktuális kör
    round_finished = False

    # Egy kör addig tart, amíg nincs győztes
    while round_finished == False:

        # Első játékos választása
        player_1 = input("Player 1 - rock, paper or scissors? ")

        # Ha hibás választ ad meg, újra bekérjük
        while player_1 not in valid_choices:
            print("Invalid choice!")
            player_1 = input("Player 1 - please choose rock, paper or scissors: ")


        # Második játékos választása
        player_2 = input("Player 2 - rock, paper or scissors? ")

        # Itt is addig kérjük újra, amíg jó választ nem kapunk
        while player_2 not in valid_choices:
            print("Invalid choice!")
            player_2 = input("Player 2 - please choose rock, paper or scissors: ")


        # Ha ugyanazt választják, döntetlen van
        if player_1 == player_2:
            print("Draw!")
            print("You have to play this round again.")

        else:

            # Ellenőrizzük külön-külön, hogy Player 1 nyert-e
            if player_1 == "rock":
                if player_2 == "scissors":
                    player_1_score += 1
                    print("Player 1 wins this round!")
                else:
                    player_2_score += 1
                    print("Player 2 wins this round!")

                # Mivel nem volt döntetlen, vége a körnek
                round_finished = True


            elif player_1 == "paper":

                if player_2 == "rock":
                    player_1_score += 1
                    print("Player 1 wins this round!")

                elif player_2 == "scissors":
                    player_2_score += 1
                    print("Player 2 wins this round!")

                # Itt is véget ér a kör
                round_finished = True


            elif player_1 == "scissors":

                if player_2 == "paper":
                    player_1_score += 1
                    print("Player 1 wins this round!")

                elif player_2 == "rock":
                    player_2_score += 1
                    print("Player 2 wins this round!")

                # Nem döntetlen, ezért kilépünk az aktuális körből
                round_finished = True


    # Minden kör végén kiírjuk az aktuális pontokat
    print(f"Player 1 score: {player_1_score}")
    print(f"Player 2 score: {player_2_score}")


# A játék végén megvizsgáljuk, melyik játékosnak van több pontja

print("Game finished!")

if player_1_score > player_2_score:
    print(f"Player 1 won with {player_1_score} points!")

elif player_2_score > player_1_score:
    print(f"Player 2 won with {player_2_score} points!")

else:
    # Elvileg páratlan körszám mellett ide nem kellene eljutnia
    print("The game ended in a draw!")
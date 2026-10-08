CHOICES = ["rock", "paper", "scissors"]
total_rounds = 0
while True:
    total_rounds = int(input("How many would you like to play? ").strip())
    if total_rounds > 0 and total_rounds % 2 != 0:
        break
    else:
        print("Invalid number! Please enter an odd number! ")

print("Game starts!")

player1_score = 0
player2_score = 0
for current_round in range(1, total_rounds + 1):
    print(f"Round {current_round}")

    while True:
        p1 = input("Player 1 (rock, paper, scissors): ").strip().lower()
        p2 = input("Player 2 (rock, paper, scissors): ").strip().lower()

        if p1 not in CHOICES or p2 not in CHOICES:
            print("Invalid choice! Must choose rock, paper, or scissors.")
            continue
        if p1==p2:
            print("Draw! Please repaet it!")
        elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
            print("Player 1 won this round!")
            player1_score += 1
            break
        else:
            print("Player 2 won this round!")
            player2_score += 1
            break

print(f"Result score Player 1: {player1_score}, Result score Player 2: {player2_score}")

if player1_score > player2_score:
    print(f"Player 1 won the game with {player1_score} points!")
else:
    print(f"Player 2 won the game with {player2_score} points!")
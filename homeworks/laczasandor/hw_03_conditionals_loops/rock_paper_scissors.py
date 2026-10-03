VALID_CHOICES = ("rock", "paper", "scissors")
# key beats value: e.g. "rock" beats "scissors"
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
 
players = ["Player 1", "Player 2"]
scores = {"Player 1": 0, "Player 2": 0}
 
# Ask for the number of rounds until a positive odd number is given
while True:
    rounds_input = input("How many rounds do you want to play? ").strip()
    if rounds_input.isdigit() and int(rounds_input) % 2 == 1:
        rounds = int(rounds_input)
        break
    print("Invalid number! Please enter a positive ODD number, so there can be no draw.")
 
for round_number in range(1, rounds + 1):
    print(f"\n--- Round {round_number} of {rounds} ---")
 
    # The round is repeated until somebody wins
    while True:
        choices = []
        for player in players:
            # Walrus operator: read the input and check it in one step
            while (choice := input(f"{player}, choose rock, paper or scissors: ").strip().lower()) not in VALID_CHOICES:
                print("Invalid choice! Only 'rock', 'paper' or 'scissors' is accepted.")
            choices.append(choice)
 
        first_choice, second_choice = choices  # unpacking
 
        if first_choice == second_choice:
            print(f"It's a tie ({first_choice} vs {second_choice})! Play this round again.")
            continue
 
        winner = players[0] if BEATS[first_choice] == second_choice else players[1]
        scores[winner] += 1
        print(f"{winner} wins this round ({first_choice} vs {second_choice})!")
        print(f"Score: {players[0]} {scores[players[0]]} - {scores[players[1]]} {players[1]}")
        break
 
overall_winner = players[0] if scores[players[0]] > scores[players[1]] else players[1]
print(f"\nThe winner is {overall_winner} with {scores[overall_winner]} points!")
 
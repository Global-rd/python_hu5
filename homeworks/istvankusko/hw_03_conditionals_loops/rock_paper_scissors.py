

print(f"Welcome to the Rock-Paper-Scissors game\n")

# Requesting the number of circles (until an odd number is entered)
periods = 0
while True:
  try:
    periods_number = input("Enter the number of circles (it must be an odd number): ")
    periods = int(periods_number)
    if periods % 2 != 0 and periods > 0:
      break
    else:
      print("Error: Please enter a positive odd number!")
  except ValueError:
    print("Error: Please enter a valid integer!")

# For loop 
choice_option  = ["rock", "paper", "scissors"]
print("\nThe valid options are:")
for option in choice_option:
  print(f"- {option}")

score_1 = 0
score_2 = 0
rounds_played = 0

# while loop
while rounds_played < periods:
  print(f"\n--- {rounds_played + 1}. valid circle ---")

  # First player's response
  games_1 = ""
  while True:
    games_1 = (
        input("First player's response (rock/paper/scissors): ").strip().lower()
    )
    if games_1 in choice_option:
      break
    print("Error: Invalid selection! Only 'rock', 'paper' or 'scissors'.")

  # Second player's response
  games_2 = ""
  while True:
    games_2 = (
        input("Second player's response (rock/paper/scissors): ").strip().lower()
    )
    if games_2 in choice_option:
      break
    print("Error: Invalid selection! Only 'rock', 'paper' or 'scissors'.")

  # Check for a tie (if it's a tie, the round restarts without counting)
  if games_1 == games_2:
    print("It's a tie! We'll have to replay this round.")
    continue

  # the winner
  if (
      (games_1 == "rock" and games_2 == "scissors")
      or (games_1 == "paper" and games_2 == "rock")
      or (games_1 == "scissors" and games_2 == "paper")
  ):
    score_1 += 1
    print("Player 1 won this round!")
  else:
    score_2 += 1
    print("Player 2 won this round!")

  rounds_played += 1

# Display Final Results
print("\n" + "=" * 30)
print("FINAL RESULTS:")
print(f"1. Player Points: {score_1}")
print(f"2. Player Points: {score_2}")

if score_1 > score_2:
  print("The winner of the game is Player 1!")
elif score_2 > score_1:
  print("The winner of the game is Player 2!")
else:
  print("The game ended in a tie.")
print("=" * 30)
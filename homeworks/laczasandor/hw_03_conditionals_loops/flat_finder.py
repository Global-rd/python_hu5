# Constants based on Sarah's preferences
LOVED_CITIES = {"new york", "san francisco"}
LOVED_CITY_MAX_RENT = 4000  # rent must be LESS than this
HATED_CITY = "washington"
DREAM_CITY = "chicago"
OTHER_CITY_MAX_RENT = 3000  # rent must be this or LESS
 
city = input("Enter the city: ").strip().lower()
 
# Ask for the rent until a valid whole number is given
rent_input = input("Enter the monthly rent in USD: ").strip()
while not rent_input.isdigit():
    print("Invalid rent! Please enter a whole number (e.g. 3500).")
    rent_input = input("Enter the monthly rent in USD: ").strip()
rent = int(rent_input)
 
if city == DREAM_CITY:
    can_move = True
elif city == HATED_CITY:
    can_move = False
elif city in LOVED_CITIES:
    can_move = rent < LOVED_CITY_MAX_RENT
else:
    can_move = rent <= OTHER_CITY_MAX_RENT
 
# Ternary operator: pick the right word for the answer
answer = "would move" if can_move else "would NOT move"
print(f"Sarah {answer} to {city.title()} for {rent} USD per month.")
 
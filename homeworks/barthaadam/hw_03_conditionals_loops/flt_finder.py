#Sarah's conditions for moving to a new city

city = input("Enter the city: ").strip().lower()
rent = int(input("Enter the monthly rent in USD: "))

# Determine if Sarah can move to the city based on her conditions

if city == "washington":
    can_move = False

elif city == "chicago":
    can_move = True

elif city == "new york" or city == "san francisco":
    can_move = rent < 4000

else:
    can_move = rent <= 3000


if can_move:
    print(f"Sarah would move to {city.title()}.")
else:
    print(f"Sarah would not move to {city.title()}.")
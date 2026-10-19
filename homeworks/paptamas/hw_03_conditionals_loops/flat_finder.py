city = input("Enter the city: ").strip().title()
rent = int(input("Enter the monthly rent in USD: "))

if city in ["New York", "San Francisco"]:
    can_move = rent < 4000
elif city == "Washington":
    can_move = False
elif city == "Chicago":
    can_move = True
else:
    can_move = rent <= 3000

print(f"Given the city ({city}) and the rent ({rent} USD), Sarah can move there: {can_move}.")

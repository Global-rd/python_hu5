city = input("Which city is the apartment in? ")
rent = int(input("How much is the monthly rent? "))

if city == "Washington":
    can_move = False

elif city == "Chicago":
    can_move = True

elif (city == "New York" or city == "San Fransisco") and rent < 4000:
    can_move = True

elif city != "New York" and city != "San Fransisco" and rent <= 3000:
    can_move = True

else:
    can_move = False

print(f"Sarah can move to {city}: {can_move}")
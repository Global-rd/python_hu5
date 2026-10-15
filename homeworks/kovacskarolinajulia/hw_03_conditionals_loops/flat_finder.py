city = input("Add meg a várost: ")
rent = int(input("Add meg a havi lakbért USD-ben: "))

if city == "Washington":
    can_move = False
elif city == "Chicago":
    can_move = True
elif city == "New York" or city == "San Francisco":
    can_move = rent < 4000
else:
    can_move = rent <= 3000

print(fSarah be tud költözni: {can_move}")
city = input("Enter the city: ").strip().lower()
rent = int(input("Enter the monthly rent in USD: "))
if city == "new york" or city == "san francisco":
    can_move = rent < 4000
elif city == "washington":
    can_move = False
elif city == "chicago":
    can_move = True
else:
    can_move = rent <= 3000
print(
    f"Sarah can move to {city.title()} with a monthly rent of "
    f"{rent} USD: {can_move}"
)

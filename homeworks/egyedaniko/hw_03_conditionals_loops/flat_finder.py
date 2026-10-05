# Bekérem a várost és a bérleti díjat.
city = input("Enter city: ").strip().title()
rent = int(input("Enter monthly rent (USD): "))

# Meghatározom, hogy Sarah költözhet-e.
if city == "Washington":
    can_move = False

elif city == "Chicago":
    can_move = True

elif city in ["New York", "San Francisco"]:
    can_move = rent < 4000

else:
    can_move = rent <= 3000

# Kiíratom az eredményt.
print(
    f"Sarah can move to {city}: {can_move}. Monthly rent: {rent} USD."
)
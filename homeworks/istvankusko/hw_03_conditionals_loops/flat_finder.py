#flat_finder

city = input("Enter the city: ").strip().lower()
rent_cost = int(input("Enter the rent amount (in USD): "))

# Condition check.
if city in ["new york", "san francisco"]:
    move_in = rent_cost < 4000
elif city == "washington":
    move_in = False
elif city == "chicago":
    move_in = True
else:
    move_in <= 3000

# Ternary 
# ez így jó??
ability = "can" if move_in else "can't"

# 
print(f"If the apartment is located in {city.title()} and costs ${rent_cost} a month, Sarah {ability} move in.")


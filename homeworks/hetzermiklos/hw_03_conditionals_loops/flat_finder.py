
city = input("Enter the city: ")
rent = int(input("Enter the monthly rent in USD: "))

print(f"City: {city}, Monthly rent: {rent} USD")

if city == "Washington":
    decision = "would not move"

elif city == "Chicago":
    decision = "would move"

elif city == "New York" or city == "San Francisco":
    if rent < 4000:
        decision = "would move"
    else:
        decision = "would not move"

else:
    if rent <= 3000:
        decision = "would move"
    else:
        decision = "would not move"

print(f"Sarah {decision} to {city} for {rent} USD per month.")

cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Francisco",
    "Austin",
    "Jacksonville",
    "Fort Worth",
    "Columbus",
    "Charlotte",
    "Washington"
]

city = input("Please enter the name of the City: ")
monthly_rent = input("Please enter the Rental Cost: ")

if city.lower() in [c.lower() for c in cities]:  # hogy ne számítson a kis- ill. nagybetű
    if city == "New York" or city == "San Francisco" or city == "Chicago":
        if int(monthly_rent) < 4000:
            print(f"{city} is a great choice for you!")

    elif city == "Washington":
        print(f"{city} is not a good choice for you.")

    else:
        if int(monthly_rent) < 3000:
            print(f"{city} is a great choice for you!")



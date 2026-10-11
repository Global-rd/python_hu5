cities = [
    "New York",
    "Chicago",
    "San Francisco",
    "Washington"
]

city = input("Please enter the name of the City: ")
monthly_rent = input("Please enter the Rental Cost: ")

if city.lower() in [c.lower() for c in cities]:  # hogy ne számítson a kis- ill. nagybetű
    if city == "New York" or city == "San Francisco":
        if int(monthly_rent) < 4000:
            print(f"{city} is a great choice for you!")

    elif city == "Chicago":
        print(f"{city} is an amazing choice for you.")

    elif city == "Washington":
        print(f"{city} is not a good choice for you.")

else:
    if int(monthly_rent) <= 3000:
        print(f"{city} is also a great choice for you!")



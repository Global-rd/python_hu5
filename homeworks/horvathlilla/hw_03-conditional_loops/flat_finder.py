city=input("Enter the city name: ").strip().lower()
rent=float(input ("Enter monthly rent: "))

if city in("new york", "san francisco") and rent<=4000:
    print(f"Sarah can afford to rent in {city} with a monthly rent of ${rent}.")

elif city=="washington":
    print(f"Sarah will not rent in {city}.")

elif city=="chicago":
    print(f"Sarah is happy to rent in {city} with a monthly rent of ${rent}.")

elif city not in("new york", "san francisco", "washington", "chicago") and rent<=3000:
    print (f"Sarah can afford to rent in {city} with a monthly rent of ${rent}.")
else:
     print(f"Sarah cannot afford to rent in {city} with a monthly rent of ${rent}.")


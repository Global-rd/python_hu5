town=input("Add a city: ")
price=int(input("Rent price: "))

if town in ("New York", "San Francisco") and price < 4000:
    print(f"Sarah, you can move into {town} at this price: {price}.")
elif town == "Washington":
    print(f"Sarah hate {town}!")
elif town == "Chicago":
    print(f"Sarah love {town}! Rent price is: {price}")
elif price <= 3000 :
    print(f"Sarah, you can move into {town} at this price: {price}.")
else: 
    print(f"This apartment in {town} is expensive for Sarah, because the rent price is {price}. ")
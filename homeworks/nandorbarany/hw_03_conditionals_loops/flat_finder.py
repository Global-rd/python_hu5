
location = (input("Enter the location: ")).title().strip()

if location == "Washington":
    print(f"Flats located in {location} are NOT approvable for Sarah at all.")
else:
    price = int(input("Enter the price in USD: "))

    result = False

    if price < 4000 and location in ["New York", "San Francisco"]:
        result = True
    elif location == "Chicago":
        result = True
    elif price <= 3000:
        result = True

    if result:
        print(f"The flat in {location} is approvable for Sarah for ${price}.")
    else:
        print(f"The flat in {location} is NOT approvable for Sarah for ${price}.")


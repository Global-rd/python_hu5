
for i in range(10):
    max_price = 4000
    answer = input("Enter the city: ").strip().title()

    if answer in ("New York", "San Francisco"):
        flat_price = float(input("Enter the price: "))

        possibility = "can" if flat_price <= max_price else "can not"

    elif answer == "Washington":
        flat_price = float(input("Enter the price: "))
        possibility = "can not"

    elif answer == "Chicago":
        possibility = "can"
        flat_price = 0

    else:
        flat_price = float(input("Enter the flat price: "))

        possibility = "can" if flat_price <= 3000 else "can not"

    print(f"With the given attributes you {possibility} move in {answer} for {flat_price} $.")


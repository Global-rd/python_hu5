preferred_city = input("Which city do you want to rent in?")
rent_budget = int(input("How much do you want to spend on rent?"))


if preferred_city in ("New York", "San Francisco") and rent_budget <=4000:
        print(f"You can afford New York or San Francisco on {rent_budget}!")
elif preferred_city == "Washington":
    print(f"I don't want to live in {preferred_city}!")
elif preferred_city == "Chicago":
    print(f"I love {preferred_city}, there's no rent limit!")
elif rent_budget <= 3000:
    print(f"Let's move to {preferred_city} for {rent_budget}")
else:
    print("Change city or rent budget, or stay home!")
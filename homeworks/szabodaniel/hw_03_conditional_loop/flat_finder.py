preferred_city = input("Which city do you want to rent in?")
rent_budget = int(input("How much do you want to spend on rent?"))


if (preferred_city == "New York") or (preferred_city == "Sun Fransisco"):
    if rent_budget <= 4000:
        print(f"You can afford New York or San Francisco on {rent_budget}!")
elif (preferred_city == "Washington"):
    print(f"I don't want to live in {preferred_city}!")
elif (preferred_city == "Chicago"):
    print(f"I love {preferred_city}, there's no rent limit!")
elif (rent_budget <= 3000) and (preferred_city != "Washington"): #mondjuk a Washington törölhető, mert nem jut el idáig a program
    print(f"Let's move to {preferred_city} for {rent_budget}")
else:
    print("Change city or rent budget, or stay home!")
#data_input
#washington
#chicago
#new york
#san francisco

city = input("Enter the city: ").strip().lower()


if city == "washington":
    print(f"Sarah can not move into the apartment in {city.title()}.")
elif city == "chicago":
    print(f"Sarah loves {city.title()}, she can move into {city.title()}.")
else:
    rent = int(input("Enter the monthly rent (USD): ").strip())

    if city in["new york", "san francisco"] and rent < 4000:
        can_move_in = True
    elif rent <= 3000:
        can_move_in = True
    else:
        can_move_in = False

    decision = "can move into" if can_move_in else "can not move into"
    print(f"Sarah {decision} the apartment in {city.title()} for {rent} USD per month.")
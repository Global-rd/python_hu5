city = input("Which city is the flat in? ").strip().lower()
rent = float(input("How much is the monthly rent? "))
if city == "chicago":
    suitable = True
elif city == "washington":
    suitable = False
elif city in ("new york", "san francisco"):
    suitable = rent < 4000
else:
    suitable = rent <= 3000
decision = "suitable" if suitable else "not suitable"

print(
    f"The flat in {city.title()} with a monthly rent of ${rent:.2f} "
    f"is {decision} for Sarah."
)

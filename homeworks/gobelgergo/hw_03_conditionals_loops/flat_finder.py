city = input("Írd be hogy melyik városban van a lakás:").lower().strip()
rent = float(input("Írd be a lakás havi lakbérét:"))

move_in = True

if city == "chicago":
    move_in = True

elif city == "washington":
    move_in = False

elif city in ["new york", "san fransisco"]:
    move_in = rent < 4000

else:
    move_in = rent <= 3000


if move_in:
    print(f"Sarah be tudna költözni a {city}-i lakásba {rent:.2f} USD havi lakbérért.")
else:
    print(f"Sarah nem tudna beköltözni a {city}-i lakásba {rent:.2f} USD havi lakbérért.")
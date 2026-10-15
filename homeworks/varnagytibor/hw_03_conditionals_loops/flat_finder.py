#bekérjük a várost, levágjuk a szóközöket és kisbetűsítjük, hogy a "New York" és a "new york " is ugyanaz legyen
city = input("City: ").strip().lower()
#bekérjük a havi lakbért USD-ben, és számmá alakítjuk, hogy össze tudjuk hasonlítani
rent = float(input("Monthly rent (USD): "))

#a feltételeket a hétköznapi leírás sorrendjében fordítjuk le Pythonra
if city == "new york" or city == "san francisco":
    #New York és San Francisco: csak ha a lakbér KEVESEBB, mint 4000
    can_move = rent < 4000
elif city == "washington":
    #Washington: semmi pénzért
    can_move = False
elif city == "chicago":
    #Chicago: a pénz nem akadály
    can_move = True
else:
    #bármilyen más város: 3000 vagy az ALATT
    can_move = rent <= 3000

#az eredményt egy f-stringgel írjuk ki (a ternary operatorral választjuk ki a szöveget)
answer = "would" if can_move else "would not"
print(f"Sarah {answer} move to {city.title()} for {rent:.0f} USD per month.")

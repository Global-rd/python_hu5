# Város és ár bekérése a felhasználótól
city = input("Add meg a várost: ").strip().lower()
price = int(input("Add meg a havi lakbér árát (USD): "))

# Logikai feltételek ellenőrzése Sarah elvárásai alapján
if city == "chicago":
    can_move_in = True  # Chicago esetén a pénz nem akadály
elif city == "washington":
    can_move_in = False  # Washingtonba semmi pénzért nem költözik
elif city in ["new york", "san fransisco"]:
    can_move_in = price < 4000  # NY és SF esetén az ár < 4000 USD
else:
    can_move_in = price <= 3000  # Bármilyen más helyen az ár <= 3000 USD

# Eredmény kiíratása f-string segítségével
status_text = "be tudna költözni" if can_move_in else "NEM tudna beköltözni"
print(f"Sarah {status_text} a megadott helyre ({city.title()}, {price} USD).")

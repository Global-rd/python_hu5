
# --- Sarah lakáskeresése ---
 
# --- város és lakbér bekérése ---
city = input("Melyik városban van a lakás? ")
rent = int(input("Mennyi a havi lakbér (USD)? "))
 
# --- Washingtonba nem költözne, ez alapján ---
if city == "Washington":
    can_move = False
 
# --- Chicagoba lakbértől függetlenül költözne ---
elif city == "Chicago":
    can_move = True
 
# --- New York és San Fransisco esetében feltétel, hogy az albérlet ára kisebb legyen, mint 4000 dollár ---

elif city == "New York" or city == "San Francisco":
    can_move = rent < 4000
 
# --- egyéb városokba, 3000 USD vagy ez alatti havi lakbér esetén költözne ---
# --- 3000 USD még benne van ezért <= (a 3000 még jó)
else:
    can_move = rent <= 3000
 
# --- kiírni az eredményt ---
if can_move:
    print(f"Sarah beköltözne ide: {city}, {rent} USD/hó.")
else:
    print(f"Sarah nem költözne ide: {city}, {rent} USD/hó.")
 


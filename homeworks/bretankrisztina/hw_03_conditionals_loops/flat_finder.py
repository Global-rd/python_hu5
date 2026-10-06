#Infók: 
# Sarahnak segíteni kell a lakáskeresésben
# New York, San Fransisco- szereti, de max. 4000 USD, 
# Washington- nem akar ide menni, 
# Chicago- nincs anyagi korlát
# ha a havi bér 3000 USD-nél kisebb- bárhova

#házi feladat kidolgozva

condition = False

city = input("Which city would you like to move to? ").strip()
rental_fee = float(input("How much is the monthly rent? "))

# Washington- nem akar ide menni, 
if city == "WASHINGTON" or city == "WA":
    condition = False

# Chicago- nincs anyagi korlát    
elif city == "CHICAGO" or city == "CHI":
    condition = True

# New York, San Fransisco- szereti, de max. 4000 USD, 
elif city == "NEW YORK" or city == "NYC" or city == "SAN FRANCISCO" or city == "SF" and (rental_fee < 4000):
    condition = True

# ha a havi bér 3000 USD-nél kisebb- bárhova
elif rental_fee < 3000:
    condition = True
    
#egyik feltételnek sem felel meg
else:
    condition = False

#El kell tárolni a választ és kiértékelni
condition = "good" if condition else "not good"

print(f"This flat {city}, {rental_fee} is {condition} for you ")



#Egy kis játék - a párom kitalálta, hogy csak akkor kérje be az összeget, ha nem Washington a válasz, én 
#meg továbbgondoltam, hogy meddig akarja keresni az albérletet?

valasz = input("Would you like to search rental fleet? yes/no: ")
if valasz == "yes":

    while True: 
        city = input("Which city would you like to move to? ").strip().upper()

        if city == "WASHINGTON" or city == "WA":
            print(f"I wouldn't move to this {city}")
        elif city == "CHICAGO" or city == "CHI":
            print(f"Money's no problem — I'm moving! {city}")
        else: 
            rental_fee = float(input("How much is the monthly rent? "))

            if (city == "NEW YORK" or city == "NYC" or city == "SAN FRANCISCO" or city == "SF") and (rental_fee < 4000):
                print(f"OK, I'm moving in this city: {city} and this rental fee: {rental_fee}" )
            elif rental_fee < 3000:
                print ("I'll move anywhere!")
            else:
                print ("I'm definitely not moving!")

        exit = input("Would you like to search more?: yes/no: ").lower()
        if exit == "yes":
            continue
        else:
            print("Exit")
            break
else:
    print("Exit")
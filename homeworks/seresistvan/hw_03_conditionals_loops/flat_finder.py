cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Francisco",
    "Austin",
    "Jacksonville",
    "Fort Worth",
    "Columbus",
    "Charlotte",
    "Washington"
]

city = input("Please enter the name of the City: ")
monthly_rent = input("Please enter the Rental Cost: ")

if city.lower() in [c.lower() for c in cities]:  # hogy ne számítson a kis- ill. nagybetű
    print(f"{city}
else:
    print(f"{city} nem szerepel a listában.")

# A feladat célja, hogy elsajátítsd azt a képességet hogy hétköznapi módon
# megfogalmazott feladatokat fordítasz le python-ra. Sarah-nak kell segítened
# a lakáskeresésben, a következőket tudjuk:
# ● Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban
# kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD
# havonta.
# ● Gyűlöli Washington-t, és semmi pénzért nem lakna ott
# ● Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit
# megadna azért hogy ott lakhasson
# ● Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
# ellenében költözne oda.
# Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát.
# Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott
# feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""
Sarah-nak kell segítened 
a lakáskeresésben, a következőket tudjuk: 
● Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban 
kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD 
havonta. 
● Gyűlöli Washington-t, és semmi pénzért nem lakna ott 
● Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit 
megadna azért hogy ott lakhasson 
● Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér 
ellenében költözne oda. 
Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát. 
Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott 
feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""


while True:
    city = input("Melyik városból jött az ajánlat? ").strip().title()
    rent = int(input("Mennyi a havi lakbér USD-ben? "))

    if city == "New York":
        if rent < 4000:
            print(f"Sarah elfogadja a {city}-i ajánlatot havi {rent} USD-ért.")
        else:
            print(f"Sarah nem fogadja el a {city}-i ajánlatot havi {rent} USD-ért.")

    elif city == "San Francisco":
        if rent < 4000:
            print(f"Sarah elfogadja a {city}-i ajánlatot havi {rent} USD-ért.")
        else:
            print(f"Sarah nem fogadja el a {city}-i ajánlatot havi {rent} USD-ért.")

    elif city == "Washington":
        print(f"Sarah nem fogadja el a {city}-i ajánlatot.")

    elif city == "Chicago":
        print(f"Sarah elfogadja a {city}-i ajánlatot havi {rent} USD-ért.")

    else:
        if rent <= 3000:
            print(f"Sarah elfogadja a {city}-i ajánlatot havi {rent} USD-ért.")
        else:
            print(f"Sarah nem fogadja el a {city}-i ajánlatot havi {rent} USD-ért.")

    answer = input("Van még egy ajánlat? (igen/nem): ")

    if answer == "nem":
        break


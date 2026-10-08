"""
Sarah-nak kell segítened a lakáskeresésben, a következőket tudjuk

Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban
kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD
havonta.

Gyűlöli Washington-t, és semmi pénzért nem lakna ott

Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit
megadna azért hogy ott lakhasson

Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér
ellenében költözne oda.

Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát.
Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott
feltételek (város és albérlet ára) mellett be tudna-e költözni az adott helyre.
"""

city = input("Kérlek add meg a kiszemelt várost: ").strip().title()
rent_price = ""

# int/string validalast azt hiszem nem vettunk meg, de utananeztem, hogy legyen benne egy minimalis ellenorzes

while True:
  rent_price = input("Kérlek add meg a leendő bérleti díjat (/hó, USD, csak egész szám, pl. 1000): ")
  if not(rent_price.isdigit()):
    print("A megadott érték nem szám, kérlek próbáld újra!")
  else:
    break

rent_price = int(rent_price)

# inputok ok, kiertekeles
# bar mindharom vizsgalat True-ra allitja, lehetne csak egy if() or-okkal, de
# az olvashatosag miatt vettem 3 fele, hogy ne legyen spagetti kod

decision = False

if city == "Chicago":
  decision = True
elif rent_price < 4000 and (city == "New York" or city == "San Francisco"):
  decision = True
elif city != "Washington" and rent_price <= 3000:
  decision = True

print(f"Ez a lakás {"MEGFELEL" if decision else "sajnos NEM FELEL MEG"} a preferenciáidnak!")

""" 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
HW 03 - Feladat 1. Hétköznapi nyelven leírt szöveg konvertálása Python kód-ra 
(if-elif-else, operátorok)
by Kiss Tibor
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""
# Bekérjük a várost. A strip() levágja a véletlenül beírt szóközöket a szélekről.
city = input("Melyik városban keres lakást Sarah? ").strip()
# A casefold() kis- és nagybetűtől független összehasonlításhoz alakítja a nevet.
normalized_city = city.casefold()

# Addig kérjük be a lakbért, amíg számot és nemnegatív értéket nem kapunk.
while True:
    rent_text = input("Add meg a havi lakbért USD-ben: ").strip()
    try:
        # Az input() szöveget ad vissza, ezért a lakbért számmá alakítjuk.
        monthly_rent = float(rent_text)
    except ValueError:
        # Ha az átalakítás nem sikerült, hibaüzenetet adunk, majd újra kérdezünk.
        print("Hibás összeg. Számot adj meg.")
        continue

    # A negatív lakbér nem életszerű bemenet, ezért ezt is újra bekérjük.
    if monthly_rent < 0:
        print("A lakbér nem lehet negatív.")
        continue
    # A break csak akkor fut le, ha az összeg érvényes; ezzel kilépünk a bekérő ciklusból.
    break

# Sarah Chicagóban bármilyen áron lakna.
if normalized_city == "chicago":
    decision = True
# Washingtonban semmilyen áron nem lakna.
elif normalized_city == "washington":
    decision = False
# New Yorkban és San Franciscóban a lakbérnek szigorúan 4000 USD alatt kell lennie.
elif normalized_city in {"new york", "san francisco"}:
    decision = monthly_rent < 4000
# Minden más városban legfeljebb 3000 USD-t fizetne.
else:
    decision = monthly_rent <= 3000

# A logikai döntést rövid, magyar szöveggé alakítjuk a kiíráshoz.
answer = "be tud költözni" if decision else "nem tud beköltözni"
# Az f-string a kapcsos zárójelek között behelyettesíti a változók értékét.
print(
    f"Sarah {answer} {city} városába "
    f"{monthly_rent:g} USD havi lakbér mellett."
)
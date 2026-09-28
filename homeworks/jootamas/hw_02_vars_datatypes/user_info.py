import pprint

user_info = {
  "name": "Mike",
  "age": 25,
  "favourite_meals": [
    "pizza",
    "carbonara",
    "sushi"
  ],
  "phone_contacts": {
    "Mary": "+36701234567",
    "Tim": "+36207654321",
    "Tim2": "+36304567321",
    "Jim": "+364005000"
  }
}

print("Kiindulás:")
pprint.pprint(user_info)

# 1 - Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül.
# Konvertáld a kapott stringet egy listává, és add hozzá a fenti dictionary-hez “skills” néven.

skills_str = input("Adj meg 4 általad ismert programozási nyelvet, egymás után, vesszőkkel elválasztva: ")
skills_list = skills_str.split(",")
user_info["skills"] = skills_list

print("1. skills hozzáadva:")
print(user_info["skills"])

# 2 - Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.

user_info["favourite_meals"].sort()

print("2. favourite_meals ABC:")
print(user_info["favourite_meals"])

# 3 - Printeld ki a favourite_meals lista utolsó előtti elemét

print("3. favourite_meals utolsó előtti eleme:")

print(user_info["favourite_meals"][-2])

# 4 - Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.

user_info["favourite_meals"].append("spaghetti")

print("4. spaghetti hozzáadva a favourite_meals-hez:")
print(user_info["favourite_meals"])

# 5 - Add hozzá a favourite_meals-hez az aktuális favourite_meals lista harmadik és negyedik elemét (nem az index-ét) újra.

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

print("5. favourite_meals-hez hozzáadva az 3. és 4. elem újra:")
print(user_info["favourite_meals"])

# 6 - Ezután töröld az így keletkezett duplikátumokat!

# Megjegyzes: mivel itt egy lepesben set() lett, igy azt hiszem az uj listaban nem feltetlen marad meg az ABC sorrend a 2. lepesbol,
# de ezzel nem foglalkozok, mert nem fealdat

user_info["favourite_meals"]=list(set(user_info["favourite_meals"]))

print("6. favourite_meals-ben duplikátumok törölve:")
print(user_info["favourite_meals"])

# 7 - Cseréld fel a favourite_meals lista első és utolsó elemét!

"""
A fapados megoldas az, hogy egy temp-be kiteszem az elsot, majd az elso megkapja az utolsot, vegul pedig az utolso az elsot a temp-bol

De gondoltam biztos van szebb megoldas is, ezert Claude-tol kerdeztem

Ket megkozelitest irt a Claude, az egyik ez volt:

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

De ez inkabb leve2 megoldasnak tunik, ezert az egyszerubbet hasznaltam
"""

user_info["favourite_meals"] = [ user_info["favourite_meals"][-1] ] + user_info["favourite_meals"][1:-1] + [ user_info["favourite_meals"][0] ]

print("7. favourite_meals lista első és utolsó eleme felcserélve:")
print(user_info["favourite_meals"])

# 8 - A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.

user_info["phone_contacts"]["Bob"] = "+36301111222"

print("8. új elem a phone_contacts-ban: Bob")
print(user_info["phone_contacts"])

# 9 - Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!

del user_info["phone_contacts"]["Tim"]

print("9. régi Tim törölve:")
print(user_info["phone_contacts"])

# 10 - Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!

user_info["phone_contacts"]["John"] = ["+36201111111","+36302222222"]

print("10. új ember hozzáadva a phone_contacts-ba két telefonszámmal:")
print(user_info["phone_contacts"])

# extra 1 - Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!

print("Extra 1: skills utolsó 3 eleme ellentétes sorrendben:")
print(user_info["skills"][:-4:-1])
print(f"Eredeti: {user_info["skills"]}")

# extra 2 - Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!

"""
Itt is kerdeztem egyet, hogy van-e egysoros megoldas, de egyelore hagytam az egyszerubbet, a ketsorost

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

(jegyzet magamnak, mit csinal ez: toroljuk a Tim2 kulcsot es egyben adjuk at az erteket az uj Tim kulcsnak)
"""

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
del user_info["phone_contacts"]["Tim2"]

print("Extra 2: Tim2 átnevezve Tim-re")
print(user_info["phone_contacts"])

# kiirom az eredmenyt a vegen

print("A teljes user_info:")
pprint.pprint(user_info)

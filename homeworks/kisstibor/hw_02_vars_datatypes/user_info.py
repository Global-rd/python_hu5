# Házifeladat 2. Feladat 2. List és dictionary műveletek használata
import nt
from pprint import pprint
import os

# Létrehozzuk a 'clear' parancsot
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

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

print('''\n---------------------------
2-01 Feladat: Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva,
szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá
a fenti dictionary-hez “skills” néven

  skills = input("Enter your skills (comma-separated): ").split(",")
  user_info ["skills"] = skills
''')

skills = input("Enter your skills (comma-separated): ").split(",")
#skills=("Python,JavaScript,Java,C++".split(","))  # Csak hogy ne kelljen mindig beírni, ha tesztelni akarom a kódot
user_info ["skills"] = skills
pprint(user_info)


print('''\n---------------------------
2-02 Feladat: Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
  
  user_info["favourite_meals"].sort()
''')
user_info["favourite_meals"].sort()
pprint(user_info)


print('''\n---------------------------
2-03 Feladat: Printeld ki a favourite_meals lista utolsó előtti elemét
  
  print(user_info["favourite_meals"][-2])
''')
print(user_info["favourite_meals"][-2])


print('''\n---------------------------
2-04 Feladat: Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
  
  user_info["favourite_meals"].append("spaghetti")
''')
user_info["favourite_meals"].append("spaghetti")
pprint(user_info)

print('''\n---------------------------
2-05 Feladat: Add hozzá a favourite_meals-hez az aktuális favourite_meals lista
harmadik és negyedik elemét (nem az index-ét) újra.
  user_info["favourite_meals"].extend([user_info["favourite_meals"][2], user_info["favourite_meals"][3]])
''')
user_info["favourite_meals"].extend([user_info["favourite_meals"][2], user_info["favourite_meals"][3]])
pprint(user_info)


print('''\n---------------------------
2-06 Feladat: Ezután töröld az így keletkezett duplikátumokat!

Első megoldás, ami eszembe jutott, hogy a listát set() adatszerkezetté alakítom, majd vissza listává:
user_info["favourite_meals"]=list(set(user_info["favourite_meals"]))
pprint(user_info)

Ezzel a megoldással megváltozik a lista elemek sorrendje 
Ennek oka az, hogy a set() adatszerkezet nem garantálja az elemek sorrendjét !!!.

A megoldás az aláábbiakkal érhető el, ami megtartja az eredeti sorrendet, és törli a duplikátumokat:
      user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
''')

user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
pprint(user_info)
# input("Press Enter to continue...")

'''
    Magyarázat: 
    A dict.fromkeys() metódus létrehoz egy dictionary-t a favourite_meals lista elemeiből,
    ahol a kulcsok az eredeti lista elemei lesznek. 
    Mivel a dictionary kulcsai egyediek, így a duplikátumok automatikusan eltávolításra kerülnek. 
    Ezután a list() függvény segítségével visszaalakítjuk a kulcsokat egy listává, így megőrizve az eredeti sorrendet.

    Ez zseniális! -Nyilván nem magamtól jöttem rá !
'''

print('''\n---------------------------
2-07 Feladat: Cseréld fel a favourite_meals lista első és utolsó elemét!

  user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
''')
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
pprint(user_info)


print('''\n---------------------------
2-08 Feladat: A "phone_contacts" dictionary-hez adj hozzá egy új elemet,
tetszőleges névvel és telefonszámmal.
  
  user_info["phone_contacts"]["Tibi"] = "+36701234567"
''')
user_info["phone_contacts"]["Tibi"] = "+36701234567"
pprint(user_info)

print('''\n---------------------------
2-09 Feladat: Tim és Tim2 ugyanazt az embert reprezentálják a
“phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám
már nem él. Töröld ki a telefonkönyvből!

  user_info["phone_contacts"].pop("Tim")
''' )
user_info["phone_contacts"].pop("Tim")
pprint(user_info)       

print('''\n---------------------------
2-10 Feladat: Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2
telefonszáma is van!

# A Multiple telefonszámok egy listában  
  user_info["phone_contacts"]["Dual SIMon"] = ["+36701234567", "+36207654321"]
''')

user_info["phone_contacts"]["Dual SIMon"] = ["+36701234567", "+36207654321"]
pprint(user_info)

print('''\n---------------------------
A ["phone_contacts"] adatszerkezet viszont nem lesz konzisztens, mert a "Dual SIMon" key-hez tartozó value egy lista lesz, 
míg a többi key-hez tartozó értéke meg string típusú. 

Igénytől és további feldolgozástól függően az alábbi két megoldás gondolnám:
1. A "Dual SIMon" key-hez tartozó value-t is string típusúvá alakítom, és vesszővel elválasztom a két telefonszámát.

  user_info["phone_contacts"]["Dual SIMon"] = ", ".join(user_info["phone_contacts"]["Dual SIMon"])
''')

user_info["phone_contacts"]["Dual SIMon"] = ", ".join(user_info["phone_contacts"]["Dual SIMon"])
pprint(user_info)

print('''\n---------------------------
2. A "phone_contacts" összes elemét List vagy Dictionary típusban kellene kezelni egységesen, hogy a további feldolgozás során ne legyenek típusbeli eltérések.
    "phone_contacts": {
        "Mary": { "Primary": "+36701234567", "Secondary": "+36207654321"},
        "Tim":  { "Primary": "+36207654321", "Secondary": None}, 
        "Tim2": { "Primary": "+36304567321", "Secondary": None},
        "Jim":  { "Primary": "+364005000",   "Secondary": None},

}
De ennek átalakításához kevés vagyok mind erdőtűzhöz a vizipisztoly :)
Úgy is fogalmazhatnék, hogy "It's as big a mouthful for me as a reticulated python is for a pygmy python." :)
''')


print('''\n---------------------------
Extra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!

  print(user_info["skills"][-1:-4:-1])
''')

print(user_info["skills"][-1:-4:-1])

print('''\n---------------------------
Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne
átnevezni Tim2-t Tim-re!

  user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
''')

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
pprint(user_info)


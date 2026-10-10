from pprint import pprint
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


#1  Programozási nyelvek bekérése
programming_languages = input(
    "Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: "
)
# A kapott string átalakítása listává, a split mikor vesszőt talál, ott vágja el
programming_languages = programming_languages.split(",")
# A lista hozzáadása a dictionary-hez "skills" néven
user_info["skills"] = programming_languages


#2  favourite_meals rendezése ABC szerint
print("-------------------------")

user_info["favourite_meals"].sort()

pprint(user_info)


#3 egy key-nek aminek a value-ja egy lista, kiirja az utolsó értékét.
print("-------------------------")

print(user_info["favourite_meals"][-1])

#4 hozzáadok a egy új elemet a listához
user_info["favourite_meals"].append("spagetti")

#5 hozzáadom index szerint a 2,3 elemét újra.
"""user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])
#print(user_info["favourite_meals"])"""

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
#pprint(user_info["favourite_meals"])

#6 a duplikátumok eltüntetése
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
#print(user_info["favourite_meals"])

#7 elemek felcserélése a dic.-ben az indexek felcserélésével
user_info["favourite_meals"][0],user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
#p(user_info["favourite_meals"])

#8 hozzáadtam egy új key/value-t a dic.-en belül
user_info["phone_contacts"]["john"] = "+36204567894"
#pprint(user_info["phone_contacts"])

#9 elem törlése
del user_info["phone_contacts"]["Tim"]
#del user_info["skills"][-1]
#pprint(user_info["phone_contacts"])

#10 egy új dic. a dic.-en belül
user_info["phone_contacts"]["Dani"] = ["+36704561231","+491514567891"]
#pprint(user_info["phone_contacts"])

#extra1
print("-------------------------")

pprint(user_info["skills"][-3:][::-1])

#extra2
print("-------------------------")
"""user_info["phone_contacts"]["Tim2"] = user_info["phone_contacts"]["Tim"]
del user_info["phone_contacts"]["Tim2"]"""
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
pprint(user_info["phone_contacts"])


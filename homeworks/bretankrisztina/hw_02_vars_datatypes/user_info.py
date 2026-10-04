#kiinduló táblázat
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

#Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva,szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá
#a fenti dictionary-hez “skills” néven.
programming_languages = input("Kérlek, adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: ")
programming_languages_list = programming_languages.split(",")
user_info["skills"] = programming_languages_list
print(user_info)

#Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
user_info["favourite_meals"].sort()

#Printeld ki a favourite_meals lista utolsó előtti elemét
print(user_info["favourite_meals"][-2])

#Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
user_info["favourite_meals"].append("spaghetti")

#Add hozzá a favourite_meals-hez az aktuális favourite_meals lista harmadik és negyedik elemét
user_info2 = user_info["favourite_meals"][2:4]
user_info["favourite_meals"].extend(user_info2)

#Ezután töröld az így keletkezett duplikátumokat!
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

#Cseréld fel a favourite_meals lista első és utolsó elemét!
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

#A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"].update({"Jonny": "+36305236543"})
print(user_info["phone_contacts"])

#Tim és Tim2 ugyanazt az embert reprezentálják a phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám
# már nem él. Töröld ki a telefonkönyvből!
user_info["phone_contacts"].pop("Tim", None)

#​Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
user_info["phone_contacts"].update({"Roland": ["+36204587985", "+36354235645"]})

#Extra feladat
#Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2", None)
print(user_info["phone_contacts"])

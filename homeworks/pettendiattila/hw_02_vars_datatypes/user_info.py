#Homwework_02_datatypes

#2_exercise

from pprint import pprint

#Basic_dictionary
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

#1 Kérj be a felhasználótól 4 programozási nyelvet...
#Input_adat: Python,Java,C++,Sql

print("-"*100)
inputs_skills = input("Adj meg 4 programozási nyelvet vesszővel elválasztva (szóköz nélkül): ")
user_skills = inputs_skills.split(",")
user_info["skills"] = user_skills
print(user_info["skills"])

#pprint(user_info)
print("-"*100)

#2 Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])
print("-"*100)

#3 Printeld ki a favourite_meals lista utolsó előtti elemét
print(f"Utolsó előtti kedvenc étel: {user_info["favourite_meals"][-2]}")
print("-"*100)

#4 Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
user_info["favourite_meals"].append("spaghetti")
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])
print("-"*100)

#5 Add hozzá a favourite_meals-hez az aktuális favourite_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
extended_user_info = user_info["favourite_meals"][2:4]
user_info["favourite_meals"].extend(extended_user_info)
print(user_info["favourite_meals"])
print("-"*100)

#6 Ezután töröld az így keletkezett duplikátumokat!
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])
print("-"*100)

#7 Cseréld fel a favourite_meals lista első és utolsó elemét!
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = (user_info["favourite_meals"][-1], user_info["favourite_meals"][0],)
print(user_info["favourite_meals"])
print("-"*100)

#8 A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"]["Eva"] = "+36901112233"
print(user_info["phone_contacts"])
print("-"*100)

#9 Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!
del user_info["phone_contacts"]["Tim"]
print(user_info["phone_contacts"])
print("-"*100)

#10 Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
user_info["phone_contacts"]["Ivan"] = ["+36109998877", "+36301114455"]
print(user_info["phone_contacts"])
print("-"*100)

#1 Extra feladat
user_info["skills"][-3:][::-1]
print(f"Az utolsó 3 skill fordítva: {user_info["skills"][-3:][::-1]}")
print("-"*100)

#2 Extra feladat
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info["phone_contacts"])
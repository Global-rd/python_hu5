user_info = {
    "name" : "Mike",
    "age" : 25,
    "favourite_meals" : [
        "pizza",
        "carbonara",
        "sushi"
    ],
    "phone_contacts" : {
        "Mary" : "+36701234567",
        "Tim" : "+36207654321",
        "Tim2" : "+36304567321",
        "Jim" : "+364005000"
    }
}

#1.feladat
programming_languages = input("Please enter 4 programming languages, separated by commas (no spaces): ")
skills = programming_languages.split(",")
user_info["skills"] = skills

print(user_info["skills"])

#2.feladat
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])

#3. feladat
print(user_info["favourite_meals"][-2])

#4.feladat
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])

#5.feladat
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])

#6.feladat
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])
#ezzel eltuntettuk a duplikátumokat, de a sorrend megváltozott, mert a set nem tartja meg az eredeti sorrendet

#Kerdes: ilyenkor rendezzem ujra ABC rendbe, mert ez volt egy korabbi feladat?

#7.feladat
#eleg nyakatekert modon, de eloszor hozzaadom az utols elemet az elso helyre, majd kitorlom az utolsot.
user_info["favourite_meals"].insert(0, user_info["favourite_meals"][-1])
print(user_info["favourite_meals"])

user_info["favourite_meals"].pop(-1)
print(user_info["favourite_meals"])

#aztan a masodik elemet (ami az elso volt a listaban) hozzaadom az utolso helyre, majd kitorlom az eredtei helyereol.
user_info["favourite_meals"].append(user_info["favourite_meals"][1])
print(user_info["favourite_meals"])

user_info["favourite_meals"].remove(user_info["favourite_meals"][1])
print(user_info["favourite_meals"])

#es ez egy jo gyakorlas is volt a kulonbozo metodusokkal, ugyanazt csinaljak es megsem.

#de, biztos van ennek egy egyszerubb modja is, ugyhogy az interneten a kovetkezo megoldast talaltam:
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

#8. feladat
import pprint
user_info["phone_contacts"].update({("Brian", "+36201234567")})
pprint.pprint(user_info["phone_contacts"])

#9. feladat
del user_info["phone_contacts"]["Tim"]
pprint.pprint(user_info["phone_contacts"])

#10. feladat
user_info["phone_contacts"].update({("Cohen", "+36207654321" " +3630456789")})
pprint.pprint(user_info["phone_contacts"])

#Extra 1.
print(user_info["skills"][-1:-4:-1])

#Extra 2.
contacts = user_info["phone_contacts"]
contacts["Tim"] = contacts.pop("Tim2")
pprint.pprint(user_info["phone_contacts"])
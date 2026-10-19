# A felhasználó adatait egy szótárban tárolom....
user_info = {
    "name": "Mike",
    "age": 25,

    "favourite_meals": [
        "pizza",
        "carbonara",
        "sushi",
    ],
        "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    },
}
# Bekérek négy programozási nyelvet, majd listává alakítjuk.
skills_input = input("Enter four programming languages separated by commas: ")
user_info["skills"] = skills_input.split(",")
# Most Ábécés sorrendbe rendezem a kedvenc ételeket.
user_info["favourite_meals"].sort()
# Es most Kiírom a kedvenc ételek közül az utolsó előttit....
print(user_info["favourite_meals"][-2])
# Hozzáadom a spagettit a kedvenc ételekhez....ez a lista vegehez adja hozza
user_info["favourite_meals"].append("spaghetti")
# A harmadik és negyedik elemet újra hozzáadom a listához
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
# Ezzel eltávolítom az ismétlődő ételeket, de megtartom a sorrendet.
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
# Felcserélem az első és az utolsó ételt....
meals = user_info["favourite_meals"]
meals[0], meals[-1] = meals[-1], meals[0]
# Hozzáadok egy új személyt a telefonos névjegyekhez.
user_info["phone_contacts"]["John"] = "+36705555555"
# Törlöm az elavult Tim névjegyet most....
del user_info["phone_contacts"]["Tim"]
# Hozzáadok egy új személyt két telefonszámmal.
user_info["phone_contacts"]["Anna"] = ["+36701111111", "+36302222222"]
# Kiírom az utolsó három programozási nyelvet fordított sorrendben.
print(user_info["skills"][-3:][::-1])
# A Tim2 névjegyet átnevezem Tim névre.
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")



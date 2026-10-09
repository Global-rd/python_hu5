user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza", "carbonara", "sushi"],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
    }
}

# Programzozási nyelvek bekérése és lkistává alakítása.
skills = input("Adj meg 4 programozási nyelvet vesszővel, szóközök nélkül: ")

user_info["skills"] = skills.split(",")

# Az ételek rendezése
user_info["favourite_meals"].sort()

# Utolsó előtti étel kiírása.
print(user_info["favourite_meals"][-2])

# A spaghetti hozzáadása.
user_info["favourite_meals"].append("spaghetti")

# A harmadik és negyedik étel újbóli hozzáadása.

user_info["favourite_meals"].extend([

    user_info["favourite_meals"][2],

    user_info["favourite_meals"][3]
])

# 6. Duplikátumok törlése
unique_meals = []

for meal in user_info["favourite_meals"]:
    if meal not in unique_meals:
        unique_meals.append(meal)

user_info["favourite_meals"] = unique_meals

# első és utolsó elem felcserélése


#  Új név és telefonszám hozzáadása.
user_info["phone_contacts"]["Stefan"] = "+41786662343"

# Tim telefonszámának törlése.
del user_info["phone_contacts"]["Tim"]

# 10. Az új ember két telefonszámát egy listában tároljuk.
user_info["phone_contacts"]["Peter"] = ["+36702223344", "+36205556677"]

print(user_info)




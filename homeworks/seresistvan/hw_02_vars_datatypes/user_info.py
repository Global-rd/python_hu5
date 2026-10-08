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

# 3. Az utolsó előtti étel kiírása.
print(user_info["favourite_meals"][-2])

# 4. A spaghetti hozzáadása.
user_info["favourite_meals"].append("spaghetti")

# A harmadik és negyedik étel újbóli hozzáadása.

user_info["favourite_meals"].extend([

    user_info["favourite_meals"][2],

    user_info["favourite_meals"][3]
])


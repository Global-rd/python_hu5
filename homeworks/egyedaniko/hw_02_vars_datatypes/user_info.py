print("---")
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

# 1. Programozási nyelvek bekérése
skills_input = input("Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: ")
user_info["skills"] = skills_input.split(",")

# 2. favourite_meals rendezése
user_info["favourite_meals"].sort()

# 3. Utolsó előtti elem kiírása
print(
    "Utolsó előtti kedvenc étel:",
    user_info["favourite_meals"][-2]
    )

# 4. Spaghetti hozzáadása
user_info["favourite_meals"].append("spaghetti")

# 5. Harmadik és negyedik elem újra hozzáadása
user_info["favourite_meals"].extend(
user_info["favourite_meals"][2:4]
)

# 6. Duplikátumok eltávolítása
user_info["favourite_meals"] = list(
dict.fromkeys(user_info["favourite_meals"])
)

# 7. Első és utolsó elem felcserélése
meals = user_info["favourite_meals"]
meals[0], meals[-1] = meals[-1], meals[0]

print("Favourite meals:", meals)

# 8. Új telefonszám hozzáadása
user_info["phone_contacts"]["Aniko"] = "+36304118355"

# 9. Tim törlése
del user_info["phone_contacts"]["Tim"]

# 10. Új ember két telefonszámmal
user_info["phone_contacts"]["Zsolt"] = [
    "+36209374680",
    "+3612575835"
    ]

# Extra 1
print(
"Utolsó 3 skill fordított sorrendben:",
user_info["skills"][-1:-4:-1]
)

# Extra 2
user_info["phone_contacts"]["Tim"] = (
user_info["phone_contacts"].pop("Tim2")
)

print(user_info)
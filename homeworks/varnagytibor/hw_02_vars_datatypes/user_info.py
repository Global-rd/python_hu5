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

# 1. Bekérünk 4 programozási nyelvet vesszővel elválasztva, listává alakítjuk, és "skills" néven hozzáadjuk.
skills_input = input("Enter 4 programming languages, separated by commas, no spaces: ")
user_info["skills"] = skills_input.split(",")

# 2. A favourite_meals listát ABC szerint növekvő sorrendbe rendezzük.
user_info["favourite_meals"].sort()

# 3. Kiírjuk a favourite_meals utolsó előtti elemét (a teljes listát is, hogy lásd).
print("Utolsó előtti étel:", user_info["favourite_meals"][-2])
print("Teljes lista:", user_info["favourite_meals"])

# 4. Hozzáadunk egy "spaghetti" elemet a listához.
user_info["favourite_meals"].append("spaghetti")

# 5. Hozzáadjuk újra a jelenlegi lista 3. és 4. elemének ÉRTÉKÉT (így duplikátumok keletkeznek).
user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])

# 6. Töröljük a keletkezett duplikátumokat: set-té alakítunk (az nem tűr dupla elemet), majd vissza listává.
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# 7. Megcseréljük a lista első és utolsó elemét.
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = \
    user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

# 8. A phone_contacts-hoz hozzáadunk egy új embert tetszőleges névvel és számmal.
user_info["phone_contacts"]["Anna"] = "+36701112222"

# 9. A "Tim" kulcs mögötti szám már nem él (Tim és Tim2 ugyanaz) -> töröljük a "Tim" kulcsot.
del user_info["phone_contacts"]["Tim"]

# 10. Hozzáadunk egy új embert, akinek 2 telefonszáma van (ezért az értéke egy lista).
user_info["phone_contacts"]["Peter"] = ["+36201111111", "+36302222222"]

# Extra 1: Kiírjuk a "skills" lista utolsó 3 elemét ellentétes sorrendben.
print("Utolsó 3 skill fordítva:", user_info["skills"][-3:][::-1])

# Extra 2: Mivel Tim-nek már csak 1 sz kulcsot "Tim"-re.
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
del user_info["phone_contacts"]["Tim2"]

# A végén kiírjuk a teljes dictionary-s.
print("Végeredmény:", user_info)



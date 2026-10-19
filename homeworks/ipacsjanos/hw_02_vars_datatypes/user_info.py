# Kiinduló dictionary
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

# 1. Programozási nyelvek bekérése, listává alakítása (.split-tel) és hozzáadása a szótárhoz
skills_input = input("Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: ")
user_info["skills"] = skills_input.split(",")

# 2. A favourite_meals lista elemeinek abc szerinti növekvő sorrendbe rendezése
user_info["favourite_meals"].sort()

# 3. A favourite_meals lista utolsó előtti elemének kiprintelése (index: -2)
print(f"3. A favourite_meals utolsó előtti eleme: {user_info['favourite_meals'][-2]}")

# 4. 'spaghetti' hozzáadása a listához
user_info["favourite_meals"].append("spaghetti")

# 5. Az aktuális lista harmadik és negyedik elemének hozzáadása egyszerre, extend és index range használatával
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# 6. Duplikátumok törlése (set-té alakítással kiszűrjük a duplikációt, majd visszalistásítjuk)
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# 7. Az első (0) és utolsó (-1) elem felcserélése egy átmeneti változóval
temp = user_info["favourite_meals"][0]
user_info["favourite_meals"][0] = user_info["favourite_meals"][-1]
user_info["favourite_meals"][-1] = temp

# 8. Új kontakt hozzáadása a phone_contacts-hoz
user_info["phone_contacts"]["Alex"] = "+36509998877"

# 9. Régi Tim kontakt törlése (.pop vagy del használatával)
user_info["phone_contacts"].pop("Tim")

# 10. Új ember hozzáadása, akinek 2 telefonszáma is van (egy listában tárolva a számokat)
user_info["phone_contacts"]["Kate"] = ["+361111111", "+362222222"]

# Extra 1: A 'skills' lista utolsó 3 elemének kiprintelése ellentétes sorrendben (slicing lépésközzel: [start:stop:step])
print(f"Extra 1 - Skills utolsó 3 eleme fordítva: {user_info['skills'][-1:-4:-1]}")

# Extra 2: Tim2 átnevezése Tim-re
# A .pop("Tim2") kitörli Tim2-t és egyből visszaadja a számát, amit elmentünk az új "Tim" kulcs alá
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

# A teljes dictionary ellenőrző kiíratása a végén
print("\nA módosított teljes user_info szótár:")
print(user_info)

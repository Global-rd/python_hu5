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
#Skillek bekérése, dictionary-hez adása
skills = input("Adj meg 4 programozási nyelvet vesszővel elválasztva: ").split(",")
user_info["skills"] = skills
print(user_info)

#A favourite_meals lista abc rendezése
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"][-2]) #A favourite_meals lista utolsó előtti elemének kiíratása

#spagetti hozzáadása
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])

# 3. és 4. elem újbóli hozzáadása
third_meal = user_info["favourite_meals"][2]
fourth_meal = user_info["favourite_meals"][3]
user_info["favourite_meals"].append(third_meal)
user_info["favourite_meals"].append(fourth_meal)
print(user_info["favourite_meals"])

# Duplikátumok törlése
user_info["favourite_meals"].remove(third_meal)
user_info["favourite_meals"].remove(fourth_meal)
print(user_info["favourite_meals"])

# Első és utolsó elem cseréje
first_meal = user_info["favourite_meals"][0]
user_info["favourite_meals"][0] = user_info["favourite_meals"][-1]
user_info["favourite_meals"][-1] = first_meal
print(user_info["favourite_meals"])

# Új kontakt
user_info["phone_contacts"]["Aladár"] = "+36301234567"
print(user_info["phone_contacts"])

# Tim-szám törlése
del user_info["phone_contacts"]["Tim"]
print(user_info["phone_contacts"])

# Kontakt két telefonszámmal
user_info["phone_contacts"]["Kriszta"] = ["+36201234567", "+36207654321"]
print(user_info["phone_contacts"])

# Sillek utolsó 3 eleme fordított sorrendben
print(skills[-1], skills[-2], skills[-3])

# Tim2 átnevezése Tim-re
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
del user_info["phone_contacts"]["Tim2"]
print(user_info)
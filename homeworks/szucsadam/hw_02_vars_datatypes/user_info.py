programming_languages = input("Enter four programming languages separated by commas: ")

skills = programming_languages.split(",")

languages_list = {}

languages_list["skills"] = skills


"""
print("Enter four programming languages.")

programming_language_1 = input("Enter a programming language 1: ").strip()
programming_language_2 = input("Enter a programming language 2: ").strip()
programming_language_3 = input("Enter a programming language 3: ").strip()
programming_language_4 = input("Enter a programming language 4: ").strip()

skills = [programming_language_1, programming_language_2, programming_language_3, programming_language_4]
"""
# print(programming_language_list)


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
    },
    "skills": skills
}

user_info["favourite_meals"].sort() # abc szerint sorba

print(user_info["favourite_meals"])

print(user_info["favourite_meals"][-2]) # utolsó előtti elem

user_info["favourite_meals"].append("spaghetti") # hozzáadunk egy új elemet a listához

# user_info["favourite_meals"].extend(["sushi", "spagetti"]) 

#user_info["favourite_meals"].append(user_info["favourite_meals"][2]) 

#user_info["favourite_meals"].append(user_info["favourite_meals"][3])

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

print(user_info["favourite_meals"])

# user_info["favourite_meals"].remove(user_info["favourite_meals"][-1])

# del user_info["favourite_meals"][-2:] # utolsó kettő törlése, 6. feladat

user_info["favourite_meals"] = list(set(user_info["favourite_meals"])) #  6. feladat javítás

print(user_info["favourite_meals"])

# szavak cseréje
change1 = user_info["favourite_meals"][0]
user_info["favourite_meals"][0] = user_info["favourite_meals"][-1]
user_info["favourite_meals"][-1] = change1

print(user_info["favourite_meals"])

# tel hozzáadása

user_info["phone_contacts"]["Adam"] = "+36205634158"

print(user_info["phone_contacts"])

del user_info["phone_contacts"]["Tim"] # Tim törlése

user_info["phone_contacts"]["Bobi"] = ["+36301111111", "+36702222222"]

print(user_info["phone_contacts"])

print("szorgalmi1")

print(skills[-1:-4:-1])

print("szorgalmi2")

# user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
# del user_info["phone_contacts"]["Tim2"]

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2") # szorjalmi javítés

print(user_info)


input("Press Enter to close...") # ez csak magamm miatt van itt
